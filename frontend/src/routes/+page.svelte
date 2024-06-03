<script lang="ts">
	import { enhance } from "$app/forms";

    interface Question {
        label: string;
        value: number | string;
        options: number[] | string[];
    }

	const two: number[] = [1, 2];
	const five: number[] = [0, 1, 2, 3, 4, 5];
	const ten: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    let questions: Question[] = [
        { label: "How many fruits or vegetables do you eat every day?", value: -1, options: five },
        { label: "How many new places do you visit?", value: -1, options: ten },
        { label: "How many people are very close to you?", value: -1, options: ten },
        { label: "How many people do you help achieve a better life?", value: -1, options: ten },
        { label: "With how many people do you interact with during a typical day?", value: -1, options: ten },
        { label: "How many remarkable achievements are you proud of?", value: -1, options: ten },
        { label: "How many times do you donate your time or money to good causes?", value: -1, options: five },
        { label: "What is your Body Mass Index (BMI) range?", value: -1, options: two },
        { label: "How well do you complete your weekly to-do lists?", value: -1, options: ten },
        { label: "In a typical day, how many hours do you experience 'flow'?", value: -1, options: ten },
        { label: "How many steps (in thousands) do you typically walk every day?", value: -1, options: ten },
        { label: "For how many years ahead is your life vision very clear for?", value: -1, options: ten },
        { label: "About how long do you typically sleep?", value: -1, options: ten },
        { label: "How many days of vacation do you typically lose every year?", value: -1, options: ten },
        { label: "How often do you shout or sulk at somebody?", value: -1, options: five },
        { label: "How sufficient is your income to cover basic life expenses?", value: -1, options: two },
        { label: "How many recognitions have you received in your life?", value: -1, options: ten },
        { label: "How many hours do you spend every day doing what you are passionate about?", value: -1, options: ten },
        { label: "In a typical week, how many times do you have the opportunity to think about yourself?", value: -1, options: ten },
        { label: "Age group", value: -1, options: ['20 or less', '21 to 35', '36 to 50', '51 or more'] },
        { label: "Gender", value: -1, options: ['Male', 'Female'] }
    ].map(question => ({...question, value: question.options[0]}));
	

    let result: string | null = null;
	export let form;

    function handleSubmit() {
        result = 'Processing...';
        setTimeout(() => {
            result = form?.verdict === 1 ? 'You are stressed...' : 'You are not stressed!';
        }, 1000);
    }

	const enhanceOptions = ({ formData }) => {
		const answers = questions.map(question => ({
			label: question.label,
			value: question.value
		}));
		formData.append('answers', JSON.stringify(answers));
	};
</script>

<h1 class="text-3xl font-bold">&#129760; Stress</h1>
<br />
<div class="flex flex-col items-center gap-3">
    <div
        class="border-2 border-dashed border-orange-200 w-[50%] rounded-md p-3 bg-orange-100/50 text-center"
    >
        {result ? result : 'Result here...'}
    </div>
    <form class="grid grid-cols-2 gap-3 items-start bg-orange-100 p-3 rounded-lg" 
			on:submit|preventDefault={handleSubmit} 
			method="POST" 
			use:enhance = {enhanceOptions}>
        {#each questions as question}
            <div class="question">
                {question.label}
                <select bind:value={question.value} class="input" required>
                    {#each question.options as option}
                        <option value={option}>{option}</option>
                    {/each}
                </select>
            </div>
        {/each}
        <button
            type="submit"
            class="bg-orange-100 rounded-md px-3 py-2 border-2 border-solid border-orange-400 hover:bg-orange-400 hover:text-white transition-all"
        >Submit</button>
    </form>
</div>
