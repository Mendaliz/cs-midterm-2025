from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def list_characters():
    try:
        data = requests.get("https://swapi.dev/api/people/")
        if data.status_code != 200:
            print(data.status_code)
            raise Exception("Message") 
        data = data.json()["results"][:10]
        name = request.args.get('name')
        if name != None:
            char = requests.get(f"https://swapi.dev/api/people/?search={name}")
            if char.status_code != 200:
                raise Exception("Message")
            char = char.json()["results"]
            return render_template('char.html', data=char)
        return render_template('list.html', data=data)
    except:
        print("exception")
        with open('character.json', 'r') as file:
            data = json.load(file)["results"][:10]
            name = request.args.get('name')
            if name != None:
                for person in data:
                    if person.name == name:
                        char = [person]
                print(data)
                print()
                print(char)
                return render_template('char.html', data=char)
            return render_template('list.html', data=data)

@app.route('/contact')
def register():
    return render_template('contact.html', error=0)

@app.route('/login', methods=["POST"])
def handle_form():
    email = request.form.get("email", "")
    message = request.form.get("message", "")
    print(f"User email: {email}")
    print(f"Message: {message}")
    return render_template('login.html', email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)