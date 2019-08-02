# Weather Bot (updated using Rasa 1.0 & later)

This chat bot let us know the weather.

# Rasa Installation
[https://rasa.com/docs/rasa/user-guide/installation/#installation](https://rasa.com/docs/rasa/user-guide/installation/#installation)

# Steps:
1. Create a new virtual environment. (Python version : Python 3.6.5)
2. Activate the environment
3. Copy the folder to your local path
4. Perform the steps mentioned in [https://rasa.com/docs/rasa/user-guide/rasa-tutorial/](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/)
5. Run rasa action server in a new terminal using the below command`rasa run actions`
6. Then in a new terminal start rasa shell by typing the command `rasa shell` and wait for few seconds until the chatbot is initiated.

`2019-08-02 14:21:06 **INFO**  root  - Starting Rasa server on http://localhost:5005
2019-08-02 14:21:18 **INFO**  rasa.nlu.components  - Added 'SpacyNLP' to component cache. Key 'SpacyNLP-en'.
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  Hi 
Hello! How can I help?
Your input ->  Whats the weather like in Berlin? 
It is currently Partly cloudy in Berlin at the moment. The temperature is 22.0 degrees, the humidity is 61% and the wind speed is 0.0 mph.
Your input ->`
