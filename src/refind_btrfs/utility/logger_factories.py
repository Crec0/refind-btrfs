# region Licensing
# SPDX-FileCopyrightText: 2020 Luka Žaja <luka.zaja@protonmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

""" refind-btrfs - Generate rEFInd manual boot stanzas from btrfs snapshots
Copyright (C) 2020  Luka Žaja

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# endregion

import sys
from logging import Handler, NullHandler, StreamHandler
from typing import Type

from systemd.journal import JournalHandler

from common.abc import BaseLoggerFactory


class StreamLoggerFactory(BaseLoggerFactory):
    def get_handler(self) -> Type[Handler]:
        return StreamHandler(sys.stdout)


class NullLoggerFactory(BaseLoggerFactory):
    def get_handler(self) -> Type[Handler]:
        return NullHandler()


class SystemdLoggerFactory(BaseLoggerFactory):
    def get_handler(self) -> Type[Handler]:
        return JournalHandler()
