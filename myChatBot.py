from flask import Flask
from flask_socketio import SocketIO, emit
import openai
import logging
from course import Course
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()
# הגדרת מפתח ה-API
openai_api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

logging.basicConfig(level=logging.INFO)

def natural_language_to_sql(prompt):
    conversion_prompt = f"Convert the following natural language query to an SQL query: '{prompt}'"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that converts natural language questions into SQL queries."},
                {"role": "user", "content": conversion_prompt},
            ],
            max_tokens=150
        )
        sql_query = response['choices'][0]['message']['content'].strip()
        return sql_query
    except openai.error.RateLimitError:
        logging.error("שגיאת מערכת: Exceeded quota")
        return "להפעלה נא פנו להנהלת דיברסיטק"

def query_db(sql_query):
    courses = [
        Course(1, "Introduction to Python", "A beginner's course on Python programming.",
               datetime(2022, 1, 1, 10, 0, 0), datetime(2023, 1, 1, 10, 0, 0)),
        Course(2, "Advanced Java", "An advanced course on Java programming.", datetime(2022, 2, 1, 10, 0, 0),
               datetime(2023, 2, 1, 10, 0, 0)),
        Course(3, "Database Systems", "A comprehensive course on database systems.", datetime(2022, 3, 1, 10, 0, 0),
               datetime(2023, 3, 1, 10, 0, 0))
    ]
    return courses

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def ask_chatgpt(prompt):
    sql_query = natural_language_to_sql(prompt)
    if(sql_query== "להפעלה נא פנו להנהלת דיברסיטק"):
        return  "להפעלה נא פנו להנהלת דיברסיטק"
    results = query_db(sql_query)
    formatted_data = '\n'.join([str(res) for res in results])
    chatgpt_prompt = f"User asked: {prompt}\nHere is the relevant data:\n{formatted_data}\nProvide a response to the user based on the above data"
    chatgpt_response = get_chatgpt_response(chatgpt_prompt)
    return chatgpt_response

@socketio.on('message')
def handle_message(message):
    logging.info(f'Received message: {message}')
    response = ask_chatgpt(message)
    emit('response', response)

if __name__ == '__main__':
    socketio.run(app, debug=True)