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

frisee_endive = plants.Vegetable(base_name="Endive", optimal_temp=[45, 75],
    company_name="https://www.rareseeds.com/store/vegetables/endive-and-escarole/frisee-endive-or-curly-endive",
    variety_name="Frisee", days_to_maturity=[50])
plant_list.append(frisee_endive)

alexandria_alpine_strawberry = plants.Vegetable(base_name="Strawberry", optimal_temp=[60, 75],
    company_name="https://www.rareseeds.com/store/vegetables/garden-berries/alexandria-alpine-strawberry",
    variety_name="Alexandria Alpine", days_to_maturity=[120])
plant_list.append(alexandria_alpine_strawberry)

banana_pepper = plants.Vegetable(base_name="Pepper", optimal_temp=[60, 75],
    variety_name="Banana Pepper", days_to_maturity=[60, 75], owned=True)
plant_list.append(banana_pepper)

kale_blue = plants.Vegetable(base_name="Kale", optimal_temp=[45, 85],
    variety_name="Dazzling Blue Kale", days_to_maturity=[0, 95], owned=True)
plant_list.append(kale_blue)

autumn_giant_leek = plants.Vegetable(base_name="Leek", optimal_temp=[45, 80],
    variety_name="Autumn Giant Leek", days_to_maturity=[100, 120], owned=True)
plant_list.append(autumn_giant_leek)

green_tatsoi = plants.Vegetable(base_name="Tatsoi", optimal_temp=[60, 80],
    variety_name="Green Tatsoi", days_to_maturity=[50, 55], owned=True)
plant_list.append(green_tatsoi)
 
koral_carrot = plants.Vegetable(base_name="Carrot", optimal_temp=[50, 75],
    variety_name="Koral", days_to_maturity=[75], owned=True)
plant_list.append(koral_carrot)

anaheim_pepper = plants.Vegetable(base_name="Pepper", optimal_temp=[70, 95],
    variety_name="anaheim hot", days_to_maturity=[80], owned=True)
plant_list.append(anaheim_pepper)

chijimisai = plants.Vegetable(base_name="Greens", optimal_temp=[60, 80],
    variety_name="Chijimisai", days_to_maturity=[55], owned=True)
plant_list.append(chijimisai)

yod_fa = plants.Vegetable(base_name="Broccoli", optimal_temp=[60, 80],
    variety_name="Yod Fa Chinese Brocolli", days_to_maturity=[55], owned=True)
plant_list.append(yod_fa)

tete_cabbage = plants.Vegetable(base_name="Cabbage", optimal_temp=[50, 75],
    variety_name="Tete Noire Cabbage", days_to_maturity=[65], owned=True)
plant_list.append(tete_cabbage)

blot_pepper = plants.Vegetable(base_name="Pepper", optimal_temp=[70, 95],
    variety_name="Blot Pepper", days_to_maturity=[60, 90], owned=True)
plant_list.append(blot_pepper)

five_color_chard = plants.Vegetable(base_name="Swiss Chard", optimal_temp=[50, 75],
    variety_name="Five Color Silver Beet", days_to_maturity=[60], owned=True)
plant_list.append(five_color_chard)

rugosa_squash = plants.Vegetable(base_name="Squash", optimal_temp=[70, 95],
    variety_name="Rugosa Friulana Squash", days_to_maturity=[60], owned=True)
plant_list.append(rugosa_squash)

zucchino_squash = plants.Vegetable(base_name="Squash", optimal_temp=[70, 95],
    variety_name="Zucchino Rampicante Squash", days_to_maturity=[70], owned=True)
plant_list.append(rugosa_squash)


for item in plant_list:
    print("==========================================================")
    print(f"base: {item.base_name}")
    print(f"variety: {item.variety_name}")
    print(f"optimal_temp: {item.optimal_temp}")
    print(f"maturity: {item.days_to_maturity}")
    print(f"owned: {item.owned}")
    print("==========================================================")

