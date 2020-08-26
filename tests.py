import unittest
from solution import InventoryAllocator

class InventoryAllocatorTest(unittest.TestCase):

	# test happy case of exact inventory match
	def test_exact_match(self):
		inventory_allocator = InventoryAllocator()

		order = {'apple': 1}
		warehouses = [{'name': 'owd', 'inventory': {'apple': 1}}]
		expected_result = [{'owd': {'apple': 1}}]

		self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)

	# test when no enough inventory
	def test_not_enough_inventory(self):
		inventory_allocator = InventoryAllocator()

		order = {'apple': 1}
		warehouses = [{'name': 'owd', 'inventory': {'apple': 0}}]
		expected_result = []

		self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)

	# test when should split an item across warehouses
	def test_split_warehouses(self):
		inventory_allocator = InventoryAllocator()

		order = {'apple': 10}
		warehouses = [
			{'name': 'owd', 'inventory': {'apple': 5}},
			{'name': 'dm', 'inventory': {'apple': 5}}
		]
		expected_result = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]

		self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)

	# test for no order input
	def test_no_order(self):
		inventory_allocator = InventoryAllocator()

		order = {}
		warehouses = [{'name': 'owd', 'inventory': {'apple': 1}}]
		expected_result = []

		self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)

	# test for no warehouse input
	def test_no_warehouses(self):
		inventory_allocator = InventoryAllocator()

		order = {'apple': 1}
		warehouses = []
		expected_result = []

		self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)

	# test for no input at all
	def test_no_input(self):
		inventory_allocator = InventoryAllocator()

		order = {}
		warehouses = []
		expected_result = []

		self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)


	# test when order has 0 count items
	def test_order_exists_0_count(self):
		inventory_allocator = InventoryAllocator()

		order = {'apple': 0, 'banana': 5}
		warehouses = [
			{'name': 'owd', 'inventory': {'apple': 5}},
			{'name': 'dm', 'inventory': {'banana': 5}}
		]
		expected_result = [{'dm': {'banana': 5}}]

		self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)

		# test when inventory in warehouse has 0 count items
		def test_warehouse_exists_0_count(self):
			inventory_allocator = InventoryAllocator()

			order = {'apple': 0, 'banana': 5}
			warehouses = [
				{'name': 'owd', 'inventory': {'apple': 5,'banana': 0}},
				{'name': 'dm', 'inventory': {'banana': 5}}
			]
			expected_result = [{'dm': {'banana': 5}}]

			self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)

	# test when order has an item that the inventory does not have
	def test_no_item_match(self):
		inventory_allocator = InventoryAllocator()

		order = {'apple': 5, 'banana': 1}
		warehouses = [
			{'name': 'owd', 'inventory': {'apple': 5}},
		]
		expected_result = []

		self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)

	# test when order items are less than inventory in warehouses
	def test_less_items(self):
		inventory_allocator = InventoryAllocator()

		order = {'apple': 5, 'banana': 3}
		warehouses=[{'name': 'owd', 'inventory': { 'apple': 0, 'banana': 10}},
			{'name': 'dm', 'inventory': { 'apple': 10, 'orange': 2}},
		]
		expected_result = [
			{'owd': {'banana': 3}},
			{'dm': {'apple': 5}},
		]

		self.assertEqual(inventory_allocator.get_inventory_allocator(order, warehouses), expected_result)



if __name__ == '__main__':
	unittest.main()