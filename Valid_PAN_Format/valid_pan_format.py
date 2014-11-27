def main():
    nb_tests = int(input())

    for i in range(0, nb_tests):
        pan = PanNumber(input())

        if pan.isValid:
            print("YES")
        else:
            print("NO")


class PanNumber():

    def __init__(self, pan_number):
        self.pan = pan_number
        self.isValid = False
        self._validate()

    def _validate(self):
        if self.pan.isupper():
            if self._validate_digits() and self._validate_alpha():    
                self.isValid = True

    def _validate_digits(self):
        isValid = False
        if self.pan[5:9].isnumeric():
            isValid = True

        return isValid

    def _validate_alpha(self):
        isValid = False
        if self.pan[:5].isalpha() and self.pan[-1:].isalpha():
            isValid = True

        return isValid

if __name__ == "__main__":
    main()
