import React from "react";
import EmailList from "./emailList"


let GroupList = React.createClass({
  passItem(e) {
    e.preventDefault();
    this.props.deleteItem(e.target.id);
    console.log("grouplist", this.props);
  },

  render() {
    return (
      <div>
        <ul>
          {
            Object.keys(this.props.mailingLists).map(function (item, index) {
              return (
                <form key={index} id={index} onSubmit={this.passItem}>
                  <EmailList 
                    title={this.props.mailingLists[index]} 
                    counter={this.props.counter}
                    triggerIncr={this.props.triggerIncr}/>
                  <button type="submit">Delete</button>
                </form>
              )
            }.bind(this))
          }
        </ul>
      </div>
    );
  }
});


export default GroupList;