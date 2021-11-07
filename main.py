# Протокол Диффи — Хеллмана для двух абонентов
class ProtocolDiffieHellman:
    def __init__(self, close_key_first, open_root_number, open_prime_number, close_key_second):
        self.close_key_first = close_key_first  # а
        self.close_key_second = close_key_second  # b
        self.open_root_number = open_root_number  # g
        self.open_prime_number = open_prime_number  # p
        self.open_key_first = None  # A
        self.open_key_second = None  # B
        self.private_key = None  # k

    @staticmethod
    def test_Ferma(check_number):
        # искл: числа кармайкла
        status_number = 0
        for i in range(1, check_number):
            answer_chek = (i ** check_number - i) % check_number
            if answer_chek == 0:
                status_number += 0
            else:
                status_number += 1
                break
        if status_number == 0:

            return status_number
        else:

            return status_number

    @staticmethod
    def calculate_key(g, a, p):
        key = g ** a % p
        return key

    def interaction_numbers(self):
        if self.open_root_number > 0 and self.open_prime_number > 0:
            if self.test_Ferma(self.open_root_number) == 0 and self.test_Ferma(self.open_prime_number) == 0:
                self.open_key_first = self.calculate_key(g=self.open_root_number,
                                                         a=self.close_key_first,
                                                         p=self.open_prime_number)
                print("g ** a % p = A({})".format(self.open_key_first))
                self.open_key_second = self.calculate_key(g=self.open_root_number,
                                                          a=self.close_key_second,
                                                          p=self.open_prime_number)
                print("g ** a % p = B({})".format(self.close_key_second))

                self.private_key = self.calculate_key(g=self.open_key_second,
                                                      a=self.close_key_first,
                                                      p=self.open_prime_number)
                print("g ** a % p = K({})".format(self.private_key))
            elif self.test_Ferma(self.open_root_number) != 0 and self.test_Ferma(self.open_prime_number) != 0:
                print("error")
            else:
                print("error")
        elif self.open_root_number <= 0 and self.open_prime_number <= 0:
            print("error")
        else:
            print("error")

    def exchange(self):
        # модуль передачи
        pass


if __name__ == '__main__':
    test = ProtocolDiffieHellman(close_key_first=5, close_key_second=3, open_root_number=7, open_prime_number=11)
    test.interaction_numbers()
