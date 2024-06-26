from os.path import join, isdir, expanduser
from pathlib import Path
from unittest import TestCase

from mavenrunner.mvn_project import MvnProject
from mbertnteval.d4jeval.yaml_utils import load_config


class TestMvnProject(TestCase):

    def setUp(self):
        self.TEST_PATH = Path(__file__).parent.parent.parent
        self.RES_PATH = join(self.TEST_PATH, 'res')
        self.DUMMY_REPO = join(self.RES_PATH, 'exampleclass/DummyProject')

        self.CONFIG = load_config(join(Path(__file__).parent, 'mbert_test_config.yml'))

        self.dummy_dir_as_jdk = self.CONFIG['java']['home8']
        if not isdir(self.dummy_dir_as_jdk):
            self.dummy_dir_as_jdk = expanduser(self.dummy_dir_as_jdk)
        self.assertTrue(isdir(self.dummy_dir_as_jdk))

        self.dummy_dir_as_mvn = self.CONFIG['maven']
        if not isdir(self.dummy_dir_as_mvn):
            self.dummy_dir_as_mvn = expanduser(self.dummy_dir_as_mvn)
        self.assertTrue(isdir(self.dummy_dir_as_mvn))

    def test_cmd_base__no_jvm_no_mvn(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", None)
        self.assertEqual('mvn', project.cmd_base())

    def test_cmd_base__no_mvn_wrong_jdk(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", "dummy_path_as_jdk")
        self.assertEqual('mvn', project.cmd_base())

    def test_cmd_base__no_mvn_with_jdk(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", jdk_path=str(self.dummy_dir_as_jdk))
        self.assertEqual("JAVA_HOME='" + str(self.dummy_dir_as_jdk) + "'" + ' mvn', project.cmd_base())

    def test_cmd_base__with_mvn_no_jdk(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", mvn_home=str(self.dummy_dir_as_mvn))
        self.assertEqual("M2_HOME='" + str(self.dummy_dir_as_mvn) + "'" + ' mvn', project.cmd_base())

    def test_cmd_base__with_mvn_and_jdk(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", jdk_path=self.dummy_dir_as_jdk, mvn_home=self.dummy_dir_as_mvn)
        self.assertEqual("JAVA_HOME='" + str(self.dummy_dir_as_jdk) + "' M2_HOME='" + str(self.dummy_dir_as_mvn) + "'" + ' mvn',
                          project.cmd_base())

    def test_get_project_name_from_git_url(self):
        dummy_url = 'https://github.com/Ahmedfir/mBERTa.git'
        self.assertEqual('mBERTa', MvnProject.get_project_name_from_git_url(dummy_url))

    def test_compile(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", jdk_path=self.dummy_dir_as_jdk, mvn_home=self.dummy_dir_as_mvn)
        result = project.compile()
        self.assertTrue(result)
    def test_compile_no_comments(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", jdk_path=self.dummy_dir_as_jdk, mvn_home=self.dummy_dir_as_mvn)
        project.no_comments = True
        project.remove_comments_from_repo()
        result = project.compile()
        self.assertTrue(result)

    def test_test(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", jdk_path=self.dummy_dir_as_jdk,
                             mvn_home=self.dummy_dir_as_mvn)
        result = project.test()
        self.assertEqual(set(), result)

    def test_test_timeout(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", jdk_path=self.dummy_dir_as_jdk,
                             mvn_home=self.dummy_dir_as_mvn, tests_timeout=200)
        self.assertEqual(200, project.tests_timeout)
        result = project.test()
        self.assertEqual(set(), result)

    def test_test_one_test(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", jdk_path=self.dummy_dir_as_jdk,
                             mvn_home=self.dummy_dir_as_mvn, tests_timeout=200)
        self.assertEqual(200, project.tests_timeout)
        result = project.test(target_tests='example.DummyClassTest#parseStringToInt_str')
        self.assertEqual(set(), result)

    def test_test_two_test(self):
        project = MvnProject(self.DUMMY_REPO, "ignore_repos", jdk_path=self.dummy_dir_as_jdk,
                             mvn_home=self.dummy_dir_as_mvn, tests_timeout=200)
        self.assertEqual(200, project.tests_timeout)
        result = project.test(target_tests='example.DummyClassTest#parseStringToInt_str,example.DummyClassTest#parseStringToInt_float')
        self.assertEqual(set(), result)
