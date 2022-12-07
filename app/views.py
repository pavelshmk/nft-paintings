from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from app.models import TokenData


class TokenMetadataView(View):
    def get(self, request: HttpRequest, **kwargs):
        token = get_object_or_404(TokenData, pk=kwargs['id'])

        return JsonResponse({
            "name": token.title,
            # "description": "Mjölnir, the legendary hammer of the Norse god of thunder.",
            "description": token.description,
            "image_url": request.build_absolute_uri(token.image.url) if token.image else None,
            "image": request.build_absolute_uri(token.image.url) if token.image else None,
        })
