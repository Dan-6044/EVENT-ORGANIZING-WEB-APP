function openEditModal(vendorId) {
  document.getElementById('vendorId').value = vendorId;
  console.log("Vendor ID:", vendorId);

  fetch(`/get_vendor_details/${vendorId}/`)
    .then(response => response.json())
    .then(data => {
      // Basic fields
      document.getElementById('vendorName').value = data.vendor_name || '';
      document.getElementById('vendorType').value = data.vendor_type || '';
      document.getElementById('VendorDescription').value = data.description || '';
      document.getElementById('VendorPayment_cost').value = data.payment_cost || '';
      document.getElementById('VendorDeposit').value = data.deposit || '';
      document.getElementById('VendorCredit_days').value = data.credit_days || '';
      document.getElementById('VendorPayment_status').value = data.payment_status || '';

      // Example nested field population (Venue)
      if (data.venue) {
        document.getElementById('venue_address').value = data.venue.address || '';
        document.getElementById('venue_capacity').value = data.venue.capacity || '';
        document.getElementById('venue_rental_cost').value = data.venue.rental_cost || '';
        document.getElementById('venue_booking_time').value = data.venue.booking_time || '';
        document.getElementById('venue_requirements').value = data.venue.requirements || '';
      }

      // Add similar sections here for: catering, av, decor, entertainment, etc.

    })
    .catch(error => {
      console.error('Error fetching vendor details:', error);
      alert('Failed to load vendor details. Please try again.');
    });

  // Show modal
  const editVendorModal = new bootstrap.Modal(document.getElementById('editVendorModal'));
  editVendorModal.show();
}

document.getElementById('editVendorForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const vendorId = document.getElementById('vendorId').value;

  // Collect form data
  const updatedData = {
    vendor_name: document.getElementById('vendorName').value,
    vendor_type: document.getElementById('vendorType').value,
    description: document.getElementById('VendorDescription').value,
    payment_cost: document.getElementById('VendorPayment_cost').value,
    deposit: document.getElementById('VendorDeposit').value,
    credit_days: document.getElementById('VendorCredit_days').value,
    payment_status: document.getElementById('VendorPayment_status').value,

    
  };

  fetch(`/update_vendor/${vendorId}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify(updatedData),
  })
    .then(response => response.json())
    .then(data => {
      alert('Vendor updated successfully!');
      $('#editVendorModal').modal('hide');
    })
    .catch(error => {
      console.error('Error updating vendor:', error);
      alert('Failed to update vendor. Please try again.');
    });
});

// CSRF helper
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// JavaScript function to handle vendor deletion
function confirmDelete(vendorId) {
    // Ask the user for confirmation before deletion
    if (confirm('Are you sure you want to delete this vendor?')) {
        // If confirmed, redirect to the delete vendor URL
        const url = `/delete_vendor/${vendorId}/`;
        window.location.href = url;  // Redirect to the delete URL
    }
}
