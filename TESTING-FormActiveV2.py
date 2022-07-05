#!/usr/bin/env python
# encoding: utf-8

import oscscreen
import curses

#oscscreen.disableColor()
class TestApp(oscscreen.NPSApp):
    def main(self):
        #self.test_memory_use()
        self.test()
    
    def test(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = oscscreen.ActionFormV2WithMenus(name = "Welcome to Oscscreen",)

        ms = F.add(oscscreen.MultiLineActionWithShortcuts, max_height=4, value = [1,], name="Pick One", 
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        
        root = F.new_menu()
        root.addItem('test', curses.beep)
        
        # This lets the user play with the Form.
        F.edit()

    def test_memory_use(self):
        n = 0 
        while 1:
            F  = oscscreen.fmActionFormV2.ActionFormV2(name = "Welcome to Oscscreen %s" % n)
            #F  = oscscreen.ActionForm(name = "Welcome to Oscscreen %s" % n)
            
            ms = F.add(oscscreen.MultiLineActionWithShortcuts, max_height=4, value = [1,], name="Pick One", 
                    values = ["Option1","Option2","Option3"], scroll_exit=True)
        
            F.display()
            n +=1
if __name__ == "__main__":
    App = TestApp()
    App.run()   
