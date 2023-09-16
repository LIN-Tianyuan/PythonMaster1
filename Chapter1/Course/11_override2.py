class Phone:
    serial_number = None
    producer = "HUAWEI"

    def call_by_5g(self):
        print("Father 5g calls.")


class MyPhone(Phone):
    producer = "Apple"

    def call_by_5g(self):
        print(f"La marque de la classe père est: {Phone.producer}")
        Phone.call_by_5g(self)

        print(f"La marque de la classe père est: {super().producer}")
        super().call_by_5g()


my_phone = MyPhone()
my_phone.call_by_5g()
print(Phone.producer)
print(my_phone.producer)