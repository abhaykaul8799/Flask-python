from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Put /puppify/name in url to puppify your pets name</h1>'

# Dynamic routing
# pet variable will be initialized by the <pet> part of url
@app.route("/puppify/<pet>")
def pets(pet):
    if pet.endswith('y') or pet.endswith('e') or pet.endswith('u'):
        pet = pet[:-1] + "iful"
    elif pet.endswith('i'):
        pet = pet + "ful"
    elif pet.endswith('r'):
        pet = pet + 'ing'
    else:
        pet = pet + 'y'
    return "Puppified name: {}".format(pet)


if __name__ == "__main__":
    app.run(debug=True)