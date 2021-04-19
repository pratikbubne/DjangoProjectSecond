from django.db import models
from AssetModel.models import AssetModel
from Project_site.models import ProjectSite
from Supplier.models import Supplier
from Department.models import Department
from Functional_group.models import FunctionalGroup
from django.urls import reverse


class Equipment(models.Model):
    # General
    Equipment_ID = models.AutoField(primary_key=True)
    Asset_Number = models.CharField(max_length=50)
    Equipment_Name = models.CharField(max_length=50)
    Alternative_Name = models.CharField(max_length=50, blank=True)
    ECRI_Number = models.CharField(max_length=50)
    Manufacturer = models.CharField(max_length=50)
    Model_Name = models.ForeignKey(AssetModel, on_delete=models.SET_NULL, null=True)
    Serial_Number = models.CharField(max_length=50)
    Supplier_Name = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    Site_Name = models.ForeignKey(ProjectSite, on_delete=models.SET_NULL, null=True)
    Functional_Group = models.ForeignKey(FunctionalGroup, on_delete=models.SET_NULL, blank=True, null=True)
    Dept_Name = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    Installation_Date = models.CharField(max_length=50)
    Warranty = models.CharField(max_length=50)
    End_of_Warranty = models.CharField(max_length=50)
    Depreciation_Years = models.CharField(max_length=50, blank=True)
    Replacement_Date = models.CharField(max_length=50)
    Acceptance_Date = models.CharField(max_length=50)
    Purch_Price = models.CharField(max_length=50)
    Accessories = models.CharField(max_length=500, blank=True)
    Location_Name = models.CharField(max_length=500, blank=True)
    Location_Number = models.CharField(max_length=500, blank=True)

    # Technical

    Operating_System = models.CharField(max_length=50, blank=True)
    Antivirus_Software = models.CharField(max_length=50, blank=True)
    Application_Software = models.CharField(max_length=50, blank=True)
    Revision = models.CharField(max_length=50, blank=True)
    IP_Address = models.CharField(max_length=50, blank=True)
    MAC_Address = models.CharField(max_length=50, blank=True)
    Port_No = models.CharField(max_length=50, blank=True)
    Switch_Specs = models.CharField(max_length=50, blank=True)
    Equipment_License_Details = models.CharField(max_length=50, blank=True)
    Test_Equipment_Needed_For_Test_Or_PM = models.CharField(max_length=50, blank=True)
    Operating_Voltage = models.CharField(max_length=50, blank=True)
    Power_Consumption = models.CharField(max_length=50, blank=True)
    Battery_Type = models.CharField(max_length=50, blank=True)
    Battery_Rating = models.CharField(max_length=50, blank=True)
    Fuse_Type = models.CharField(max_length=50, blank=True)
    Fuse_Rating = models.CharField(max_length=50, blank=True)
    Various_Passwords_For_User = models.CharField(max_length=50, blank=True)
    Various_Passwords_For_Demo = models.CharField(max_length=50, blank=True)
    Various_Passwords_For_Service = models.CharField(max_length=50, blank=True)
    Various_Passwords_For_Configuration = models.CharField(max_length=50, blank=True)

    # Economic
    PO_Number = models.CharField(max_length=50)
    Purchase_Value = models.CharField(max_length=50)
    Residual_Value = models.CharField(max_length=50)
    Depreciated_Value = models.CharField(max_length=50)
    Hourly_Code = models.CharField(max_length=50, blank=True)
    Risk_Code = models.CharField(max_length=50, blank=True)
    Material_AssetNumber = models.CharField(max_length=50)
    Internal_RequestNumber = models.CharField(max_length=50)
    Internal_RequestDate = models.CharField(max_length=50)
    Financial_ACNumber = models.CharField(max_length=50)

    # Maintenance
    Service_Provider_Name = models.CharField(max_length=50)
    Concerned_Person_Name = models.CharField(max_length=50, blank=True)
    Concerned_Person_Contact = models.CharField(max_length=50, blank=True)
    Contract_Number = models.CharField(max_length=50, blank=True)
    No_of_Planned_PM = models.CharField(max_length=50, blank=True)
    No_of_Corrective_Planned = models.CharField(max_length=50, blank=True)
    No_of_Planned_QC = models.CharField(max_length=50, blank=True)
    Spare_Part_Inclusion_in_PM = models.CharField(max_length=50, blank=True)
    Spare_Part_Inclusion_in_CM = models.CharField(max_length=50, blank=True)
    Max_Down_Time = models.CharField(max_length=50, blank=True)
    Response_Time = models.CharField(max_length=50, blank=True)
    Estimated_Time_to_Repair = models.CharField(max_length=50, blank=True)
    Standardized_Reason_for_Delay_in_PM = models.CharField(max_length=50, blank=True)
    Operating_Manual = models.CharField(max_length=50, blank=True)
    Service_Manual = models.CharField(max_length=50, blank=True)
    Battery_Replacement_Frequency = models.CharField(max_length=50, blank=True)
    Battery_Maintenance = models.CharField(max_length=50, blank=True)

    @staticmethod
    def get_absolute_url():
        return reverse('asset')

    def __str__(self):
        return self.Equipment_ID
