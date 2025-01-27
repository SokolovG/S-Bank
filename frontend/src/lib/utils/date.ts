import type { ISODateString } from "$lib/types/events";

export function formatEventDate(dateString: ISODateString) {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('ru-RU', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(date);
}