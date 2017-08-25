import React from "react";


let AddListForm = React.createClass({

  createList(e) {
    e.preventDefault();
    let newMailingList = this.refs.listName.value;
    if (typeof newMailingList === 'string' && newMailingList.length > 0) {
      this.props.addItem(newMailingList);
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


export default AddListForm;