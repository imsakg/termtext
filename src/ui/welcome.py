from typing import Type
from textual.app import App
from textual.reactive import Reactive
from textual.widgets import Footer, Placeholder
from textual.widgets import Button, ButtonPressed
from textual.layout import Layout

from textual.driver import Driver
from decimal import Decimal

from rich.align import Align
from rich.console import Console, ConsoleOptions, RenderResult, RenderableType
from rich.padding import Padding
from rich.text import Text

from textual.views import GridView
from textual.widget import Widget

try:
    from pyfiglet import Figlet
except ImportError:
    print("Please install pyfiglet to run this example")
    raise


class FigletText:
    """A renderable to generate figlet text that adapts to fit the container."""

    def __init__(self, text: str) -> None:
        self.text = text

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """Build a Rich renderable to render the Figlet text."""
        size = min(options.max_width / 2, options.max_height)
        if size < 4:
            yield Text(self.text, style="bold")
        else:
            if size < 7:
                font_name = "mini"
            elif size < 8:
                font_name = "small"
            elif size < 10:
                font_name = "standard"
            else:
                font_name = "big"
            font = Figlet(font=font_name, width=options.max_width)
            yield Text(font.renderText(self.text).rstrip("\n"), style="bold")


class Numbers(Widget):
    """The digital display of the calculator."""

    value = Reactive("0")

    def render(self) -> RenderableType:
        """Build a Rich renderable to render the calculator display."""
        return Padding(
            Align.right(FigletText(self.value), vertical="middle"),
            (0, 1),
            style="white on rgb(51,51,51)",
        )


class Welcome(App):
    def __init__(
        self,
        screen: bool = True,
        driver_class: Type[Driver] | None = None,
        log: str = "",
        log_verbosity: int = 1,
        title: str = "Textual Application",
    ):
        super().__init__(screen, driver_class, log, log_verbosity, title)
        self.placeholder_top = Placeholder()
        self.placeholder_top.content = "Welcome to Textual!"
        self.placeholder_top.console_color = "green"

        # set height
        self.placeholder_top.height = 5

        self.placeholder_top.refresh()
        self.placeholder_top.render()

        self.placeholder_bottom = Placeholder()
        self.placeholder_bottom.content = "Welcome to Textual!"
        self.placeholder_bottom.console_color = "green"

        # set height
        # offset

        self.placeholder_bottom.refresh()
        self.placeholder_bottom.render()

    """Demonstrates smooth animation. Press 'b' to see it in action."""

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("b", "toggle_sidebar", "Toggle sidebar")
        await self.bind("q", "quit", "Quit")

    show_bar = Reactive(False)

    def watch_show_bar(self, show_bar: bool) -> None:
        """Called when show_bar changes."""
        self.bar.animate("layout_offset_x", 0 if show_bar else -40)

    def action_toggle_sidebar(self) -> None:
        """Called when user hits 'b' key."""
        self.show_bar = not self.show_bar

    async def on_mount(self) -> None:
        """Build layout here."""
        footer = Footer()
        self.bar = Placeholder(name="left")

        await self.view.dock(footer, edge="bottom")
        await self.view.dock(self.placeholder_top, self.placeholder_bottom, edge="top")
        await self.view.dock(self.bar, edge="left", size=40, z=1)

        self.bar.layout_offset_x = -40

        # self.set_timer(10, lambda: self.action("quit"))
