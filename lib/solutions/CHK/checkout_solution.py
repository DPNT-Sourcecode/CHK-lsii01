

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
        item_base_prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
        }
        item_special_prices = {
            'A': (3, 130),
            'B': (2, 45),
        }

        item_counts = {}
        total = 0
        for item in skus:
            if not item in item_base_prices.keys():
                return -1
            
            item_counts[item] = item_counts.get(item, 0) + 1


            if item in item_special_prices.keys(): #handle special items when count reaches the expected special count
                if item_counts[item] == item_special_prices[item][0]:
                    total += item_special_prices[item][1]
                    item_counts[item] = 0

        for item, count in item_counts.items():
            total += count * item_base_prices[item]
        return total


