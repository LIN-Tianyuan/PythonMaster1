class Phone:
    # variable public
    serial_number = None
    producer = None

    # variable private
    __current_voltage = None

    # method public
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            self.__keep_single_core()
            print("Les appels 5g sont désormais possibles.")
        else:
            print("Défaut d'appel, batterie faible.")

    # method private
    def __keep_single_core(self):
        print("Faire fonctionner l'unité centrale en mode "
              "mono-coeur pour économiserde l'énergie.")


    def __init__(self, serial_number, producer, current_voltage):
        self.serial_number = serial_number
        self.producer = producer
        self.__current_voltage = current_voltage

    def __str__(self):
        return f"serial_number = {self.serial_number}, producer = {self.producer}, current_voltage = {self.__current_voltage}"


phone = Phone(101, "Apple", 1)
phone.call_by_5g()


"""
phone = Phone(101, "Apple", 50)
print(phone)
print("serial_number = " + str(phone.serial_number))
print("producer = " + phone.producer)
phone.__current_voltage = 40
phone.serial_number = 100
print("current voltage = " + str(phone.__current_voltage))
print(phone)
phone.call_by_5g()
# phone.__keep_single_core()
"""