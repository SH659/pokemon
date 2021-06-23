<template xmlns="http://www.w3.org/1999/html">
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Pokedex</div>
      </v-card-title>
      <div>blah-blah..!</div>

<!--      <ul>-->
<!--        <li v-for="pokemon in stringArray()">-->
<!--          {{pokemon}}-->
<!--          {{ pokemon.name }}-->
<!--        </li>-->
<!--      </ul>-->

<!--      <ol>-->
<!--        <li v-for="pokemon in stringArray">-->
<!--          {{pokemon}}-->
<!--          {{ pokemon.name }}-->
<!--        </li>-->
<!--      </ol>-->

      <v-data-table :items="pokemons">
        <template slot="items" slot-scope="props">
          <td>{{ props.item.name }}</td>
          <td>{{ props.item.picture_url }}</td>
        </template>
      </v-data-table>

<!--      <div class="col-lg-2" v-for="pokemon in getPokemons(0, 100)">-->
<!--        <div>-->
<!--          pokemon: <b>{{pokemon.name}}</b>-->
<!--          <br/>-->
<!--          {{pokemon.picture_url}}-->
<!--        </div>-->
<!--        <img :src="getPokemonById(pokemon['picture_url'])" v-bind:alt="getPokemonById(pokemon['name'])">-->
<!--      </div>-->
    </v-card>
  </v-container>
</template>


<script lang="ts">
import {api} from "@/api";
import { Component, Vue } from 'vue-property-decorator';
import {IPokemon} from "@/interfaces";
import {readPokemons} from "@/store/main/getters";

@Component
export default class UserPokemon extends Vue {
    public pokemons() {
      return readPokemons(this.$store)
    }
    // public async getPokemonById(id) {
    //   return await api.getPokemonById(id);
    // }
}

</script>

<style scoped>

</style>