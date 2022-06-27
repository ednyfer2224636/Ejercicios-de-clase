
def palindrome(frase):
    if frase == " ".join(reversed(frase)):
        print("Es palindrome")
    else:
        print("No es palindrome")

x =input("Ingrese una frase: ")
palindrome(x)
