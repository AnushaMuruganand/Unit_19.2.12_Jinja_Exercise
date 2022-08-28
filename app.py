from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def list_stories():

    # Here we pass just the values in the stories dict and NOT the keys
    return render_template('list-stories.html', stories = stories.values())

@app.route('/questions')
def matlib_question_form():

    # Getting the story.code based on the story the  user selected 
    story_selected = request.args["story_id"]

    # Based on the story.code we got we selecg that particulat story instance
    story = stories[story_selected]

    # Getting the questions from the "prompts" from the story class
    questions = story.prompts
    prompts = [question.capitalize() for question in questions]

    return render_template('questions.html', story_id = story_selected, title = story.title, prompts = prompts)

@app.route('/story')
def show_story():

    # Getting the story.code from the <input> which is hidden in our form and which was retrieved from "/" path 
    story_selected = request.args["story_id"]

    # Based on the story.code we got we selecg that particulat story instance
    story = stories[story_selected]

    # We generate a story based on the input we got from the form and pass in that input as a dict to the "generate()" in story class

    my_story = story.generate(request.args)

    return render_template('story.html',title = story.title, text = my_story)

    