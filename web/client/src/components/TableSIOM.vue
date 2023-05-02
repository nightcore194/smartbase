<template>
    <div class="h-full w-full m-1" :style="{ 'background-color': color, 'marginRight': '10 px', 'border': 'solid rgb(122, 122, 122) 1px', 'border-radius': '10px' }">
        <DataTable :value="products"  tableStyle="min-width: 50rem" scrollHeight="500px">
            <Column field="id" header="№ СИОМ" header-style="background: #aecfff" sortable="true"></Column>
            <Column field="price" header="Date" header-style="background: #aecfff"></Column>
        </DataTable>
    </div>

</template>
  
<script  lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    setup() {
        return {
            products: [
                {
                    id: '1000',
                    code: 'f230fh0g3',
                    name: 'Bamboo Watch',
                    description: 'Product Description',
                    image: 'bamboo-watch.jpg',
                    price: 65,
                    category: 'Accessories',
                    quantity: 24,
                    inventoryStatus: 'INSTOCK',
                    rating: 5
                },
                {
                    id: '1000',
                    code: 'f230fh0g3',
                    name: 'Bamboo Watch',
                    description: 'Product Description',
                    image: 'bamboo-watch.jpg',
                    price: 65,
                    category: 'Accessories',
                    quantity: 24,
                    inventoryStatus: 'INSTOCK',
                    rating: 5
                },
                {
                    id: '1000',
                    code: 'f230fh0g3',
                    name: 'Bamboo Watch',
                    description: 'Product Description',
                    image: 'bamboo-watch.jpg',
                    price: 65,
                    category: 'Accessories',
                    quantity: 24,
                    inventoryStatus: 'INSTOCK',
                    rating: 5
                },
                {
                    id: '2000',
                    code: 'f230fh0g3',
                    name: 'Bamboo Watch',
                    description: 'Product Description',
                    image: 'bamboo-watch.jpg',
                    price: 65,
                    category: 'Accessories',
                    quantity: 24,
                    inventoryStatus: 'INSTOCK',
                    rating: 5
                },
            ]
        }
    },
    props: {
        color: String
    },
    mounted() {

    }
})
</script>
  
<style scoped>
.green {
    background-color: green;
}
</style>
  