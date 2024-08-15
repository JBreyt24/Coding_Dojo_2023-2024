import React, {useState} from 'react';
import {Link} from 'react-router-dom';

const Home = (props) => {
    return (
        <div>
            <Link to = {'/form'} style= {{color: 'red'}} >Go to Form</Link>
            <h2>HOME</h2>
        </div>
    )}

export default Home;