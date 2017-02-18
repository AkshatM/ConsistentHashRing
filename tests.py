import uuid
import random
import unittest
from chr import ConsistentHashRing

class StandardBehaviourTestCase(unittest.TestCase):

    '''

    Conditions to check:
    
    1. Does binary tree correctly get instantiated as None or with a value?
    2. Does addition of a node to a node with no children work? Is the order correct?
    3. Does addition of a node to a node with multiple children work? Is the order correct?
    4. Does deletion of a node with no children work? Is the order correct?
    5. Does deletion of a node with one child work? Is the order correct?
    6. Does deletion of a node with two children work? Is the order correct?
    7. Does searching for best match return closest upper bound, including exact match?
    8. Does searching for best match return lowest number if match is higher than all numbers?

    Types of Inputs:

        1) Signed integers. This allows us to test against a known, predictable hash order.
        2) Strings. This allows us to test invariants against an unpredictable hash order.
    '''

    def setUp(self):

        self.consistentRingWithSignedInputs = ConsistentHashRing()
        self.consistentRingWithStringInputs = ConsistentHashRing()

        # http://stackoverflow.com/questions/10130454/why-do-1-and-2-both-hash-to-2-in-cpython 
        self.test_number_range = list(range(-20, 20))
        self.test_number_range.remove(-1)

        self.list_of_unique_strings = [uuid.uuid4() for _ in range(10)]
        self.list_of_unique_strings.sort(key = lambda string: hash(string))

    def testcase_1(self):

        '''
        Can we handle pure addition of nodes?

        We test by inserting a series of numbers and strings into each corresponding hash ring, and 
        testing if the overall in-order traversal is preserved. This simultaneously tests all known
        conditions: if the ring is empty, if a node in the tree has no child, one child or two children.
        '''

        self.assertIsNone(self.consistentRingWithSignedInputs.head)
        self.assertIsNone(self.consistentRingWithStringInputs.head) 

        for number in self.test_number_range:
            self.consistentRingWithSignedInputs.add_node(number)

        for string in self.list_of_unique_strings:
            self.consistentRingWithStringInputs.add_node(string)

        self.assertEqual(list(self.consistentRingWithSignedInputs), self.test_number_range)
        self.assertEqual(list(self.consistentRingWithStringInputs), self.list_of_unique_strings)

    def testcase_2(self):

        '''
        Can we handle pure deletion of nodes?

        This assumes testcase_1 has run, and the hash ring's state is unaltered. We test this by
        removing all numbers we have inserted, and checking the hash ring correctly becomes empty.
        This tests deletion when a node has two children, one child, no child and when the node is 
        meant to be empty.
        '''

        for number in self.test_number_range:
            self.consistentRingWithSignedInputs.remove_node(number)

        for string in self.list_of_unique_strings:
            self.consistentRingWithStringInputs.remove_node(string)

        self.assertIsNone(self.consistentRingWithSignedInputs.head)
        self.assertIsNone(self.consistentRingWithStringInputs.head)

    def testcase_3(self):

        '''
        Can we return best matches?     
        '''

        for number in self.test_number_range:
            self.consistentRingWithSignedInputs.add_node(number)

        for string in self.list_of_unique_strings:
            self.consistentRingWithStringInputs.add_node(string)

        number_to_test = random.choice(self.test_number_range)
        string_to_test = random.choice(self.list_of_unique_strings)

        self.assertEqual(self.consistentRingWithSignedInputs.find_best_match(number_to_test), number_to_test)

        self.assertEqual(self.consistentRingWithStringInputs.find_best_match(string_to_test), string_to_test)

        # check if the hash ring is indeed cyclic. Unfortunately, unless we have a way of generating a string with a hash predictably
        # higher than all others, we cannot test it for our string input hash ring.

        number_higher_than_all_numbers, number_lower_than_all_numbers = self.test_number_range[-1] + 1, self.test_number_range[0] - 1
        self.assertEqual(self.consistentRingWithSignedInputs.find_best_match(number_higher_than_all_numbers), self.test_number_range[0])
        

        # check if the hash ring is indeed finds best match by choosing a number lower than all numbers. This should return the lowest
        # number. 

        self.assertEqual(self.consistentRingWithSignedInputs.find_best_match(number_lower_than_all_numbers), self.test_number_range[0])
        

    def tearDown(self):
        
        self.consistentRingWithSignedInputs = None
        self.consistentRingWithStringInputs = None

if __name__ == '__main__':
    unittest.main()
