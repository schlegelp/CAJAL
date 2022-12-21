from _typeshed import Incomplete

class BlitManager:
    ax: Incomplete
    canvas: Incomplete
    background: Incomplete
    artists: Incomplete
    def __init__(self, ax) -> None: ...
    def add_artists(self, artists) -> None: ...
    def remove_artists(self, artists) -> None: ...
    def on_draw_event(self, event: Incomplete | None = ...) -> None: ...
    def redraw(self) -> None: ...
    def draw_artists(self) -> None: ...

class EventManager:
    canvas: Incomplete
    tools: Incomplete
    active_tool: Incomplete
    def __init__(self, ax) -> None: ...
    def connect_event(self, name, handler) -> None: ...
    def attach(self, tool) -> None: ...
    def detach(self, tool) -> None: ...
    def on_mouse_press(self, event) -> None: ...
    def on_key_press(self, event) -> None: ...
    def on_mouse_release(self, event) -> None: ...
    def on_move(self, event) -> None: ...
    def on_scroll(self, event) -> None: ...
