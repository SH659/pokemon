<template xmlns="http://www.w3.org/1999/html">
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Selected Pokemons</div>
      </v-card-title>

      <v-data-table :items="selectedPokemons">
        <template slot="items" slot-scope="props">
          <td><img v-bind:src="props.item.picture_url"
                   @error="$event.target.src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdB3JUjeFV1bzYfvTsHoR5UFldN0TX1P-_1S_fpMsjjdAaI_mX_3HYcUeIne8-9tp1vwc&usqp=CAU'"/>
          </td>
          <td><a v-bind:href="props.item.picture_url">{{ props.item.name }}</a></td>
          <td></td>
        </template>
      </v-data-table>

    </v-card>
  </v-container>
</template>


<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {dispatchGetUserPokemons} from "@/store/main/actions";
import {IPokemon, IUserPokemon} from "@/interfaces";
import {api} from "@/api";
import {readToken, readUserPokemons} from "@/store/main/getters";

@Component
export default class UserPokemon extends Vue {
  selectedPokemons: IPokemon[] = []
  userPokemons: IUserPokemon[] = []

  public async mounted() {
    const me = (await api.getMe(readToken(this.$store))).data;
    console.log(me);
    await dispatchGetUserPokemons(this.$store, me.id);
    this.userPokemons = readUserPokemons(this.$store);
    console.log(this.userPokemons);

    for (let i = 0; i < this.userPokemons.length; i++) {
      let userPokemon = this.userPokemons[i];
      console.log(userPokemon);
      let pokemon = (await api.getPokemonById(userPokemon.pokemon)).data;
      console.log(pokemon);
      this.selectedPokemons.push(pokemon);
    }
  }
}

</script>

<style scoped>

</style>