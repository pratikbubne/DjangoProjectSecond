from django import forms
from django.views.generic import CreateView, DetailView
from Asset.models import Equipment
from AssetModel.models import AssetModel
from Project_site.models import ProjectSite
from Functional_group.models import FunctionalGroup
from Department.models import Department
from Supplier.models import Supplier
from django.shortcuts import render

import django_filters


# Create your views here.
class AssetCreateView(CreateView):
    model = Equipment
    template_name = 'Asset/Equipment_Form.html'
    fields = ['Asset_Number', 'Equipment_Name', 'Alternative_Name', 'ECRI_Number', 'Manufacturer', 'Model_Name',
              'Serial_Number', 'Supplier_Name', 'Site_Name', 'Location_Name', 'Location_Number', 'Functional_Group',
              'Dept_Name', 'Installation_Date', 'Warranty', 'End_of_Warranty', 'Depreciation_Years', 'Replacement_Date', 'Acceptance_Date', 'Purch_Price',
              'Accessories', 'Operating_System', 'Antivirus_Software', 'Application_Software', 'Revision', 'IP_Address',
              'MAC_Address', 'Port_No', 'Switch_Specs', 'Equipment_License_Details',
              'Test_Equipment_Needed_For_Test_Or_PM', 'Operating_Voltage', 'Power_Consumption', 'Battery_Type', 'Battery_Rating',
              'Fuse_Type', 'Fuse_Rating', 'Various_Passwords_For_User', 'Various_Passwords_For_Demo', 'Various_Passwords_For_Service',
              'Various_Passwords_For_Configuration', 'PO_Number', 'Purchase_Value', 'Residual_Value', 'Depreciated_Value',
              'Hourly_Code', 'Risk_Code', 'Material_AssetNumber', 'Internal_RequestNumber', 'Internal_RequestDate',
              'Financial_ACNumber', 'Service_Provider_Name', 'Contract_Number', 'Concerned_Person_Name', 'Concerned_Person_Contact',
              'No_of_Planned_PM', 'No_of_Corrective_Planned', 'No_of_Planned_QC', 'Spare_Part_Inclusion_in_PM',
              'Spare_Part_Inclusion_in_CM', 'Max_Down_Time', 'Response_Time', 'Estimated_Time_to_Repair',
              'Standardized_Reason_for_Delay_in_PM', 'Operating_Manual', 'Service_Manual',
              'Battery_Replacement_Frequency', 'Battery_Maintenance']


class AssetDetailView(DetailView):
    model = Equipment
    template_name = "Asset/AssetDetailView.html"


class UserFilter(django_filters.FilterSet):
    Model_Name = django_filters.ModelChoiceFilter(queryset=AssetModel.objects.all(), to_field_name='Model_Name',
                                                  empty_label="Select Model_Name")

    Supplier_Name = django_filters.ModelChoiceFilter(queryset=Supplier.objects.all(), to_field_name='Supplier_Name',
                                                     empty_label="Select Supplier_Name")

    Site_Name = django_filters.ModelChoiceFilter(queryset=ProjectSite.objects.all(), to_field_name='Site_Name',
                                                 empty_label="Select Site_Name")

    Functional_Group = django_filters.ModelChoiceFilter(queryset=FunctionalGroup.objects.all(),
                                                        to_field_name='Functional_Group',
                                                        empty_label="Select Functional_Group")

    Dept_Name = django_filters.ModelChoiceFilter(queryset=Department.objects.all(), to_field_name='Dept_Name',
                                                 empty_label="Select Dept_Name")

    class Meta:
        model = Equipment
        fields = ['Asset_Number', 'Equipment_Name', 'ECRI_Number', 'Model_Name', 'Supplier_Name',
                  'Site_Name', 'Functional_Group', 'Dept_Name', 'End_of_Warranty', 'Installation_Date',
                  'Location_Number', 'Manufacturer', 'Serial_Number', 'Operating_System', 'Antivirus_Software',
                  'Application_Software', 'IP_Address', 'MAC_Address', 'PO_Number', 'Hourly_Code', 'Risk_Code',
                  'Material_AssetNumber', 'Internal_RequestNumber', 'Service_Provider_Name', 'Concerned_Person_Name', 'Contract_Number']


def search(request):
    user_list = Equipment.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'Asset/searchlist.html', {'filter': user_filter})
