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
    <v-footer app>
      <footer>
        &copy;
      </footer>
    </v-footer>
  </v-app>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-align: center;
  color: #203142;
  max-width: 50rem;
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
