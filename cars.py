class Car:
    '''Сбор информаций по машинам'''

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def save_response(self, new_response):
        self.responses.append(new_response)

    def show_result(self):
        print("Полученная информация: ")
        for response in self.responses:
            print('- ' + response)