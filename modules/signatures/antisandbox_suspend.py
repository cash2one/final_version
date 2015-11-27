# -*- coding: utf-8 -*-
# Copyright (C) 2015 Optiv, Inc. (brad.spengler@optiv.com)
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

class AntiSandboxSuspend(Signature):
    name = "antisandbox_suspend"
    description = "尝试阻止Cuckoo线程以防止恶意行为被记录"
    severity = 3
    confidence = 80
    categories = ["anti-sandbox"]
    authors = ["Optiv"]
    minimum = "1.3"
    evented = True

    filter_apinames = set(["NtSuspendThread"])

    def __init__(self, *args, **kwargs):
        Signature.__init__(self, *args, **kwargs)

    def on_call(self, call, process):
        alert = self.get_argument(call, "Alert")
        if alert:
            return True
