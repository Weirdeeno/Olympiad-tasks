"""
8.	Разработать программу, которая осуществляет перевод не более чем трехзначного целого положительного числа
 в соответствующее ему составное числительное на украинском, русском или английском языке.
"""
import random

def convert_ua(num):
    single_digit_ua = ("", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять", "десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п'ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев'ятнадцять")
    two_digit_ua = ("", "", "двадцять", "тридцять", "сорок", "п'ятдесят", "шістдесят", "сімдесят", "вісімдесят", "дев'яносто")
    three_digit_ua = ("", "сто", "двісті", "триста", "чотириста", "п'ятсот", "шістсот", "сімсот", "вісімсот", "дев'ятсот")

    if num < 20:
        return single_digit_ua[num]

    if num < 100:
        return two_digit_ua[num // 10] + " " + single_digit_ua[int(num % 10)]

    if num < 1000:
        return three_digit_ua[num // 100] + " " + convert_ua(int(num % 100))


def convert_ru(num):
    single_digit_ru = ("", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",  "семнадцать", "восемнадцать", "девятнадцать")
    two_digit_ru = ("", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто")
    three_digit_ru = ("", "сто", "двести", "триста", "четыристая", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот")

    if num < 20:
        return single_digit_ru[num]

    if num < 100:
        return two_digit_ru[num // 10] + " " + single_digit_ru[int(num % 10)]

    if num < 1000:
        return three_digit_ru[num // 100] + " " + convert_ru(int(num % 100))


def convert_us(num):
    single_digit_us = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    two_digit_us =("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if num < 20:
        return single_digit_us[num]

    if num < 100:

        return two_digit_us[num // 10]  + single_digit_us[int(num % 10)]

    if num<1000:
        return single_digit_us[num // 100]  +"hundred " +convert_us(int(num % 100))


n = random.randint(1, 999)
print(n)
print("Число українською -", convert_ua(n))
print("Число на русском -", convert_ru(n))
print("Number in English -", convert_us(n))
