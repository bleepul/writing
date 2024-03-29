from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
d = GraphDatabase.driver(uri, auth=("neo4j", "password"))


def print_friends_of(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(f) "
                         "WHERE a.name = {name} "
                         "RETURN f.name", name=name):
        print(record["f.name"])


def create_person(driver, name):
    with driver.session() as session:
        return session.run("CREATE (a:Person {name:$name}) "
                           "RETURN id(a)", name=name).single().value()


def create_dog(driver, name):
    with driver.session() as session:
        return session.run("CREATE (a:Dog {name:$name}) "
                            "RETURN id(a)", name=name).single().value()


a = create_person(d,"Kim")
a = create_dog(d,"Fido")

with d.session() as session:
    session.read_transaction(print_friends_of, "Alice")