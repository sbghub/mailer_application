import React from "react";
import ReactDOM from "react-dom";

let ListOfMailingLists = React.createClass({
  render() {
    return (
      <div name="mailingList">
        <button name="add">Add Email List</button>
        <ul name="listOfEmailLists">
          <li name="emailList">
            name 1
            <button name="delete">Delete</button>
          </li>
        </ul>
      </div>
    )
  }
})

export default ListOfMailingLists;