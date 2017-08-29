import React from "react";


let EmailList = React.createClass({
  setInitalState() {
    return (
      { counter: 0 }
    )
  },

  passItem(e) {
    e.preventDefault();
    this.props.triggerIncr;
    console.log("emaillist", this.props)
  },

  render() {
    return (
      <div>
        {this.props.title}
        <button onClick={this.passItem}>incr</button>
      </div>
    );
  }
});


export default EmailList;