import logging
import json
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import json
from discord import app_commands
from responses import *

logger = logging.getLogger(__name__)

CODES = {
    "AFN": "Afghan Afghani",
    "ALL": "Albanian Lek",
    "DZD": "Algerian Dinar",
    "AOA": "Angolan Kwanza",
    "ARS": "Argentine Peso",
    "AMD": "Armenian Dram",
    "AWG": "Aruban Florin",
    "AUD": "Australian Dollar",
    "AZN": "Azerbaijani Manat",
    "BSD": "Bahamian Dollar",
    "BHD": "Bahraini Dinar",
    "BBD": "Bajan dollar",
    "BDT": "Bangladeshi Taka",
    "BYR": "Belarusian Ruble",
    "BYN": "Belarusian Ruble",
    "BZD": "Belize Dollar",
    "BMD": "Bermudan Dollar",
    "BTN": "Bhutan currency",
    "BTC": "Bitcoin",
    "BCH": "Bitcoin Cash",
    "BOB": "Bolivian Boliviano",
    "BAM": "Bosnia-Herzegovina Convertible Mark",
    "BWP": "Botswanan Pula",
    "BRL": "Brazilian Real",
    "BND": "Brunei Dollar",
    "BGN": "Bulgarian Lev",
    "BIF": "Burundian Franc",
    "XPF": "CFP Franc",
    "KHR": "Cambodian riel",
    "CAD": "Canadian Dollar",
    "CVE": "Cape Verdean Escudo",
    "KYD": "Cayman Islands Dollar",
    "XAF": "Central African CFA franc",
    "CLP": "Chilean Peso",
    "CLF": "Chilean Unit of Account (UF)",
    "CNY": "Chinese Yuan",
    "CNH": "Chinese Yuan (offshore)",
    "COP": "Colombian Peso",
    "KMF": "Comorian franc",
    "CDF": "Congolese Franc",
    "CRC": "Costa Rican Colón",
    "HRK": "Croatian Kuna",
    "CUP": "Cuban Peso",
    "CZK": "Czech Koruna",
    "DKK": "Danish Krone",
    "DJF": "Djiboutian Franc",
    "DOP": "Dominican Peso",
    "XCD": "East Caribbean Dollar",
    "EGP": "Egyptian Pound",
    "ETH": "Ether",
    "ETB": "Ethiopian Birr",
    "EUR": "Euro",
    "FJD": "Fijian Dollar",
    "GMD": "Gambian dalasi",
    "GEL": "Georgian Lari",
    "GHC": "Ghanaian Cedi",
    "GHS": "Ghanaian Cedi",
    "GIP": "Gibraltar Pound",
    "GTQ": "Guatemalan Quetzal",
    "GNF": "Guinean Franc",
    "GYD": "Guyanaese Dollar",
    "HTG": "Haitian Gourde",
    "HNL": "Honduran Lempira",
    "HKD": "Hong Kong Dollar",
    "HUF": "Hungarian Forint",
    "ISK": "Icelandic Króna",
    "INR": "Indian Rupee",
    "IDR": "Indonesian Rupiah",
    "IRR": "Iranian Rial",
    "IQD": "Iraqi Dinar",
    "ILS": "Israeli New Shekel",
    "JMD": "Jamaican Dollar",
    "JPY": "Japanese Yen",
    "JOD": "Jordanian Dinar",
    "KZT": "Kazakhstani Tenge",
    "KES": "Kenyan Shilling",
    "KWD": "Kuwaiti Dinar",
    "KGS": "Kyrgystani Som",
    "LAK": "Laotian Kip",
    "LBP": "Lebanese pound",
    "LSL": "Lesotho loti",
    "LRD": "Liberian Dollar",
    "LYD": "Libyan Dinar",
    "LTC": "Litecoin",
    "MOP": "Macanese Pataca",
    "MKD": "Macedonian Denar",
    "MGA": "Malagasy Ariary",
    "MWK": "Malawian Kwacha",
    "MYR": "Malaysian Ringgit",
    "MVR": "Maldivian Rufiyaa",
    "MRO": "Mauritanian Ouguiya (1973–2017)",
    "MUR": "Mauritian Rupee",
    "MXN": "Mexican Peso",
    "MDL": "Moldovan Leu",
    "MAD": "Moroccan Dirham",
    "MZM": "Mozambican metical",
    "MZN": "Mozambican metical",
    "MMK": "Myanmar Kyat",
    "TWD": "New Taiwan dollar",
    "NAD": "Namibian dollar",
    "NPR": "Nepalese Rupee",
    "ANG": "Netherlands Antillean Guilder",
    "NZD": "New Zealand Dollar",
    "NIO": "Nicaraguan Córdoba",
    "NGN": "Nigerian Naira",
    "NOK": "Norwegian Krone",
    "OMR": "Omani Rial",
    "PKR": "Pakistani Rupee",
    "PAB": "Panamanian Balboa",
    "PGK": "Papua New Guinean Kina",
    "PYG": "Paraguayan Guarani",
    "PHP": "Philippine Piso",
    "PLN": "Poland złoty",
    "GBP": "Pound sterling",
    "QAR": "Qatari Rial",
    "ROL": "Romanian Leu",
    "RON": "Romanian Leu",
    "RUR": "Russian Ruble",
    "RUB": "Russian Ruble",
    "RWF": "Rwandan franc",
    "SVC": "Salvadoran Colón",
    "SAR": "Saudi Riyal",
    "CSD": "Serbian Dinar",
    "RSD": "Serbian Dinar",
    "SCR": "Seychellois Rupee",
    "SLL": "Sierra Leonean Leone",
    "SGD": "Singapore Dollar",
    "PEN": "Sol",
    "SBD": "Solomon Islands Dollar",
    "SOS": "Somali Shilling",
    "ZAR": "South African Rand",
    "KRW": "South Korean won",
    "VEF": "Sovereign Bolivar",
    "XDR": "Special Drawing Rights",
    "LKR": "Sri Lankan Rupee",
    "SSP": "Sudanese pound",
    "SDG": "Sudanese pound",
    "SRD": "Surinamese Dollar",
    "SZL": "Swazi Lilangeni",
    "SEK": "Swedish Krona",
    "CHF": "Swiss Franc",
    "TJS": "Tajikistani Somoni",
    "TZS": "Tanzanian Shilling",
    "THB": "Thai Baht",
    "TOP": "Tongan Paʻanga",
    "TTD": "Trinidad & Tobago Dollar",
    "TND": "Tunisian Dinar",
    "TRY": "Turkish lira",
    "TMM": "Turkmenistan manat",
    "TMT": "Turkmenistan manat",
    "UGX": "Ugandan Shilling",
    "UAH": "Ukrainian hryvnia",
    "AED": "United Arab Emirates Dirham",
    "USD": "United States Dollar",
    "UYU": "Uruguayan Peso",
    "UZS": "Uzbekistani Som",
    "VND": "Vietnamese dong",
    "XOF": "West African CFA franc",
    "YER": "Yemeni Rial",
    "ZMW": "Zambian Kwacha"
}


def get_conversion_rate(currency_from, currency_to):
    """
    fethes the conversion rate from google finance
    """
    url = f"https://www.google.com/finance/quote/{currency_from}-{currency_to}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"failed (status: {response.status_code})")
    
    soup = BeautifulSoup(response.text, "html.parser")
    rate_element = soup.find("div", class_="YMlKec fxKbKc") #the class 
    
    if not rate_element:
        raise Exception("failed to extract converison rate")
    
    return float(rate_element.text.replace(",", "").strip())

def convert(currency_from, currency_to, amount):
    """
    converts an amount from one currency to another using live rates from google finance
    """
    if not isinstance(currency_from, str) or not isinstance(currency_to, str):
        raise TypeError("Currency codes must be strings.")
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number.")
    
    currency_from, currency_to = currency_from.upper(), currency_to.upper()
    
    result = {"from": currency_from, "to": currency_to, "amount": 0, "converted": False}
    
    try:
        if currency_from not in CODES or currency_to not in CODES:
            raise KeyError("Invalid currency code")
        
        conversion_rate = get_conversion_rate(currency_from, currency_to)
        result["amount"] = round(amount * conversion_rate, 4)
        result["converted"] = True
    except Exception as error:
        logger.error(error)
    
    return json.dumps(result, indent=4)

@commands.command(
    name="convert",
    aliases=["c"],
    help="converts currencies using country code",
    enabled=True
)
@app_commands.describe(_from="From", _to="To", _amount="Amount")
async def convert_currency(
    ctx, 
    _from: str=commands.parameter(default=None, description='The country code to convert from'),
    _to: str=commands.parameter(default=None, description='The country code to convert to'),
    _amount: float=commands.parameter(default=None, description='The amount to convert')
    ):

    if _from is None or _to is None or _amount is None:
        await ctx.send("use it like")
        await ctx.send("`//convert <from_currency_code> <to_currency_code> <amount>`")
        return
    
    if _from.upper() not in CODES:
        print (_from, 'doesnt exist')
        await ctx.send(f"{_from} is not a valid currency code")

    if _to.upper() not in CODES:
        print (_to, 'doesnt exist')
        await ctx.send(f"{_to} is not a valid currency code")


    if not (0.00000001 < _amount < 999999999999999):
        await ctx.send("fuk off")
    else:
        conversion = json.loads(convert(_from, _to, _amount))
        if conversion["converted"]:
            await ctx.send(f"its {conversion['amount']} {conversion['to']}")
        else:
            await ctx.send("idk")

@convert_currency.error
async def convert_currency_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(respond(not_a_number_responses))

        


async def setup(bot):
    bot.add_command(convert_currency)
    
