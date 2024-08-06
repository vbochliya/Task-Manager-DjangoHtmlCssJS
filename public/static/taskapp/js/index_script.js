

if (a_for_highlighting){
    var element=document.querySelector('#'+a_for_highlighting)
        element.style.backgroundColor = '#6f6f6f';
}

function confirm_action(event, action) {
    const confirmMessage = action === 'complete' ? "Are you sure you want to mark this task as complete?" : "Are you sure you want to delete this task?";
    
    if (!confirm(confirmMessage)) {
        event.preventDefault(); 
    }
}


function new_task(){
    document.querySelector('.add_tasks').style.display = 'flex';
}
function hide_new_task(){
    document.querySelector('.add_tasks').style.display = 'none';
}    

function side_menu_on() {
    document.getElementById("side-menu").style.display='flex';
    }
  function side_menu_off(){
    document.getElementById("side-menu").style.display='none';
  }
  