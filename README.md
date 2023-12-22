# **RSMAILEVENT**

## 1. Introduction
Remote Syslog EVENT is python connector for open mail relay to create mails for events.

## 2. Usage
Change the variables within the message.py file to the variables needed by the organation.

Test the file as:
```
python message.py
```
Add to contab with "contab -e" and copy the file to: /opt/message.py:
```
mv ./message.py /opt/message.py
0 * * * * /usr/bin/python3 /opt/message.py
```
## 3. Donation

Crypto:

```
BTC (Bitcoin): bc1qulyuywjkeamqu0h9ctuj5cla8u0pagkaa83hf6
LTC (Litecoin): ltc1q25j4yxg9dkwknrh4a7fvndtt3358c4gjnsf9qv
BCH (Bitcoin Cash): qq9qd6gshp4n9gkk3zy9505p8j8jlhur4uv0lxv2d8
```
PayPal:

[![paypal](https://www.paypalobjects.com/en_US/NL/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=KQKRPDQYHYR7W&currency_code=EUR&source=url)

## 4. Help

To improve the code and functions we like to have you help. Send your idea or code to: info@remotesyslog.com or create a pull request. We will review it and add it to this project.

## 5. License
"Remote Syslog EVENT for mail" is a free application what can be used to create event mails.

Copyright (C) 2023 Tom Slenter

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

For more information contact the author:

Name author: Tom Slenter

E-mail: info@remotesyslog.com

## 6. More info

More information can be found:

Website:
https://www.remotesyslog.com/

Read the docs:
https://remote-syslog.readthedocs.io/en/latest/

Master script:
https://www.github.com/tslenter/RS
