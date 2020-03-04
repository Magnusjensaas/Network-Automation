import unittest2
import re


class ConfigurationParser:
    deviceConfig = open("config.txt", "r").read()

    def parse_customer_names(self):
        customer_name_pattern = r"ip vrf ([a-zA-Z_]+)\n"
        customer_names = re.findall(customer_name_pattern, self.deviceConfig)
        return customer_names

    def parse_customer_vlan(self, customer_name):
        intPattern = (
                r"interface GigabitEthernet0/0.([0-9]+)\n"
        )
        all_customer_vlans = re.search(intPattern, self.deviceConfig)
        return int(all_customer_vlans.group(1))

    def parse_customer_ip(self, customer_vlan):
        customer_ip_pattern = r"GigabitEthernet0/0.%s[ ]+([0-9\.]+)" % customer_vlan
        customer_ip_address = re.search(customer_ip_pattern, self.deviceConfig)
        return  customer_ip_address.group(1)

    def parse_customer_data(self):
        customer_data = {}
        customer_names = self.parse_customer_names()
        for customer in customer_names:
            vlan = self.parse_customer_vlan(customer)
            ip = self.parse_customer_ip(vlan)
            customer_data[customer] = [vlan, ip]
        return customer_data


class TestParse(unittest2.TestCase):
    def test_parse_cust_name(self):
        cp = ConfigurationParser()
        expected_names = ["CUSTOMER_A", "CUSTOMER_B"]
        parsed_names = cp.parse_customer_names()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)

    def test_parse_customer_vlan(self):
        cp = ConfigurationParser()
        customer_name = "CUSTOMER_A"
        expected_vlan = 100
        parsed_vlan = cp.parse_customer_vlan(customer_name)
        self.assertEqual(expected_vlan, parsed_vlan)

    def test_parse_customer_ip(self):
        cp = ConfigurationParser()
        customer_vlan = 100
        expected_ip = "10.10.100.1"
        parsed_ip = cp.parse_customer_ip(customer_vlan)
        self.assertEqual(expected_ip, parsed_ip)

    def test_parse_customer_data(self):
        cp = ConfigurationParser()
        expected_data = {"CUSTOMER_A": [100, "10.10.100.1"]}
        parsed_Data = cp.parse_customer_data
        self.assertEqual(expected_data, parsed_Data)
