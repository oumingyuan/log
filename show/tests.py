from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class UserModelTests(TestCase):

    def test(self):
        self.assertIs(1 == 1, True)


class UrlsTests(TestCase):

    def test_index(self):
        """
        这个是app 的主页面
        这个页面会返回一个index
        访问请求后返回200，说明请求是成功了
        """
        url = reverse('show:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_ip(self):
        """
        这个会返回主机的ip地址
        """
        url = reverse('show:get_ip')
        response = self.client.get(url)
        content = response.content
        print(content)
        self.assertEqual(response.status_code, 200)

    # path('submit/', views.submit, name="submit_log"),
    def test_submit_log(self):
        """
        会激活批量跑批程序

        :return:
        """
        url = reverse('show:submit_log', )
        response = self.client.post(url, data={"data": "past"})
        content = response.content
        print(content)
        self.assertEqual(response.status_code, 200)
