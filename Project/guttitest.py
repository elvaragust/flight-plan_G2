"""from uiLayer.mainmenu_ui import MainMenu_UI
main_menu = MainMenu_UI()

if __name__ == "__main__":
    main_menu.input_prompt()"""

from uiLayer.mainmenu_ui import MainMenu_UI
from logicLayer.flightL import FlightL  

main_menu = MainMenu_UI()
flight_logic = FlightL() 

if __name__ == "__main__":
    main_menu.input_prompt()

    day = '01/01/2022' 
    employees_not_working = flight_logic.get_employees_not_working(day)
    for employee in employees_not_working:
        print(f"Name: {employee['Name']}, SSN: {employee['SSN']}, Rank: {employee['Rank']}")