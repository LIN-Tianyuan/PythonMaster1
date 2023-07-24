class Phone:
    __is_5g_enable = None

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g on.")
        else:
            print("5g off, using 4g network.")

    def call_by_5g(self):
        self.__check_5g()
        print("On the phone.")


phone = Phone()
phone.call_by_5g()