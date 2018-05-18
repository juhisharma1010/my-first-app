from import_export import resources
from .models import Post_new

class PersonResource(resources.ModelResource):
	class Meta:
		model = Post_new