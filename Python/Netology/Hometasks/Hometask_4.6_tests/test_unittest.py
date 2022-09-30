import unittest
from unittest.mock import patch
import mock
import builtins
from parameterized import parameterized
from main import check_document_existance,delete_doc, append_doc_to_shelf, get_doc_owner_name, directories,add_new_shelf, remove_doc_from_shelf, documents  

  


class TestFuncion (unittest.TestCase):
    @parameterized.expand(['1', '11-2', '112', '2207 876234', '2208 876234'])     
    def test_check_document_existance(self, a):
        result = check_document_existance(a)
        self.assertTrue(result)
    
    # @parameterized.expand(['1', '11-2', '5', '2207 876234'])
    # def test_get_doc_owner_name(self,a):
    #     result = get_doc_owner_name(a)
    #     self.assertTrue(result)
    
    # @parameterized.expand(['1', '3', '5', '6'])
    # def test_add_new_shelf(self,a):
    #     result = add_new_shelf(a)
    #     self.assertTrue(result)
        
    # @parameterized.expand(['1','11-2', '2207 876234', '2207 976234'])
    # def test_remove_doc_from_shelf(self, a):
    #     result = remove_doc_from_shelf (a)
    #     self.assertTrue(result)
        
    # @parameterized.expand([('1/45', '1'), ('2/45', '5'), ('111-2', '3') ])
    # def test_append_doc_to_shelf(self, doc_number, shelf_number):
    #       result = append_doc_to_shelf(doc_number, shelf_number)
    #       self.assertTrue(result)
     
    # @parameterized.expand(['1', '11-2', '5', '2207 876234'])
    # def test_delete_doc(self, user_doc_number):
    #       result = delete_doc(user_doc_number)
    #       self.assertTrue(result)
             
         
    

  
     
if __name__ == "__main__":
    unittest.main()

# включаем для Теста 3
# directories.pop('5')
# directories.pop('6')

# # включаем для Теста 4
# directories['1'].extend(['11-2', '2207 876234'])

# # включаем для Теста 5
# directories.pop('5')
# directories['1'].remove('1/45')
# directories['3'].remove('111-2')

# # включаем для Теста 6
# directories['1'].extend(['11-2', '2207 876234'])
# documents.extend([
#     {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#     {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#     ])

# print(directories)
# print(documents)