import requests
from bs4 import BeautifulSoup
from time_it import time_def


class Scraper:
    @staticmethod
    def scrape_weather_data():
        url = "https://www.cpa.unicamp.br"

        @time_def
        def cepagri_scrapping():
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            previsao_div = soup.select_one("div.sessao-previsao")
            grid_div = previsao_div.select_one("div.grid")

            temperatura = grid_div.select_one("div.temperatura").text.strip()

            info_div = grid_div.select_one("div.info")

            data = {
                "temperatura": temperatura,
                "umidade": None,
                "vento": None,
                "pressao": None,
                "atualizacao": None,
            }

            for span in info_div.select("span"):
                text = span.get_text(strip=True)
                if text == "Umidade:":
                    data["umidade"] = span.find_next_sibling("span").text.strip()
                elif text == "Vento:":
                    data["vento"] = span.find_next_sibling("span").text.strip()
                elif text == "Pressão:":
                    data["pressao"] = span.find_next_sibling("span").text.strip()
                elif text == "Atualização:":
                    data["atualizacao"] = span.find_next_sibling("span").text.strip()

            return data

        return cepagri_scrapping()