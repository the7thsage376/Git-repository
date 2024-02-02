# Function that saves users biographical information and calls from another function to verify the province
name=input("Name: ")
surname=input("Surname: ")
address1=int(input("address 1: "))
address2=input("address 2: ")
address3=input("Suburb: ")
address4=input("City: l")
address5=input("Province:")

def biographical_information():
    print(name)
    print(surname)
    print(address1)
    print(address2)
    print(address3)
    print(address4)
    print(address5)

#function that stores provinces of south africa so as to verify them under biographical information
def province_verifier():
    provinces=['Gauteng','Free State','Northern Cape','Eastern Cape','Western Cape','North West','Mpumalanga','Limpopo','Kwazulu Natal']
    if address5  not in provinces:
        print('Incorrect province')