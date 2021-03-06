import unittest
from cStringIO import StringIO

from .. import parser

class Test_Tools(unittest.TestCase):

    def test_empty_file(self):
        self.assertRaises(IOError, parser.parse_tool_names, StringIO(""))

    def test_valid_file(self):
        tools = parser.parse_tool_names(StringIO("tool1\ntool2\n"))
        self.assertEquals(len(tools), 2)
        self.assertEquals(tools[0], "tool1")
        self.assertEquals(tools[1], "tool2")


class  Test_Samples(unittest.TestCase):
    
    def test_empty_file(self):
        self.assertRaises(IOError, parser.parse_samples, StringIO(""))

    def test_incorrect_file_format(self):
        self.assertRaises(IOError, parser.parse_samples, StringIO("name1\tfastq\n"))

    def test_file_does_not_exist(self):
        parser.os.path.isfile = lambda _ : False 
        self.assertRaises(IOError, parser.parse_samples, 
            StringIO("name1\tAbsent_fastq1\tAbsent_fastq2\n"))

    def test_valid_file(self):
        parser.os.path.isfile = lambda _ : True 
        samples = parser.parse_samples(
            StringIO("name1\tfastq1\tfastq2\nname2\tfastq3\tfastq4\n"))
        self.assertEqual(len(samples), 2)
        self.assertEqual(samples[0], ("name1", "fastq1", "fastq2"))
        self.assertEqual(samples[1], ("name2", "fastq3", "fastq4"))

#class Test_Reads(unittest.TestCase):
#
#    def test_reads(self):
#        self.assertTrue(False)
