import os
import pytest
import csv
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from medication_reminder import create_csv_file, add_medication, view_medications  

# Test for create_csv_file
def test_create_csv_file():
    """Test if the CSV file is created correctly."""
    filename = 'test_medications.csv'
    create_csv_file(filename)
    assert os.path.exists(filename), f"File {filename} was not created."

    # Clean up after test
    if os.path.exists(filename):
        os.remove(filename)

# Test for add_medication
@patch('builtins.input', side_effect=['Test Med', '100mg', '08:00 AM', '2025-04-08', 'Take after breakfast', ''])

def test_add_medication(mock_input):
    """Test if a new medication is added to the CSV file correctly."""
    filename = 'test_medication_data.csv'

    # Ensure file is empty before the test
    if os.path.exists(filename):
        os.remove(filename)
    
    add_medication(filename)

    # Check if medication data is written to the file
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  
        row = next(reader)  
        assert row == ['Test Med', '100mg', '08:00 AM', '2025-04-08', 'Take after breakfast'], f"Unexpected data in CSV: {row}"
    
   
    if os.path.exists(filename):
        os.remove(filename)

# Test for view_medications
def test_view_medications():
    """Test if medications are displayed correctly."""
    filename = 'test_medication_data.csv'

    # Write test data to the file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Dosage', 'Time', 'Date', 'Notes'])
        writer.writerow(['Test Med', '100mg', '08:00 AM', '2025-04-08', 'Take after breakfast'])
    
    # Test the viewing of medications using StringIO to capture printed output
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        view_medications(filename)
        output = mock_stdout.getvalue().strip()
        
    assert "Test Med" in output, "Medication name was not found in the output"
    assert "100mg" in output, "Medication dosage was not found in the output"

    # Clean up after test
    if os.path.exists(filename):
        os.remove(filename)

 
if __name__ == "__main__":
    pytest.main()
