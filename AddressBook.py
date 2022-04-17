class AddressBook:
    def __init__(self,firstName,lastName,address,city,state,zip,phoneNumber,email):
        """
        Description:
            main constrcutor whenever we will create object then we can runn this.
        Parameter:
            passing all contact details.
        Return:
            Returning nothing but saving values in main variables.
        """
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phoneNumber = phoneNumber
        self.email = email

    def __str__(self):
        return 'first Name= '+str(self.firstName)+'Last Name= '+str(self.lastName)+'Address= '+str(self.address)+'City= '+str(self.city)+'State= '+str(self.state)+'ZipCode= '+str(self.zip)+'PhoneNo='+str(self.phoneNumber)+'Email= '+str(self.email)

if __name__ == '__main__':
    print("Welcome to the address book system.")
    contact1 = AddressBook("Nikita", "Khapare", "Chandur Bazar", "Amravati", "maharashtra", 444723, 9075194857,
                            "nikitaKhapare53@gmail.com")
    print(contact1.__str__())
    
