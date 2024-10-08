#!/usr/bin/env python
# encoding: utf-8
import curses
import osc_npyscreen
#osc_npyscreen.disableColor()

class SyntaxTest(osc_npyscreen.Textfield):
    def update_highlighting(self, start, end):
        # highlighting color
        hl_color  = self.parent.theme_manager.findPair(self, 'IMPORTANT')
        hl_colorb = self.parent.theme_manager.findPair(self, 'WARNING')
        hl_colorc = self.parent.theme_manager.findPair(self, 'CRITICAL')
        
        self._highlightingdata = [curses.A_BOLD, 
                        curses.A_BOLD,
                        hl_color,
                        hl_color,
                        hl_color,
                        hl_color,
                        hl_colorb,
                        hl_colorb,
                        hl_colorc,
                        hl_colorc,
                        hl_colorc,
                        hl_colorc,
        ]

#class SyntaxTestMultiline(osc_npyscreen.MultiLineEdit):
#    def update_highlighting(self, start, end):
#        self._highlightingdata = [curses.A_BOLD, curses.A_BOLD, curses.A_BOLD]



class TestApp(osc_npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F = osc_npyscreen.Form(name = "Welcome to Oscscreen",)
        t = F.add(SyntaxTest, name = "Text:",)
        t.syntax_highlighting = True
        ml= F.add(osc_npyscreen.MultiLineEdit, 
            value = """try typing here!\nMutiline text, press ^R to reformat.\n""", 
            max_height=5, rely=9)
        ml.syntax_highlighting = True
        
        # This lets the user play with the Form.
        F.edit()


if __name__ == "__main__":
    App = TestApp()
    App.run()   
