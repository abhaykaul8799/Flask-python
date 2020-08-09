from basic import db,Puppy

## CREATE

my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

## READ

all_puppies = Puppy.query.all()

print(all_puppies)

puppy_one = Puppy.query.get(1)

print(puppy_one)

puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

## UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

## DELETE

second_puppy = Puppy.query.get(3)
db.session.delete(second_puppy)
db.session.commit()

print(Puppy.query.all())