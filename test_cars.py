import unittest
from cars import Car

class TestCars(unittest.TestCase):

    def setUp(self) -> None:
        question = "Перечислите авто, информация по которым вам нужна?"
        self.res_car = Car(question)
        self.responses = ['Audi', 'BMW', 'Nissan', 'Skoda']

    def test_save_single_response(self):
        self.res_car.save_response(self.responses[0])
        self.assertIn(self.responses[0], self.res_car.responses)

    def test_save_three_response(self):
        for response in self.responses:
            self.res_car.save_response(response)
        for response in self.responses:
            self.assertIn(response, self.res_car.responses)

    @unittest.expectedFailure
    def test_save_null_response(self):
        self.assertEqual(self.responses == 0, True)

    def test_not_save_response(self):
        try:
            c1 = self.responses
            c2 = "BMW"

            self.assertNotIn(c2, c1, "% s содержится в% s " % (c2, c1))
        except AssertionError as e:
                print(e)

if __name__ == '__main__':
    unittest.main()
