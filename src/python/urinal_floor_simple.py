# This FreeCAD macro script makes a side panel
# for basic testing illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from urinal_floor import Urinal_Floor

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple side outlet T object
urinal_floor = Urinal_Floor(freecad_document = document,
                        structure_label = "Urinal_Floor")