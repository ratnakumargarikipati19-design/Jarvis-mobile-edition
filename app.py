from flask import Flask, render_template, jsonify
import subprocess
import pyttsx3
import threading
app = Flask(__name__)
# Initialize Voice Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150) # Speed of speech
def speak(text):
 engine.say(text)
 engine.runAndWait()
# Route for Mobile UI
@app.route('/')
def home():
return render_template('index.html')
# Route for Commands
@app.route('/command/<action>')
def command(action):
 reply = ""
if action == 'youtube':
 subprocess.Popen("explorer https://www.youtube.com", shell=True)
 reply = "Opening YouTube, sir."
elif action == 'google':
 subprocess.Popen("explorer https://www.google.com", shell=True)
 reply = "Opening Google, sir."
elif action == 'calculator':
 subprocess.Popen("calc.exe")
 reply = "Opening Calculator, sir."
elif action == 'morning':
 reply = 
"Good morning sir! Weather is 28 degrees. You have 3 meetings today. Opening your dashboard."
 subprocess.Popen("explorer https://www.google.com", shell=True)
# Run voice in background so UI doesn't freeze
 threading.Thread(target=speak, args=(reply,)).start()
return jsonify({"status": "success", "reply": reply})
# Speak the reply
 threading.Thread(target=speak, args=(reply,)).start()
return jsonify({"status": "success", "reply": reply})
if __name__ == '__main__':
print(" JARVIS MOBILE SERVER RUNNING...")
# host='0.0.0.0' is MUST for mobile access
 app.run(host='0.0.0.0', port=5000, debug=False)