from raytensor import RayTensor


def raytest():
    RayTensor().xray_predict('tests/xray_test.png')
    RayTensor().ct_predict('tests/ct_test.png')


if __name__ == '__main__':
    raytest()
