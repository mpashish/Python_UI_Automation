from utility.BaseClass import BaseClass


class Test_Read_Data(BaseClass):

    def test_read_data(self):
        excel_data = self.get_data_for(record_key="Name", record_value="Sachin")
        print(excel_data)

    def test_read_data1(self, get_data_as_fixture_parameter):
        print(self.get_data_as_fixture_parameter["Name"])
        print(self.get_data_as_fixture_parameter["Surname"])

