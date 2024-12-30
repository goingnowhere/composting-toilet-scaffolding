# This defines a Single Sided Clip Class It can be run as a
# FreeCAD macro to display the clip for basic testing
# illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from fittings import Single_Sided_Clip




## Draw Fitting
###############        

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple single male swivel
single_sided_clip_1 = Single_Sided_Clip(freecad_document = document,
                               fitting_label = "Single_Sided_Clip_1")
