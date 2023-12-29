import React, { useState } from 'react'

const FormComponent = (props) => {

    // const {firstName, lastName, email, password, confirmPass} = props;

    const [firstName, setFirstName] = useState ("");
    const [lastName, setLastName] = useState ("");
    const [email, setEmail] = useState ("");
    const [password, setPassword] = useState ("");
    const [confirmPass, setConfirmPass] = useState ("");

    // const createUser = (e) => {
    //     e.preventDefault();

    //     const newUser = { firstName, lastName, email, password, confirmPass };
    //     console.log("Welcome", newUser);

    // }

    return (
        <>
        <form>

            <div>
                <label htmlFor = "firstName"> First Name: </label>
                <input type = "text" name = "firstName" onChange = { e => setFirstName(e.target.value) } />
            </div>
            <div>
                <label htmlFor = "lastName"> Last Name: </label>
                <input type = "text" name = "lastName" onChange = { e => setLastName(e.target.value) } />
            </div>
            <div>
                <label htmlFor = "email"> Email: </label>
                <input type = "text" name = "email" onChange = { e => setEmail(e.target.value) } />
            </div>
            <div>
                <label htmlFor = "password"> Password: </label>
                <input type = "password" name = "password" onChange = { e => setPassword(e.target.value) } />
            </div>            
            <div>
                <label htmlFor = "confirmPass"> Confirm Password: </label>
                <input type = "password" name = "confirmPass" onChange = { e => setConfirmPass(e.target.value) } />
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