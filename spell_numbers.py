"""Convert numbers from digits to words in Basque."""

from argparse import ArgumentParser
import sys

LANGUAGES = ["eus"]

ones_tens = ["zero", "bat", "bi", "hiru", "lau", "bost", "sei",
             "zazpi", "zortzi", "bederatzi", "hamar", "hamaika", "hamabi",
             "hamairu", "hamalau", "hamabost", "hamasei", "hamazazpi",
             "hamazortzi", "hemeretzi"]
multiple_twenties = ["hogei", "berrogei", "hirurogei", "laurogei"]
hundreds = ["", "ehun", "berrehun", "hirurehun", "laurehun", "bostehun",
            "seiehun", "zazpiehun", "zortziehun", "bederatziehun"]

def thousands(nums):
    """thousands() is a sub function of eus() and helps us get our large nums
    that are above 999

    Args:
        nums (int): number to be translated to basque 

    Returns:
        str: returns strings of numbers that are over 999
    """
    if nums[0] > 1:
        if nums[1] == 0:
            return eus(nums[0]) + " mila"
        elif nums[1] > 0:
            return eus(nums[0]) + " mila " + eus(nums[1])
        else:
            return eus(nums[0]) + " mila eta " + eus(nums[1])
        
    elif nums[0] == 1:
        if nums[1] == 0:
            return "mila"
        else:
            return "mila eta " + eus(nums[1]) 
    else:
        return eus(nums[1])
    
def two_dig(nums):
    """two dig() works with numbers that are greater than 19 but less than 100

    Args:
        nums (int): number to be converted to basque language

    Returns:
        str: returns string of numbers between 20 and 99
    """
    words = []
    if nums < 20:
        return ones_tens[nums]
    else:
        twenties = nums // 20
        modulo = nums % 20
        if twenties != 0:
            words.append(multiple_twenties[twenties - 1])
        if modulo != 0:
            if twenties != 0:
                words.append("ta ")
            words.append(ones_tens[modulo])
        return "".join(words)

def eus(nums):
    """eus() is the function that returns all of our basque conversions

    Args:
        nums (int): numbers to be changed to basque

    Returns:
        str: strings of words in basque
    """
    if nums < 1000:
        if nums < 100:
            return two_dig(nums)
        else:
            hundred = nums // 100
            rest = nums % 100
            if rest != 0:
                return hundreds[hundred] + " " + "eta" + " " + two_dig(rest)
            else:
                return hundreds[hundred]
    else:
        thousands_part = nums // 1000
        rest = nums % 1000
        if rest != 0:
            return thousands([thousands_part, rest])
        else:
            return thousands([thousands_part, 0])


def main(lang_code, input_path, output_path):
    """main helps us run our code and get out number_words file with output.
    Args:
        lang_code (str):
        input_path (str):
        output_path (str):
    Raises:
        ValueError: will raise if they are not testing basque, aka eus
    Side effects:
        the output file will change when the program runs
    """
    if lang_code != "eus":
        raise ValueError
    with open(input_path, "r", encoding="utf-8") as input_file:
        with open(output_path, "w", encoding="utf-8") as output_file:
            for line in input_file:
                number = int(line.strip())
                words = eus(number)
                output_file.write(f"{number} = {words}\n")

            


def parse_args(arglist):
    """Parse command-line arguments.
    
    Three arguments are required, in the following order:
    
        lang (str): the ISO 639-3 language code of the language the user wants
            to convert numbers into.
        input_file (str): path to a file containing numbers expressed as digits.
        output_file (str): path to a file where numbers will be written as words
            in the target language.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments as a namespace. The following attributes
        will be defined: lang, input_file, and output_file. See above for
        details.
    """
    parser = ArgumentParser()
    parser.add_argument("lang", help="ISO 639-3 language code")
    parser.add_argument("input_file", help="input file containing numbers")
    parser.add_argument("output_file", help="file where output will be stored")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.lang, args.input_file, args.output_file)
