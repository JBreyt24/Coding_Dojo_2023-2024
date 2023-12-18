const PersonCard = (props) => {

    const {firstName, lastName, age, hairColor } = props

    return (
        <div>
            <h1> {lastName}, {firstName} </h1>
            <h3> {age} </h3>
            <h3> {hairColor} </h3>
        </div>
    )
}

export default PersonCard;