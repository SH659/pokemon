import {IPokemon, IUserPokemon, IUserProfile} from '@/interfaces';
import { MainState, AppNotification } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';
import Main from "@/views/main/Main.vue";


export const mutations = {
    setToken(state: MainState, payload: string) {
        state.token = payload;
    },
    setLoggedIn(state: MainState, payload: boolean) {
        state.isLoggedIn = payload;
    },
    setLogInError(state: MainState, payload: boolean) {
        state.logInError = payload;
    },
    setUserProfile(state: MainState, payload: IUserProfile) {
        state.userProfile = payload;
    },
    setDashboardMiniDrawer(state: MainState, payload: boolean) {
        state.dashboardMiniDrawer = payload;
    },
    setDashboardShowDrawer(state: MainState, payload: boolean) {
        state.dashboardShowDrawer = payload;
    },
    addNotification(state: MainState, payload: AppNotification) {
        state.notifications.push(payload);
    },
    removeNotification(state: MainState, payload: AppNotification) {
        state.notifications = state.notifications.filter((notification) => notification !== payload);
    },
    addPokemon(state: MainState, payload: IPokemon){
        state.pokemons.push(payload)
    },
    setPokemons(state: MainState, payload: IPokemon[]) {
        state.pokemons = Array.from(payload);
    },
    removePokemon(state: MainState, payload: IPokemon){
        state.pokemons = state.pokemons.filter((pokemon) => pokemon !== payload);
    },
    addUserPokemon(state: MainState, payload: IUserPokemon){
        state.userPokemons.push(payload)
    },
    setUserPokemons(state: MainState, payload: IUserPokemon[]) {
        state.userPokemons = Array.from(payload);
    },
    removeUserPokemon(state: MainState, payload: IUserPokemon){
        state.userPokemons = state.userPokemons.filter((pokemon) => pokemon !== payload);
    },
    removeUserPokemonById(state: MainState, payload: {userPokemonId: string}){
        state.userPokemons = state.userPokemons.filter((pokemon) => pokemon.id !== payload.userPokemonId);
    }
};

const {commit} = getStoreAccessors<MainState | any, State>('');

export const commitSetDashboardMiniDrawer = commit(mutations.setDashboardMiniDrawer);
export const commitSetDashboardShowDrawer = commit(mutations.setDashboardShowDrawer);
export const commitSetLoggedIn = commit(mutations.setLoggedIn);
export const commitSetLogInError = commit(mutations.setLogInError);
export const commitSetToken = commit(mutations.setToken);
export const commitSetUserProfile = commit(mutations.setUserProfile);
export const commitAddNotification = commit(mutations.addNotification);
export const commitRemoveNotification = commit(mutations.removeNotification);

export const commitAddPokemon = commit(mutations.addPokemon);
export const commitSetPokemons = commit(mutations.setPokemons);
export const commitRemovePokemon = commit(mutations.removePokemon);

export const commitAddUserPokemon = commit(mutations.addUserPokemon);
export const commitSetUserPokemons = commit(mutations.setUserPokemons);
export const commitRemoveUserPokemon = commit(mutations.removeUserPokemon);
export const commitRemoveUserPokemonById = commit(mutations.removeUserPokemonById);
