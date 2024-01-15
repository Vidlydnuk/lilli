class NamesArray:
    def __init__(self, names, default_value=""):
        self.names = names
        self.default_value = default_value
        self.create_dynamic_attributes()

    def create_dynamic_attributes(self):
        for name in self.names:
            setattr(self, name, self.default_value)

if __name__ == "__main__":
    names_array = NamesArray(["Іван", "Сергій", "Володя"], default_value="здав екзамен")

    print(names_array.Іван)  
    print(names_array.Сергій)  
    print(names_array.Володя)  