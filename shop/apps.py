from django.apps import AppConfig


class ShopConfig(AppConfig):
    name = 'shop'

    def ready(self): #method just to import the signals
    	import shop.signals
