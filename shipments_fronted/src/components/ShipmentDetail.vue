<template>
  <v-row>
    <v-col justify="left" align="left" class="fill-height">
      <v-card class="mx-auto" max-width="344" tonal v-for="shipment in shipments" :key="shipment.id">
        <v-toolbar dense color="#42b983">
          <v-toolbar-title>#{{shipment.id}} Details:</v-toolbar-title>
        </v-toolbar>
        <v-text-field v-model="shipment.title" label="Title" readonly hide-details="auto"
        ></v-text-field>
        <v-text-field v-model="shipment.description" label="Description" readonly hide-details="auto"
        ></v-text-field>
        <v-text-field hide-details="auto" v-model="shipment.status" label="Status" readonly
        ></v-text-field>
        <v-textarea v-model="shipment.delivery_address" label="Delivery address" readonly hide-details="auto" auto-grow
                    outlined
        ></v-textarea>
        <v-textarea v-model="shipment.pickup_address" label="Pickup address" readonly hide-details="auto" auto-grow
                    outlined
        ></v-textarea>
        <v-card-text>
          <v-timeline align-top dense>
            <v-timeline-item v-for="shipment in shipments">
              <div>
                <div class="font-weight-normal">
                  <v-col>
                    <strong>{{ shipment.created_at }}</strong>
                  </v-col>
                </div>
              </div>
            </v-timeline-item>
          </v-timeline>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

import axios from "axios";
import {notify} from "@kyvg/vue3-notification";


export default {
  name: "ShipmentDetail",
  data() {
    return {
      shipments: [],
    }
  },
  methods: {
    async getData() {
      try {
        // fetch shipment
        const response = await axios.get(
            '/api/v1/shipments/' + parseInt(this.$route.params.id) + '/'
        )
        response.data.created_at = new Date(response.data.created_at).toUTCString();
        this.shipments = [response.data];
      } catch (error) {
        notify({
          type: "error",
          title: "Problem with get details!",
        });

      }
    },
  },
  created() {
    // Fetch shipment on page load
    this.getData();
  }
}
</script>

<style>
</style>