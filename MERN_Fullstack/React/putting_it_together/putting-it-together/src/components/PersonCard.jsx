import React, {useState} from "react";

const PersonCard = (props) => {

const {firstName, lastName, age, hairColor } = props;

const [ personAge, setPersonAge] = useState(age);
//       getter  ,   setter    


    return (
        <div>
            <h1> {lastName}, {firstName} </h1>
            <h3> {personAge} </h3>
            <h3> {hairColor} </h3>
            <button onClick={ () => setPersonAge(personAge + 1)}> Birthday Button for {firstName} {lastName}
            </button>
        </div>
    )
}

export default PersonCard;