import pandas as pd

# Assuming your CSV file is named "fictional_richest_people.csv"
data = pd.read_csv(r"C:\Users\SaiRamaKrishnaNampal\Downloads\fictional_richest_people_.csv")


# Find the richest person (assuming wealth is a numeric column)
if not data.empty:  # Check if DataFrame is not empty
    richest_person = data.loc[data["Net Worth"].idxmax(), "Name"]
    richest_wealth = data["Net Worth"].max()
    print(f"The richest person in the list is {richest_person} with a net worth of ${richest_wealth:,.2f}.")

else:
    print("The CSV file is empty or there's an error in processing data.")

# Count people with missing email addresses
missing_email_count = data["Email Address"].isnull().sum()

# Count people with missing phone numbers
missing_phone_count = data["Phone Number"].isnull().sum()

# Print the results
print(f"Number of people without email addresses: {missing_email_count}")
print(f"Number of people without phone numbers: {missing_phone_count}")
