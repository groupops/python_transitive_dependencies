import unittest
from nose.tools import assert_equal
from com.epam.training.Dependencies import Dependencies


class TestDependencies(unittest.TestCase):
    def test_Basic(self):
        dependencies = Dependencies()

        dependencies.add_direct('A', ["B", "C"])
        dependencies.add_direct('B', ["C", "E"])
        dependencies.add_direct('C', ["G"])
        dependencies.add_direct('D', ["A", "F"])
        dependencies.add_direct('E', ["F"])
        dependencies.add_direct('F', ["H"])

        assert_equal(sorted(["B", "C", "E", "F", "G", "H"]), dependencies.sorted_transitive_dependencies_for('A'))
        assert_equal(sorted(["C", "E", "F", "G", "H"]), dependencies.sorted_transitive_dependencies_for('B'))
        assert_equal(sorted(["G"]), dependencies.dependencies_for('C'))
        assert_equal(sorted(["A", "B", "C", "E", "F", "G", "H"]), dependencies.sorted_transitive_dependencies_for('D'))
        assert_equal(sorted(["F", "H"]), dependencies.sorted_transitive_dependencies_for('E'))
        assert_equal(sorted(["H"]), dependencies.sorted_transitive_dependencies_for('F'))
