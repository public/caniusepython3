# Copyright 2014 Google Inc. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import unicode_literals

from caniusepypy import pypi
from caniusepypy.test import unittest


class NameTests(unittest.TestCase):

    def test_simple(self):
        want = 'simple-name_with.everything-separator_known'
        got = pypi.just_name(want)
        self.assertEqual(got, want)

    def test_requirements(self):
        want = 'project.name'
        got = pypi.just_name(want + '>=2.0.1')
        self.assertEqual(got, want)

    def test_bad_requirements(self):
        # From the OpenStack requirements file:
        # https://raw2.github.com/openstack/requirements/master/global-requirements.txt
        want = 'warlock'
        got = pypi.just_name(want + '>1.01<2')
        self.assertEqual(got, want)

    def test_metadata(self):
        want = 'foo'
        got = pypi.just_name("foo; sys.platform == 'okook'")
        self.assertEqual(got, want)


class OverridesTests(unittest.TestCase):

    def test_all_lowercase(self):
        for name in pypi.overrides():
            self.assertEqual(name, name.lower())


class NetworkTests(unittest.TestCase):

    def pypy_classifiers(self):
        key_classifier = 'Programming Language :: Python :: Implementation :: PyPy'
        classifiers = frozenset(pypi.pypy_classifiers())
        self.asssertIn(key_classifier, classifiers)
        self.assertGreaterEqual(len(classifiers), 5)
        for classifier in classifiers:
            self.assertTrue(classifier.startswith(key_classifier))


    def test_all_pypy_projects(self):
        projects = pypi.all_pypy_projects()
        self.assertGreater(len(projects), 300)
        self.assertTrue(all(project == project.lower() for project in projects))
        self.assertTrue(frozenset(pypi.overrides().keys()).issubset(projects))

    def test_all_pypy_projects_explicit_overrides(self):
        added_port = 'asdfasdfasdfadsffffdasfdfdfdf'
        projects = pypi.all_pypy_projects(set([added_port]))
        self.assertIn(added_port, projects)

    def test_all_projects(self):
        projects = pypi.all_projects()
        self.assertTrue(all(project == project.lower() for project in projects))
        self.assertGreaterEqual(len(projects), 40000)

    def test_is_pure_python(self):
        self.assertTrue(pypi.is_pure_python('urllib3'))

    def test_is_not_pure_python(self):
        self.assertFalse(pypi.is_pure_python('cryptography'))

    def test_pure_python_with_no_wheels(self):
        self.assertFalse(pypi.is_pure_python('ipaddr'))
