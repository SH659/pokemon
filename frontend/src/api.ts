import axios from 'axios';
import { apiUrl } from '@/env';
import {IUserProfile, IUserProfileUpdate, IUserProfileCreate, IPokemon, IUserPokemon} from './interfaces';

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  async updateMe(token: string, data: IUserProfileUpdate) {
    return axios.put<IUserProfile>(`${apiUrl}/api/v1/users/me`, data, authHeaders(token));
  },
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/users/`, authHeaders(token));
  },
  async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.put(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
  async createUserOpen(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/open`, data, authHeaders(token));
  },
  async passwordRecovery(email: string) {
    return axios.post(`${apiUrl}/api/v1/password-recovery/${email}`);
  },
  async resetPassword(password: string, token: string) {
    return axios.post(`${apiUrl}/api/v1/reset-password/`, {
      new_password: password,
      token,
    });
  },
  async getPokemons(skip: number, limit: number) {
    return axios.get<Iterable<IPokemon>>(`${apiUrl}/api/v1/pokemons/?skip=${skip}&limit=${limit}`);
  },
  async getPokemonById(id: number) {
    return axios.get<IPokemon>(`${apiUrl}/api/v1/pokemons/${id}`);
  },
  async getUserPokemons(userId: number) {
    return axios.get<Iterable<IUserPokemon>>(`${apiUrl}/api/v1/user_pokemons/user/${userId}`);
  },
  async getUserPokemon(userPokemonId: string) {
    return axios.get<IUserPokemon>(`${apiUrl}/api/v1/user_pokemons/${userPokemonId}`);
  },
  async createUserPokemon(token: string, payload: {user: number, pokemon: number}) {
    return axios.post<IUserPokemon>(`${apiUrl}/api/v1/user_pokemons/`, payload, authHeaders(token));
  },
  async deleteUserPokemon(token: string, id: string)
  {
    return axios.delete(`${apiUrl}/api/v1/user_pokemons/${id}`, authHeaders(token))
  }
};
