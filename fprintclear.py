#!/usr/bin/env python

from os import geteuid

import typer
from gi import require_version

# Load FPrint gi module
require_version("FPrint", "2.0")
from gi.repository import FPrint

app = typer.Typer()


@app.command()
def main(delete: bool = typer.Option(False, "-d", help="Delete enrolled fingerprints")):
    if geteuid() != 0:
        typer.echo(
            "You need to have root privileges to run this script.\n"
            "Please try again, this time using 'sudo'. Exiting."
        )
        raise typer.Exit()

    # Get FPrint Context
    fprint_context = FPrint.Context()

    # Loop over FPrint devices
    for fprint_device in fprint_context.get_devices():

        # Print device info
        typer.echo(fprint_device)
        typer.echo(fprint_device.get_driver())
        typer.echo(fprint_device.props.device_id)

        # Open the device synchronously.
        fprint_device.open_sync()

        # Get list of enrolled prints
        enrolled_fingerprints = fprint_device.list_prints_sync()
        typer.echo(f"Device has {len(enrolled_fingerprints)} enrolled fingerprints.")

        # Loop through enrolled fingerprints
        for fingerprint in enrolled_fingerprints:

            # Print fingerprint info
            date = fingerprint.props.enroll_date
            typer.echo(
                f"    {date.get_year():04d}-{date.get_month():02d}-{date.get_day():02d} valid: {date.valid()}"
            )
            typer.echo(f"    {fingerprint.props.finger}")
            typer.echo(f"    {fingerprint.props.username}")
            typer.echo(f"    {fingerprint.props.description}")

            # Check for delete flag
            if delete:
                # Delete print
                typer.echo("Deleting print:")
                fprint_device.delete_print_sync(fingerprint)
                typer.echo("Deleted")

        # Close the device synchronously.
        fprint_device.close_sync()


if __name__ == "__main__":
    app()
