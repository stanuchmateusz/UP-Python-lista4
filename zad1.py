class Pulpit:
    available_marks = set(
        {1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6})

    def __init__(self, name: str, surname: str):
        if name == "" or surname == "":
            raise ValueError("Nie podano imienia lub nazwiska")
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError("Imie i nazwisko musza byc napisami")
        if len(name) < 3 or len(surname) < 3:
            raise ValueError("Imie i nazwisko musza miec conajmniej 3 znaki")
        self.name = name
        self.surname = surname
        self.marks = dict()

    def complete_marks(self, subject: str, mark: float):
        if isinstance(mark, int):
            mark = float(mark)
        if not isinstance(subject, str) or not isinstance(mark, float):
            raise TypeError("Przedmiot i ocena musza byc napisami")
        if subject == "" or mark == "":
            raise ValueError("Nie podano przedmiotu lub oceny")
        if mark not in Pulpit.available_marks:
            raise ValueError("Nieprawidlowa ocena")
        self.marks[subject] = mark

    def print_marks(self):
        print(f'Oceny ucznia: {self.name} {self.surname}')
        for subject, mark in self.marks.items():
            print(f'{subject}: {mark}')

    def mean(self):
        suma = 0
        for mark in self.marks.values():
            suma += mark
        return suma / len(self.marks)

    def __str__(self, avg=None):
        if avg is None:
            avg = self.mean()
        return f'{self.name} {self.surname} {avg}'


class Student(Pulpit):

    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.weights = dict()

    def complete_weights(self, subject: str, weight: float):
        if not isinstance(subject, str) or not isinstance(weight, float):
            raise TypeError("Przedmiot musi byc napisem, a waga liczba")
        if subject is None or weight is None:
            raise ValueError("Nie podano przedmiotu lub wagi")
        if weight < 0 or weight > 1:
            raise ValueError("Waga musi byc w przedziale [0, 1]")
        self.weights[subject] = weight

    def mean(self):
        suma = 0
        for subject, mark in self.marks.items():
            suma += mark * self.weights[subject]
        return suma / len(self.marks)

    def __str__(self):
        return super().__str__(self.mean())


def main():
    student = Student("Jan", "Kowalski")
    student.complete_marks("matematyka", 5)
    student.complete_marks("fizyka", 4)
    student.complete_marks("chemia", 3)
    student.complete_marks("biologia", 2)
    student.complete_marks("geografia", 1)
    student.complete_weights("matematyka", 0.5)
    student.complete_weights("fizyka", 0.25)
    student.complete_weights("chemia", 0.25)
    student.complete_weights("biologia", 0.25)
    student.complete_weights("geografia", 0.25)
    student.print_marks()
    print(student)

    pulpit = Pulpit("Jan", "Kowalski")
    pulpit.complete_marks("matematyka", 5)
    pulpit.complete_marks("fizyka", 4)
    pulpit.complete_marks("chemia", 3)
    pulpit.complete_marks("biologia", 2)
    pulpit.complete_marks("geografia", 1)
    pulpit.print_marks()
    print(pulpit)


if __name__ == "__main__":
    main()
