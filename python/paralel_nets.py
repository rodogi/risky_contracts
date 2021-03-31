#!/usr/local/bin python3

""" Multi-threading the calculation of distances between OSM features and
crime locations.
"""

import itertools
import multiprocessing as mp
import pandas as pd
import numpy as np
from geopy.distance import distance


def get_distance(pair):
    """Get the distance in meters between a and b"""
    a = pair[0]
    b = pair[1]
    if a % 100 == 0:
        print(a)
    # p_crime = crime_points[a]
    p_perims = perims_points[a]
    id_perims = perims_ids[a]
    p_osm = osm_points[b]
    id_osm = osm_ids[b]

    return [id_perims, id_osm, distance(p_perims, p_osm).meters]


if __name__ == '__main__':
    main_roads = ['motorway', 'trunk', 'primary']
    PATH_OSM = 'osm_geo.csv'
    # PATH_CRIME = 'crime.csv'
    # PATH_CENTROID = 'centroids.csv'
    PATH_PERIMS = 'perims.csv'

    osm = pd.read_csv(PATH_OSM)
    osm = osm[osm['tag_value'].isin(main_roads)]
    # osm = osm[osm['tag_key'] == 'amenity']
    # osm = osm[osm['tag_key'] == 'leisure']
    # osm = osm[osm['tag_key'] == 'shop']
    osm['point'] = list(zip(osm['lat'], osm['lon']))

    # crime = pd.read_csv(PATH_CRIME)
    # crime['point'] = list(zip(crime['lat'], crime['lon']))
    # centroid = pd.read_csv(PATH_CENTROID)
    perims = pd.read_csv(PATH_PERIMS)
    perims['point'] = list(zip(perims['lat'], perims['lon']))

    osm_points = osm['point'].values
    osm_ids = osm['id'].values
    # crime_points = crime['point'].values
    perims_points = perims['point'].values
    perims_ids = perims['OBJECTID'].values

    product = itertools.product(range(perims.shape[0]),
                                range(osm.shape[0]))

    pool = mp.Pool(46)
    res = pool.map(get_distance, product)
    pool.close()
    pool.join()
    np.savetxt('perims_distances.csv',
               res,
               delimiter=',',
               fmt='%s')
