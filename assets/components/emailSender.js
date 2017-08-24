import React from "react";
import ReactDOM from "react-dom";

let EmailSender = React.createClass({
  render() {
    return (
      <div name="emailSender">
        <div>
          <input name="sendToAddress" placeholder="to address"></input>
        </div>
        <div>
          <input name="subject" placeholder="subject"></input>
        </div>
        <div>
          <input name="emailBody" placeholder="body"></input>
        </div>
        <button name="send">Send</button>
      </div>
    )
  }
})

export default EmailSender;