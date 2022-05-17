from raytensor import RayTensor


def raytest():
    RayTensor().xray_predict('static/images/logo.jpeg')
    RayTensor().ct_predict('static/images/indexlogo.png')


if __name__ == '__main__':
    raytest()
