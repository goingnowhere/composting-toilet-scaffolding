# This FreeCAD macro script makes a single male swivel object
# for basic testing illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from make_fittings import Single_Male_Swivel

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple single male swivel
single_male_swivel_1 = Single_Male_Swivel(freecad_document = document,
                               fitting_label = "Single_Male_Swivel_1")
