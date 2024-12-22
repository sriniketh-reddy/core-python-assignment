class TicketBookingSystem:
    def __init__(self,no_of_tickets):
        self.booked = []
        self.avaliable = [i for i in range(1,no_of_tickets+1)]
    
    def book_ticket(self, ticket_number):
        if ticket_number in self.avaliable:
            self.booked.append(ticket_number)
            self.avaliable.remove(ticket_number)
            return f"Ticket {ticket_number} booked successfully."
        else:
            return "Ticket is already booked."
        
    def cancel_ticket(self, ticket_number):
        if ticket_number in self.booked:
            self.avaliable.append(ticket_number)
            self.booked.remove(ticket_number)
            return f"Ticket {ticket_number} cancelled successfully."
        else:
            return "Ticket is not booked Earlier."
        
    def get_available(self):
        return self.avaliable
    
no_of_tickets = int(input("Enter the Total no.of Tickets: "))
tbs = TicketBookingSystem(no_of_tickets)

booked_tickets = list(map(int,input("Enter the Booked Ticket Numbers: ").split()))
(tbs.book_ticket(ticket_number) for ticket_number in booked_tickets)

n = int(input("Enter the number of operations to perform: "))
i=0
while(i<n):
    operation = input("\tEnter the operation (book/cancel): ")
    ticket_number = int(input("\tEnter the Ticket Number: "))
    if operation == "book":
        print("\t",tbs.book_ticket(ticket_number),"\n")
    elif operation == "cancel":
        print("\t",tbs.cancel_ticket(ticket_number),"\n")
    else:
        print("\tInvalid operation. Please enter either 'book' or 'cancel'.\n")
        n+=1
    i+=1

print("Available Tickets:", tbs.get_available())