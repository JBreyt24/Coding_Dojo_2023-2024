import React, {useState} from 'react';

const Display = (props) => {
    const {todoList, setTodoList} = props

    const toggleList = (list) => {
        const updatedTodoList = todoList.map((listFromMap) => {
            if(listFromMap === list){
                listFromMap.hasBeenCompleted = !listFromMap.hasBeenCompleted
            }
            return listFromMap
        })
        setTodoList(updatedTodoList)
    }
    const removeFromList = (list) => {
        const updatedTodoList = todoList.filter((listFromFilter) => listFromFilter !== list)
        setTodoList(updatedTodoList)
    }
    return (
        <div>
            <h2>Your List</h2>
            {
                todoList.map((list, idx) => (
                    <div key= {idx} style={{border: "2px solid white", backgroundColor: 'grey'}}>
                        {
                            list.hasBeenCompleted?
                            <h3 style={{textDecoration: "line-through"}}>Title: {list.title}</h3>:
                            <h3>Title: {list.title}</h3>
                        }
                        <input type="checkbox" onClick={() => toggleList(list)} defaultChecked ={list.hasBeenCompleted}/>
                        <button onClick={() => removeFromList(list)}>Delete</button>
                    </div>
                ))
            }
        </div>
    )
}

export default Display;