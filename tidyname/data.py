"""Seed name lists for RandomNameGenerator.

These are pulled from common US given-name and surname frequency lists, then
deliberately left in inconsistent casing - it mirrors the kind of input this
package is meant to clean up, and it means the generator's default output
doubles as a demo of the formatter. The list is real-sized (a few hundred
entries each) so `many()` can produce a decent run without obvious repeats.
"""

FIRST_NAMES = [
    "MARY", "james", "Patricia", "JOHN", "jennifer", "Robert",
    "linda", "MICHAEL", "Elizabeth", "william", "BARBARA", "David",
    "susan", "RICHARD", "Jessica", "joseph", "SARAH", "Thomas",
    "karen", "CHARLES", "Nancy", "christopher", "LISA", "Daniel",
    "betty", "MATTHEW", "Margaret", "anthony", "SANDRA", "Mark",
    "ASHLEY", "donald", "Kimberly", "STEVEN", "emily", "Paul",
    "DONNA", "andrew", "Michelle", "JOSHUA", "carol", "Kenneth",
    "AMANDA", "kevin", "Melissa", "BRIAN", "deborah", "George",
    "STEPHANIE", "edward", "Rebecca", "RONALD", "laura", "Timothy",
    "SHARON", "jason", "Cynthia", "JEFFREY", "kathleen", "Ryan",
    "AMY", "jacob", "Shirley", "GARY", "angela", "Nicholas",
    "ANNA", "eric", "Brenda", "JONATHAN", "pamela", "Stephen",
    "EMMA", "larry", "Nicole", "JUSTIN", "samantha", "Scott",
    "KATHERINE", "frank", "Christine", "BRANDON", "helen", "Raymond",
    "SAMUEL", "diane", "Gregory", "BENJAMIN", "julie", "Alexander",
    "VICTORIA", "patrick", "Joyce", "JACK", "frances", "Dennis",
    "OLIVIA", "jerry", "Evelyn", "HENRY", "denise", "Douglas",
    "SOPHIA", "tyler", "Joan", "PETER", "marie", "Aaron",
    "GRACE", "jose", "Judith", "WALTER", "megan", "Harold",
    "CHLOE", "adam", "Cheryl", "CARL", "andrea", "Arthur",
    "hannah", "NATHAN", "janet", "ZACHARY", "catherine", "KYLE",
    "gloria", "ALAN", "teresa", "JUAN", "ann", "ELIJAH",
    "sara", "WAYNE", "madison", "ROY", "abigail", "EUGENE",
    "ruth", "LOUIS", "kayla", "PHILIP", "christina", "BOBBY",
    "alexis", "JOHNNY", "lori", "MASON", "beverly", "ETHAN",
    "jean", "NOAH", "danielle", "LOGAN", "marilyn", "AUSTIN",
    "kathryn", "SEAN", "isabella", "TERRY", "theresa", "JESSE",
    "diana", "KEITH", "natalie", "ROGER", "tiffany", "BILLY",
    "sophie", "LUIS", "mia", "RANDY", "julia", "VINCENT",
    "heather", "RUSSELL", "olivia", "BRUCE", "judy",
]

LAST_NAMES = [
    "SMITH", "johnson", "Williams", "BROWN", "jones", "Garcia",
    "miller", "DAVIS", "Rodriguez", "martinez", "HERNANDEZ", "Lopez",
    "gonzalez", "WILSON", "Anderson", "thomas", "TAYLOR", "Moore",
    "o'brien", "MCDONALD", "van der berg", "DE LA CRUZ", "d'angelo",
    "Nguyen", "PATEL", "mackenzie", "O'CONNOR", "St-Pierre",
    "JACKSON", "martin", "Thompson", "WHITE", "lee", "Harris",
    "SANCHEZ", "clark", "Ramirez", "LEWIS", "robinson", "Walker",
    "YOUNG", "allen", "King", "WRIGHT", "scott", "Torres",
    "NGUYEN", "hill", "Flores", "GREEN", "adams", "Nelson",
    "BAKER", "hall", "Rivera", "CAMPBELL", "mitchell", "Carter",
    "ROBERTS", "gomez", "Phillips", "EVANS", "turner", "Diaz",
    "PARKER", "cruz", "Edwards", "COLLINS", "reyes", "Stewart",
    "MORRIS", "morales", "Murphy", "COOK", "rogers", "Gutierrez",
    "ORTIZ", "morgan", "Cooper", "PETERSON", "bailey", "Reed",
    "KELLY", "howard", "Ramos", "COX", "ward", "Richardson",
    "WATSON", "brooks", "Chavez", "WOOD", "james", "Bennett",
    "GRAY", "mendoza", "Ruiz", "HUGHES", "price", "Alvarez",
    "CASTILLO", "sanders", "Patel", "MYERS", "long", "Ross",
    "FOSTER", "jimenez", "Powell", "JENKINS", "perry", "Russell",
    "SULLIVAN", "bell", "Coleman", "BUTLER", "gonzales", "Barnes",
    "fisher", "HENDERSON", "vasquez", "SIMMONS", "romero", "GORDON",
    "hunt", "PALMER", "black", "MCCARTHY", "west", "SIMPSON",
    "delgado", "REYNOLDS", "hart", "GRIFFIN", "franklin", "WEBB",
    "salazar", "BURNS", "fox", "MASON", "guzman", "CURTIS",
    "hays", "BISHOP", "duncan", "NASH", "figueroa", "O'DONNELL",
    "mac laren", "de leon", "VAN DYKE", "l'heureux", "St-Amand",
    "SCHNEIDER", "walsh", "Osei", "MULLER", "beaulieu", "Nakamura",
    "KOVACS", "petrov", "Hassan", "AL-RASHID", "bianchi", "Kowalski",
]
