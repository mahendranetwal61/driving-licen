import requests
from requests import session
from lxml import etree
import base64
from PIL import Image
from io import BytesIO

session = requests.Session()


class Dl:

    dl_no = input("enter dl numbert")
    dob = input("enter dob")
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    url = "https://parivahan.gov.in/rcdlstatus/?pur_cd=101"

    def dl_extract(self):
        response = session.get(url=self.url, headers=self.headers)
        tree_reponse = etree.HTML(response.content)
        viewstate = tree_reponse.xpath("//*[@id='j_id1:javax.faces.ViewState:0']/@value")[0]

        url_1 = "https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml"
        payload = {
            'javax.faces.partial.ajax': 'true',
            'javax.faces.source': 'form_rcdl:tf_dlNO',
            'javax.faces.partial.execute': 'form_rcdl:tf_dlNO',
            'javax.faces.partial.render': 'form_rcdl:tf_dlNO',
            'javax.faces.behavior.event': 'valueChange',
            'javax.faces.partial.event': 'change',
            'form_rcdl': 'form_rcdl',
            'form_rcdl:tf_dlNO': self.dl_no,
            'form_rcdl:tf_dob_input': '',
            'form_rcdl:j_idt30:CaptchaID': '',
            'javax.faces.ViewState': viewstate
        }
        headers_2 = {

            'Accept': 'application/xml, text/xml, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Length': '2607',
            'Faces-Request': 'partial/ajax',
            'Host': 'parivahan.gov.in',
            'Origin': 'https://parivahan.gov.in',
            'Referer': 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101',
            'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        response_2 = session.post(url=url_1, data=payload, headers=headers_2)

        tree_reponse_2 = etree.XML(response_2.content)
        viewstate_2 = tree_reponse_2.xpath("//update[@id='j_id1:javax.faces.ViewState:0']/text()")

        payload_2 = {
            'javax.faces.partial.ajax': 'true',
            'javax.faces.source': 'form_rcdl:tf_dlNO',
            'javax.faces.partial.execute': 'form_rcdl:tf_dlNO',
            'javax.faces.partial.render': 'form_rcdl:tf_dlNO',
            'javax.faces.behavior.event': 'valueChange',
            'javax.faces.partial.event': 'change',
            'form_rcdl': 'form_rcdl',
            'form_rcdl:tf_dlNO': self.dl_no,
            'form_rcdl:tf_dob_input': self.dob,
            'form_rcdl:j_idt30:CaptchaID': '',
            'javax.faces.ViewState': viewstate_2
        }

        headers_3 = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'close',
            'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Faces-Request': 'partial/ajax',
            'Origin': 'https://parivahan.gov.in',
            'Referer': 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response_3 = session.post(url=url_1, data=payload_2, headers=headers_3)
        tree_reponse_3 = etree.XML(response_3.content)

        viewstate_3 = tree_reponse_3.xpath("//update[@id='j_id1:javax.faces.ViewState:0']/text()")

        captcha_url = "https://parivahan.gov.in/rcdlstatus/DispplayCaptcha?txtp_cd=1&bkgp_cd=2&noise_cd=2&gimp_cd=3&txtp_length=5&pfdrid_c=true?1828647525&pfdrid_c=true"
        captcha_headers = {
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'close',
            'Referer': 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101',
            'Sec-Fetch-Dest': 'image',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        captcha = session.get(captcha_url, headers=captcha_headers)
        encoded_image = base64.b64encode(captcha.content)
        decoded_image_str = encoded_image.decode("utf-8")
        captcha_bytes = base64.b64decode(decoded_image_str)
        captcha_image = Image.open(BytesIO(captcha_bytes))

        # Display the image
        captcha_image.show()

        captcha_input = input("enter capthca -->")

        headers_4 = {
            'Accept': 'application/xml, text/xml, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'close',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Faces-Request': 'partial/ajax',
            'Origin': 'https://parivahan.gov.in',
            'Referer': 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        payload_3 = {
            'javax.faces.partial.ajax': 'true',
            'javax.faces.source': 'form_rcdl:j_idt43',
            'javax.faces.partial.execute': '@all',
            'javax.faces.partial.render': 'form_rcdl:pnl_show form_rcdl:pg_show form_rcdl:rcdl_pnl',
            'form_rcdl:j_idt43': '',
            'form_rcdl': '',
            'form_rcdl:tf_dlNO': self.dl_no,
            'form_rcdl:tf_dob_input': self.dob,
            'form_rcdl:j_idt30:CaptchaID': captcha_input,
            'javax.faces.ViewState': viewstate_3
        }

        response_4 = session.post(url=url_1, data=payload_3, headers=headers_4)
        tree_reponse_4 = etree.XML(response_4.content)

        data = {
            "d_name": tree_reponse_4.xpath("//*[@id='form_rcdl:j_idt65']/table[1]/tbody/tr[2]/td[2]/text()")
        }
        return data


if __name__ == "__main__":
    dl = Dl()

    print(dl.dl_extract())
