import React from "react";
import AddListForm from "./mailing_list_components/addListForm"
import GroupList from "./mailing_list_components/groupList"


let ListOfMailingLists = React.createClass({

  getInitialState() {
    return (
      {
        mailingLists: [],
        counter: 0
      }
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

  increment() {
    this.setState({ counter: this.state.counter + 1 });
    console.log(this.state.counter);
  },

  render() {
    return (
      <div>
        <AddListForm addItem={this.addItem} />
        <GroupList
          mailingLists={this.state.mailingLists}
          deleteItem={this.deleteItem}
          counter={this.state.counter}
          triggerIncr={this.increment} />
      </div>
    );
  }
});


export default ListOfMailingLists;