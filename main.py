from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from contextvars import ContextVar

Builder.load_file('main_design.kv')

Window.softinput_mode = "below_target"

flag = ContextVar('flag', default=False)

# show/hide the widgets associated with the button


def show(widget1, widget2, widget3, box, button):
    for widget in (widget1, widget2, widget3):
        if widget.opacity == 0:
            if widget == widget3:
                widget.size_hint = 0.1, 0.7
                widget.color = [0, 0, 0, 1]
            else:
                widget.size_hint = 0.6, 0.7
                widget.color = [0, 0, 0, 1]
            widget.opacity = 1
        else:
            widget.size_hint = 0, 0
            widget.opacity = 0
    
    if box.height == 0:
        box.size_hint_y = 0.5
        flag.set(True)

    else:
        box.size_hint_y = None
        box.height = 0
        flag.set(False)



class ImageButton(ButtonBehavior, Image):
    pass


class MainScreen(Screen):

    def select(self, instance, n):
        if instance.focus == True:
            if ' ' in instance.text:
                instance.text = instance.text[:-n]
            Clock.schedule_once(lambda dt: instance.select_all())
        else:
            if instance.text != '' and instance.text != '-' and instance.text != '.' and instance.text != '-.':
                instance.text += ' ' + instance.hint_text


    def fahrenheit(self, f):
        if self.ids.fahrenheit.focus == True:
            self.ids.celzijus.text = ''
            if f != '' and f != '-' and f != '.' and f != '-.':
                self.ids.celzijus.text = str(int((float(f) - 32) * 5 / 9)) + ' °C'

    def celzijus(self, c):
        if self.ids.celzijus.focus == True:
            self.ids.fahrenheit.text = ''
            if c != '' and c != '-' and c != '.' and c != '-.':
                self.ids.fahrenheit.text = str(int((float(c) * 9 / 5) + 32)) + ' °F'

    def miles(self,miles):
        if self.ids.miles.focus == True:
            self.ids.kilometar.text = ''
            if miles != '' and miles != '.' and '-' not in miles:
                self.ids.kilometar.text = '{:.2f}'.format(float(miles) * 1.60934) + ' kilometara'

    def kilometar(self,kilometar):
        if self.ids.kilometar.focus == True:
            self.ids.miles.text = ''
            if kilometar != '' and kilometar != '.' and '-' not in kilometar:
                self.ids.miles.text = '{:.2f}'.format(float(kilometar) / 1.60934) + ' miles'

    def feet(self,ft):
        if self.ids.feet.focus == True:
            self.ids.metar11.text = ''
            if ft!= '' and ft != '.' and '-' not in ft:
                self.ids.metar11.text = '{:.2f}'.format(float(ft) * 0.3048) + ' metara'

    def metar11(self,metar):
        if self.ids.metar11.focus == True:
            self.ids.feet.text = ''
            if metar != '' and metar != '.' and '-' not in metar:
                self.ids.feet.text = '{:.2f}'.format(float(metar) / 0.3048) + ' feet'

    def gallon(self,gallon):
        if self.ids.gallon.focus == True:
            self.ids.litra.text = ''
            if gallon!= '' and gallon != '.' and '-' not in gallon:
                self.ids.litra.text = '{:.2f}'.format(float(gallon) * 3.785411784) + ' litra'

    def litra(self,litra):
        if self.ids.litra.focus == True:
            self.ids.gallon.text = ''
            if litra != '' and litra != '.' and '-' not in litra:
                self.ids.gallon.text = '{:.2f}'.format(float(litra) / 3.785411784) + ' gallons'

    def pound(self,pound):
        if self.ids.pound.focus == True:
            self.ids.kilogram5.text = ''
            if pound!= '' and pound != '.' and '-' not in pound:
                self.ids.kilogram5.text = '{:.2f}'.format(float(pound) * 0.453592) + ' kilograma'

    def kilogram5(self,kg):
        if self.ids.kilogram5.focus == True:
            self.ids.pound.text = ''
            if kg != '' and kg != '.' and '-' not in kg:
                self.ids.pound.text = '{:.2f}'.format(float(kg) / 0.453592) + ' pound'

    def hvat(self, hvat):
        if self.ids.hvat.focus == True:
            self.ids.metar.text = ''
            if hvat != '' and hvat != '.' and '-' not in hvat:
                self.ids.metar.text = '{:.2f}'.format(float(hvat) * 3.59665) + ' metara kvadratnih'

    def metar(self, metar):
        if self.ids.metar.focus == True:
            self.ids.hvat.text = ''
            if metar != '' and metar != '.' and '-' not in metar:
                self.ids.hvat.text = '{:.2f}'.format(float(metar) / 3.59665) + ' hvati'

    def ral(self, ral):
        if self.ids.ral.focus == True:
            self.ids.metar2.text = ''
            if ral != '' and ral != '.' and '-' not in ral:
                self.ids.metar2.text = '{:.2f}'.format(float(ral) * 5754.642) + ' metara kvadratnih'

    def metar2(self, metar2):
        if self.ids.metar2.focus == True:
            self.ids.ral.text = ''
            if metar2 != '' and metar2 != '.' and '-' not in metar2:
                self.ids.ral.text = '{:.2f}'.format(float(metar2) / 5754.642) + " jutra/rala"

    def lanac(self, metar5):
        if self.ids.lanac.focus == True:
            self.ids.metar3.text = ''
            if metar5 != '' and metar5 != '.' and '-' not in metar5:
                self.ids.metar3.text = '{:.2f}'.format(float(metar5) * 7193.3) + ' metara kvadratnih'

    def metar3(self, m):
        if self.ids.metar3.focus == True:
            self.ids.lanac.text = ''
            if m != '' and m != '.' and '-' not in m:
                self.ids.lanac.text = '{:.2f}'.format(float(m) / 7193.3) + ' lanaca'

    def dulum(self, dulum):
        if self.ids.dulum.focus == True:
            self.ids.metar4.text = ''
            if dulum != '' and dulum != '.' and '-' not in dulum:
                self.ids.metar4.text = '{:.2f}'.format(float(dulum) * 1000) + ' metara kvadratnih'

    def metar4(self, metar4):
        if self.ids.metar4.focus == True:
            self.ids.dulum.text = ''
            if metar4 != '' and metar4 != '.' and '-' not in metar4:
                self.ids.dulum.text = '{:.2f}'.format(float(metar4) / 1000) + ' duluma'

    def dan_oranja(self, dan_oranja):
        if self.ids.dan_oranja.focus == True:
            self.ids.metar5.text = ''
            if dan_oranja != '' and dan_oranja != '.' and '-' not in dan_oranja:
                self.ids.metar5.text = '{:.2f}'.format(float(dan_oranja) * 4000) + ' metara kvadratnih'
    
    def metar5(self, metar5):
        if self.ids.metar5.focus == True:
            self.ids.dan_oranja.text = ''
            if metar5 != '' and metar5 != '.' and '-' not in metar5:
                self.ids.dan_oranja.text = '{:.2f}'.format(float(metar5) / 4000) + ' dana oranja'

    
    def show_temp(self):
        if flag.get() == True:
            if self.ids.layout_dist1.height != 0:
                flag.set(False)
                self.show_dist()
        show(self.ids.fahrenheit, self.ids.celzijus, self.ids.equal_temp, 
        self.ids.layout_temp, self.ids.imper_metric)
        show(self.ids.miles, self.ids.kilometar, self.ids.equal_con11, 
        self.ids.layout_con11, self.ids.imper_metric)
        show(self.ids.feet, self.ids.metar11, self.ids.equal_con12, 
        self.ids.layout_con12, self.ids.imper_metric)
        show(self.ids.gallon, self.ids.litra, self.ids.equal_con13, 
        self.ids.layout_con13, self.ids.imper_metric)
        show(self.ids.pound, self.ids.kilogram5, self.ids.equal_con14, 
        self.ids.layout_con14, self.ids.imper_metric)
        self.ids.fahrenheit.text = ''
        self.ids.celzijus.text = ''
        self.ids.miles.text = ''
        self.ids.kilometar.text = ''
        self.ids.feet.text = ''
        self.ids.metar11.text = ''
    
    
    def show_dist(self):
        if flag.get() == True:
            if self.ids.layout_temp.height != 0:
                flag.set(False)
                self.show_temp()
        show(self.ids.hvat, self.ids.metar, self.ids.equal_dist1, 
        self.ids.layout_dist1, self.ids.distance)
        show(self.ids.ral, self.ids.metar2, self.ids.equal_dist2, 
        self.ids.layout_dist2, self.ids.distance)
        show(self.ids.lanac, self.ids.metar3, self.ids.equal_dist3, 
        self.ids.layout_dist3, self.ids.distance)
        show(self.ids.dulum, self.ids.metar4, self.ids.equal_dist4, 
        self.ids.layout_dist4, self.ids.distance)
        show(self.ids.dan_oranja, self.ids.metar5, self.ids.equal_dist5, 
        self.ids.layout_dist5, self.ids.distance)
        self.ids.hvat.text = ''
        self.ids.metar.text = ''
        self.ids.ral.text = ''
        self.ids.metar2.text = ''
        self.ids.lanac.text = ''
        self.ids.metar3.text = ''
        self.ids.dulum.text = ''
        self.ids.metar4.text = ''
    

sm = ScreenManager(transition=NoTransition())
sm.add_widget(MainScreen(name='main_screen'))



class MainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MainApp().run()
