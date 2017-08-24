<<<<<<< Updated upstream
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
=======
import React, { PropTypes } from "react";
import connect from "react-redux";

class ListOfMailingLists extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      mailingLists: {}
    };
    this.addItem = this.addItem.bind(this);
    this.createList = this.createList.bind(this);
  }

  addItem(newItem) {
    let timestamp = (new Date()).getTime();
    this.state.mailingLists['fruit-' + timestamp] = newItem;
    this.setState({ mailingLists: this.state.mailingLists });
  }

  createList(e) {
    e.preventDefault();
    let mailList = this.refs.listName.value;
    if (typeof mailList === 'string' && mailList.length > 0) {
      this.props.addItem(mailList);
      this.refs.listForm.reset();
    }
  }

  render() {
    return (
      <div>
        <form ref="listForm" onSubmit={this.createList}>
          <button type="submit" >Add Mailing List</button>
          <div>
            <div>
              List Name
            <input type="text" placeholder="ex. Incubate" ref="listName" />
            </div>
          </div>
        </form>
        <div>
          <ul>
            {
              Object.keys(this.props.mailingLists).map(function (key) {
                return <li>{this.props.mailingLists[key]}</li>
              }.bind(this))
            }
          </ul>
        </div>
      </div>
    );
  }
};


function mapStateToProps(state, ownProps) {
  return {
    mailingLists: state.mailingLists,
  };
}
>>>>>>> Stashed changes

export default connect(mapStateToProps, mapDispatchToProps)(ListOfMailingLists);
