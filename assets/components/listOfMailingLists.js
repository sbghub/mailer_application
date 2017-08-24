import React from "react";


let ListOfMailingLists = React.createClass({

  getInitialState() {
    return (
      { mailingLists: [] }
    )
  },

  addItem(newItem) {
    let newList = this.state.mailingLists;
    newList.push(newItem);
    this.setState({ mailingLists: newList });
  },

  render() {
    return (
      <div>
        <AddListForm addItem={this.addItem} />
        <GroupList mailingLists={this.state.mailingLists} />
      </div>
    );
  }
});


let GroupList = React.createClass({

  render() {
    return (
      <div>
        <ul>
          {
            Object.keys(this.props.mailingLists).map(function (item, index) {
              return (
                <div>
                  <li>{this.props.mailingLists[index]}</li>
                  <button>Delete</button>
                </div>
              )
            }.bind(this))
          }
        </ul>
      </div>
    );
  }
});


let AddListForm = React.createClass({

  createList(e) {
    e.preventDefault();
    let mailingList = this.refs.listName.value;
    if (typeof mailingList === 'string' && mailingList.length > 0) {
      this.props.addItem(mailingList);
      this.refs.listForm.reset();
    }
  },

  render() {
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