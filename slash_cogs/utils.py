from discord.ext import commands
from discord import app_commands, Interaction
from discord.ext import commands
from discord import app_commands, Interaction
import requests
from bs4 import BeautifulSoup

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

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_conversion_rate(self, currency_from, currency_to):
        url = f"https://www.google.com/finance/quote/{currency_from}-{currency_to}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch conversion rate (status: {response.status_code})")

        soup = BeautifulSoup(response.text, "html.parser")
        rate_element = soup.find("div", class_="YMlKec fxKbKc")
        if not rate_element:
            raise Exception("Could not extract conversion rate.")
        return float(rate_element.text.replace(",", "").strip())

    def convert(self, currency_from, currency_to, amount):
        currency_from, currency_to = currency_from.upper(), currency_to.upper()
        result = {"from": currency_from, "to": currency_to, "amount": 0, "converted": False}
        try:
            if currency_from not in CODES or currency_to not in CODES:
                raise KeyError("idk what that code is")

            rate = self.get_conversion_rate(currency_from, currency_to)
            result["amount"] = round(amount * rate, 4)
            result["converted"] = True
        except Exception as e:
            print(e)
        return result

    # Autocomplete callback
    async def currency_autocomplete(self, interaction: Interaction, current: str):
        current = current.upper()
        return [
            app_commands.Choice(name=f"{name} ({code})", value=code)
            for code, name in CODES.items()
            if current in code or current in name.upper()
        ][:25]  # max 25 suggestions

    @app_commands.command(name="convert", description="convert currency using live exchange rate")
    @app_commands.describe(
        currency_from="currency code to convert from",
        currency_to="currency code to convert to",
        amount="amount to convert"
    )
    @app_commands.rename(currency_from="_from", currency_to="_to")  
    async def convert_slash(
        self,
        interaction: Interaction,
        currency_from: str,
        currency_to: str,
        amount: float,
    ):
        if currency_from.upper() not in CODES:
            await interaction.response.send_message(f"`{currency_from}`???", ephemeral=True)
            return

        if currency_to.upper() not in CODES:
            await interaction.response.send_message(f"tf is `{currency_to}`", ephemeral=True)
            return

        if not (0.00001 < amount < 1e12):
            await interaction.response.send_message("fuk off", ephemeral=True)
            return

        result = self.convert(currency_from, currency_to, amount)
        if result["converted"]:
            await interaction.response.send_message(f"`{amount} {result['from']}` is: \n{result['amount']} {result['to']}")
        else:
            await interaction.response.send_message("idk", ephemeral=True)

    # Register autocomplete on convert_slash command
    @convert_slash.autocomplete("currency_from")
    async def from_autocomplete(self, interaction: Interaction, current: str):
        return await self.currency_autocomplete(interaction, current)

    @convert_slash.autocomplete("currency_to")
    async def to_autocomplete(self, interaction: Interaction, current: str):
        return await self.currency_autocomplete(interaction, current)

async def setup(bot):
    await bot.add_cog(Utility(bot))
