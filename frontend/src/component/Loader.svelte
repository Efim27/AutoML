<script lang="ts">
    import {Circle2} from 'svelte-loading-spinners'

    export let loading: boolean = false;

</script>

{#if loading}
    <div class="background">
        <Circle2 size="5" unit="rem"/>
    </div>
{/if}

<style>

    .background {
        z-index: 999;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;

        background: rgba(0, 0, 0, 0.15);

        display: flex;
        justify-content: center;
        align-items: center;
    }

</style>