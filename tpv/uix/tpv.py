# -*- coding: utf-8 -*-
from kivy.uix.anchorlayout import AnchorLayout
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty
from shared.botonera import Botonera
from shared.utils import json_to_list
from uix.pedidowidget import PedidoWidget
from kivy.clock import Clock



class Inicio(AnchorLayout):
    onPress = ObjectProperty(None, allownone=True)
    def __init__(self, **kargs):
        super(Inicio, self).__init__(**kargs)
        self.botonera = Botonera(onPress=self.onPress)
        self.crear_inicio()
        self.add_widget(self.botonera)

    def crear_inicio(self):
        self.botonera.completo = True
        src = JsonStore('db/clases.json')
        src = json_to_list(src['db'].get('lista'))
        src.append({"text": "Abrir cajón", "tipo": "abri_cajon",
                    "color": "#BDBDBD"})
        self.botonera.botones = src
        self.botonera.titulo = "Bienvenido"


class Tpv(AnchorLayout):

    def __init__(self, **kargs):
        super(Tpv, self).__init__(**kargs)
        self.inicio = Inicio(onPress=self.onPress_seccion)
        self.pedido = PedidoWidget(tpv=self)
        self.add_widget(self.inicio)
        Clock.schedule_interval(self.enviar_pedido, .5)

    def onPress_seccion(self, boton):
        tipo = boton.tag.get('tipo')
        if tipo == 'clase':
            self.remove_widget(self.inicio)
            self.add_widget(self.pedido)
            self.pedido.nuevo_pedido(boton.tag)
        elif tipo == "abrir_cajon":
            self.abrir_cajon()

    def abrir_cajon(self):
        pass

    def enviar_pedido(self, pd):
        pass

    def mostrar_inicio(self):
        self.remove_widget(self.pedido)
        self.add_widget(self.inicio)
