from cars import Car

question = "Перечислите авто, информация по которым вам нужна?"
res_car = Car(question)
res_car.show_question()
print('Нажмите на "E" для завершения вопросов')
while True:
    response = input("Авто: ")
    if response == "E":
        break
    res_car.save_response(response)

print("Спасибо за ответы! Всего хорошего!")
res_car.show_result()