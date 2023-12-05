import React from "react";

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