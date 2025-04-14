import asyncio

import click
from click import Group
from litestar.plugins import CLIPluginProtocol

from src.infrastructure.database.seeders.run_seeder import run


class CLIPlugin(CLIPluginProtocol):
    def on_cli_init(self, cli: Group) -> None:
        @cli.command()
        def run_seeders():
            asyncio.run(run())
            click.echo("Seeders executed successfully!")