<script lang="ts">
    import 'filepond/dist/filepond.css';
    import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css';
    import MainPage from "./page/MainPage.svelte";
</script>

<MainPage/>

<style>
    :global(body) {
        margin: 0;
        padding: 0;

        font-weight: 400;
        font-family: IBM Plex Sans, Helvetica Neue, Arial, sans-serif;

        background: #999999;
    }
</style>