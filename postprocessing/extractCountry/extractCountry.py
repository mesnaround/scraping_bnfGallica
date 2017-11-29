import pandas as pd

def extractCountry(title, dct):
  for key in dct.keys():
    if key in title:
      return dct[key]
  return ''  

city_to_country = {
  'Constantinople': 'Turkey',
  'Baalbec': 'Lebanon',
  'Alep': 'Syria',
  'Liban': 'Lebanon',
  'Alexandrie': 'Egypt',
  'Phile': 'Egypt',
  'Kaire': 'Egypt',
  'Jérusalem': 'Israel',
  'Aphrodisias': 'Turkey',
  'Athènes': 'Greece',
  'Paris': 'France',
  'Damas': 'Syria',
  'Paris': 'France',
  'Samarie': 'Israel',
  'Tuaires': 'France',
  'Dendérah': 'Egypt',
  'Tripoli' : 'Libya',
  'Milet': 'Turkey',
  'Scutari':'Turkey',
  'Assouan': 'Egypt',
  'Syra': 'Greece',
  'Jaffa': 'Israel',
  'Karnak': 'Egypt',
  'Syrie': 'Syria',
  'Tuileries': 'France',
  'Mylasa': 'Turkey',
  'Frascati': 'Italiy',
  'Bosphor': 'Turkey',
  'Memphis': 'Egypt',
  'Caire': 'Egypt',
  'Smyrne': 'Turkey',
  'Cordove': 'Spain'
}

df = pd.read_csv('clean.csv', sep='#')

df['Country'] = df.Titre.apply(lambda x: extractCountry(x, city_to_country))

df.to_csv('withCountry.txt', index=False, sep='#')
