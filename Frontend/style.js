console.log("Distributed Task System Running");

const tasks = [
    "Distributed Systems Task",
    "Microservices Project",
    "Failure Isolation Demo"
];

const taskList = document.getElementById("taskList");

tasks.forEach(task => {
    const li = document.createElement("li");
    li.textContent = task;
    taskList.appendChild(li);
});
