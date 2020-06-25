# Lesson 8_4-6

class Office_Equipment():
    def __init__(self, manufacturer, quantity, type):
        self.manufacturer = manufacturer
        self.type = type
        try:
            if (int(quantity)):
                self.quantity = quantity
        except Exception as e:
            print('Ошибка. Пожалуйста, введите количество целым числом.')


class Printer(Office_Equipment):
    def __init__(self, manufacturer, quantity, color):
        super().__init__(manufacturer, quantity, 'printer')
        self.color = color


class Scanner(Office_Equipment):
    def __init__(self, manufacturer, quantity, quality):
        super().__init__(manufacturer, quantity, 'scanner')
        self.quality = quality


class Fax(Office_Equipment):
    def __init__(self, manufacturer, quantity, and_phone):
        super().__init__(manufacturer, quantity, 'fax')
        self.phone = and_phone


class Copier(Office_Equipment):
    def __init__(self, manufacturer, quantity, and_scanner):
        super().__init__(manufacturer, quantity, 'copier')
        self.scanner = and_scanner


class Shredder(Office_Equipment):
    def __init__(self, manufacturer, quantity, max_format):
        super().__init__(manufacturer, quantity, 'shredder')
        self.max_format = max_format


class Storage():
    """Класс склада"""
    dict_product = {
        'printer': {'color': 0, 'b&w': 0},
        'scanner': 0,
        'fax': 0,
        'copier': 0,
        'shredder': 0
    }

    def Receiving(self, OfEquip):
        try:
            if (OfEquip.type == 'printer'):
                self.dict_product[OfEquip.type][OfEquip.color] = self.dict_product[OfEquip.type][
                                                                     OfEquip.color] + OfEquip.quantity
            else:
                self.dict_product[OfEquip.type] = self.dict_product[OfEquip.type] + OfEquip.quantity
            print('Благодарим, товар принят.')
        except KeyError:
            print("Извините, наш склад не хранит подобные товары")
        except Exception:
            print('Мы принимаем на склад только офисное оборудование')

    def Print_store(self):
        print('В данный момент на складе имеются ', self.dict_product['printer']['color'], ' цветных и ',
              self.dict_product['printer']['b&w'], ' черно-белых принтеров (всего ',
              self.dict_product['printer']['color'] + self.dict_product['printer']['b&w']
              , ' штук). Также ', self.dict_product['scanner'], ' сканеров, ', self.dict_product['fax'], ' факсов, ',
              self.dict_product['copier'], ' ксероксов, ', self.dict_product['shredder'], ' шредеров.')


M = Storage()
p_hp = Printer('hp', 230, 'color')
p_samsung = Printer('samsung', 50, 'b&w')
sc = Scanner('hp', 20, '500dpi')
sh = Shredder('Sony', 58, 'A2')
cop = Copier('Sony', 102, 'with scanner')
f = Fax('Samsung', 'one', 'with phone')
f = Fax('HP', 17, 'with phone')

M.Receiving(2)
M.Receiving(p_hp)
M.Receiving(p_samsung)
M.Receiving(sc)
M.Receiving(sh)
M.Receiving(cop)
M.Receiving(f)

M.Print_store()
