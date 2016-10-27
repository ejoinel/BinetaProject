from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from Bineta.models import Document
from Bineta.serializers import DocumentSerializer, FileListSerializer


class DocumentViewSet( viewsets.ModelViewSet ):

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def list( self, request ):
        return None

    def retrieve( self, request, pk=None ):
        return None

    def create( self, request ):
        serializer = FileListSerializer( None )
        return None

DocumentList = DocumentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
