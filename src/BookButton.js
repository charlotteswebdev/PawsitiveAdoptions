import React from "react";

// create a function to handle the BOOK NOW button
function BookButton() {
    function HandleBooking() {
        alert("You have booked an event");
    }
  return (
    <button onClick ={HandleBooking}>Book Now
    </button>
  );
}
export default BookButton;