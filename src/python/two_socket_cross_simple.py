# This FreeCAD script makes a Short T Fitting 
# for basic testing and illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from fittings import Two_Socket_Cross

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
two_socket_cross = Two_Socket_Cross(freecad_document = document,
                               fitting_label = "Two_Socket_Cross")
