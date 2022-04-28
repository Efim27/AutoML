<script lang="ts">

    export let value: string;
    export let label: string = undefined;
    export let info: string = undefined;
    export let placeholderText: string = ' ';
    export let error: boolean = false;

    const inputId = Date.now().toString(36) + Math.random().toString(36).substring(2);

</script>


<div class="input_container" class:error>

    <input id={inputId} class="input_field" type="text" placeholder={placeholderText} autocomplete="on"
           bind:value>
    {#if label && placeholderText === ' '}
        <label for={inputId} class="input_label">{label}</label>
    {/if}
    <div class="void"></div>
</div>
{#if info}
    <div class="input-info">{info}</div>
{/if}


<style>

    :root {
        --custom-height: 22px;
        --custom-width: 100%;
        --custom-margin: 0;
        --custom-border-color: #dddfe2;
        --own-input-error-color: #f84040;
        --custom-transition-duration: 150ms
    }

    .input_container {
        position: relative;

        background: white;
        max-width: var(--custom-width, 100%);
        max-height: var(--custom-height);
        margin: var(--custom-margin);

        padding: 12px 14px;
        font-size: 17px;
        border: 1px solid var(--custom-border-color);
        border-radius: 6px;

        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .input_container.error {
        color: var(--own-input-error-color);
        border-color: var(--own-input-error-color);
    }

    .input_label {
        position: absolute;

        top: 50%;
        left: 1rem;
        transform: translate(0, -50%);

        cursor: text;

        transition: top var(--custom-transition-duration) ease-in,
        left var(--custom-transition-duration) ease-in,
        font-size var(--custom-transition-duration) ease-in,
        transform var(--custom-transition-duration) ease-in;

        background: inherit;
    }

    .input_field:focus ~ .input_label,
    .input_field:not(:placeholder-shown).input_field:not(:focus) ~ .input_label {
        top: -10%;
        font-size: 1rem;
        left: 0.8rem;
        transform: translate(0px, -30%);
    }

    .input_field ~ .input_label {
        font-size: 1.25rem;
        font-weight: 400;
    }

    .input_field {
        height: 100%;
        flex: 1;
        border: none;

        font-size: 1rem;

        padding: 0;
        margin: 0;
    }

    .input_field:focus {
        outline: none;
    }

    .input-info {
        margin-left: 4px;
        font-size: 12px;
        line-height: 1.4;
        color: rgba(0, 0, 0, .75);
    }


    .void {
        width: 30px;
        height: 30px;
        visibility: hidden;
    }

</style>