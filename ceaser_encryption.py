alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Create function called 'encrypt()' that takes 'original_text and 'shift_amount' as 2 inputs 
#insdie the 'encrypt()' function shift each letter of the 'original_text' forwward in the alphabet
#by shift amount and print the encrypted text


#Combine the encrypt() and decrypt() functions into one function called caesar()
#use value of the user chosen 'direction; variabel to detemrine which function to use 

def caesar(original_text,shift_amount,crpyt):
      output_text = "" #will
      if crypt == "decode":
          shift_amount *= -1 #changes value to opposite sign

      for letter in original_text:
          shift_position = alphabet.index(letter) + shift_amount
          #When number inputed is above the range of the alphabet 
          #modules will make sure its within range while still getting the right index
          shift_position %= len(alphabet)
          output_text += alphabet[shift_position] #gets the index user shifted too
    
print(f" here is the {crypt} results: {output_text}")
#test 
caesar(original_text=text, shift_amount=shift, crpyt=direction)

         
        
        