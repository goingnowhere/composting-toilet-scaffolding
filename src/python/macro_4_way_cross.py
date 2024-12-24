# This FreeCAD macro script makes a single 4 way cross object
# for basic testing illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from make_fittings import Four_Way_Cross

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple side outlet T object
Four_Way_Cross_1 = Four_Way_Cross(freecad_document = document,
                               fitting_label = "Four_Way_Cross_1")