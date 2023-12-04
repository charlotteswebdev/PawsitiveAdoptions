import React from 'react';
import './checkbox.css';

function CategoryBox(props){

    // Testing user input to checkboxes in the console
    const checkBoxState = (event) => {
        if(props.checkboxCategory === "Romantic" && event.target.checked) {
            console.log("'Romantic' checkbox is connected");
        }
    }


    return ( <label id={props.id} class="checkboxes"> 
    {props.checkboxCategory} 
    <input type="checkbox" onChange={checkBoxState}/> 
    <span class="checkmark"> </span>  
    </label>
    )
}

export default CategoryBox;