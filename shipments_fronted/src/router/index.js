import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Shipments from '../components/Shipments.vue'
import ShipmentEdit from "@/components/ShipmentEdit"
import ShipmentAdd from "@/components/ShipmentAdd"

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/shipments',
        name: 'shipments',
        component: Shipments
    },
    {
        path: '/shipment/:id',
        name: 'shipmentEdit',
        component: ShipmentEdit
    },
    {
        path: '/shipment/add',
        name: 'shipmentAdd',
        component: ShipmentAdd
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
