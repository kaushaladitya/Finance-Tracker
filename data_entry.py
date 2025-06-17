# creating this folder which is easily understandable and readable 
#having all the funciton related to getting the user data 

from datetime import datetime


FORMATE='%d-%m-%Y'
CATEGORY={
    'I': 'Income',
    'E': 'Expense'
}


def get_date(prompt,allow_default=False):
    date_str=input(prompt)
    # If it's optional → use allow_default=True (fall back to today's date).
    # If it's required → use allow_default=False (must give a valid input).
    if allow_default and not date_str:
        return datetime.today().strftime(FORMATE)
    
    #date validation
    try:    
        valid_date = datetime.strptime(date_str, FORMATE)
        return valid_date.strftime(FORMATE)
    except ValueError:
        print('Invalid date format. Please use dd-mm-yyyy.')
        ## here we are again recalling the fucntion again the case of the recurssion where if there is no valid input of the date than again this funtion called
        return get_date(prompt,allow_default=False)

def get_amount():

    try:
        amount=float(input('Enter the amount: '))
        if amount <= 0:
            raise ValueError("Amount must be greater than Zero.")
        return amount
    except ValueError as e:
        print(e)
        print('Invalid amount fomate input should be the number and greater than zero')
        return get_amount()


def get_description():
    try:
        description=input('Enter the description: ')
        # check that user cannot forgot to enter the decription that user should enter the description as it is good for the record
        
        if not description:
            raise ValueError("Description cannot be empty.")
        return description.strip()  # Remove leading/trailing spaces
    except ValueError as e:
        print('There might be some error in the description you entered',e)
        return get_description()
    
def get_category():
    try:
        category=input('Enter the category For Income("I")/Expense("E"):  ').upper()
        if category in CATEGORY:
            return CATEGORY[category]
        else:
            raise ValueError("Invalid category. Please enter 'I' for Income or 'E' for Expense.")

    except ValueError as e:
        print(e)
        return get_category()

