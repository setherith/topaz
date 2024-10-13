<script>
    import QuestionRadioInput from "./QuestionRadioInput.svelte";
    
    export let name;
    export let question;
</script>

<div class="form-input my-5">
    <label class="label">
        <span>{question.title}</span>
        <div class="space-y-2">
            {#each question.responses as response}
                <QuestionRadioInput 
                    name="{name}-{question.title}"
                    value={response.score}
                    description={response.description} />
            {/each}
        </div>
        <input type="hidden" />
    </label>
</div>