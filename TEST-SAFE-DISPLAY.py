# coding=utf-8
import oscscreen
oscscreen.npysGlobalOptions.ASCII_ONLY = False

class TestApp(oscscreen.NPSAppManaged):
    
    #__TEXT_WIDGET = oscscreen.TitleText
    __TEXT_WIDGET = oscscreen.TextfieldUnicode
    
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        oscscreen.setTheme(oscscreen.Themes.ColorfulTheme)
        F = oscscreen.ActionFormWithMenus(name = "Welcome to Oscscreen",)
        t1 = F.add(self.__class__.__TEXT_WIDGET, name = "Text:", )
        t2 = F.add(self.__class__.__TEXT_WIDGET, name = "Text:", )
        t3 = F.add(self.__class__.__TEXT_WIDGET, name = "Text:", )
        t4 = F.add(self.__class__.__TEXT_WIDGET, name = "Text:", )
        
        m1 = F.add(oscscreen.MultiLine, name = "Mutliline", scroll_exit=True, max_height=5)
        
        me = F.add(oscscreen.MultiLineEdit, name="Testing", autowrap=False)
        
        
        t1.value = u"This is a \n test"
        t2.value = u"This is a é test"
        t3.value = u"This is ∑ a test"
        t1.value = u"Testing tripple width \u3111 stuff."
        t2.value = u"Testing double width stuff \u1000 <- there"
        t4.value = u"another test is \u1D656 this one."
        
        m1.values = [t1.value, t2.value, t3.value, 
                        'another test \u24AF is here',
                        'another test is \u1D666 this one.']
        
        me.value = '\n'.join([t1.value, t2.value, t3.value,
                                'another test is \u1D656 this one.'])
        
        
        # This lets the user play with the Form.
        F.edit()


if __name__ == "__main__":
    App = TestApp()
    App.run()
