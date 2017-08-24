import React from "react";
import ReactDOM from "react-dom";
import EmailSender from "../components/emailSender"
import ListOfMailingLists from "../components/listOfMailingLists"

let BaseComponent = React.createClass({
  render() {
    return (
      <div>
        <ListOfMailingLists/>
        <EmailSender/>
      </div>
    )
  }
})

ReactDOM.render(<BaseComponent />, document.getElementById('container'))