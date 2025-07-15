# Galactic Hitchhiker

#### Video Demo: <>

#### Description:

**Galactic Hitchhiker** is an interactive fiction game built in Python, inspired by Douglas Adams' *The Hitchhiker's Guide to the Galaxy*. The user plays as a character thrown into strange and humorous galactic situations, navigating an unpredictable branching story via a terminal interface.

The game begins with the user standing on Earth as a spaceship descends. From there, the player makes choices that determine their path: from bureaucratic alien planets to cat-filled dimensions and black hole meditations. Each decision leads to unique story outcomes, including triumph, transcendence, or hilarious failure.

---

## Files in the Project

### `project.py`
This is the main Python program. It includes:

- `main()`: Starts the interactive game, loading the story and looping through scenes based on player choices.
- `load_story(path)`: Loads a `.json` story file and returns it as a Python dictionary.
- `display_scene(scene, name)`: Displays the scene's text (with name formatting) and available choices.
- `get_next_scene(scene, choice)`: Returns the ID of the next scene based on user input. Handles invalid input gracefully.

### `story.json`
A structured JSON file that contains all the story scenes, choices, and possible paths the user can take. Each node includes scene text and options that lead to other scenes.

### `test_project.py`
Contains tests for three of the core functions:

- `test_load_story()`: Verifies that story data is correctly loaded from a file.
- `test_get_next_scene_valid()` and `test_get_next_scene_invalid()`: Check that valid and invalid choices are handled properly.
- `test_display_scene()`: Confirms that text and choices are printed correctly, including proper name formatting.

### `requirements.txt`
Lists the necessary dependencies for the project. Only `pytest` is required to run the test suite:

### Future Improvements

In the future, I’d like to expand this into a web-based or GUI version using something like Tkinter or Flask. I’d also like to add more scenes and allow the player to save their progress.

### Reflections

This project was a fun and challenging way to apply everything I learned in CS50P. I enjoyed working with JSON, building reusable functions, and writing testable code that tells a story.
