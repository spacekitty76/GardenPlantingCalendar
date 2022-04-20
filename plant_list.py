"""Cool weather plants."""

import plants

plant_list = []

gai_lan_chinese_broccoli_blue_star = plants .Vegetable(base_name="Broccoli", optimal_temp=[65, 75],
    company_name="https://deepharvestfarm.com/product/blue-star-gai-lan/", variety_name="gai_lan_chinese_broccoli_blue_star",
    days_to_maturity=[50, 60])
plant_list.append(gai_lan_chinese_broccoli_blue_star)

cabbage_primax = plants.Vegetable(base_name="Cabbage", optimal_temp=[65, 80],
    company_name="https://deepharvestfarm.com/product/primax-cabbage/", variety_name="Primax", days_to_maturity=[60, 70])
plant_list.append(cabbage_primax)

red_rubine_brussels_sprouts = plants.Vegetable(base_name="Brussels Sprouts", optimal_temp=[50, 75],
    company_name="https://www.rareseeds.com/store/vegetables/brussels-sprouts/red-rubine-brussels-sprout",
    variety_name="Red Rubine", days_to_maturity=[90])
plant_list.append(red_rubine_brussels_sprouts)

tete_noire_cabbage = plants.Vegetable(base_name="Cabbage", optimal_temp=[50, 75],
    company_name="https://www.rareseeds.com/store/vegetables/fall-favorites/tete-noire-cabbage",
    variety_name="Tete noire", days_to_maturity=[65])
plant_list.append(tete_noire_cabbage)

frisee_endive = plants.Vegetable(base_name="Endive", optimal_temp=[45, 75],
    company_name="https://www.rareseeds.com/store/vegetables/endive-and-escarole/frisee-endive-or-curly-endive",
    variety_name="Frisee", days_to_maturity=[50])
plant_list.append(frisee_endive)

alexandria_alpine_strawberry = plants.Vegetable(base_name="Strawberry", optimal_temp=[60, 75],
    company_name="https://www.rareseeds.com/store/vegetables/garden-berries/alexandria-alpine-strawberry",
    variety_name="Alexandria Alpine", days_to_maturity=[120])
plant_list.append(alexandria_alpine_strawberry)

for item in plant_list:
    print("==========================================================")
    print(f"base: {item.base_name}")
    print(f"variety: {item.variety_name}")
    print(f"optimal_temp: {item.optimal_temp}")
    print(f"maturity: {item.days_to_maturity}")
    print("==========================================================")

