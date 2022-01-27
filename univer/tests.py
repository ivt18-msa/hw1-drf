from rest_framework.test import APITestCase


class StudentApiTests(APITestCase):
    def test_get_students(self):
        res = self.client.get('/students/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['count'], 0)

    def test_post_students(self):
        new_stud = {
            'last_name': 'Иванов',
            'first_name': 'Иван',
            'second_name': 'Иванович',
            'id_number': '123456',
        }
        res = self.client.post('/students/', new_stud)
        self.assertEqual(res.status_code, 201)
        self.assertGreater(res.data['id'], 0)
        temp = res.data
        temp.pop('id')
        temp.pop('grade_set')
        self.assertEqual(temp, new_stud)
        
        res = self.client.get('/students/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['count'], 1)
