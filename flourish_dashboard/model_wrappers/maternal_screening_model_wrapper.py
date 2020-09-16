from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .maternal_screening_model_wrapper_mixin import \
    MaternalScreeningModelWrapperMixin


class MaternalScreeningModelWrapper(MaternalScreeningModelWrapperMixin, ModelWrapper):
    model = 'flourish_maternal.subject_screening'
    querystring_attrs = ['screening_identifier']
    next_url_attrs = ['screening_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
                                'maternal_screening_listboard_url')