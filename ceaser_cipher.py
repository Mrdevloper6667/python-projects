bucket = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", ',', '.', '<', '>', '?', '/', '`', '~', '"', '\\'
]



def main():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
        before_message = input("Type the message : ")
        user_shift_message = int(input("Type the shift number : "))
        if direction == "decode":
            user_shift_message *= -1
        after_message = ""
        for letter in before_message:
            if letter in bucket:
                index = bucket.index(letter) + user_shift_message
                index %= len(bucket)
                after_message += bucket[index]        
        print(f"Here is your message : {after_message}")
        proceed = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
        if proceed == "no":
            print("good bye")
            break
            


main()


        







