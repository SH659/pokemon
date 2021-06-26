<template xmlns="http://www.w3.org/1999/html">
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Pokedex</div>
      </v-card-title>

      <v-data-table :items="pokemons">
        <template slot="items" slot-scope="props">
          <td><img v-bind:src="props.item.picture_url" @error="$event.target.src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdB3JUjeFV1bzYfvTsHoR5UFldN0TX1P-_1S_fpMsjjdAaI_mX_3HYcUeIne8-9tp1vwc&usqp=CAU'"/></td>
          <td><a v-bind:href="props.item.picture_url">{{ props.item.name }}</a></td>
          <td></td>
        </template>
      </v-data-table>

    </v-card>
  </v-container>
</template>


<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {readPokemons} from "@/store/main/getters";
import {dispatchGetPokemons} from "@/store/main/actions";

@Component
export default class UserPokemon extends Vue {
  public async mounted() {
    return await dispatchGetPokemons(this.$store, {skip: 0, limit: 100});
  }

  get pokemons() {
    return  readPokemons(this.$store);
  }
}

</script>

<style scoped>

</style>