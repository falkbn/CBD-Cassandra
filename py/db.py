import cassandra.cluster as cass_cluster


def connect_db():

    cluster = cass_cluster.Cluster(contact_points=['localhost'], port=9042)
    session = cluster.connect()
    return session


def create_keyspace(name, strategy, replication_factor):

    session = connect_db()

    session.execute(
        "CREATE KEYSPACE {} WITH replication={'class':'{}', 'replication_factor':{};".format(
            name, strategy, replication_factor
        )
    )
