import osc_npyscreen

class myEmployeeForm(osc_npyscreen.Form):
    def afterEditing(self):
        self.parentApp.NEXT_ACTIVE_FORM = None

    def create(self):
       self.myName        = self.add(osc_npyscreen.TitleText, name='Name')
       self.myDepartment = self.add(osc_npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
       self.myDate        = self.add(osc_npyscreen.TitleDateCombo, name='Date Employed')

class MyApplication(osc_npyscreen.NPSAppManaged):
   def onStart(self):
       self.addForm('MAIN', myEmployeeForm, name='New Employee')
       # A real application might define more forms here.......

if __name__ == '__main__':
   TestApp = MyApplication().run()

