<template xmlns="http://www.w3.org/1999/html">
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Selected Pokemons</div>
      </v-card-title>

      <v-data-table :items="pokemons">
        <template slot="items" slot-scope="props">
          <td><img v-bind:src="props.item.pokemon.picture_url"
                   @error="$event.target.src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdB3JUjeFV1bzYfvTsHoR5UFldN0TX1P-_1S_fpMsjjdAaI_mX_3HYcUeIne8-9tp1vwc&usqp=CAU'"/>
          </td>
          <td><a v-bind:href="props.item.picture_url">{{ props.item.pokemon.name }}</a></td>
          <td>
            <v-btn v-on:click="RemovePokemonFromSelectedList(props.item)">Remove</v-btn>
          </td>
        </template>
      </v-data-table>

    </v-card>
  </v-container>
</template>


<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {dispatchDeleteUserPokemon, dispatchGetUserPokemons} from "@/store/main/actions";
import {IPokemon, IUserFullPokemon, IUserPokemon} from "@/interfaces";
import {api} from "@/api";
import {readToken, readUserPokemons} from "@/store/main/getters";

@Component
export default class UserPokemon extends Vue {
  pokemons: IUserFullPokemon[] = []

  public async mounted() {
    const me = (await api.getMe(readToken(this.$store))).data;
    await dispatchGetUserPokemons(this.$store, me.id);
    const userPokemons = readUserPokemons(this.$store);

    for (let i = 0; i < userPokemons.length; i++) {
      let userPokemon = userPokemons[i];
      let pokemon: IPokemon = (await api.getPokemonById(userPokemon.pokemon)).data;
      let fullUserPokemon: IUserFullPokemon = {id: userPokemon.id, user: userPokemon.user, pokemon: pokemon};
      this.pokemons.push(fullUserPokemon);
    }
  }

  public async RemovePokemonFromSelectedList(pokemonPair: IUserFullPokemon) {
    await dispatchDeleteUserPokemon(this.$store, {userPokemonId: pokemonPair.id})
    this.pokemons = this.pokemons.filter((pp) => pp !== pokemonPair)
  }
}

</script>

<style scoped>

</style>