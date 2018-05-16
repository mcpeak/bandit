# -*- coding:utf-8 -*-
#
# Copyright 2018 Netflix
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import bandit
from bandit.core import test_properties as test
@test.checks('Call')
@test.test_id('B901')
def execution_in_setup_py(context):
    """**B901: Check for execution in setup.py**
    """
    if context.call_function_name_qual in ['setuptools.setup']:
        if 'cmdclass' in context.call_keywords:
            return bandit.Issue(
                severity=bandit.LOW,
                confidence=bandit.HIGH,
                text='Execution in setup.py',
                lineno=context.get_lineno_for_call_arg('cmd_class'),
            )
