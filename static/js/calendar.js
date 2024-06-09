
const state = {
    today: new Date(),
    todayYear: 2024,
    todayMonth: new Date().getMonth(),
    todayDate: new Date().getDate()
};

const monthsStr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const daysStr = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
const monthsIndex = { "Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "May": 4, "Jun": 5, "Jul": 6, "Aug": 7, "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11 };
const daysIndex = { "Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6 };

function analyizYear(year) {
    const currentYear = { year, is_leap: false, months: {} };
    for (let month in monthsStr) {
        currentYear.months[monthsStr[month]] = analyizMonth(monthsStr[month], year);
    }
    if (currentYear.months["Feb"].days_length === 29) {
        currentYear.is_leap = true;
    }
    return currentYear;
}

function analyizMonth(month, year) {
    const monthObj = {
        year,
        month,
        month_idx: monthsIndex[month],
        first_day: "",
        first_day_index: null,
        days_length: 0,
        last_day: "",
        last_day_index: null
    };

    const testDays = new Date(year, monthsIndex[month] + 1, 0).getDate();
    for (let day = 1; day <= testDays; day++) {
        const date = new Date(year, monthsIndex[month], day);
        const dayStr = daysStr[date.getDay()];
        if (day === 1) {
            monthObj.first_day = dayStr;
            monthObj.first_day_index = daysIndex[dayStr];
        }
        monthObj.days_length = day;
        monthObj.last_day = dayStr;
        monthObj.last_day_index = daysIndex[dayStr];
    }
    return monthObj;
}

function makePrevMonthArr(firstDayIndex) {
    const prevMonthIdx = state.todayMonth === 0 ? 11 : state.todayMonth - 1;
    const prevMonthDays = analyizMonth(monthsStr[prevMonthIdx], state.todayYear).days_length;
    return Array.from({ length: firstDayIndex }, (_, i) => prevMonthDays - firstDayIndex + i + 1);
}

function calcMonthCalendar() {
    const currentMonth = analyizMonth(monthsStr[state.todayMonth], state.todayYear);
    const currMonth = Array.from({ length: currentMonth.days_length }, (_, i) => i + 1);
    const prevMonthArr = makePrevMonthArr(currentMonth.first_day_index);
    const nextMonthArr = Array.from({ length: 42 - (currMonth.length + prevMonthArr.length) }, (_, i) => i + 1);
    return [...prevMonthArr, ...currMonth, ...nextMonthArr];
}

function printMonthCalendarInDOM() {
    const monthArr = calcMonthCalendar();
    const weeks = [];
    while (monthArr.length) {
        weeks.push(monthArr.splice(0, 7));
    }

    const calendarBody = document.getElementById("calendar-body");
    calendarBody.innerHTML = "";
    const currentMonth = analyizMonth(monthsStr[state.todayMonth], state.todayYear);
    weeks.forEach(week => {
        const row = document.createElement("tr");
        week.forEach(day => {
            const cell = document.createElement("td");
            cell.innerText = day;
            if (day === state.todayDate && state.todayMonth === state.today.getMonth() && state.todayYear === state.today.getFullYear()) {
                cell.classList.add("today");
            }
            row.appendChild(cell);
        });
        calendarBody.appendChild(row);
    });

    document.getElementById("calendar-month-year").innerText = `${monthsStr[state.todayMonth]} ${state.todayYear}`;
}

function nextMonth() {
    state.todayMonth += 1;
    if (state.todayMonth === 12) {
        state.todayYear += 1;
        state.todayMonth = 0;
    }
    printMonthCalendarInDOM();
}

function prevMonth() {
    state.todayMonth -= 1;
    if (state.todayMonth < 0) {
        state.todayYear -= 1;
        state.todayMonth = 11;
    }
    printMonthCalendarInDOM();
}

document.getElementById("next-month").addEventListener("click", nextMonth);
document.getElementById("prev-month").addEventListener("click", prevMonth);

printMonthCalendarInDOM();


