import pandas as pd
from datetime import datetime, timedelta

colnames =['sng_id', 'user_id', 'country']
streaming_data=pd.read_csv('sample_listen-2023-05_2Mlines.log',sep='|',error_bad_lines=False,warn_bad_lines=False,names=colnames)

# Calculer les 50 chansons les plus écoutées par pays
top50_by_country = streaming_data['sng_id'].value_counts().groupby(streaming_data['country']).head(50)
top50_by_country = top50_by_country.groupby(streaming_data['country']).apply(lambda x: ','.join(f'{sng_id}:{count}' for sng_id, count in x.iteritems()))

# Générer le nom de fichier basé sur la date
today = pd.Timestamp.now().strftime('%Y%m%d')
filename = f'country_top50_{today}.txt'

# Écrire les résultats dans le fichier
with open(filename, 'w') as file:
    for country, top50 in top50_by_country.items():
        file.write(f'{country}|{top50}\n')