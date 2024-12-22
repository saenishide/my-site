from django.apps import AppConfig
from game_area.service.machineLearningService import MachineLearningService


class GameAreaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "game_area"
    mservice = MachineLearningService()
    mservice.act_image_machine_learning()

default_app_config = 'game_area.apps.GameAreaConfig'