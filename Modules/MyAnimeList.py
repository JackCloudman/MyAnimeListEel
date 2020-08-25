from jikanpy import Jikan
import re
class MyAnimeListService():
    def __init__(self):
        self.jk = Jikan()
    def get_anime(self,anime_name):
        # BUSCAMOS EL ANIME
        result = self.jk.search("anime",anime_name,parameters={"limit": 1})
        anime_data = self.jk.anime(result["results"][0]["mal_id"])
        anime = {}
        ## OBTENEMOS NADA MAS LA INOFMRACIÓN QUE NECESITAMOS
        anime["title"] = anime_data["title"] # TITULO
        anime["episodes"] = anime_data["episodes"] # EPISODIOS
        anime["airing"] = "🔴 Finished Airing" if not anime_data["airing"] else "✅ Currently Airing" # Al aire
        ## SCORE con emoji
        if anime_data["score"]>7.5:
            score = "%s 😍"%anime_data["score"]
        elif 5<anime_data["score"]<=7.5:
            score = "%s 🙂"%anime_data["score"]
        elif 2.5<anime_data["score"]<=5:
            score = "%s 😞"%anime_data["score"]
        elif anime_data["score"]<=2.5:
            score = "%s 😠"%anime_data["score"]
        anime["score"] = score # Score
        anime["date"] = "%s"%anime_data["aired"]["from"][:10] #Fecha en que se publico
        anime["rated"] = anime_data["rating"] # Rating
        anime["synopsis"] = anime_data["synopsis"] # Sinpopsis
        anime["background"] = anime_data["background"] # Contexto
        anime["genres"] = ", ".join([x["name"] for x in anime_data["genres"] ]) # Generos
        anime["ranked"] = str(anime_data["rank"]) # Rank en MAL
        anime["trailer"] = anime_data["trailer_url"] # URL del trailer
        # Tratamos de obtener su imagen
        try:
            regex = re.search(r"\.jpg",anime_data["image_url"])
            anime["image"] = anime_data["image_url"][:regex.end()]
        except:
            anime["image"] = None
        return anime
