from py2neo import Graph, Node, Relationship

graph = Graph(password="12345678")

graph.run("CREATE (:Animal {name: 'Simpa', type: 'Cat', color: 'White'})")
graph.run("CREATE (:Animal {name: 'Cat', type: 'Mammal'})")
graph.run("CREATE (:Animal {name: 'Killdeer', type: 'Bird', fur: true, beak: 'Long and Thin'})")
graph.run("CREATE (:Person {name: 'Alia', race: 'Hobbit'})")
graph.run("CREATE (:Location {name: 'Acciaroli', age: 100, location: 'Oceanic Shore'})")
graph.run("CREATE (:Animal {name: 'Whale', type: 'Mammal', habitat: 'Water'})")


graph.run("""
    MATCH (simpa:Animal {name: 'Simpa'})
    MERGE (white:Color {name: 'White'})
    MERGE (simpa)-[:HAS_COLOR]->(white)
""")

graph.run("""
    MATCH (simpa:Animal {name: 'Simpa'})
    MATCH (cat:Animal {name: 'Cat'})
    MERGE (simpa)-[:IS_A]->(cat)
    WITH simpa
    SET simpa.color = 'White'
""")

graph.run("""
    MATCH (simpa:Animal {name: 'Simpa'})
    MATCH (killdeer:Animal {name: 'Killdeer'})
    MERGE (simpa)-[:CAUGHT]->(killdeer)
""")

graph.run("""
    MATCH (simpa:Animal {name: 'Simpa'})
    MATCH (alia:Person {name: 'Alia'})
    MERGE (simpa)-[:OWNED_BY]->(alia)
""")

graph.run("""
    MATCH (cat:Animal {name: 'Cat'})
    MERGE (milk:Food {name: 'Milk', type: 'Drink'})
    MERGE (salmon:Food {name: 'Salmon fish', type: 'Eat'})
    MERGE (cat)-[:LIKES]->(milk)
    MERGE (cat)-[:LIKES]->(salmon)
    MERGE (cat)-[:SITS_ON]->(:Object {name: 'Carpet'})
    MERGE (cat)-[:IS_A]->(mammalAttribute:Attribute {name: 'Mammal'})
""")

graph.run("""
    MATCH (killdeer:Animal {name: 'Killdeer'})
    MATCH (mammalAttribute:Attribute {name: 'Mammal'})
    MERGE (birdAttribute:Attribute {name: 'Bird'})
    MERGE (killdeer)-[:IS_A]->(birdAttribute)
    MERGE (birdAttribute)-[:IS_A]->(mammalAttribute)
    MERGE (killdeer)-[:HIDES_BETWEEN]->(:Object {name: 'Curtain'})
    MERGE (killdeer)-[:HIDES_BETWEEN]->(:Object {name: 'Window'})
""")

graph.run("""
    MATCH (alia:Person {name: 'Alia'})
    MERGE (magicRing:Object {name: 'Magic Ring'})
    MERGE (cave:Object {name: 'Cave'})
    MERGE (alia)-[:FOUND]->(magicRing)
    MERGE (magicRing)-[:IN_A]->(cave)
""")

graph.run("""
    MATCH (alia:Person {name: 'Alia'})
    MATCH (acciaroli:Location {name: 'Acciaroli'})
    MERGE (alia)-[:LIVES_IN]->(acciaroli)
""")

graph.run("""
    MATCH (alia:Person {name: 'Alia'})
    MATCH (whale:Animal {name: 'Whale'})
    MERGE (alia)-[:SAW]->(whale)
""")

graph.run("""
    MATCH (acciaroli:Location {name: 'Acciaroli'})
    MERGE (acciaroli)-[:IS_ON]->(:Location {name: 'Oceanic Shore'})
    SET acciaroli.age = 100
""")

graph.run("""
    MATCH (whale:Animal {name: 'Whale'})
    MATCH (mammalAttribute:Attribute {name: 'Mammal'})
    MERGE (whale)-[:LIVES_IN]->(:Habitat {name: 'Water'})
    MERGE (whale)-[:IS_A]->(mammalAttribute)
""")

graph.run("""
    MATCH (mammalAttribute:Attribute {name: 'Mammal'})
    MERGE (vertebrae:Attribute {name: 'Vertebrae'})
    MERGE (mammalAttribute)-[:HAS]->(vertebrae)
""")


graph.run("""
    MATCH (mammalAttribute:Attribute {name: 'Mammal'})
    MATCH (birdAttribute:Attribute {name: 'Bird'})
    MERGE (animalKingdom:Attribute {name: 'Kingdom_Animal'})
    MERGE (mammalAttribute)-[:BELONGS_TO]->(animalKingdom)
    MERGE (birdAttribute)-[:BELONGS_TO]->(animalKingdom)
""")

graph.run("""
    MATCH (alia:Person {name: 'Alia'})
    MERGE (hobbitRace:Race {name: 'Hobbit'})
    MERGE (alia)-[:IS_A]->(hobbitRace)
""")

# 1.1. Alia likes to catch and eat fish
graph.run("""
    MATCH (alia:Person {name: 'Alia'})
    MATCH (fish:Animal {name: 'Fish'})
    MERGE (alia)-[:LIKES]->(fish)
    MERGE (alia)-[:CATCHES]->(fish)
    MERGE (alia)-[:EATS]->(fish)
""")

# 1.2. Modify the age of the village "Acciaroli"
graph.run("""
    MATCH (acciaroli:Location {name: 'Acciaroli'})
    SET acciaroli.age = 1000
""")

# 1.3. Delete statements
# a. Simpa is white in color and is owned by a Girl, Alia.
graph.run("""
    MATCH (simpa:Animal {name: 'Simpa'})-[r]->()
    WHERE TYPE(r) IN ['HAS_COLOR', 'OWNED_BY']
    DELETE r
""")

graph.run("""
    MATCH (white:Color {name: 'White'})
    DETACH DELETE white
""")

# b. Alia once saw a big Whale
graph.run("""
    MATCH (alia:Person {name: 'Alia'})-[saw:SAW]->(whale:Animal {name: 'Whale'})
    DELETE saw
""")

# 1.4. Queries
# a. What’s the age of Alia?
result_age = graph.run("""
    MATCH (alia:Person {name: 'Alia'})
    RETURN alia.age
""").evaluate()

print(f"The age of Alia is: {result_age}")

# b. What type of mammal is the Whale?
result_mammal_type = graph.run("""
    MATCH (whale:Animal {name: 'Whale'})-[:IS_A]->(mammalAttribute:Attribute {name: 'Mammal'})
    RETURN mammalAttribute.type
""").evaluate()

print(f"The type of mammal the Whale is: {result_mammal_type}")

# c. Where is Killdeer hiding?
result_hiding_place = graph.run("""
    MATCH (killdeer:Animal {name: 'Killdeer'})-[:HIDES_BETWEEN]->(curtain:Object),
          (killdeer)-[:HIDES_BETWEEN]->(window:Object)
    RETURN curtain.name, window.name
""").evaluate()

print(f"Killdeer is hiding between {result_hiding_place[0]} and {result_hiding_place[1]}")
