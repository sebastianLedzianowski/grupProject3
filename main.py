from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.mongodb.models import AddressBook, NoteBook

def read():
    # TEST
    # Initialize the database connection and data repository
    db_manager = DatabaseConnectionManager()
    data_repo = DataRepository(db_manager)

    for contact in data_repo.read_all(AddressBook):
        print(f"Name: {contact['name']}, Surname: {contact['surname']}, Phone number: {contact['phone_number']},"
              f" Email: {contact['email']}, Birthday: {contact['birthday']}\n")
    print()
    print("-"*130)
    print()
    for note in data_repo.read_all(NoteBook):
        print(f"Title: {note['title']}, Tag: {note['tag']}\nContent: {note['content']}\n")


# Główna funkcja obsługująca interakcję z użytkownikiem.
def main():
    # Inicjalizacja NotesBook oraz ContactBook

    # Pętla while pozwala na ciągłe interakcje z użytkownikiem, aż do momentu zakończenia programu.
    while True:
    # Wyświetlanie opcji menu dla użytkownika. uzywajac ".format"
    #     Po lewej stronie contacktBook a po prawej opcje wybory notesbook.
    # wybory maja byc po poodaniu numeru.

        # Oczekiwanie na wybór opcji od użytkownika.

        # Warunki odpowiadające poszczególnym opcjom menu.

        # Użytkownik może dodać, wyświetlić, sortować, edytować, usuwać lub zakończyć program.
        # opjca edycji kontaktu oraz usunecia postepna dopiero po wybtaniu konkretnego kontaktu.
        # Każda opcja jest obsługiwana przez odpowiednią funkcję klasy.

        # Po zakończeniu wybranej operacji, program wraca do menu głównego.
        break

if __name__ == '__main__':
    pass