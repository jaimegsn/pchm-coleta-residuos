import csv
import requests
import geojson

# Lê o CSV e armazena os pontos
locations = []
with open("rota_vizinho_foco_tempo.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lat = float(row['source_lat'])
        lon = float(row['source_lng'])
        name = row['source_name']
        locations.append({"name": name, "lat": lat, "lon": lon})

# Lista para armazenar todas as features (pontos e rotas)
features = []

# Adiciona os pontos como Features do tipo Point
for loc in locations:
    point = geojson.Feature(
        geometry=geojson.Point((loc['lon'], loc['lat'])),
        properties={"name": loc['name'], "type": "point"}
    )
    features.append(point)

# Adiciona as rotas como Features do tipo LineString
for i in range(len(locations) - 1):
    src = locations[i]
    dst = locations[i + 1]

    url = f"https://router.project-osrm.org/route/v1/driving/{src['lon']},{src['lat']};{dst['lon']},{dst['lat']}?overview=full&geometries=geojson"
    response = requests.get(url)
    data = response.json()

    if 'routes' in data and data['routes']:
        geometry = data['routes'][0]['geometry']
        route = geojson.Feature(
            geometry=geometry,
            properties={"from": src['name'], "to": dst['name'], "type": "route"}
        )
        features.append(route)
    else:
        print(f"Erro na rota {src['name']} → {dst['name']}")

# Cria e salva o GeoJSON final
feature_collection = geojson.FeatureCollection(features)
with open("rotas.geojson", "w") as f:
    geojson.dump(feature_collection, f)
