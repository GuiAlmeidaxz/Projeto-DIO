def get_card_brand(card_number):
    card_number_str = str(card_number)

    if card_number_str.startswith('4'):
        return 'Visa'

    if card_number_str[:2] in [str(i) for i in range(51, 56)] or \
       2221 <= int(card_number_str[:4]) <= 2720:
        return 'MasterCard'

    if card_number_str.startswith(('4011', '4312', '4389')) or \
       card_number_str[:4].isdigit() and card_number_str[0] == '4':
        return 'Elo'

    if card_number_str.startswith(('34', '37')):
        return 'American Express'

    if card_number_str.startswith('6011') or \
       card_number_str.startswith('65') or \
       644 <= int(card_number_str[:3]) <= 649:
        return 'Discover'

    if card_number_str.startswith('6062'):
        return 'Hipercard'

    if card_number_str.startswith(('30', '36', '38')):
        return 'Diners Club'

    if card_number_str.startswith(('2149', '2014')):
        return 'enRoute'

    if card_number_str.startswith('35'):
        return 'JCB'

    if card_number_str.startswith('8699'):
        return 'Voyager'
    
    if card_number_str.startswith('50'):
        return 'Aura'

    return 'Unknown'
 
card_number = 5047431869883273
print(get_card_brand(card_number)) # Output: Diners Club