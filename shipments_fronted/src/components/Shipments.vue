<template>
  <v-row justify="center">
    <v-col align-self="center" class="center-block" cols="col-6" md="4">
      <v-card v-if="shipments.length">
        <v-list v-for="(shipment, i) in shipments" two-line>
          <v-list-item-title v-html="shipment.title"></v-list-item-title>
          <v-list-item-subtitle v-html="shipment.description"></v-list-item-subtitle>
          <router-link :to="{ name: 'shipmentEdit', params: { id:shipment.id }}">
            <v-tooltip location="bottom">
              <template v-slot:activator="{ props }">
                <v-btn color="grey-lighten-1" icon="mdi-pencil" variant="text" v-bind="props"></v-btn>
              </template>
              <span>Edit</span>
            </v-tooltip>
          </router-link>
          |
          <router-link :to="{ name: 'shipmentDetail', params: { id:shipment.id }}">
            <v-tooltip location="bottom">
              <template v-slot:activator="{ props }">
                <v-btn color="grey-lighten-1" icon="mdi-information" variant="text" v-bind="props"></v-btn>
              </template>
              <span>Info</span>
            </v-tooltip>
          </router-link>
          |
          <v-tooltip location="bottom">
            <template v-slot:activator="{ props }">
              <v-btn @click="deleteShipment(shipment)" color="grey-lighten-1" icon="mdi-delete" v-bind="props"
                     variant="text"></v-btn>
            </template>
            <span>Delete</span>
          </v-tooltip>
          <v-divider inset></v-divider>
        </v-list>
      </v-card>
      <v-card v-else>
        No shipments
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from "axios";
import {notify} from "@kyvg/vue3-notification";


export default {
  name: "Shipments",
  data() {
    return {
      shipments: [],
      title: '',
      description: '',
      dialog: false,
    }
  },

  methods: {
    async getData() {
      try {
        const response = await axios.get('/api/v1/shipments/');
        // set the data returned as shipments
        this.shipments = response.data;
      } catch (error) {
        notify({
          type: "error",
          title: "Problem with get list, try later !",
        });
      }
    },
    deleteShipment: async function (shipment) {

      let confirmation = confirm("Do you want to delete this shipment?");

      if (confirmation) {
        try {
          // Send a request to delete the shipment
          await axios.delete(`/api/v1/shipments/${shipment.id}/`);
          this.getData();
        } catch (error) {
          notify({
            type: "error",
            title: "Problem with delete, try later !",
          });
        }
      }
    }
  },
  created() {
    this.getData();
  }
}
</script>

<style>


</style>