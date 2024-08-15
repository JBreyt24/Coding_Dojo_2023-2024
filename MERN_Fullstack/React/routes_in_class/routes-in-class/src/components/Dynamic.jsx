import React, {useState} from 'react';
import { useParams } from 'react-router-dom';
import {Link} from 'react-router-dom';

const Dynamic = (props) => {
    // console.log(useParams());
    const {name} = useParams()
    return (
        <div>
            <Link to = {'/'} style = {{color: 'red'}}>Back</Link>
            <h1 style = {{color:name}}>Hello, {name}</h1>
        </div>
)}

export default Dynamic;