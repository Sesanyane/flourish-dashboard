from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist


class MaternalScreeningModelWrapperMixin:

    model = 'flourish_maternal.subjectscreening'
    querystring_attrs = ['screening_identifier']
    next_url_attrs = ['screening_identifier']

    @property
    def screening_identifier(self):
        if self.maternal_model_obj:
            return self.maternal_model_obj.screening_identifier
        return None

    @property
    def maternal_model_obj(self):
        """Returns a maternal model instance or None.
        """
        try:
            return self.maternal_screening_cls.objects.get(**self.maternal_screening_options)
        except ObjectDoesNotExist:
            return None

    @property
    def maternal_screening_cls(self):
        return django_apps.get_model('flourish_maternal.subjectscreening')

    @property
    def create_maternal_screening_options(self):
        """Returns a dictionary of options to create a new
        unpersisted maternal screening model instance.
        """
        options = dict(
            screening_identifier=self.object.screening_identifier)
        return options

    @property
    def maternal_screening_options(self):
        """Returns a dictionary of options to get an existing
        maternal screening model instance.
        """
        options = dict(
            screening_identifier=self.object.screening_identifier)
        return options