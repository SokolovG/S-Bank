export interface Location {
    name: string;
    address?: string;
    city: string;
    country: string;
    createdAt: string
}

export interface Category {
    id: number;
    name: string;
    slug: string;
    description?: string;
    createdAt: string;
}

export interface Organizer {
    id: number;
    createdAt: string;
    name: string;
    description: string;
    website: string;
    contact: string;
    verified: string;
    numberOfEvents: number;
    rating: string;
}

export interface Event {
    id: number;
    name: string
    description: string
    location: Location;
    category: Category;
    organizer: Organizer;
    isPublished: boolean;
    isOnline: boolean;
    isVerify: boolean;
    pubDate: string;
    eventStartDate: string;
    eventEndDate: string;
    registrationDeadline: string;
    format: string
    status: string
    meetingLink: string;
    timezone: string
    maxParticipants: number;
    price: number
    members: number;
    currency: string
    max_participants: number
    current_participants: number

}

export type ISODateString = string;