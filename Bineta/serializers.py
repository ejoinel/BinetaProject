from rest_framework import serializers
from Bineta.models import Document, DocumentFile

class DocumentFileSerializer( serializers.ModelSerializer ):

    class Meta:
        model = DocumentFile
        fields = ( 'description', 'image', 'document' )


class DocumentSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Document
        fields = ( 'slug', 'nb_views', 'name', 'creation_date' )



class FileListSerializer ( serializers.Serializer ):
    image = serializers.ListField( child=serializers.FileField( max_length=100000,
                                                                allow_empty_file=False, use_url=False ) )

    def create(self, validated_data):
        vo_document = Document.objects.latest( 'created_at' )
        image = validated_data.pop( 'image' )
        for img in image:
            photo = DocumentFile.objects.create( image=img, blogs=vo_document, **validated_data )
        return photo
