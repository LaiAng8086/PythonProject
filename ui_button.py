from pip import main
import ui_stackedwidget
def Btn_1_Clicked(main_ui):
    ui_stackedwidget.set_stack_index(main_ui,0)

def Btn_2_Clicked(main_ui):
    print("Btn_2 clicked!")
    ui_stackedwidget.set_stack_index(main_ui,1)
