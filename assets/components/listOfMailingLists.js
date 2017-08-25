import React from "react";
import AddListForm from "./mailing_list_components/addListForm"
import GroupList from "./mailing_list_components/groupList"


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

  deleteItem(index) {
    let newList = this.state.mailingLists;
    newList.splice(index, 1);
    this.setState({ mailingLists: newList });
  },

  render() {
    return (
      <div>
        <AddListForm addItem={this.addItem} />
        <GroupList
          mailingLists={this.state.mailingLists}
          deleteItem={this.deleteItem} />
      </div>
    );
  }
});


export default ListOfMailingLists;