# No shebang line, this module is meant to be imported
#
# Copyright 2013 Oliver Palmer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Projects
========

Top level table used as a grouping mechanism for many components of PyFarm
 including jobs, tasks, agents, users, and more.
"""

from pyfarm.master.application import db
from pyfarm.models.core.types import id_column
from pyfarm.models.core.cfg import TABLE_PROJECT


class Project(db.Model):
    __tablename__ = TABLE_PROJECT
    id = id_column()
    name = db.Column(db.String)