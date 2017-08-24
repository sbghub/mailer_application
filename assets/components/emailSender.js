import React from "react";
import ReactDOM from "react-dom";

let EmailSender = React.createClass({
  render() {
    return (
      <div name="emailSender">
          <input name="sendToAddress"></input>
          <input name="subject"></input>
          <input name="emailBody"></input>
          <button name="send">Send</button>
      </div>
    )
  }
})

export default EmailSender;