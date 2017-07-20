
import csv
import logging

import predix.admin.cf.orgs

def process_users(csv_path, mode='add'):
    """
    This method demonstrates iterating over a csv file container
    user email addresses and roles.  For each, can add or remove
    a corresponding collaborator / user in the currently targeted
    cloud foundry space.
    """
    org = predix.admin.cf.orgs.Org()

    with open(csv_path) as csv_data:
        reader = csv.DictReader(csv_data)
        for row in reader:
            user_name = row['username']
            role = row['role']

            if mode == 'add':
                org.add_user(user_name, role)
            else:
                org.remove_user(user_name)

if __name__ == '__main__':
    # Give detailed debugging information for this example
    logging.basicConfig(level=logging.DEBUG)

    print("Adding users...")
    process_users('users.csv')

    print("Removing users...")
    process_users('users.csv', mode='remove')
