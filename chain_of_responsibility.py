class NullHandler:
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def handle(self, obj, event):
        if self._next_handler is not None:
            return self._next_handler.handle(obj, event)


class EventGet:
    def __init__(self, obj_type):
        self.obj_type = obj_type


class EventSet:
    def __init__(self, obj_value):
        self.obj_value = obj_value


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and issubclass(event.obj_type, int):
            return obj.integer_field
        elif isinstance(event, EventSet) and isinstance(event.obj_value, int):
            obj.integer_field = event.obj_value
            return
        return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and issubclass(event.obj_type, float):
            return obj.float_field
        elif isinstance(event, EventSet) and isinstance(event.obj_value, float):
            obj.float_field = event.obj_value
            return
        return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and issubclass(event.obj_type, str):
            return obj.string_field
        elif isinstance(event, EventSet) and isinstance(event.obj_value, str):
            obj.string_field = event.obj_value
            return
        return super().handle(obj, event)
