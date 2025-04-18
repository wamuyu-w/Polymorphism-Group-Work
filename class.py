from pet import Pet

def main():
    # Creating a new pet
    pet = input("Enter your pet name")

    # modify the current pet info level like health
    pet.hunger=int(input("Enter your pet hunger level"))
    pet.energy=int(input("Enter your pet energy level"))
    pet.happiness=int(input("Enter your pet happiness level"))
    
    # Display the pet information(Current)
    pet.pet_information()

    # Initialise pet interactions
    pet.eat()
    pet.play()
    pet.sleep()

    # initialising pet tricks and adding them with a value
    pet.train("roll over")
    pet.train("fetch")
 
    # Final status and tricks
    pet.pet_information()

# controlling script execution(running from main and being imported)
if __name__ == "__main__":
    main()
