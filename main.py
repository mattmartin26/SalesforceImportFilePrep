def update_headers(csv):
    import pandas as pd

    df = pd.read_csv(csv)
    df = df.add_suffix('__c')
    df.to_csv(csv)
    return "success"


def append_file_name(directory):
    import shutil
    import glob

    files = glob.glob1(directory, "*.csv")
    print("Success")
    for mycsv in files:
        print(mycsv)
        source_csv_path = directory + mycsv
        new_csv = mycsv.replace(".csv", "_staging.csv")
        target_csv_path = directory + new_csv
        shutil.copyfile(source_csv_path, target_csv_path)
        print(update_headers(target_csv_path))


mydirectory = input("What directory would you like to have CSV column names appended with '__c' for import to "
                    "Salesforce?\n") + '/'
print(mydirectory)
append_file_name(mydirectory)
