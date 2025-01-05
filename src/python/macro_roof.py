# This FreeCAD macro script makes a Cabin Partition
# for basic testing illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

def display_variable(name, value):
    App.Console.PrintMessage(name)
    App.Console.PrintMessage(": ")
    App.Console.PrintMessage(value)
    App.Console.PrintMessage("\n")

# from pathlib import Path
# import os
# cwd = Path.cwd()
# display_variable("cwd", cwd)
# macro_directory = os.path.dirname(os.path.abspath(__file__))
# display_variable("macro_directory", macro_directory)
# user_macro_directory = App.getUserMacroDir(True)
# display_variable("user_macro_directory", user_macro_directory)

from structures import Roof

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")




# Draw a simple side outlet T object
roof = Roof(freecad_document = document,
                        structure_label = "Roof")
