# This FreeCAD macro script makes a side panel
# for basic testing illustration purposes

#  Import the packages that we need
import FreeCAD as App
import FreeCADGui as Gui

from make_side_panel import Side_Panel
from make_fittings import display_variable

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple side outlet T object
side_panel = Side_Panel(freecad_document = document,
                        structure_label = "Side_Panel")
display_variable("ground_front_left", side_panel.ground_front_left)
display_variable("ground_front_right", side_panel.ground_front_right)
