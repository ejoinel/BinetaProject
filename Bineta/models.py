from django.db import models



class Document( models.Model ):
    class Meta:
        db_table = 'Document'

    slug = models.SlugField( max_length=50 )
    nb_views = models.IntegerField( default=0 )
    name = models.CharField( max_length=100 )
    creation_date = models.DateTimeField( auto_now_add=True )
    deletion_date = models.DateTimeField( null=True, default=None )

    def __unicode__( self ):
        return self.name + " (" + str( self.status ) + ") " + self.school.name



class DocumentFile( models.Model ):
    class Meta:
        db_table = 'DocumentFile'

    #description = models.CharField( max_length=50, null=True )
    image = models.ImageField( verbose_name='image', )
    document = models.ForeignKey( Document, default=None )

    def __unicode__( self ):
        return self.description
