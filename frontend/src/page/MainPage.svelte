<script lang="ts">
    import type {Files} from "filedrop-svelte";
    import FileDrop, {FileDropOptions} from "filedrop-svelte";
    import AnimationBackground from "../component/AnimationBackground.svelte";
    import FileCard from "../component/FileCard.svelte";
    import Loader from "../component/Loader.svelte";
    import InputField from "../component/InputField.svelte";

    const opts: FileDropOptions = {
        accept: ".csv",
        multiple: false
    }
    const productName = 'ВзлетИИ'

    let regressionCol: string;
    let files: Files;
    let loading: boolean = false;

    const handleFilesSelect = (e) => {
        files = e.detail.files;
    }

    const submit = () => {
        if (!files) return;
        if (files.accepted.length === 0) return;

        loading = true;
        const data = new FormData();
        data.append('file', files.accepted[0])
        data.append('regression_column_name', regressionCol)

        fetch('/api/v1/upload/', {
            method: 'POST',
            body: data,
        }).then((response) => {
            return response.json()
        }).then((json) => {
            fetch(`/api/v1/download?file_name=${json.filename}`)
                .then(res => res.blob())
                .then(blob => {
                    let link = document.createElement('a');
                    link.download = json.filename;
                    link.href = URL.createObjectURL(blob);
                    link.click();
                    URL.revokeObjectURL(link.href);
                    link.remove();

                    files = undefined;
                    loading = false;
                });
        });
    }

</script>

<svelte:head>
    <title>{productName}</title>
</svelte:head>
<Loader bind:loading/>
<AnimationBackground>
    <main id="app">
        <div class="content">
            <div class="form">
                <div class="form-container">
                    <div class="form-title">
                        <h1>{productName}</h1>
                    </div>
                    <div class="form-content">
                        <InputField
                                bind:value={regressionCol}
                                label="Название колонки"
                                info="Название колонки для регрессии"
                        />
                        <h4>Загрузите датасет</h4>
                        <FileDrop {...opts} on:filedrop={handleFilesSelect}/>
                        {#if files}
                            <div class="uploaded-files">
                                {#each files.accepted as file}
                                    <FileCard {file}/>
                                {/each}
                            </div>
                        {/if}
                    </div>
                    <div class="form-footer">
                        <button on:click={submit}>Отправить</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</AnimationBackground>

<style>

    #app {
        width: 100%;
        height: 100%;
    }

    .content {
        width: 100%;
        height: 100%;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .form {
        width: max(30vw, 400px);
        min-height: 320px;
        max-height: 80vh;

        margin: 0 1rem;

        background: white;
        padding: 1rem;
        box-sizing: border-box;

        border-radius: 1rem;
    }

    .form-container {
        display: flex;
        flex-direction: column;

        justify-content: space-between;

        height: 100%;
    }

    .form-title {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .form-content {
        flex: 1;
    }

    .form-content h4 {
        margin-left: .25rem;
        margin-bottom: -.5rem;
    }

    .uploaded-files {
        width: 100%;
        max-height: 30vh;

        overflow-y: scroll;
        border-radius: 10px;
    }

    .uploaded-files::-webkit-scrollbar {
        width: .5rem;
    }

    .uploaded-files::-webkit-scrollbar-track {
        background: inherit; /* цвет дорожки */
    }

    .uploaded-files::-webkit-scrollbar-thumb {
        background-color: silver; /* цвет плашки */
        border-radius: 20px; /* закругления плашки */
        border: 1px solid silver; /* padding вокруг плашки */
    }

    .form-footer {
        margin-top: .5rem;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .form-footer button {
        height: 40px;
        width: 40%;

        border: 1px solid dodgerblue;
        border-radius: 10px;
        background: #0f62fe;

        font-size: .875rem;
        font-weight: 400;
        line-height: 1.28572;
        letter-spacing: 0;

        color: #ffffff;
    }

    .form-footer button:hover {
        border: 1px solid #0353e9;
        background: #0353e9;
    }

    .form-footer button:active {
        border: 1px solid #002d9c;
        background: #002d9c;
    }

</style>