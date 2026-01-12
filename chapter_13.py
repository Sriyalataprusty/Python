#Error Handling
class TuinKahilaBoleErrorEka(Exception):
    pass
#try:
phone_number:int = input("Enter your phone number.\n")
if not phone_number.isdigit() or len(phone_number) != 10:
    raise TuinKahilaBoleErrorEka(f"phone number ta deiparunu murkha kouthikara, tote phone number deba pi kahithili para. {phone_number} aeta tora phone number ki ma murkha. ")
# except ValueError:
    # print("Enter your phone number only. ")
else:
    print(f"{phone_number} is your phone number.")