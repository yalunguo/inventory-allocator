class InventoryAllocator:

    def get_inventory_allocator(self, order, warehouses):
        ans = []

        for warehouse in warehouses:
            allocation = {}  # initialize inventory allocation as empty for each warehouse
            for item, quantity in order.items():
                if quantity == 0: # pass item if quantity needed is zero
                    continue
                # when item can be shipped from warehouse
                if item in warehouse['inventory'] and warehouse['inventory'][item]>0:
                    allocation[item] = min(quantity, warehouse['inventory'][item])
                    order[item] -= min(quantity, warehouse['inventory'][item])  # update left quanties needed
            if allocation:
                ans.append({warehouse['name']: allocation})

        # If there are still unfulfilled orders, no allocations
        if order and max(list(order.values()))>0:
            return []

        return ans
