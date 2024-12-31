# This FreeCAD script makes a Short T Fitting 
# for basic testing and illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from fittings import Short_T

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
short_t = Short_T(freecad_document = document,
                               fitting_label = "SShort_T")
