# Import necessary modules and classes
import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import banks, branches
from .serializers import BankSerializer, BranchSerializer

# Initialize a FileSystemStorage object for file handling
fs = FileSystemStorage(location='tmp/')

# Define a viewset for handling bank-related API requests
class BankViewSet(viewsets.ModelViewSet):
    queryset = banks.objects.all()
    serializer_class = BankSerializer

    # Custom action for uploading bank data from a CSV file
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from CSV"""
        file = request.FILES["file"]

        # Read the contents of the uploaded file as bytes
        content = file.read()
        # Create a ContentFile object to store the file content
        file_content = ContentFile(content)
        # Save the ContentFile with a temporary filename
        file_name = fs.save("_tmp.csv", file_content)
        # Get the path of the temporary file
        tmp_file = fs.path(file_name)

        # Open the CSV file for reading, ignoring any encoding errors
        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        # Skip the header row
        next(reader)

        # Create a list to store bank objects
        product_list = []
        for row in reader:
            # Unpack CSV row data into variables
            name, id = row
            # Create a Bank object and add it to the list
            product_list.append(
                banks(
                    name=name,
                    id=id,
                )
            )

        # Bulk insert the list of bank objects into the database
        banks.objects.bulk_create(product_list)

        # Respond with a success message
        return Response("Successfully uploaded the banks")

# Define a viewset for handling branch-related API requests
class BranchViewSet(viewsets.ModelViewSet):
    queryset = branches.objects.all()
    serializer_class = BranchSerializer

    # Custom method to filter branches by IFSC code
    def get_queryset(self):
        ifsc = self.request.query_params.get('ifsc')
        return branches.objects.filter(ifsc=ifsc)

    # Custom action for uploading branch data from a CSV file
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from CSV"""
        file = request.FILES["file"]

        # Read the contents of the uploaded file as bytes
        content = file.read()
        # Create a ContentFile object to store the file content
        file_content = ContentFile(content)
        # Save the ContentFile with a temporary filename
        file_name = fs.save("_tmp.csv", file_content)
        # Get the path of the temporary file
        tmp_file = fs.path(file_name)

        # Open the CSV file for reading, ignoring any encoding errors
        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        # Skip the header row
        next(reader)

        # Create a list to store branch objects
        product_list = []
        for row in reader:
            # Unpack CSV row data into variables
            ifsc, bank_id, branch, address, city, district, state, bank_name = row
            # Get the corresponding bank object based on the provided bank_id
            bank_id = banks.objects.get(id=bank_id)
            # Create a Branch object and add it to the list
            product_list.append(
                branches(
                    ifsc=ifsc,
                    bank_id=bank_id,
                    branch=branch,
                    address=address,
                    city=city,
                    district=district,
                    state=state,
                )
            )

        # Bulk insert the list of branch objects into the database
        branches.objects.bulk_create(product_list)

        # Respond with a success message
        return Response("Successfully uploaded the branches")
