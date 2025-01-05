# This FreeCAD macro script makes a double fixing pad object
# for basic testing illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from fittings import Double_Fixing_Pad

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple side outlet T object
double_fixing_pad_1 = Double_Fixing_Pad(freecad_document = document,
                               fitting_label = "Double_Fixing_Pad_1")
