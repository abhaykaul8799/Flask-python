from basic import db,Puppy

# CREATES ALL TABLES
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',5)

db.session.add_all([sam,frank])

db.session.commit()

print(sam.id)
print(frank.id)