# -*- coding: utf-8 -*-
# Copyright (C) 2014 Optiv, Inc. (brad.spengler@optiv.com)
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature

class InstalledApps(Signature):
    name = "recon_programs"
    description = "收集系统安装程序信息"
    severity = 3
    confidence = 20
    categories = ["recon"]
    authors = ["Optiv"]
    minimum = "1.2"

    def run(self):
        office_pkgs = ["ppt","doc","xls","eml","pdf"]
        if any(e in self.results["info"]["package"] for e in office_pkgs):
            return False

        if self.check_read_key(pattern= ".*\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Uninstall.*", regex=True):
            return True

        return False