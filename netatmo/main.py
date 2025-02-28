from swiftbarmenu import Menu

from lib import services

menu = Menu()
outdoor_data = services.get_outdoor_measures()
indoor_data = services.get_indoor_measures()
services.display_leader_measures(outdoor_data, indoor_data, menu)

outdoor_menu = menu.add_item(':icloud: Outdoor')
services.display_outdoor_measures(outdoor_data, outdoor_menu)

indoor_menu = menu.add_item(':house: Indoor')
services.display_indoor_measures(indoor_data, indoor_menu)

menu.add_link(':link: Netatmo dashboard', 'https://my.netatmo.com/app/station')

menu.dump()
