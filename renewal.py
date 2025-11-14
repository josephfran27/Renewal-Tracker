import pandas as pd

# import CSV file for renewals
df = pd.read_csv('renewals.csv')

# create filters for maybe and unknown
maybes = df[df['Status'] == 'Maybe']
unknowns = df[df['Status'] == 'Unknown']

# concatenate the two dataframes
uncertain = pd.concat([maybes, unknowns]).drop_duplicates()

# print header 
print("\n--- RENEWAL UNCERTAINTIES REPORT AS OF 11/14 ---")

# print unknowns and maybes count
print(f"\nTotal Unknowns/Maybes: {len(uncertain)}")

# print maybes
print("\n--- MAYBES ---")
print(f"Amount: {len(maybes)}")
for index, row in maybes.iterrows():
    print(f" - {row['NameFirst']} {row['NameLast']} (Unit {row['UnitNumber']})")

# print unknowns
print("\n--- UNKNOWNS ---")
print(f"Amount: {len(unknowns)}")
for index, row in unknowns.iterrows():
    print(f" - {row['NameFirst']} {row['NameLast']} (Unit {row['UnitNumber']})")

# save as new CSV file
uncertain.to_csv('renewal_uncertainties_report.csv', index=False)