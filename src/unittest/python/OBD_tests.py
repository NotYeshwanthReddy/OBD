from mockito import mock, verify
import unittest

import OBD

class OBDTest(unittest.TestCase):
    def test_OBD(self):
        out = mock()

        main(out)

        verify(out).write("Input Succesfull")
        verify(out).write("Converted to gray")
        verify(out).write("Denoising image")
        verify(out).write("Getting Boundaries")