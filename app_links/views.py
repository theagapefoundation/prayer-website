import os
from django.http import Http404
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from google.cloud import storage
from sqlmodel import Session, select


from website.db import engine
from .models import Group, Content


def group_invitation_link_renderer(request: WSGIRequest, group_id: str):
    with Session(engine) as session:
        statement = select(Group, Content).join(Content).where(Group.id == group_id)
        result = session.exec(statement).first()
        if not result:
            raise Http404
        [group, content] = result
        banner = (
            storage.Client()
            .bucket(os.getenv("BUCKET_NAME"))
            .blob(content.path)
            .public_url
        )
        return render(
            request,
            "app_links/group_invitation.html",
            {
                "group_id": group_id,
                "group": {
                    **group.model_dump(),
                    "banner": banner,
                },
            },
        )
