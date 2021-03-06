export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserOpenProfileCreate {
    email: string;
    full_name: string;
    password: string;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IPokemon {
    id: number
    name: string
    picture_url: string
}

export interface IUserPokemon {
    id: string
    user: number
    pokemon: number
}


export interface IUserFullPokemon {
    id: string
    user: number
    pokemon: IPokemon
}

