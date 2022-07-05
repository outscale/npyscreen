#!/usr/bin/env python
import oscscreen

class TestApp(oscscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F = oscscreen.ActionFormWithMenus(name = "Welcome to Oscscreen",)
        f = F.add(oscscreen.TitleFixedText, name = "Fixed Text:" , value="This is fixed text")
        t = F.add(oscscreen.TitleText, name = "Text:", )
        p = F.add(oscscreen.TitlePassword, name = "Password:")
        fn = F.add(oscscreen.TitleFilename, name = "Filename:")
        dt = F.add(oscscreen.TitleDateCombo, name = "Date:")
        cb = F.add(oscscreen.Checkbox, name = "A Checkbox")
        s = F.add(oscscreen.TitleSlider, out_of=12, name = "Slider")
        ml= F.add(oscscreen.MultiLineEdit, 
            value = """try typing here! Mutiline text, press ^R to reformat.\nPress ^X for automatically created list of menus""", 
            max_height=5, rely=9)
        ms= F.add(oscscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One", 
                values = ["Option1","Option2","Option3"], scroll_exit=True, width=30)
        ms2= F.add(oscscreen.MultiSelect, max_height=4, value = [1,], 
                values = ["Option1","Option2","Option3"], scroll_exit=True, width=20)

        bn = F.add(oscscreen.MiniButton, name = "Button",)
        
        #gd = F.add(oscscreen.SimpleGrid, relx = 42, rely=15, width=20)
        gd = F.add(oscscreen.GridColTitles, relx = 42, rely=15, width=20, col_titles = ['1','2','3','4'])
        gd.values = []
        for x in range(36):
            row = []
            for y in range(x, x+36):
                row.append(y)
            gd.values.append(row)
        
        
        # This lets the user play with the Form.
        F.edit()

if __name__ == "__main__":
    App = TestApp()
    App.run()
