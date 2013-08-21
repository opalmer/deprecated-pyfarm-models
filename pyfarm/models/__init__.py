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
Contains all the models used for database communication and object
relational management.
"""

# NOTE: All models must be loaded here so the mapper
#       can create the relationships on startup
from pyfarm.models.job import JobTagsModel, JobSoftwareModel, JobModel
from pyfarm.models.task import TaskModel
from pyfarm.models.agent import AgentTagsModel, AgentSoftwareModel, AgentModel

# load the interface classes
from pyfarm.models.agent import Agent, AgentSoftware, AgentTag
from pyfarm.models.job import Job, JobSoftware, JobTag
from pyfarm.models.task import Task

__all__ = ["Agent", "AgentSoftware", "AgentTag",
           "Job", "JobSoftware", "JobTag", "Task"]