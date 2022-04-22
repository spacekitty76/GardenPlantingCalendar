"""Plant Parent Classes."""

# TODO: Flowers

class Vegetable:
    def __init__(self, base_name, optimal_temp, company_name = None, variety_name = None, days_to_maturity = None, owned = None):
        """
            base_name (str): Ex: 'broccoli, tomato, etc.'
            optimal_temp (list[int]): Optimal temp for growth. The two items in the list should be high and low temp.
                NOTE: This is the optimal temp for germination. And probably also growth.
            company_name (str): Where the seed was bought. URL link to seed.
            variety_name (str): Ex: 'Gai Lan / Chinese Broccoli - Blue Star'
            days_to_maturity (list[int]): Days until harvest. First number lowest, second highest
            owned (bool): Whether I own a packet of these
        """
        self.base_name = base_name
        self.optimal_temp = optimal_temp
        self.company_name = company_name
        self.variety_name = variety_name
        self.days_to_maturity = days_to_maturity
        self.owned = owned