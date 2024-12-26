# This FreeCAD macro script makes a single double sided collar object
# for basic testing illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from make_fittings import Double_Sided_Collar

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple side outlet T object
double_sided_collar_1 = Double_Sided_Collar(freecad_document = document,
                               fitting_label = "Double_Sided_Collar_1")
