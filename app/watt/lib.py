def compute_energy(item1, item2, item1_quantity=1):
    """
    compute the amount of item2 for given quantity of item1
    """

    return round(item1_quantity * (item1.power / item2.power), 3)


class ItemCompute(object):
    def __init__(self, base_item, target_item, base_item_quantity=1):
        self.base_item = base_item
        self.target_item = target_item
        self.value = compute_energy(base_item, target_item, base_item_quantity)
        self.current = base_item == target_item


# def get_time(kWh_input, item_to)
#     #TODO Sketch
# # will calculate the duration/distance of item_to can be used according to the kWh_input
#     if() item_to.power_type == "electricity"
#
#     return time_item_to
#
# def get_times(kWh_input, item_to)
# # will calculate the number of times item_to can be used according to the kWh_input
#
#     return times_item_to
#
#
# def get_distance(kWh_input, item_to)
#
#     return km_item_to
