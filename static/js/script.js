

const toggleButton = document.getElementById('toggle-button');
const projectMembers = document.getElementById('project-members');

toggleButton.addEventListener('click', () => {
    projectMembers.classList.toggle('hidden');
});


function updateTime() {
    const timeElement = document.getElementById('time');
    const now = new Date();
    let hours = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();
    const ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12 || 12;  // Convert to 12-hour format
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    const currentTime = `${hours}:${minutes}:${seconds} ${ampm}`;
    timeElement.textContent = currentTime;
  }

  // Update time every second
  setInterval(updateTime, 1000);

  // Initial call to display time immediately
  updateTime();



  function updateTimeAndGreeting() {
    const now = new Date();

    // Update the time
    const options = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };
    const timeString = now.toLocaleTimeString('en-US', options);
    document.getElementById('time').textContent = timeString;

    // Update the greeting
    const hours = now.getHours();
    let greeting = 'Good Evening, Saurav!!'; // Default greeting

    if (hours < 12) {
      greeting = 'Good Morning, Saurav!!';
    } else if (hours < 18) {
      greeting = 'Good Afternoon, Saurav!!';
    }

    document.getElementById('greeting').textContent = greeting;

    // Update the date
    const dateString = now.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
    document.getElementById('date').textContent = `It's ${dateString}`;
  }

  // Call updateTimeAndGreeting every second
  setInterval(updateTimeAndGreeting, 1000);


  // Get the current date
  const today = new Date();
  const currentMonth = today.getMonth();
  const currentYear = today.getFullYear();
  const firstDay = new Date(currentYear, currentMonth, 1);
  const lastDay = new Date(currentYear, currentMonth + 1, 0);
  const totalDays = lastDay.getDate();
  const firstWeekday = firstDay.getDay();

  // Function to generate the calendar
  function generateCalendar() {
    const calendarElement = document.querySelector('.calendar');
    
    // Empty the calendar
    calendarElement.innerHTML = '';

    // Create day headers
    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    days.forEach(day => {
      const dayElement = document.createElement('div');
      dayElement.className = 'day font-semibold';
      dayElement.textContent = day;
      calendarElement.appendChild(dayElement);
    });

    // Add empty days before the first day of the month
    for (let i = 0; i < firstWeekday; i++) {
      const emptyElement = document.createElement('div');
      emptyElement.className = 'day';
      calendarElement.appendChild(emptyElement);
    }

    // Create calendar days
    for (let i = 1; i <= totalDays; i++) {
      const dayElement = document.createElement('div');
      dayElement.className = 'day' + (i === today.getDate() ? ' today' : '');
      dayElement.textContent = i;

      // Add events (example)
      if (i === 5) {
        const eventElement = document.createElement('div');
        eventElement.className = 'event';
        eventElement.textContent = 'Holiday';
        dayElement.appendChild(eventElement);
      } else if (i === 12) {
        const eventElement = document.createElement('div');
        eventElement.className = 'event';
        eventElement.textContent = 'Meeting';
        dayElement.appendChild(eventElement);
      } else if (i === 19) {
        const eventElement = document.createElement('div');
        eventElement.className = 'event';
        eventElement.textContent = 'Funny Friday';
        dayElement.appendChild(eventElement);
      }

      calendarElement.appendChild(dayElement);
    }
  }

  generateCalendar(); // Generate the calendar on page load


  function toggleDescription(button) {
    const description = button.previousElementSibling;
    if (button.textContent === 'Read More') {
      description.classList.remove('line-clamp-3');
      description.classList.add('line-clamp-none');
      button.textContent = 'Show Less';
    } else {
      description.classList.add('line-clamp-3');
      description.classList.remove('line-clamp-none');
      button.textContent = 'Read More';
    }
  }


  let tasks = []; // Array to store tasks

  function toggleDropdown() {
    const dropdownMenu = document.getElementById('dropdown-menu');
    dropdownMenu.classList.toggle('hidden');
  }

  function addTask(event) {
    event.preventDefault(); // Prevent form submission

    // Get input values
    const taskName = document.getElementById('taskName').value;
    const taskDuration = document.getElementById('taskDuration').value;
    const budget = document.getElementById('budget').value;
    const projectDescription = document.getElementById('projectDescription').value;

    // Create a new task object
    const newTask = {
      name: taskName,
      duration: taskDuration,
      budget: budget,
      description: projectDescription,
    };

    // Add the new task to the tasks array
    tasks.push(newTask);

    // Clear the input fields
    document.getElementById('taskName').value = '';
    document.getElementById('taskDuration').value = '';
    document.getElementById('budget').value = '';
    document.getElementById('projectDescription').value = '';

    // Render the tasks
    renderTasks();
  }

  function renderTasks() {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = ''; // Clear the current task list

    tasks.forEach((task) => {
      const taskCard = document.createElement('div');
      taskCard.className = 'bg-white shadow-md rounded p-4 mb-4';
      taskCard.innerHTML = `
        <h2 class="text-xl font-semibold">${task.name}</h2>
        <p class="text-gray-600">Duration: ${task.duration}</p>
        <p class="text-gray-600">Budget: $${task.budget}</p>
        <p class="text-gray-600">Description: ${task.description}</p>
      `;
      taskList.appendChild(taskCard);
    });
  }


  function previewImage(event) {
    const imagePreview = document.getElementById('image-preview');
    imagePreview.src = URL.createObjectURL(event.target.files[0]);
    imagePreview.style.display = 'block';
  }



      // Pie chart data
      const ctx = document.getElementById('taskCompletionChart').getContext('2d');
      const taskCompletionChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['Completed', 'In Progress', 'Overdue'],
          datasets: [{
            data: [40, 35, 25],
            backgroundColor: ['#48bb78', '#f6ad55', '#f56565'],
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false, // Allow the chart to resize
        }
      });


      