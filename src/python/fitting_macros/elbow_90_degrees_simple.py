# This FreeCAD script makes a Short T Fitting 
# for basic testing and illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from fittings import Elbow_90_Degrees

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
two_socket_cross = Elbow_90_Degrees(freecad_document = document,
                               fitting_label = "Elbow_90_Degrees")
