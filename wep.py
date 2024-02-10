import streamlit as st
import functions
todos = functions.get_todos()
def add_todo():
    todo = st.session_state["todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

def complete_todo():
    todotoremove = st.session_state[todo]
    index = todos.index(todotoremove)
    todos.pop(index)
    functions.write_todos(todos)

st.title("my-todo-app")
st.subheader("this is my todo app")
st.write("this app made to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,  key=todo)
    if checkbox == True:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="todo")
