from uiLayer.mainmenu_ui import MainMenu_UI
from dataLayer.logic_data_wrapper import LogicDataWrapper

data_layer = LogicDataWrapper()
main_menu = MainMenu_UI(data_layer)

if __name__ == "__main__":
    main_menu.input_prompt()