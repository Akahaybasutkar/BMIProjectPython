class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        self.height = self.height * 0.01
        self.age = None
        self.activity = None
        self.gender = None
        self.reqCalorie = None
        self.Bmi = None

    def changeDetails(self, n, w, h):
        self.name = n
        self.weight = w
        self.height = h

    def setDetails(self):
        print("Please Enter your Details of", self.name)
        self.age = int(input("Please enter your age: "))
        self.activity = int(input("Please enter the number of times you exercise weekly: "))
        self.gender = input("Enter your gender: ")

    def getInfo(self):
        print()
        print("Details of", self.name)
        print(f"Name: {self.name}\nHeight: {self.height}M\nWeight: {self.weight}")
        print(f"Age: {self.age}\nGender: {self.gender}\nWeekly Exercise: {self.activity}")
        print(f"Body Mass Index: {self.Bmi}\nRequired Calorie: {self.reqCalorie}")


class Calculator:
    def calcBMI(self, person):
        """
        Prints the Body Mass Index according to the Height and Weight
        :param person:
        :return:
        """
        bmi = person.weight / (person.height ** 2)
        print("Body Mass Index: {:.2f}".format(bmi))
        person.Bmi = bmi

        if bmi < 18.5:
            BMI = "Underweight"
        elif 18.5 < bmi < 25:
            BMI = "Normal"
        elif 25 < bmi < 30:
            BMI = "Overweight"
        else:
            BMI = "Obese"
        print("Body Mass Index: {}".format(BMI))

    def reqCalorie(self, person):
        """
        Gives the amount of calories required per day according to the details passed
        :param person:
        :return:
        """
        if person.activity is None:
            print("Please Update your Details")
            person.setDetails()

        if person.gender.lower() == "male" or person.gender.lower() == "m":
            bmr = 88.362 + (person.weight * 13.397) + (5 * (person.height * 100)) - (6.8 * person.age)
        else:
            bmr = 655 + (person.weight * 9.563) + (1.850 * (person.height * 100)) - (4.67 * person.age)

        if person.activity == 0:
            reqCal = (bmr * 1.2)
        elif 1 < person.activity < 3:
            reqCal = (bmr * 1.375)
        elif 3 < person.activity < 5:
            reqCal = (bmr * 1.55)
        elif 5 < person.activity < 7:
            reqCal = (bmr * 1.725)
        else:
            reqCal = (bmr * 1.9)

        print(f"Daily calorie requirement: {reqCal:.0f}cal")
        person.reqCalorie = reqCal.__round__(0)


p1 = Person("Akshay", 55, 150)
p1.setDetails()

calc = Calculator()
calc.calcBMI(p1)
calc.reqCalorie(p1)
p1.getInfo()
