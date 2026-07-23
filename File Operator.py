import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        """Initializes the journal manager with a specific file name."""
        self.filename = filename

    def add_entry(self, user_input):
        """Appends a new journal entry with a timestamp. Creates the file if it doesn't exist."""
        try:
           
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            
           
            with open(self.filename, 'a') as file:
                file.write(f"{timestamp}\n{user_input}\n\n")
            print("\nEntry added successfully!")
        except PermissionError:
            print("\nError: Permission denied. Cannot write to the file.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    def view_all_entries(self):

        
        if not os.path.exists(self.filename):
            print("\nError: The journal file does not exist. Please add a new entry first.")
            return

        try:
            # Open file in read ('r') mode
            with open(self.filename, 'r') as file:
                content = file.read().strip()
                
            if not content:
                print("\nNo journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print("---------------------------------------")
                print(content)
        except PermissionError:
            print("\nError: Permission denied. Cannot read the file.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    def search_entry(self, keyword):
       
        if not os.path.exists(self.filename):
            print("\nError: The journal file does not exist. Please add a new entry first.")
            return

        try:
            with open(self.filename, 'r') as file:
               
                content = file.read()
                entries = content.strip().split('\n\n')
            
            matching_entries = []
            for entry in entries:
                if keyword.lower() in entry.lower():
                    matching_entries.append(entry)
            
            if matching_entries:
                print("\nMatching Entries:")
                print("---------------------------------------")
                for match in matching_entries:
                    print(match)
                    print() 
            else:
                print(f"\nNo entries were found for the keyword: {keyword}")
        except Exception as e:
            print(f"\nAn unexpected error occurred while searching: {e}")

    def delete_all_entries(self):
        """Deletes the journal file completely after user confirmation."""
        if not os.path.exists(self.filename):
            print("\nNo journal entries to delete.")
            return

        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            except PermissionError:
                print("\nError: Permission denied. Could not delete the file.")
            except Exception as e:
                print(f"\nAn unexpected error occurred while deleting: {e}")
        else:
            print("Deletion canceled.")


def main():
   
    manager = JournalManager()

    while True:

        
        print("\n === Welcome to Personal Journal Manager! === ")
        print(" --> Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        
        user_choice = input("\n ~ User Input:\n")

        if user_choice == '1':
            entry_text = input("\n ~ Enter your journal entry:\n")
            manager.add_entry(entry_text)
            
        elif user_choice == '2':
            manager.view_all_entries()
            
        elif user_choice == '3':
            keyword = input("\n ~ Enter a keyword or date to search: ")
            manager.search_entry(keyword)
            
        elif user_choice == '4':
            manager.delete_all_entries()
            
        elif user_choice == '5':
            print("\nOutput:")
            print("\n Thank you for using Personal Journal Manager.. ")
            print("\n If you need more information.. You Will come any time.!")
            print("\n GoodBye..!")
            break
            
        else:
            print("\nOutput:")
            print("Invalid option.. ")
            print("\nPlease select a valid option from the menu..!")

if __name__ == "__main__":
    main()
