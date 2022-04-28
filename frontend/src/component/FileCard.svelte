<script lang="ts">

    export let file: File;

    const getHumanSize = (size: number): string => {
        const types = ['B', 'KB','MB','GB','TB'];
        let str: string;
        for (let i = 0; i < types.length; i++) {
            if (size <= 2 ** ((i + 1) * 10)) {
                str = (size / 2 ** (i * 10)).toFixed(2) + types[i];
                break;
            }
        }
        return str;
    }

</script>

<div class="file_card">
    <div class="content">
        <div class="file-name">{file.name}</div>
        <div class="file-size">{getHumanSize(file.size)}</div>
    </div>
</div>

<style>

    .file_card {
        width: 100%;

        margin-bottom: 4px;
        padding: .5rem;
        box-sizing: border-box;

        border-radius: .5rem;
        background: #e0e0e0;
    }

    .content {
        width: 100%;
        height: 100%;

        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }

</style>