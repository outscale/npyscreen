import osc_npyscreen

class MyTestApp(osc_npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm(lines=47))

class MainForm(osc_npyscreen.Form):
    def create(self):
        vl = []
        for x in range(100):
            vl.append("Value %s" % x)
        self.add(osc_npyscreen.MultiSelect, values=vl)

def main():
    TA = MyTestApp()
    TA.run()


if __name__ == '__main__':
    main()
