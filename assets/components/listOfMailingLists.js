import React from "react";


let ListOfMailingLists = React.createClass({

  getInitialState: function () {
    return (
      { mailingLists: {} }
    )
  },

  addItem: function (newItem) {
    let timestamp = (new Date()).getTime();
    this.state.mailingLists['fruit-' + timestamp] = newItem;
    this.setState({ mailingLists: this.state.mailingLists });
  },

  render: function () {
    return (
      <div>
        <AddListForm addItem={this.addItem} />
        <MailingList mailingLists={this.state.mailingLists} />
      </div>
    );
  }
});


let MailingList = React.createClass({

  render: function () {
    return (
      <div>
        <ul>
          {
            Object.keys(this.props.mailingLists).map(function (key) {
              return <li>{this.props.mailingLists[key]}</li>
            }.bind(this))
          }
        </ul>
      </div>
    );
  }
});


let AddListForm = React.createClass({

  createList: function (e) {
    e.preventDefault();
    let mailingList = this.refs.listName.value;
    if (typeof mailingList === 'string' && mailingList.length > 0) {
      this.props.addItem(mailingList);
      this.refs.listForm.reset();
    }
  },

  render: function () {
    return (
      <form ref="listForm" onSubmit={this.createList}>
        <button type="submit" >Add Mailing List</button>
        <div>
          <div>
            List Name
            <input type="text" placeholder="ex. Incubate" ref="listName" />
          </div>
        </div>
      </form>
    )
  }
});


export default ListOfMailingLists;