meme_dict = {
    "CRINGE": "Qualcosa di particolarmente imbarazzante",
    "DW": "Un modo per dire 'Non preoccuparti' viene usato spesso in inglese",
    "OMG": "Un modo per dire 'Oh mio dio!'"
}
termine = input("Scrivi una parola che non capisci con lettere maiuscole")
if termine in meme_dict.keys():
    print(meme_dict[termine])
else:
    print("no.")
