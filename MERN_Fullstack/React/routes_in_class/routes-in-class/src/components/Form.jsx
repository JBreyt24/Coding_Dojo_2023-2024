import React, {useState} from 'react';
import {Link, useNavigate} from 'react-router-dom';

const Form = (props) => {
    const navigate = useNavigate()
    const [firstName, setFirstName] = useState ('')

    const submitHandler = (event) => {
        event.preventDefault();
        // navigate('/dynamic/' + firstName)
        // or you can use backticks instead!
        navigate(`/dynamic/${firstName}`)
    }
    return (
        <div>
            <Link to= {'/'} style = {{color: 'red'}}>Home</Link>
            <h2>FORM</h2>
            <form onSubmit ={submitHandler}>
                <input type="text" value={firstName} onChange={(event) => setFirstName(event.target.value)}/>
                <button>Submit</button>
            </form>
        </div>
)}

export default Form;