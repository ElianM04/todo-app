function deleteTask(taskId) {
    fetch("/delete-task", {
      method: "POST",
      body: JSON.stringify({ taskId: taskId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
  function UpdateTask(taskId){
    fetch("/update-task", {
        method: "POST",
        body: JSON.stringify({ taskId: taskId }),
      }).then((_res) => {
        window.location.href = "/";
      });
    }
    

   