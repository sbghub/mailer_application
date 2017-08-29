import React from "react";
import {Input} from "react-bootstrap";

import create from "higherOrder/create";
import hasPermission from "higherOrder/hasPermission";


class EmailSender extends React.Component {
    render() {
        const {changeSet, handleChange, handleSubmit} = this.props;

        return (
            <form onSubmit={handleSubmit}>

                <Input
                    autoComplete="off"
                    bsStyle={changeSet._errors.email ? "error" : null}
                    hasFeedback
                    help={changeSet._errors.email}
                    label="Email"
                    name="email"
                    onChange={handleChange}
                    type="email"
                    value={changeSet.email}
                />
                <Input
                    bsStyle={changeSet._errors.first_name ? "error" : null}
                    hasFeedback
                    help={changeSet._errors.first_name}
                    label="Subject"
                    name="subject"
                    type="text"
                    onChange={handleChange}
                    value={changeSet.first_name}
                    help={changeSet._errors.first_name}
                />
                <Input
                    bsStyle={changeSet._errors.last_name ? "error" : null}
                    hasFeedback
                    help={changeSet._errors.last_name}
                    label="Body"
                    name="body"
                    type="text"
                    onChange={handleChange}
                    value={changeSet.last_name}
                />

                
                <button type="submit" className="hidden"/>
            </form>
        );
    }
}

export default hasPermission(create(EmailSender), "users.add_emailuser");
