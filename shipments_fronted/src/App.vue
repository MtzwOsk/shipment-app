<template>
  <v-app>
    <notifications/>
    <nav class="app__nav">
      <router-link to="/">Home</router-link>
      |
      <router-link to="/shipments">Shipments</router-link>
      |
      <router-link to="/shipment/add">Add Shipment</router-link>
    </nav>
    <v-container fluid>
      <router-view></router-view>
    </v-container>
    <v-footer app color="#2c3e50">
      <v-row>
        <v-col class="text-center" cols="12">
          {{ new Date().getFullYear() }} — <strong>Shipment</strong>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
