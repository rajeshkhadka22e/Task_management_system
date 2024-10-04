const toggleButton = document.getElementById('toggle-button');
const projectMembers = document.getElementById('project-members');

toggleButton.addEventListener('click', () => {
    projectMembers.classList.toggle('hidden');
});