import logging
import json
import requests
from bs4 import BeautifulSoup


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
    Fetches the conversion rate from Google Finance.
    """
    url = f"https://www.google.com/finance/quote/{currency_from}-{currency_to}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from Google Finance (Status {response.status_code})")

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the conversion rate in the div with class "YMlKec fxKbKc"
    rate_element = soup.find("div", class_="YMlKec fxKbKc")
    
    if not rate_element:
        raise Exception("Failed to extract conversion rate from Google Finance")
    
    conversion_rate = float(rate_element.text.replace(",", "").strip())
    
    return conversion_rate

def convert(currency_from, currency_to, amount):
    """
    Converts an amount from one currency to another using live rates from Google Finance.
    """
    if not isinstance(currency_from, str) or not isinstance(currency_to, str):
        raise TypeError("Currency codes must be strings.")

    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be an int or float.")

    currency_from = currency_from.upper()
    currency_to = currency_to.upper()

    # Default response if conversion fails
    default_response = {
        "from": currency_from,
        "to": currency_to,
        "amount": 0,
        "converted": False
    }

    try:
        if currency_from not in CODES or currency_to not in CODES:
            raise KeyError("Invalid currency code")

        # Get conversion rate from Google Finance
        conversion_rate = get_conversion_rate(currency_from, currency_to)
        
        converted_amount = round(amount * conversion_rate, 4)

        default_response["amount"] = converted_amount
        default_response["converted"] = True
        return json.dumps(default_response, indent=4)

    except Exception as error:
        logger.error(error)
        return json.dumps(default_response, indent=4)
