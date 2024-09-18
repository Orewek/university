import math
import pandas as pd
import folium


def calculate_distance(lat1, lon1, lat2, lon2) -> float:
    R = 6371.0
    lat1_rad: float = math.radians(lat1)
    lon1_rad: float = math.radians(lon1)
    lat2_rad: float = math.radians(lat2)
    lon2_rad: float = math.radians(lon2)
    dlon: float = lon2_rad - lon1_rad
    dlat: float = lat2_rad - lat1_rad
    a: float = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c: float = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


def IndexBuilding(file_path: str) -> list:
    points: list = []
    with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = pd.read_csv(csvfile)
    for index, row in reader.iterrows():
        points.append((row['name'],
                       float(row['wgs_lat']),
                       float(row['wgs_lng']),
                       row['type_code'],
                       row['base_type'],
                       row['sub_type'],
                       row['category']))
    return points


def visualize_nearby_points_on_map(query_point: list(float, float), file_path: str) -> None:
    points = IndexBuilding(file_path)
    m = folium.Map(location=[query_point[0], query_point[1]], zoom_start=15)
    folium.Marker(location=query_point,
                  popup='Query Point',
                  icon=folium.Icon(color='red')).add_to(m)

    nearby_points: list[float] = [p for p in points if str(p[3]).startswith("5") and calculate_distance(query_point[0], query_point[1], p[1], p[2]) <= 0.5]
    for point in nearby_points:
        folium.Marker(location=[point[1],
                      point[2]],
                      popup=point[0]).add_to(m)
    m.save('map_with_nearby_points.html')


def visualize_nearby_point_on_map(query_point: list(float, float), file_path: str):
    points = IndexBuilding(file_path)
    m = folium.Map(location=[query_point[0], query_point[1]], zoom_start=15)
    folium.Marker(location=query_point,
                  popup='Query Point',
                  icon=folium.Icon(color='red')).add_to(m)

    min_distance = float('inf')
    nearest_point = None
    for point in points:
        if str(point[3]).startswith("1603"):
            distance = calculate_distance(query_point[0],
                                          query_point[1],
                                          point[1],
                                          point[2])
            if distance < min_distance:
                min_distance = distance
                nearest_point = point

    if nearest_point is not None:
        folium.Marker(location=[nearest_point[1],
                      nearest_point[2]],
                      popup=nearest_point[0]).add_to(m)

    m.save('map_with_nearest_1603_point.html')


def main() -> None:
    file_path = "C:/Users/HP/Downloads/Assignment2-2012_BIT_POI.csv"

    query_point = (39.958, 116.311)
    visualize_nearby_point_on_map(query_point, file_path)

    query_point = (39.955, 116.310)
    visualize_nearby_points_on_map(query_point, file_path)


if __name__ == '__main__':
    main()
