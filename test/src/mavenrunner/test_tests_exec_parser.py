from os.path import join
from pathlib import Path
from unittest import TestCase
from utils.file_read_write import load_file

from mavenrunner.tests_exec_parser import exec_res_to_broken_tests_arr, MvnFailingTest, FailCategory


class TestMvnProject(TestCase):

    def setUp(self):
        self.TEST_PATH = Path(__file__).parent.parent.parent
        self.RES_PATH = join(self.TEST_PATH, 'res')
        self.failing_tests_example = load_file(join(self.RES_PATH, 'mavenrunner/failing_tests_mvn_output.txt'))
        self.surefire_one_test_class = load_file(
            join(self.RES_PATH, 'mavenrunner/one_test_class_mvn_surefire_output.txt'))
        self.surefire_no_errors = load_file(
            join(self.RES_PATH, 'mavenrunner/no_error_mvn_surefire_output.txt'))
        self.aws_event_ruler = load_file(
            join(self.RES_PATH, 'mavenrunner/aws_event_ruler_test_output.txt'))
        self.semverj = load_file(
            join(self.RES_PATH, 'mavenrunner/semverj_test_output.txt'))
        self.aws_event_ruler_failing_tests = load_file(
            join(self.RES_PATH, 'mavenrunner/aws_event_ruler_failing_tests_output.txt'))
        self.surefire_two_test_class = load_file(
            join(self.RES_PATH, 'mavenrunner/two_test_class_mvn_surefire_output.txt'))
        self.surefire_three_error_three_fail = load_file(
            join(self.RES_PATH, 'mavenrunner/three_error_three_failure_surefire_mvn_ouput.txt'))
        self.failing_and_error_tests_example = load_file(
            join(self.RES_PATH, 'mavenrunner/error_failing_tests_mvn_output.txt'))
        self.no_reason_failing_and_error_tests_example = load_file(
            join(self.RES_PATH, 'mavenrunner/no_reason_failing_test_maven_output.txt'))
        self.error_tests_example = load_file(join(self.RES_PATH, 'mavenrunner/error_tests_mvn_output.txt'))
        self.passing_tests_example = "\n".join(['[INFO]',
                                                '[INFO] ----------------------< org.example:DummyProject '
                                                '>----------------------',
                                                '[INFO] Building DummyProject 1.0-SNAPSHOT',
                                                '[INFO] --------------------------------[ jar '
                                                ']---------------------------------',
                                                '[INFO]',
                                                '[INFO] --- maven-resources-plugin:2.6:resources (default-resources) @ '
                                                'DummyProject ---',
                                                '[WARNING] Using platform encoding (UTF-8 actually) to copy filtered '
                                                'resources, i.e. build is platform dependent!',
                                                '[INFO] Copying 0 resource',
                                                '[INFO]',
                                                '[INFO] --- maven-compiler-plugin:3.1:compile (default-compile) @ '
                                                'DummyProject ---',
                                                '[INFO] Nothing to compile - all classes are up to date',
                                                '[INFO]',
                                                '[INFO] --- maven-resources-plugin:2.6:testResources (default-testResources) '
                                                '@ DummyProject ---',
                                                '[WARNING] Using platform encoding (UTF-8 actually) to copy filtered '
                                                'resources, i.e. build is platform dependent!',
                                                '[INFO] skip non existing resourceDirectory '
                                                '/Users/ahmed.khanfir/PycharmProjects/mBERTa/test/res/exampleclass/DummyProject/src/test/resources',
                                                '[INFO]',
                                                '[INFO] --- maven-compiler-plugin:3.1:testCompile (default-testCompile) @ '
                                                'DummyProject ---',
                                                '[INFO] Nothing to compile - all classes are up to date',
                                                '[INFO]',
                                                '[INFO] --- maven-surefire-plugin:2.12.4:test (default-test) @ DummyProject '
                                                '---',
                                                '[INFO] Surefire report directory: '
                                                '/Users/ahmed.khanfir/PycharmProjects/mBERTa/test/res/exampleclass/DummyProject/target/surefire-reports',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit47/2.12.4/surefire-junit47-2.12.4.pom',
                                                'Progress (1): 2.7/3.7 kB',
                                                'Progress (1): 3.7 kB',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit47/2.12.4/surefire-junit47-2.12.4.pom '
                                                '(3.7 kB at 8.7 kB/s)',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit48/2.12.4/common-junit48-2.12.4.pom',
                                                'Progress (1): 2.5 kB',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit48/2.12.4/common-junit48-2.12.4.pom '
                                                '(2.5 kB at 49 kB/s)',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit4/2.12.4/common-junit4-2.12.4.pom',
                                                'Progress (1): 1.7 kB',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit4/2.12.4/common-junit4-2.12.4.pom '
                                                '(1.7 kB at 50 kB/s)',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit3/2.12.4/common-junit3-2.12.4.pom',
                                                'Progress (1): 1.6 kB',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit3/2.12.4/common-junit3-2.12.4.pom '
                                                '(1.6 kB at 54 kB/s)',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-grouper/2.12.4/surefire-grouper-2.12.4.pom',
                                                'Progress (1): 2.5 kB',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-grouper/2.12.4/surefire-grouper-2.12.4.pom '
                                                '(2.5 kB at 52 kB/s)',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit3/2.12.4/common-junit3-2.12.4.jar',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit47/2.12.4/surefire-junit47-2.12.4.jar',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-grouper/2.12.4/surefire-grouper-2.12.4.jar',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit48/2.12.4/common-junit48-2.12.4.jar',
                                                'Downloading from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit4/2.12.4/common-junit4-2.12.4.jar',
                                                'Progress (1): 2.7/11 kB',
                                                'Progress (1): 5.5/11 kB',
                                                'Progress (1): 8.2/11 kB',
                                                'Progress (1): 11/11 kB',
                                                'Progress (1): 11 kB',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit3/2.12.4/common-junit3-2.12.4.jar '
                                                '(11 kB at 281 kB/s)',
                                                'Progress (1): 2.7/47 kB',
                                                'Progress (1): 5.5/47 kB',
                                                'Progress (1): 8.2/47 kB',
                                                'Progress (1): 11/47 kB',
                                                'Progress (1): 14/47 kB',
                                                'Progress (1): 16/47 kB',
                                                'Progress (1): 19/47 kB',
                                                'Progress (1): 22/47 kB',
                                                'Progress (1): 25/47 kB',
                                                'Progress (1): 27/47 kB',
                                                'Progress (1): 30/47 kB',
                                                'Progress (1): 33/47 kB',
                                                'Progress (1): 36/47 kB',
                                                'Progress (1): 38/47 kB',
                                                'Progress (1): 41/47 kB',
                                                'Progress (2): 41/47 kB | 2.7/38 kB',
                                                'Progress (3): 41/47 kB | 2.7/38 kB | 2.7/15 kB',
                                                'Progress (4): 41/47 kB | 2.7/38 kB | 2.7/15 kB | 2.7/28 kB',
                                                'Progress (4): 44/47 kB | 2.7/38 kB | 2.7/15 kB | 2.7/28 kB',
                                                'Progress (4): 44/47 kB | 5.5/38 kB | 2.7/15 kB | 2.7/28 kB',
                                                'Progress (4): 44/47 kB | 5.5/38 kB | 5.5/15 kB | 2.7/28 kB',
                                                'Progress (4): 44/47 kB | 8.2/38 kB | 5.5/15 kB | 2.7/28 kB',
                                                'Progress (4): 44/47 kB | 8.2/38 kB | 5.5/15 kB | 5.5/28 kB',
                                                'Progress (4): 46/47 kB | 8.2/38 kB | 5.5/15 kB | 5.5/28 kB',
                                                'Progress (4): 46/47 kB | 8.2/38 kB | 5.5/15 kB | 8.2/28 kB',
                                                'Progress (4): 46/47 kB | 11/38 kB | 5.5/15 kB | 8.2/28 kB',
                                                'Progress (4): 46/47 kB | 11/38 kB | 5.5/15 kB | 11/28 kB',
                                                'Progress (4): 46/47 kB | 11/38 kB | 8.2/15 kB | 11/28 kB',
                                                'Progress (4): 46/47 kB | 11/38 kB | 8.2/15 kB | 14/28 kB',
                                                'Progress (4): 46/47 kB | 14/38 kB | 8.2/15 kB | 14/28 kB',
                                                'Progress (4): 47 kB | 14/38 kB | 8.2/15 kB | 14/28 kB',
                                                'Progress (4): 47 kB | 16/38 kB | 8.2/15 kB | 14/28 kB',
                                                'Progress (4): 47 kB | 16/38 kB | 8.2/15 kB | 16/28 kB',
                                                'Progress (4): 47 kB | 16/38 kB | 11/15 kB | 16/28 kB',
                                                'Progress (4): 47 kB | 16/38 kB | 11/15 kB | 19/28 kB',
                                                'Progress (4): 47 kB | 16/38 kB | 14/15 kB | 19/28 kB',
                                                'Progress (4): 47 kB | 19/38 kB | 14/15 kB | 19/28 kB',
                                                'Progress (4): 47 kB | 19/38 kB | 14/15 kB | 22/28 kB',
                                                'Progress (4): 47 kB | 22/38 kB | 14/15 kB | 22/28 kB',
                                                'Progress (4): 47 kB | 22/38 kB | 15 kB | 22/28 kB',
                                                'Progress (4): 47 kB | 22/38 kB | 15 kB | 25/28 kB',
                                                'Progress (4): 47 kB | 25/38 kB | 15 kB | 25/28 kB',
                                                'Progress (4): 47 kB | 25/38 kB | 15 kB | 27/28 kB',
                                                'Progress (4): 47 kB | 27/38 kB | 15 kB | 27/28 kB',
                                                'Progress (4): 47 kB | 27/38 kB | 15 kB | 28 kB',
                                                'Progress (4): 47 kB | 30/38 kB | 15 kB | 28 kB',
                                                'Progress (4): 47 kB | 33/38 kB | 15 kB | 28 kB',
                                                'Progress (4): 47 kB | 36/38 kB | 15 kB | 28 kB',
                                                'Progress (4): 47 kB | 38 kB | 15 kB | 28 kB',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit47/2.12.4/surefire-junit47-2.12.4.jar '
                                                '(47 kB at 515 kB/s)',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit48/2.12.4/common-junit48-2.12.4.jar '
                                                '(28 kB at 291 kB/s)',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-grouper/2.12.4/surefire-grouper-2.12.4.jar '
                                                '(38 kB at 367 kB/s)',
                                                'Downloaded from central: '
                                                'https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-junit4/2.12.4/common-junit4-2.12.4.jar '
                                                '(15 kB at 150 kB/s)',
                                                '-------------------------------------------------------',
                                                'T E S T S',
                                                '-------------------------------------------------------',
                                                "Concurrency config is parallel='classes', perCoreThreadCount=true, "
                                                'threadCount=2, useUnlimitedThreads=false',
                                                'Running example.DummyClassTest',
                                                'Tests run: 4, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.003 sec',
                                                'Results :',
                                                'Tests run: 4, Failures: 0, Errors: 0, Skipped: 0',
                                                '[INFO] '
                                                '------------------------------------------------------------------------',
                                                '[INFO] BUILD SUCCESS',
                                                '[INFO] '
                                                '------------------------------------------------------------------------',
                                                '[INFO] Total time:  2.558 s',
                                                '[INFO] Finished at: 2024-05-28T14:25:20+02:00',
                                                '[INFO] '
                                                '------------------------------------------------------------------------'])

    def test_exec_res_to_broken_tests_arr_pass(self):
        self.assertEqual(set(), exec_res_to_broken_tests_arr(self.passing_tests_example))

    def test_exec_res_to_broken_tests_arr_fail(self):
        self.assertEqual({MvnFailingTest(method_name='parseStringToInt_int', class_name='example.DummyClassTest',
                                         reason='expected:<4> but was:<1>', failing_category=FailCategory.Fail),
                          MvnFailingTest(method_name='addCalc', class_name='example.DummyClassTest',
                                         reason='expected:<6> but was:<5>', failing_category=FailCategory.Fail)},
                         exec_res_to_broken_tests_arr(self.failing_tests_example))

    def test_exec_res_to_broken_tests_arr_fail_and_error(self):
        self.assertEqual({MvnFailingTest(method_name='parseStringToInt_int', class_name='example.DummyClassTest',
                                         reason='expected:<4> but was:<1>', failing_category=FailCategory.Fail),
                          MvnFailingTest(method_name='addCalc', class_name='example.DummyClassTest',
                                         reason='expected:<6> but was:<5>', failing_category=FailCategory.Fail),
                          MvnFailingTest(method_name='parseStringToInt_str', class_name='example.DummyClassTest',
                                         reason=None, failing_category=FailCategory.Err)
                          },
                         exec_res_to_broken_tests_arr(self.failing_and_error_tests_example))

    def test_exec_res_to_broken_tests_arr_fail_and_error_no_reason(self):
        self.assertEqual({MvnFailingTest(method_name='WHEN_eventHasBigArrayAndLegacyFinderIsUsed_THEN_itWillCompleteSuccessfully_insteadOfCrashingOOM', class_name='software.amazon.event.ruler.BigEventTest',
                                         failing_category=FailCategory.Fail),
                          MvnFailingTest(method_name='testOtherMatchTypes', class_name='software.amazon.event.ruler.input.ParserTest',
                                          failing_category=FailCategory.Err)
                          },
                         exec_res_to_broken_tests_arr(self.no_reason_failing_and_error_tests_example))

    def test_exec_res_to_broken_tests_arr_errors(self):
        self.assertEqual({MvnFailingTest(method_name='WHEN_JSONContainsArrays_THEN_RulerNoCompileMatchesWork',
                                         class_name='software.amazon.event.ruler.RulerTest',
                                         failing_category=FailCategory.Err),
                          MvnFailingTest(method_name='WHEN_WeTryReallySimpleRules_THEN_TheyWork',
                                         class_name='software.amazon.event.ruler.RulerTest',
                                         failing_category=FailCategory.Err)
                          },
                         exec_res_to_broken_tests_arr(self.error_tests_example))

    def test_exec_res_to_broken_tests_fail_errors_surefire_one_class(self):
        self.assertEqual({MvnFailingTest(method_name='should_fail_if_entries_parameter_is_null',
                                         class_name='org.assertj.vavr.api.MapAssert_doesNotContain_entries_Test',
                                         failing_category=FailCategory.Fail),
                          MvnFailingTest(method_name='should_fail_if_entries_parameter_are_empty',
                                         class_name='org.assertj.vavr.api.MapAssert_doesNotContain_entries_Test',
                                         failing_category=FailCategory.Fail)
                          },
                         exec_res_to_broken_tests_arr(self.surefire_one_test_class))

    def test_exec_res_to_broken_tests_fail_errors_surefire_two_class(self):
        self.assertEqual({MvnFailingTest(method_name='should_be_able_to_catch_exceptions_thrown_by_all_proxied_methods',
                                         class_name='org.assertj.vavr.api.soft.AutoCloseableSoftVavrAssertionsTest',
                                         failing_category=FailCategory.Fail),
                          MvnFailingTest(method_name='should_be_able_to_catch_exceptions_thrown_by_all_proxied_methods',
                                         class_name='org.assertj.vavr.api.soft.SoftVavrAssertionsTest',
                                         failing_category=FailCategory.Fail),
                          },
                         exec_res_to_broken_tests_arr(self.surefire_two_test_class))

    def test_exec_res_to_broken_tests_fail_error_errors_surefire(self):
        self.assertEqual(
            {MvnFailingTest(method_name='should_fail_if_either_does_not_contain_same_instance_on_left_side',
                            class_name='org.assertj.vavr.api.EitherAssert_containsLeftSame_Test',
                            failing_category=FailCategory.Fail),
             MvnFailingTest(method_name='should_pass_if_either_contains_same_instance_on_left_side',
                            class_name='org.assertj.vavr.api.EitherAssert_containsLeftSame_Test',
                            failing_category=FailCategory.Err),
             MvnFailingTest(
                 method_name='should_run_test_when_assumption_passes{AssumptionRunner}[7]',
                 class_name='org.assertj.vavr.api.Either_assertion_methods_in_assumptions_Test',
                 failing_category=FailCategory.Fail),
             MvnFailingTest(method_name='should_ignore_test_when_assumption_fails{AssumptionRunner}[7]',
                            class_name='org.assertj.vavr.api.Either_assertion_methods_in_assumptions_Test',
                            failing_category=FailCategory.Err),
             MvnFailingTest(method_name='should_be_able_to_catch_exceptions_thrown_by_all_proxied_methods',
                            class_name='org.assertj.vavr.api.soft.SoftVavrAssertionsTest',
                            failing_category=FailCategory.Err),
             MvnFailingTest(
                 method_name='should_be_able_to_catch_exceptions_thrown_by_all_proxied_methods',
                 class_name='org.assertj.vavr.api.soft.AutoCloseableSoftVavrAssertionsTest',
                 failing_category=FailCategory.Err),

             },
            exec_res_to_broken_tests_arr(self.surefire_three_error_three_fail))

    def test_exec_res_to_broken_tests_aws_event_ruler(self):
        self.assertEqual(
            {MvnFailingTest(method_name='testWildcardWithAnythingButPrefixPatternWildcardStartsWithPrefix',
                            class_name='software.amazon.event.ruler.ByteMachineTest',
                            reason='Failed on  expected:<0> but was:<1>',
                            failing_category=FailCategory.Fail),
             MvnFailingTest(method_name='testWildcardWithAnythingButPrefixPatternWildcardStartsWithHalfOfPrefix',
                            class_name='software.amazon.event.ruler.ByteMachineTest',
                            reason='Failed on  expected:<0> but was:<1>',
                            failing_category=FailCategory.Fail),
             MvnFailingTest(
                 method_name='WHEN_AnythingButPrefixPatternIsAdded_THEN_ItMatchesAppropriately',
                 class_name='software.amazon.event.ruler.ByteMachineTest',
                 reason='expected:<0> but was:<1>',
                 failing_category=FailCategory.Fail),
             MvnFailingTest(
                 method_name='testAnythingButEqualsIgnoreCase',
                 class_name='software.amazon.event.ruler.ACMachineTest',
                 failing_category=FailCategory.Fail),
             },
            exec_res_to_broken_tests_arr(self.aws_event_ruler))

    def test_exec_res_to_broken_tests_aws_event_ruler_failing_tests(self):
        self.assertEqual(
            {MvnFailingTest(method_name='WHEN_WeTryAnythingButRules_THEN_Theywork',
                            class_name='software.amazon.event.ruler.RulerTest',
                            reason='{    "a": "child1",(..)',
                            failing_category=FailCategory.Fail),
             MvnFailingTest(method_name='testBuild',
                            class_name='software.amazon.event.ruler.ACMachineTest',
                            reason='Event {"alpha":1,"beta":2,"gamma":3}(..)',
                            failing_category=FailCategory.Fail),
             MvnFailingTest(
                 method_name='testBuild',
                 class_name='software.amazon.event.ruler.MachineTest',
                 reason='Event Tokens: alpha / 1 / beta / 2 / gamma / 3 /  Expected: R1 / (..)',
                 failing_category=FailCategory.Fail),
             MvnFailingTest(
                 method_name='testExistencePatternsLifecycle',
                 class_name='software.amazon.event.ruler.MachineTest',
                 reason='Event Tokens: a / "1" / b / "b_val" / d / 3 /  Expected: rule1 / rule2 / (..)',
                 failing_category=FailCategory.Fail),
             MvnFailingTest(
                 method_name='matchRuleWithExistencePatternAtEnd_andMatchesAtEventAfterAllFieldsHaveExhausted',
                 class_name='software.amazon.event.ruler.MachineTest',
                 reason='Event Tokens: a / "Y" / b / 20 / c / "YES" /  Expected: rule1 / (..)',
                 failing_category=FailCategory.Fail),
             },
            exec_res_to_broken_tests_arr(self.aws_event_ruler_failing_tests))

    def test_exec_res_to_broken_tests_semverj(self):
        self.assertEqual(
            {MvnFailingTest(method_name='org.semver4j.internal.StrictParserTest.shouldParseValidVersions(String, Version)[1]',
                            class_name='org.semver4j.internal.StrictParserTest',
                            failing_category=FailCategory.Fail),

             MvnFailingTest(method_name='org.semver4j.internal.StrictParserTest.shouldParseValidVersions(String, Version)[2]',
                            class_name='org.semver4j.internal.StrictParserTest',
                            failing_category=FailCategory.Fail),
             MvnFailingTest(
                 method_name='org.semver4j.internal.StrictParserTest.shouldParseValidVersions(String, Version)[3]',
                 class_name='org.semver4j.internal.StrictParserTest',
                 failing_category=FailCategory.Fail),
             MvnFailingTest(
                 method_name='org.semver4j.internal.StrictParserTest.shouldParseValidVersions(String, Version)[20]',
                 class_name='org.semver4j.internal.StrictParserTest',
                 failing_category=FailCategory.Fail),
             MvnFailingTest(
                 method_name='org.semver4j.internal.StrictParserTest.shouldParseValidVersions(String, Version)[21]',
                 class_name='org.semver4j.internal.StrictParserTest',
                 failing_category=FailCategory.Fail),
             MvnFailingTest(
                 method_name='org.semver4j.internal.StrictParserTest.shouldParseValidVersions(String, Version)[22]',
                 class_name='org.semver4j.internal.StrictParserTest',
                 failing_category=FailCategory.Fail),
             },
            exec_res_to_broken_tests_arr(self.semverj))

    def test_exec_res_to_broken_tests_no_errors_surefire(self):
        self.assertEqual(set(),
                         exec_res_to_broken_tests_arr(self.surefire_no_errors))
