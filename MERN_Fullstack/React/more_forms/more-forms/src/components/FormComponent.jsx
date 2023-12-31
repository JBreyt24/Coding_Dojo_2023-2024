import React, { useState } from 'react'

const FormComponent = (props) => {
    const createUser = (e) => {}
    // const {firstName, lastName, email, password, confirmPass} = props;

    const [firstName, setFirstName] = useState ("");
    const [lastName, setLastName] = useState ("");
    const [email, setEmail] = useState ("");
    const [password, setPassword] = useState ("");
    const [confirmPass, setConfirmPass] = useState ("");

    //     const newUser = { firstName, lastName, email, password, confirmPass };
    //     console.log("Welcome", newUser);

    // }
    return (
        <>
        <form>

            <div>
                <label htmlFor = "firstName"> First Name: </label>
                <input type = "text" name = "firstName" onChange = { e => setFirstName(e.target.value) } />
                {
                    firstName.length < 2 && firstName.length > 0 ?
                    <p>First Name must be at least 2 or more characters long</p>
                    :null
                }
            </div>
            <div>
                <label htmlFor = "lastName"> Last Name: </label>
                <input type = "text" name = "lastName" onChange = { e => setLastName(e.target.value) } />
                {
                    lastName.length < 2 && lastName.length > 0 ?
                    <p>Last Name must be at least 2 or more characters long</p>
                    :null
                }
            </div>
            <div>
                <label htmlFor = "email"> Email: </label>
                <input type = "text" name = "email" onChange = { e => setEmail(e.target.value) } />
                {
                    email.length < 5 && email.length > 0?
                    <p>Email must be at least 5 or more characters long</p>
                    :null
                }
            </div>
            <div>
                <label htmlFor = "password"> Password: </label>
                <input type = "password" name = "password" onChange = { e => setPassword(e.target.value) } />
                {
                    password.length < 8 && password.length > 0?
                    <p>Password must be at least 8 or more characters long</p>
                    :null
                }
            </div>            
            <div>
                <label htmlFor = "confirmPass"> Confirm Password: </label>
                <input type = "password" name = "confirmPass" onChange = { e => setConfirmPass(e.target.value) } />
                {
                    confirmPass !== password ?
                    <p>Passwords must match</p>
                    :null
                }
            </div>

        </form>

        <h1>Form Data</h1>
        <p>First Name: {firstName}</p>
        <p>Last Name: {lastName}</p>
        <p>Email: {email}</p>
        <p>Password: {password}</p>
        <p>Confirm Password: {confirmPass}</p>


        </>
    )
}

export default FormComponent;