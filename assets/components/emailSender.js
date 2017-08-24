import React from "react";
import ReactDOM from "react-dom";

let EmailSender = React.createClass({
  render() {
    return (
      <div name="emailSender">
          <input name="sendToAddress" placeholder="to address"></input>
          <input name="subject" placeholder="subject"></input>
          <input name="emailBody" placeholder="body"></input>
          <button name="send">Send</button>
      </div>
    )
  }
})

export default EmailSender;