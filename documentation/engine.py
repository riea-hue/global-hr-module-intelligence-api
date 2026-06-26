from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


class DocumentationEngine:
    """
    Generic documentation rendering engine for metadata-driven artifacts.
    """

    def __init__(self, template_directory: Path):
        self.template_directory = template_directory

        self.environment = Environment(
            loader=FileSystemLoader(str(template_directory)),
            autoescape=select_autoescape(
                enabled_extensions=(),
                default=False,
            ),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render(self, template_name: str, context: dict) -> str:
        template = self.environment.get_template(template_name)
        return template.render(**context)

    @staticmethod
    def write(output_file: Path, content: str) -> None:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(content, encoding="utf-8")