#Importo la libreria 'requests' para que realice las consultas de API
#Importo la libreria 're' y la uso para evitar la busqueda con caracteres especiales
import requests
import re

#Defino la funcion 'get_character_info' para que traiga la info del nombre del personaje que se inserte
def get_character_info(character_name):
    if not character_name.strip():
        return "El nombre del personaje no puede estar vacío."
    if not re.match('^[a-zA-Z0-9 ]*$', character_name):
        return "El nombre del personaje no puede contener caracteres especiales."
    
    base_url = "https://rickandmortyapi.com/api"


    # Obtengo la información del personaje
    character_response = requests.get(f"{base_url}/character/?name={character_name}")
    character_results = character_response.json().get('results')

    # Verifico si la lista del resultado esta vacía (colocando un nombre que no existe en la lista)
    if not character_results:
        return "El personaje no fue encontrado."
    
    all_characters_info = []
    
    for character_data in character_results:
        character_info = {
            "id": character_data.get("id"),
            "species": character_data.get("species"),
            "type": character_data.get("type")
        }

        # Obteniendo la información de la ubicación del personaje
        location_url = character_data.get("location").get("url")
        if  location_url:
            location_response = requests.get(location_url)
            location_data = location_response.json()
            location_info = {
                "name": location_data.get("name"),
                "type": location_data.get("type"),
                "dimension": location_data.get("dimension")
            }
        else:  
            location_info = {
                "name": "",
                "type": "",
                "dimension": ""
            }

        # Obteniendo la información de los episodios en los que aparece el personaje
        episode_urls = character_data.get("episode")
        episode_info = []
        for url in episode_urls:
            episode_response = requests.get(url)
            episode_data = episode_response.json()
            episode_info.append({
                "episode_name": episode_data.get("name"),
                "episode_id": episode_data.get("episode"),
                "characters_count": len(episode_data.get("characters"))
            })
        
        # Agregando la información del personaje a la lista de todos los personajes si existe mas de un personaje con el mismo nombre 
        all_characters_info.append({
            "Character info": character_info,
            "Location info": location_info,
            "Episode info": episode_info
        })

    # Regresar la información de todos los personajes
    return all_characters_info

#print(get_character_info("rick"))
