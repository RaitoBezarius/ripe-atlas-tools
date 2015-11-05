from __future__ import print_function, absolute_import

from ...helpers.validators import ArgumentType
from ...settings import conf

from .base import Command


class NtpMeasureCommand(Command):

    def add_arguments(self):

        Command.add_arguments(self)

        spec = conf["specification"]["types"]["ntp"]

        specific = self.parser.add_argument_group("NTP-specific Options")
        specific.add_argument(
            "--packets",
            type=ArgumentType.integer_range(minimum=1),
            default=spec["packets"],
            help="The number of packets sent"
        )
        specific.add_argument(
            "--timeout",
            type=ArgumentType.integer_range(minimum=1),
            default=spec["timeout"],
            help="The timeout per-packet"
        )

    def _get_measurement_kwargs(self):

        r = Command._get_measurement_kwargs(self)

        r["packets"] = self.arguments.packets
        r["timeout"] = self.arguments.timeout

        return r
