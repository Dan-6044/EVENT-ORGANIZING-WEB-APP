  // Event listener for vendor type selection
  document.getElementById('vendor_type').addEventListener('change', function() {
    const vendorType = this.value;
    const vendorDetailsDiv = document.getElementById('vendor-details');
    
    vendorDetailsDiv.innerHTML = ''; // Clear existing dynamic fields

    // Dynamically render fields based on vendor type
    if (vendorType === 'venue') {
        vendorDetailsDiv.innerHTML = `
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="venue_address" class="form-label">Venue Address</label>
                    <input type="text" class="form-control" id="venue_address" name="venue_address" placeholder="Enter Venue Address" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="venue_capacity" class="form-label">Venue Size/Capacity</label>
                    <input type="number" class="form-control" id="venue_capacity" name="venue_capacity" placeholder="Enter Venue Capacity" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="venue_booking_time" class="form-label">Booking Date/Time</label>
                    <input type="datetime-local" class="form-control" id="venue_booking_time" name="venue_booking_time" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="venue_rental_cost" class="form-label">Cost of Venue Rental</label>
                    <input type="number" class="form-control" id="venue_rental_cost" name="venue_rental_cost" placeholder="Enter Cost" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="venue_requirements" class="form-label">Additional Requirements</label>
                    <input type="text" class="form-control" id="venue_requirements" name="venue_requirements" placeholder="Enter Additional Requirements">
                </div>
            </div>
        `;
    } else if (vendorType === 'catering') {
        vendorDetailsDiv.innerHTML = `
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="catering_type" class="form-label">Catering Type</label>
                    <input type="text" class="form-control" id="catering_type" name="catering_type" placeholder="Enter Catering Type" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="menu_options" class="form-label">Menu Options</label>
                    <textarea class="form-control" id="menu_options" name="menu_options" placeholder="Enter Menu Options" required></textarea>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="dietary_preferences" class="form-label">Guest Dietary Preferences</label>
                    <input type="text" class="form-control" id="dietary_preferences" name="dietary_preferences" placeholder="Enter Dietary Preferences">
                </div>
                <div class="col-md-6 form-group">
                    <label for="catering_cost" class="form-label">Catering Costs</label>
                    <input type="number" class="form-control" id="catering_cost" name="catering_cost" placeholder="Enter Catering Cost" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="service_requirements" class="form-label">Service Requirements</label>
                    <input type="text" class="form-control" id="service_requirements" name="service_requirements" placeholder="Enter Service Requirements">
                </div>
            </div>
        `;
    } else if (vendorType === 'av') {
        vendorDetailsDiv.innerHTML = `
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="equipment_provided" class="form-label">Equipment Provided</label>
                    <input type="text" class="form-control" id="equipment_provided" name="equipment_provided" placeholder="Enter Equipment Provided" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="av_cost" class="form-label">Cost of AV Equipment Rental</label>
                    <input type="number" class="form-control" id="av_cost" name="av_cost" placeholder="Enter AV Equipment Cost" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="technical_support" class="form-label">Technical Support</label>
                    <select class="form-select" id="technical_support" name="technical_support" required>
                        <option value="yes">Yes</option>
                        <option value="no">No</option>
                    </select>
                </div>
                <div class="col-md-6 form-group">
                    <label for="setup_time_av" class="form-label">Setup Time</label>
                    <input type="time" class="form-control" id="setup_time_av" name="setup_time_av" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="contact_emergency" class="form-label">Contact for Emergencies</label>
                    <input type="text" class="form-control" id="contact_emergency" name="contact_emergency" placeholder="Enter Contact Number" required>
                </div>
            </div>
        `;
    } else if (vendorType === 'decor') {
        vendorDetailsDiv.innerHTML = `
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="design_theme" class="form-label">Design Theme</label>
                    <input type="text" class="form-control" id="design_theme" name="design_theme" placeholder="Enter Design Theme" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="items_supplied" class="form-label">Items Supplied</label>
                    <input type="text" class="form-control" id="items_supplied" name="items_supplied" placeholder="Enter Items Supplied" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="decor_cost" class="form-label">Cost of Decor Services</label>
                    <input type="number" class="form-control" id="decor_cost" name="decor_cost" placeholder="Enter Decor Cost" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="set_up_time" class="form-label">Set-Up Time</label>
                    <input type="time" class="form-control" id="set_up_time" name="set_up_time" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="teardown_time" class="form-label">Return/Teardown Time</label>
                    <input type="time" class="form-control" id="teardown_time" name="teardown_time" required>
                </div>
            </div>
        `;
    } else if (vendorType === 'entertainment') {
        vendorDetailsDiv.innerHTML = `
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="entertainment_type" class="form-label">Type of Entertainment</label>
                    <input type="text" class="form-control" id="entertainment_type" name="entertainment_type" placeholder="Enter Type of Entertainment" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="entertainment_cost" class="form-label">Cost of Entertainment Services</label>
                    <input type="number" class="form-control" id="entertainment_cost" name="entertainment_cost" placeholder="Enter Entertainment Cost" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="entertainment_duration" class="form-label">Duration of Performance</label>
                    <input type="text" class="form-control" id="entertainment_duration" name="entertainment_duration" placeholder="Enter Duration (e.g. 1 hour, 3 hours)" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="entertainment_requirements" class="form-label">Special Requirements</label>
                    <input type="text" class="form-control" id="entertainment_requirements" name="entertainment_requirements" placeholder="Enter Special Requirements">
                </div>
            </div>
        `;
    } else if (vendorType === 'security') {
        vendorDetailsDiv.innerHTML = `
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="security_personnel" class="form-label">Security Personnel</label>
                    <input type="number" class="form-control" id="security_personnel" name="security_personnel" placeholder="Enter Number of Personnel" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="security_duties" class="form-label">Specific Duties</label>
                    <input type="text" class="form-control" id="security_duties" name="security_duties" placeholder="Enter Security Duties" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="security_cost" class="form-label">Security Costs</label>
                    <input type="number" class="form-control" id="security_cost" name="security_cost" placeholder="Enter Security Costs" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="security_setup" class="form-label">Required Setup</label>
                    <input type="text" class="form-control" id="security_setup" name="security_setup" placeholder="Enter Security Setup Details" required>
                </div>
            </div>
        `;
    } else if (vendorType === 'printing') {
        vendorDetailsDiv.innerHTML = `
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="printed_materials" class="form-label">Printed Materials</label>
                    <input type="text" class="form-control" id="printed_materials" name="printed_materials" placeholder="Enter Printed Materials" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="printing_cost" class="form-label">Cost of Printing Services</label>
                    <input type="number" class="form-control" id="printing_cost" name="printing_cost" placeholder="Enter Printing Cost" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="printing_design" class="form-label">Design Requirements</label>
                    <input type="text" class="form-control" id="printing_design" name="printing_design" placeholder="Enter Design Requirements" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="delivery_timeframe" class="form-label">Delivery Timeframe</label>
                    <input type="text" class="form-control" id="delivery_timeframe" name="delivery_timeframe" placeholder="Enter Delivery Timeframe" required>
                </div>
            </div>
        `;
    } else if (vendorType === 'transportation') {
        vendorDetailsDiv.innerHTML = `
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="transportation_type" class="form-label">Transportation Type</label>
                    <input type="text" class="form-control" id="transportation_type" name="transportation_type" placeholder="Enter Transportation Type" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="transportation_cost" class="form-label">Cost of Transportation</label>
                    <input type="number" class="form-control" id="transportation_cost" name="transportation_cost" placeholder="Enter Transportation Cost" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="transportation_dates" class="form-label">Transport Dates/Times</label>
                    <input type="text" class="form-control" id="transportation_dates" name="transportation_dates" placeholder="Enter Transport Dates/Times" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="passenger_capacity" class="form-label">Passenger Capacity</label>
                    <input type="number" class="form-control" id="passenger_capacity" name="passenger_capacity" placeholder="Enter Passenger Capacity" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="special_requests_transportation" class="form-label">Special Requests</label>
                    <input type="text" class="form-control" id="special_requests_transportation" name="special_requests_transportation" placeholder="Enter Special Requests">
                </div>
            </div>
        `;
    } else if (vendorType === 'waste_management') {
        vendorDetailsDiv.innerHTML = `
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="waste_collection_services" class="form-label">Waste Collection Services</label>
                    <input type="text" class="form-control" id="waste_collection_services" name="waste_collection_services" placeholder="Enter Waste Collection Services" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="waste_management_cost" class="form-label">Cost of Waste Management</label>
                    <input type="number" class="form-control" id="waste_management_cost" name="waste_management_cost" placeholder="Enter Waste Management Cost" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 form-group">
                    <label for="waste_service_details" class="form-label">Service Details</label>
                    <input type="text" class="form-control" id="waste_service_details" name="waste_service_details" placeholder="Enter Waste Service Details" required>
                </div>
                <div class="col-md-6 form-group">
                    <label for="restroom_facilities" class="form-label">Restroom Facilities</label>
                    <input type="text" class="form-control" id="restroom_facilities" name="restroom_facilities" placeholder="Enter Restroom Facilities" required>
                </div>
            </div>
        `;
    }
});