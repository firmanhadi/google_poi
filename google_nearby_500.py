import csv
import json
import codecs
import simplejson
import urllib

poi = [(-6.20521,106.82718),
       (-6.2142,106.78221),
        (-6.35809,106.8002),
        (-6.35809,106.80919)]

types = ['airport','amusement_park','health','local_government_office','park','pharmacy','physiotherapist','place_of_worship','post_office']

for i,j in poi:
    for t in types:
        AUTH_KEY = 'AIzaSyAnPnFArk9D0kK7xuO10SyVp04P42kmqXc'
        LOCATION = str(i) + "," + str(j)
        RADIUS = 500
        TYPES = t
        MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
             '?location=%s'
             '&radius=%s'
             '&types=%s'
             '&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
        response = urllib.urlopen(MyUrl)
        result = response.read()
        d = simplejson.loads(result)
        g=d['results']

        outfile_path='/tmp/poi_' + t + str(i) + '_' + str(j) + '.csv'
        # open it up, the w means we will write to it
        writer = csv.writer(open(outfile_path, 'w'))
        #create a list with headings for our columns
        headers = ['lat', 'long', 'name', 'vicinity','type']
        #write the row of headings to our CSV file
        writer.writerow(headers)
        for d in g:
            row = []
            row.append(d['geometry']['location']['lat'])
            row.append(d['geometry']['location']['lng'])
            row.append(d['name'].encode('utf8'))
            row.append(d['vicinity'].encode('utf8'))
            row.append(TYPES.encode('utf8'))
            writer.writerow(row)