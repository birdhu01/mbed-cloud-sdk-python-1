# --------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Some shared utilities"""
import datetime
import uuid

from mbed_cloud.exceptions import CloudValueError


def force_utc(time, name='field'):
    """Appending 'Z' to isoformatted time - explicit timezone is required for most APIs"""
    if not isinstance(time, datetime.datetime):
        raise CloudValueError("%s should be of type datetime" % (name,))
    return time.isoformat() + "Z"


def new_async_id():
    """A source of new client-side async ids"""
    return str(uuid.uuid4())
