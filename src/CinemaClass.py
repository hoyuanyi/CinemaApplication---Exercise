
class CinemaClass():
    def __init__(self):
        self.movies_dict = {'Morbius': {'price': 8, 'max_slots': 10, 'total_bought': 0}}
    
    def add_movie(self):
        pass
    
    def get_movie_name(self):
        pass
    
    def set_movie_price(self):
        pass
  
    def set_movie_max_slot(self):
        pass

    def remove_movie(self):
        pass
    
    def buy_movie(self):
        pass

    def buy_movie_amount(self, movie_name):
        pass
 
    def show_movies(self):
        pass
        
    def movie_menu(self):
        while True:
            print("----- Movie Interface -----")
            print("1 - Add Movie")
            print("2 - Remove Movie")
            print("3 - Buy Movie")
            print("4 - Show all Movies")
            print("0 - Exit Interface")
            option = input("Choose option: ")
            if option.strip() == "1":
                print("You have selected Option 1: Add - Movie")
                self.get_movie_name()
            elif option.strip() == "2":
                print("You have selected Option 2: Remove - Movie")
                self.remove_movie()
            elif option.strip() == "3":
                print("You have selected Option 3: Buy - Movie")
                self.buy_movie()
            elif option.strip() == "4":
                print("You have selected Option 4: Show all Movies")
                self.show_movies()
            elif option.strip() == "0":
                print("You have selected Option 0: Exit Interface")
                break
            else:
                print("Invalid Option")