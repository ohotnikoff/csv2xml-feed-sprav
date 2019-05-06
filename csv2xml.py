"""
Convert csv to xml file for sprav.yandex.ru
"""

#!/usr/bin/python
import lxml.etree
import lxml.builder
from pandas import read_csv as read
from datetime import datetime

csvFile = read("data/file.csv", delimiter=",")

companies = lxml.etree.Element("companies")

i = 0
for item in csvFile.values:
    company = lxml.etree.SubElement(companies, "company")

    #company-id    
    i += 1
    company_id = lxml.etree.SubElement(company, "company-id")
    company_id.text = str(i)
    
    #name
    name = lxml.etree.SubElement(company, "name")
    name.set("lang", "ru")
    name.text = item[0]

    #shortname
    shortname = lxml.etree.SubElement(company, "shortname")
    shortname.set("lang", "ru")
    shortname.text = item[0]

    #address
    address = lxml.etree.SubElement(company, "address")
    address.set("lang", "ru")
    address.text = item[2]

    #country
    country = lxml.etree.SubElement(company, "country")
    country.set("lang", "ru")
    country.text = item[1]

    #coordinates
    coordinates = lxml.etree.SubElement(company, "coordinates")
    lon = lxml.etree.SubElement(coordinates, "lon")
    lon.text = str(item[8])
    lat = lxml.etree.SubElement(coordinates, "lat")
    lat.text = str(item[7])

    #phone
    phone = lxml.etree.SubElement(company, "phone")
    lxml.etree.SubElement(phone, "ext")
    phone_type = lxml.etree.SubElement(phone, "type")
    phone_type.text = "phone"
    number = lxml.etree.SubElement(phone, "number")
    number.text = item[3]
    lxml.etree.SubElement(phone, "info")

    #url
    url = lxml.etree.SubElement(company, "url")
    url.text = item[4]

    #working-time
    working_time = lxml.etree.SubElement(company, "working-time")
    working_time.set("lang", "ru")
    working_time.text = item[6]

    #rubric-id
    for rubric in item[5].split(", "):
        rubric_id = lxml.etree.SubElement(company, "rubric-id")
        rubric_id.text = rubric

    #actualization-date
    actualization_date = lxml.etree.SubElement(company, "actualization-date")
    actualization_date.text = datetime.now().strftime('%d.%m.%Y')

tree = lxml.etree.ElementTree(companies)
tree.write("data/file.xml", xml_declaration=True, encoding='UTF-8')

print(lxml.etree.tostring(tree, pretty_print=True))
