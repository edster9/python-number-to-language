def number_to_english(number):
    # all text translation is handled in this dictonary so other language with similar grammer can be supported
    words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
             30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
             'h': 'hundred', 't': 'thousand', 'm': 'million', 'b': 'billion', 'tr': 'trillion'}

    # basic unit limits by order of magnitude
    kilo = 1000
    million = kilo * 1000
    billion = million * 1000
    trillion = billion * 1000

    # convert the number to text translation
    if (number < 20):
        return words[number]
    elif (number < 100):
        if number % 10 == 0:
            return words[number]
        else:
            return f"{words[number // 10 * 10]}-{words[number % 10]}"
    elif (number < kilo):
        if number % 100 == 0:
            return f"{words[number // 100]} {words['h']}"
        else:
            return f"{words[number // 100]} {words['h']} and {number_to_english(number % 100)}"
    elif (number < million):
        if number % kilo == 0:
            return f"{number_to_english(number // kilo)} {words['t']}"
        else:
            return f"{number_to_english(number // kilo)} {words['t']}, {number_to_english(number % kilo)}"
    elif (number < billion):
        if (number % million) == 0:
            return f"{number_to_english(number // million)} {words['m']}"
        else:
            return f"{number_to_english(number // million)} {words['m']}, {number_to_english(number % million)}"
    elif (number < trillion):
        if (number % billion) == 0:
            return f"{number_to_english(number // billion)} {words['b']}"
        else:
            return f"{number_to_english(number // billion)} {words['b']}, {number_to_english(number % billion)}"
    elif (number % trillion == 0):
        return f"{number_to_english(number // trillion)} {words['tr']}"
    else:
        return f"{number_to_english(number // trillion)} {words['tr']}, {number_to_english(number % trillion)}"

    raise AssertionError(
        f"number supplied is outside supported range: {str(number)}")


def number_to_spanish(number):
    # all text translation is handled in this dictonary so other language with similar grammer can be supported
    words = {0: 'cero', 1: 'uno', 2: 'dos', 3: 'tres', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve', 10: 'diez',
             11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce', 15: 'quince', 16: 'dieciséis', 17: 'diecisiete', 18: 'dieciocho', 19: 'diecinueve', 20: 'veinte',
             30: 'treinta', 40: 'cuarenta', 50: 'cincuenta', 60: 'sesenta', 70: 'setenta', 80: 'ochenta', 90: 'noventa',
             'h': 'ciento', 't': 'mil', 'm': 'millón', 'b': 'mil millones', 'tr': 'billones'}

    # basic unit limits by order of magnitude
    kilo = 1000
    million = kilo * 1000
    billion = million * 1000
    trillion = billion * 1000

    # convert the number to text translation
    if (number < 20):
        return words[number]
    elif (number < 100):
        if number % 10 == 0:
            return words[number]
        else:
            return f"{words[number // 10 * 10]} y {words[number % 10]}"
    elif (number < kilo):
        if number % 100 == 0:
            return f"{words[number // 100]} {words['h']}"
        else:
            return f"{words[number // 100]} {words['h']} {number_to_spanish(number % 100)}"
    elif (number < million):
        if number % kilo == 0:
            return f"{number_to_spanish(number // kilo)} {words['t']}"
        else:
            return f"{number_to_spanish(number // kilo)} {words['t']}, {number_to_spanish(number % kilo)}"
    elif (number < billion):
        if (number % million) == 0:
            return f"{number_to_spanish(number // million)} {words['m']}"
        else:
            return f"{number_to_spanish(number // million)} {words['m']}, {number_to_spanish(number % million)}"
    elif (number < trillion):
        if (number % billion) == 0:
            return f"{number_to_spanish(number // billion)} {words['b']}"
        else:
            return f"{number_to_spanish(number // billion)} {words['b']}, {number_to_spanish(number % billion)}"
    elif (number % trillion == 0):
        return f"{number_to_spanish(number // trillion)} {words['tr']}"
    else:
        return f"{number_to_spanish(number // trillion)} {words['tr']}, {number_to_spanish(number % trillion)}"

    raise AssertionError(
        f"number supplied is outside supported range: {str(number)}")
