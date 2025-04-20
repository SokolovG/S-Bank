from collections.abc import Callable


class EventBus:
    def __init__(self) -> None:
        """Set a dictionary where the key is the event type and the value is a list of handlers."""
        self._handlers: dict = {}

    def subscribe(self, event_type: type, handler: Callable) -> None:
        """We subscribe the handler to a certain type of event.

        Args:
            event_type: Type of our event.
            handler: The action we perform with the event.

        """
        if event_type not in self._handlers:
            self._handlers[event_type] = []

        # Adding the handler to the list.
        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)

    def publish(self, event: object) -> None:
        """Publish the event to all subscribers.

        Args:
            event: Our event

        """
        event_type = type(event)

        if event_type not in self._handlers:
            return

        for handler in self._handlers[event_type]:
            handler(event)
