class Phone:
    serial_number = None
    producer = None

    def call_by_4g(self):
        print("4g calls.")


class Phone2022(Phone):
    face_id = True

    def call_by_5g(self):
        print("2022 latest 5g calls.")


phone = Phone2022()
print(phone.serial_number)
print(phone.producer)
phone.call_by_5g()

