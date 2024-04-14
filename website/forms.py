import typing


class StyleFormMixin:
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field_name == "is_active":
                field.widget.attrs["class"] = "form-check-input"
