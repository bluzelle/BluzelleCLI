import pyBluzelle
import factory
import models
import csv

# factory used to create random key/value pairings (based on faker_boy module)


class RandomUserFactory(factory.Factory):
    class Meta:
        model = models.KeyValue

    keyRec = factory.Faker('first_name')
    valRec = factory.Faker('last_name')

# function to drop all keys with a specified uuid


def dropAllBluzelle(url, port, uuid):
    b = pyBluzelle.create_connection(url, port, uuid)

    for key in b.keys():
        b.delete(key)
    print('')
    print('Dropped all records from the uuid')
    print('')


# creates records depending on the given number of records to be made OR
# file input

def createRecords(url, port, uuid, recNum):
    b = pyBluzelle.create_connection(url, port, uuid)
    recsCommitted = 0

    print('')
    print('These are the records inserted into the Bluzelle Database')
    print('----------------------------------------------------------------')

    recs = RandomUserFactory.create_batch(size=recNum)

    for model in recs:
        key = model.keyRec.encode('utf-8')
        val = model.valRec.encode('utf-8')
        print('[KEY]: ' + model.keyRec + ' [VALUE]: ' + model.valRec)
        res = b.create(key, val)
        if(res is None):
            recsCommitted += 1

    print('')
    print('A total of {} has been successfully loaded into the database'.format(
        recsCommitted))
    print('')


#creates records depending on the given csv file
def createRecordsFromFile(url, port, uuid, fileLoad):
    b = pyBluzelle.create_connection(url, port, uuid)
    recsCommitted = 0

    print('')
    print('These are the records inserted into the Bluzelle Database')
    print('----------------------------------------------------------------')

    with open(fileLoad) as csvfile:
            reader = csv.reader(csvfile, delimiter=':')
            for row in reader:
                print('[KEY]: {} [VALUE]: {}'.format(row[0], row[1]))
                res = b.create(row[0], row[1])
                if(res is None):
                    recsCommitted += 1

    print('')
    print('A total of {} has been successfully loaded into the database'.format(
        recsCommitted))
    print('')