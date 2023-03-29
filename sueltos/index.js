const year = 2022;
const holidays = ['01/06', '04/01', '12/25'];

function countHours(year, holidays) {
    let hours = 0;

    holidays.map(holiday => {
        holiday = holiday.split("/");
        const month = holiday[0] - 1;
        const day = holiday[1];
        const date = new Date(year, month, day);

        const dayOfWeek = date.getDay();
        if(dayOfWeek > 0 && dayOfWeek < 6) {
            hours += 2;
        }
    })

    return hours;
}

const extraHours = countHours(year, holidays);
console.log(extraHours)