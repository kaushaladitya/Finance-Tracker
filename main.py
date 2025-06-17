import pandas as pd
import csv
from data_entry import *
import matplotlib.pyplot as plt
import seaborn as sns     



class CSV:
    CSV_FILE='Finance_data.csv'
    COLUMNS=['Date','Description','Amount','Category']
    FORMAT='%d-%m-%Y'

    @classmethod
    def initialization_csv(cls):
        '''Initializes the csv file with headers'''
        print('aditya')
        try:
            df=pd.read_csv(cls.CSV_FILE)
        
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls,date,description ,amount, category):
        '''Add the new entry in the csv file or in the dataframe'''
        # creating the dictionary
        # This dictionary should match the columns that we have in the data frame if not than it give the error 
        ##**here updation is required do something good like if we dinmically change the cols constant from the top that it also reflects here**
        new_entry={
            'Date': date,
            'Description': description,
            'Amount': amount,
            'Category':category
        }
        ## Using the new dictionary to create the correct columns get the correct data in our data frame
        #using context manager we are going to write the data or going to append the data in the csv file we are not removing or any thing we are just simply appending at the end of the csv file with the new entry and each feild according to the columns mentions which should be matched with the one that we created in the initialization_csv method
        with open(cls.CSV_FILE,'a',newline='') as csvfile: # context manager automalically closes the file after the block of code is executed


            # Using DictWriter to write the new entry takes the csv file and the fieldnames which are the columns that we created in the initialization_csv method
            # this is the clss DictWriter which is used to write the data in the csv file
            # we created the writer as the object which having the class DictWriter and passing the csv file and the fieldnames which are the columns that we created in the initialization_csv method
            writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)

            writer.writerow(new_entry)
        print(f'New entry added sucessfully')   

    @classmethod
    def get_transaction(cls,start_date,end_date):
        df=pd.read_csv(cls.CSV_FILE)
        if not df.empty:
            df['Date']=pd.to_datetime(df['Date'],format=CSV.FORMAT)
            #converting the string to the datetime object so that we can filter the data based on the date
            start_date=pd.to_datetime(start_date,format=CSV.FORMAT)
            end_date=pd.to_datetime(end_date,format=CSV.FORMAT)

            # df['Date'] >= start returns a Series of True/False (one for each row).
#               # Similarly, df['Date'] <= end returns another Series of True/False.
                # To compare them element by element, you need & (bitwise AND)
            mask=(df['Date'] >= start_date) & (df['Date'] <= end_date)
            filtered_df=df.loc[mask]
            if not filtered_df.empty:
                print(f'transaction from {start_date} to {end_date}:')
                print(filtered_df.to_string(index=False,formatters={'Date': lambda x:x.strftime(CSV.FORMAT)}))

                total_expense=filtered_df[filtered_df['Category']=='Expense']['Amount'].sum()
                total_income=filtered_df[filtered_df['Category']=='Income']['Amount'].sum()
                print("\n summary: ")
                print(f'Total Income: {total_income:.2f}')
                print(f'Total Expense: {total_expense}')
            else:
                print('No transactions found in the given date range.')

        return filtered_df



def add():
    '''Funciton that add the new entry in the csv file'''
    CSV.initialization_csv()
    date=get_date('enter the date in dd-mm-yyyy FORMAT: ',allow_default=True)
    description=get_description()
    amount=get_amount()
    category=get_category()
    CSV.add_entry(date, description, amount, category)

def plot_graphs(df):
    # Ensure 'Date' is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set the index
    df.set_index('Date', inplace=True)
    
    # Resample income and expense by day and fill missing dates with 0
    income_df = df[df['Category'] == 'Income'].resample('D').sum()
    expens_df = df[df['Category'] == 'Expense'].resample('D').sum()

    # Create full date range for the plot
    full_index = pd.date_range(start=df.index.min(), end=df.index.max())

    income_df = income_df.reindex(full_index, fill_value=0)
    expens_df = expens_df.reindex(full_index, fill_value=0)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(income_df.index, income_df['Amount'], label='Income', color='green')
    plt.plot(expens_df.index, expens_df['Amount'], label='Expense', color='red')
    plt.title('Income and Expense Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# add()

# CSV.get_transaction('01-10-2023', '04-06-2025')

# CSV.get_transaction('04-06-2025', '30-06-2025')

#now we are not going to do in that way we have to create the one main funciton which holds the true

def main():
    while True:
        print('Having 3 choices')
        print('1. Add a new entry')
        print('2. Get transaction in a date range')
        print('3. Exit')
        choice = input('Enter your choice (1/2/3): ')
        if choice=='1':
            add()
        elif choice=='2':
            start_date =get_date('Enter start date (dd-mm-yyyy): ')
            end_date = get_date('Enter end date (dd-mm-yyyy): ', allow_default=True)
            df=CSV.get_transaction(start_date, end_date)
            if df.empty:
                print('No transactions found in the given date range.')

            if input('Do you want to plot the graph? (yes/no): ').lower() == 'yes':
                plot_graphs(df)
            else:
                print('Graph plotting skipped.')
        elif choice=='3':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__=='__main__':
    main()
        