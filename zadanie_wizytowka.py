# GOTOWE Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej klasy (BusinessContact) rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
# GOTOWE Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.
# GOTOWE Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.
# MAM PROBLEM Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje dwa parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.
class Basecontact:
    def __init__ (self, name, surname, telephone, email):
        self.name=name
        self.surname=surname
        self.telephone=telephone
        self.email = email


    def __str__ (self):
        return f'{self.name} {self.surname} {self.telephone} {self.email}'

    def contact (self):
        return f' Wybieram {self.telephone} i dzwonię do {self.name} {self.surname}'
    
    @property
    def label_length(self):
         return len(self.name + ' ' + self.surname)

base_contact_ola = Basecontact (name='Ola', surname='Fasola', telephone='+48602222222', email='ola@ola.pl')
base_contact_ala = Basecontact (name='Ala', surname='Makota', telephone='+48602222223', email='ala@ala.pl')
base_contact_iza = Basecontact (name='Iza', surname='Unia', telephone='+48602222224', email='iza@iza.pl')
base_contact_list=[base_contact_ola, base_contact_ala, base_contact_iza]

print('Długość')
print(base_contact_ola.label_length)
print(base_contact_ola.contact())

print('Basecontacts:')
for element in base_contact_list:
    print (element)

class BusinessContact(Basecontact):
    def __init__(self, position, company_name, business_phone,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position=position
        self.company_name=company_name
        self.business_phone=business_phone


    def __str__ (self):
        return f'{self.name} {self.surname} {self.telephone} {self.email} {self.position} {self.company_name} {self.business_phone}'

    def contact(self):
        return f'Wybieram {self.business_phone} i dzwonię do {self.name} {self.surname}'

    @property
    def label_length(self):
        return len(self.name + ' ' + self.surname)


business_contact_ola = BusinessContact (name='Ola', surname='Fasola', telephone='+48602222222', email='ola@ola.pl', position = 'Manager', company_name = '"Manageme"', business_phone ='+48792888886' )
business_contact_ala = BusinessContact (name='Ala', surname='Makota', telephone='+48602222223', email='ala@ala.pl', position = 'Team Leader', company_name = '"Manageme"', business_phone ='+48792888887' )
business_contact_iza = BusinessContact (name='Iza', surname='Unia', telephone='+48602222224', email='iza@iza.pl', position = 'Secretary', company_name = '"Manageme"', business_phone ='+48792888888' )
business_contact_list = [business_contact_ola, business_contact_ala, business_contact_iza]

print('Businesscontacts:')
for element in business_contact_list:
    print (element)

def create_contacts(contact_type, count):
    if not issubclass(contact_type, Basecontact):
        raise ValueError('Must inherit from Basecontact')

    contacts = []
    fake = Faker()

    for c in range(count):
        if contact_type is Basecontact:
            contacts.append(Basecontact(
                name=fake.first_name(),
                surname=fake.last_name(),
                telephone=fake.msisdn(),
                email=fake.email()
            ))
        else:
            contacts.append(BusinessContact(
                name=fake.first_name(),
                surname=fake.last_name(),
                telephone=fake.msisdn(),
                email=fake.email(),
                position='Manager',
                company_name='"Manageme"',
                business_phone='+48792888886'
            ))

    return contacts

print('BaseContact')
print(create_contacts(Basecontact, 5))
print()
print('BusinessContact')
print(create_contacts(BusinessContact, 5))
print()