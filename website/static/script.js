// Dropdown menu

document.addEventListener("mouseover", e => {
  const isDropdownButton = e.target.matches("[data-dropdown-button]")
  if (!isDropdownButton && e.target.closest("[data-dropdown]") != null) return

  let currentDropdown
  if (isDropdownButton) {
    currentDropdown = e.target.closest("[data-dropdown]")
    currentDropdown.classList.toggle("active")
  }

  document.querySelectorAll("[data-dropdown].active").forEach(dropdown => {
    if (dropdown === currentDropdown) return
    dropdown.classList.remove("active")
  })
})

// Sidebar 

let arrow = document.querySelectorAll(".arrow")
  for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e)=>{
   let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
   arrowParent.classList.toggle("showMenu")
    });
  }
  let sidebar = document.querySelector(".sidebar")
  let sidebarBtn = document.querySelector(".bx-menu")
  console.log(sidebarBtn);
  sidebarBtn.addEventListener("click", ()=>{
    sidebar.classList.toggle("close");
  });

// Add task

function addTask() { 
    const taskContainer = document.querySelector("#task-container");

    let newTask = document.createElement("p")
    let taskDescription = document.querySelector(".task-description").value
    newTask.innerHTML = taskDescription
    newTask.classList.add("show-tasks")
    taskContainer.appendChild(newTask)
}

// Check if task is empty

function checkIfTaskIsEmpty() {
    const taskDescription = document.querySelector(".task-description").value
    if (taskDescription === "") {
        swal({
            title: "Oops!",
            text: "You need to enter a task description!",
            icon: "error",
        })
    } else {
        addTask()
    }
}