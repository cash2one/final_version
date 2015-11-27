# -*- coding: utf-8 -*-
# Copyright (C) 2012 Claudio "nex" Guarnieri (@botherder), Optiv, Inc. (brad.spengler@optiv.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class VBoxDetectACPI(Signature):
    name = "antivm_vbox_acpi"
    description = "通过ACPI技术检测VirtualBox系统"
    severity = 3
    categories = ["anti-vm"]
    authors = ["nex", "Optiv"]
    minimum = "1.2"

    def run(self):
        if self.check_key(pattern=".*\\\\HARDWARE\\\\ACPI\\\\(DSDT|FADT|RSDT)\\\\VBOX__$", regex=True):
            return True

        return False
