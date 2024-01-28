import React, {useState} from 'react';

const Form = (props) => {
    const {todoList, setTodoList} = props
    const [title, setTitle] = useState ('')

    const submitHandler = (e) => {
        e.preventDefault()
        console.log("Submitted");
        const newList = {
            title,
            hasBeenCompleted: false
        }
        setTodoList([...todoList, newList])
        setTitle("")
    }
    return (
        <div>
            <form onSubmit = {submitHandler}>
                <div>
                    <input type="text" value={title} onChange={(e) => setTitle(e.target.value)}/>
                </div>
                <button>Add to list</button>
            </form>
        </div>
)}

export default Form;