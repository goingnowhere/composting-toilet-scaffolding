# This FreeCAD macro script makes a Double Sided Clip object
# for basic testing illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from fittings import Double_Sided_Clip

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple single male swivel
double_sided_clip_1 = Double_Sided_Clip(freecad_document = document,
                               fitting_label = "Double_Sided_Clip_1")
