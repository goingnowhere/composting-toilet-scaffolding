# This FreeCAD macro script makes a Cabin Back
# for basic testing illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from structures import Cabin_Back

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple side outlet T object
cabin_back = Cabin_Back(freecad_document = document,
                        structure_label = "Cabin_Back")
