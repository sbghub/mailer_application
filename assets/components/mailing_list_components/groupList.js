import React from "react";


let GroupList = React.createClass({
  passItem(e) {
    e.preventDefault();
    this.props.deleteItem(e.target.id);
  },

  render() {
    return (
      <div>
        <ul>
          {
            Object.keys(this.props.mailingLists).map(function (item, index) {
              return (
                <form key={index} id={index} onSubmit={this.passItem}>
                  <li>{this.props.mailingLists[index]}</li>
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