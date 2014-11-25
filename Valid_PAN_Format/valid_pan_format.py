def main():
    nb_tests = int(input())
    for i in range(0, nb_tests):
        pan = PanNumber(input())
        print(pan.validate())


class PanNumber():

    def __init__(self, pan_number):
        self.pan = pan_number

    def validate(self):
        output = 'NO'
        if self.pan.isupper():
            if self._validate_digits() and self._validate_alpha():    
                output = 'YES'

        return output

    def _validate_digits(self):
        if self.pan[:5].isalpha() and self.pan[-1:].isalpha():
            return True

        return False

    def _validate_alpha(self):
        if self.pan[5:9].isnumeric():
            return True

        return False

if __name__ == '__main__':
    main()
