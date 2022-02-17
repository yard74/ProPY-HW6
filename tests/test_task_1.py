import unittest
from functionsHW import get_doc_owner_name, get_shelf_number, get_docs_list, put_new_doc, delete_doc


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.docs = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        self.doc = '11-2'
        self.wrong_doc = '11'
        self.shelves = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
        }

    def test_get_doc_owner_name(self):
        test_cases = [
            {
                'arguments': {'docs': self.docs, 'doc_number': self.doc},
                'exp_result': 'Геннадий Покемонов'
            },
            {
                'arguments': {'docs': self.docs, 'doc_number': self.wrong_doc},
                'exp_result': 'Человека с таким документом нет в системе.'
            }
        ]
        for test_case in test_cases:
            result = get_doc_owner_name(**test_case['arguments'])
            self.assertEqual(test_case['exp_result'], result)

    def test_get_shelf_number(self):
        test_cases = [
            {
                'arguments': {'shelves': self.shelves, 'doc_number': self.doc},
                'exp_result': '1'
            },
            {
                'arguments': {'shelves': self.shelves, 'doc_number': self.wrong_doc},
                'exp_result': 'Документ отсутствует в системе.'
            }
        ]
        for test_case in test_cases:
            result = get_shelf_number(**test_case['arguments'])
            self.assertEqual(test_case['exp_result'], result)

    def test_get_docs_list(self):
        i = 0
        while i < len(self.docs):
            doc = self.docs[i]
            i += 1
            result = get_docs_list([doc])
            exp_result = str(f'{doc["type"]} {doc["number"]} {doc["name"]}')
            self.assertEqual(exp_result, result)

    def test_put_new_doc(self):
        test_cases = [
            {
                'arguments': {
                    'docs': self.docs,
                    'shelves': self.shelves,
                    'doc_type': 'pasport',
                    'doc_number': '6611 502347',
                    'doc_name': 'Максим Волков',
                    'shelf_number': '3'
                },
                'exp_result': 'Новый документ добавлен'
            },
            {
                'arguments': {
                    'docs': self.docs,
                    'shelves': self.shelves,
                    'doc_type': 'pasport',
                    'doc_number': '5148 101299',
                    'doc_name': 'Кристина Орлова',
                    'shelf_number': '7'
                },
                'exp_result': 'Полки с таким номером не существует. Документ не добавлен.'
            }
        ]
        for test_case in test_cases:
            result = put_new_doc(**test_case['arguments'])
            self.assertEqual(test_case['exp_result'], result)

    def test_delete_doc(self):
        test_cases = [
            {
                'arguments': {'docs': self.docs, 'shelves': self.shelves, 'doc_number': self.doc},
                'exp_result': 'Документ успешно удален.'
            },
            {
                'arguments': {'docs': self.docs, 'shelves': self.shelves, 'doc_number': self.wrong_doc},
                'exp_result': 'Документа c таким номером не существует.'
            }
        ]
        for test_case in test_cases:
            result = delete_doc(**test_case['arguments'])
            self.assertEqual(test_case['exp_result'], result)


if __name__ == '__main__':
    unittest.main()
