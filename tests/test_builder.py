import json
import os
import tempfile

import pytest

from builder import Builder, ComponentNotFoundError


def test_add_and_render_happy_path():
    b = Builder()
    c1 = b.add_component("button", (10, 20))
    c2 = b.add_component("text", (30, 40))

    rendered = b.render()
    assert rendered == [
        {"id": c1.id, "type": "button", "position": [10, 20]},
        {"id": c2.id, "type": "text", "position": [30, 40]},
    ]


def test_move_component_updates_position():
    b = Builder()
    comp = b.add_component("image", (0, 0))
    b.move_component(comp.id, (100, 200))
    rendered = b.render()
    assert rendered[0]["position"] == [100, 200]


def test_move_nonexistent_component_raises():
    b = Builder()
    b.add_component("button", (0, 0))
    with pytest.raises(ComponentNotFoundError):
        b.move_component(999, (1, 1))


def test_save_and_load_preserves_design(tmp_path):
    b = Builder()
    b.add_component("button", (5, 5))
    b.add_component("text", (15, 25))

    file_path = tmp_path / "design.json"
    b.save(str(file_path))

    # Load into a new builder
    loaded = Builder.load(str(file_path))
    assert loaded.render() == b.render()


def test_load_with_higher_ids_continues_counter():
    # Prepare a file with a component id of 42
    data = [{"id": 42, "type": "button", "position": [0, 0]}]
    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".json") as tf:
        json.dump(data, tf)
        tf_path = tf.name

    try:
        loaded = Builder.load(tf_path)
        # Next added component should have id 43
        new_comp = loaded.add_component("text", (1, 1))
        assert new_comp.id == 43
    finally:
        os.unlink(tf_path)


def test_add_component_invalid_position_raises():
    b = Builder()
    with pytest.raises(ValueError):
        b.add_component("button", "not-a-tuple")
    with pytest.raises(ValueError):
        b.add_component("button", (1,))  # wrong length
