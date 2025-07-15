import pytest
from project import load_story, get_next_scene,display_scene


# Mock story for testing
mock_story = {
    "start": {
        "text": "You wake up on a spaceship.",
        "choices": {
            "a": {"desc": "Go left", "next": "left_room"},
            "b": {"desc": "Go right", "next": "right_room"}
        }
    }
}

def test_load_story(tmp_path):
    # Create a temporary story.json file
    story_data = {
        "start": {
            "text": "Test scene.",
            "choices": {
                "a": {"desc": "Choice A", "next": "end"}
            }
        }
    }
    file = tmp_path / "story.json"
    file.write_text(str(story_data).replace("'", '"'))  # valid JSON

    loaded_story = load_story(file)
    assert loaded_story["start"]["text"] == "Test scene."
    assert "a" in loaded_story["start"]["choices"]

def test_get_next_scene_valid():
    scene = mock_story["start"]
    next_id = get_next_scene(scene, "a")
    assert next_id == "left_room"

def test_get_next_scene_invalid(capfd):
    scene = mock_story["start"]
    next_id = get_next_scene(scene, "x")
    captured = capfd.readouterr()
    assert "Invalid choice." in captured.out
    assert next_id is None

def test_display_scene(capfd):
    scene = {
        "text": "Hello, {name}! Welcome to the test scene.",
        "choices": {
            "a": {"desc": "Option A"},
            "b": {"desc": "Option B"}
        }
    }
    player_name = "Zaphod"

    display_scene(scene, player_name)

    captured = capfd.readouterr()
    assert "Hello, Zaphod! Welcome to the test scene." in captured.out
    assert "a: Option A" in captured.out
    assert "b: Option B" in captured.out
