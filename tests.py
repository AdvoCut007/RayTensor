import unittest
from raytensor import RayTensor


class ImgTestCase(unittest.TestCase):

    def xray_test(self):
        try:
            predict = RayTensor().xray_predict('static/images/logo.jpeg')
            predict = True
        except:
            predict = False
        self.assertEqual(predict, True)
