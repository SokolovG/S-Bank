export interface Location {
    name: string;
    adress?: string;
    city: string;
    country: string;
}

export interface Category {
    id: number;
    createdAt: string;
    name: string;
    slug: string;
    description?: string;
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
    location: Location;
    meetingLink: string;
    organizer: Organizer;
    category: Category;
    name: string;
    description: string;
    pubDate: string;
    eventStartDate: string;
    eventEndDate: string;
    isOnline: boolean;
    isVerify: boolean;
    maxParticipants: number;
    registrationDeadline: string;
    format: string;
    members: number;
    photos: string[] | null;
    participants: any[];

}

export interface Comment {
    id: number;
    text: string;
    event: number;
    author: number;
}