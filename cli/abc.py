#!/usr/bin/env python3
from cement.core import foundation, controller, handler
from cement.core.controller import CementBaseController, expose

# define application controllers
class MyAppBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = "my application does amazing things"
        arguments = [
            (['--base'], dict(help="option under base controller")),
            ]

    @expose(help="base controller default command", hide=True)
    def default(self):
        print("Inside MyAppBaseController.default()")

    @expose(help="another base controller command")
    def command1(self):
        print("Inside MyAppBaseController.command1()")

class SecondController(CementBaseController):
    class Meta:
        label = 'second_controller'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "this is the second controller (stacked/nested on base)"
        arguments = [
            (['--2nd-opt'], dict(help="another option under base controller")),
            ]

    @expose(help="second-controller default command", hide=True)
    def default(self):
        print("Inside SecondController.default()")

    @expose(help="this is a command under the second-controller namespace")
    def command2(self):
        print("Inside SecondController.command2()")



def main():
    try:
        # create the application
        app = foundation.CementApp('myapp')

        # register controllers
        handler.register(MyAppBaseController)
        handler.register(SecondController)
      

        # setup the application
        app.setup()

        # run the application
        app.run()
    finally:
        # close the application
        app.close()

if __name__ == '__main__':
    main()