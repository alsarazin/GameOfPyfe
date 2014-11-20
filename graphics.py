from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class PyfeWidget(Widget):
	
	state = NumericProperty(0)

	def on_touch_down(self,touch):
		self.state = (self.state-1)**2
		print self.state

class PyfeApp(App):

	def build(self):
		parent = Widget()
		w = PyfeWidget()
		parent.add_widget(w)
		return parent

if __name__ == '__main__':
	PyfeApp().run()
