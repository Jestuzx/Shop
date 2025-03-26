const themeToggleSwitch = document.getElementById('theme-toggle')
const body = document.body

// Проверяем, сохранена ли предыдущая тема в localStorage
if (localStorage.getItem('theme') === 'dark') {
	body.classList.add('dark-theme')
	themeToggleSwitch.checked = true // Включаем переключатель, если тема темная
}

// Обработчик для переключения темы
themeToggleSwitch.addEventListener('change', () => {
	body.classList.toggle('dark-theme')

	// Сохраняем выбор в localStorage, чтобы тема сохранялась при перезагрузке страницы
	if (body.classList.contains('dark-theme')) {
		localStorage.setItem('theme', 'dark')
	} else {
		localStorage.setItem('theme', 'light')
	}
})
