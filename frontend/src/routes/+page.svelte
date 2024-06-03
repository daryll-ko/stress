<script lang="ts">
	import { enhance } from '$app/forms';

	interface Question {
		label: string;
		value: number | string;
		options: number[] | string[];
		col: string;
	}

	const two: number[] = [1, 2];
	const five: number[] = [0, 1, 2, 3, 4, 5];
	const ten: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

	let questions: Question[] = [
		{
			label: 'How many fruits or vegetables do you eat every day?',
			value: -1,
			options: five,
			col: 'FRUITS_VEGGIES'
		},
		{ label: 'How many new places do you visit?', value: -1, options: ten, col: 'PLACES_VISITED' },
		{
			label: 'How many people are very close to you?',
			value: -1,
			options: ten,
			col: 'CORE_CIRCLE'
		},
		{
			label: 'How many people do you help achieve a better life?',
			value: -1,
			options: ten,
			col: 'SUPPORTING_OTHERS'
		},
		{
			label: 'With how many people do you interact with during a typical day?',
			value: -1,
			options: ten,
			col: 'SOCIAL_NETWORK'
		},
		{
			label: 'How many remarkable achievements are you proud of?',
			value: -1,
			options: ten,
			col: 'ACHIEVEMENT'
		},
		{
			label: 'How many times do you donate your time or money to good causes?',
			value: -1,
			options: five,
			col: 'DONATION'
		},
		{
			label: 'What is your Body Mass Index (BMI) range?',
			value: -1,
			options: two,
			col: 'BMI_RANGE'
		},
		{
			label: 'How well do you complete your weekly to-do lists?',
			value: -1,
			options: ten,
			col: 'TODO_COMPLETED'
		},
		{
			label: "In a typical day, how many hours do you experience 'flow'?",
			value: -1,
			options: ten,
			col: 'FLOW'
		},
		{
			label: 'How many steps (in thousands) do you typically walk every day?',
			value: -1,
			options: ten,
			col: 'DAILY_STEPS'
		},
		{
			label: 'For how many years ahead is your life vision very clear for?',
			value: -1,
			options: ten,
			col: 'LIVE_VISION'
		},
		{
			label: 'About how long do you typically sleep?',
			value: -1,
			options: ten,
			col: 'SLEEP_HOURS'
		},
		{
			label: 'How many days of vacation do you typically lose every year?',
			value: -1,
			options: ten,
			col: 'LOST_VACATION'
		},
		{
			label: 'How often do you shout or sulk at somebody?',
			value: -1,
			options: five,
			col: 'DAILY_SHOUTING'
		},
		{
			label: 'How sufficient is your income to cover basic life expenses?',
			value: -1,
			options: two,
			col: 'SUFFICIENT_INCOME'
		},
		{
			label: 'How many recognitions have you received in your life?',
			value: -1,
			options: ten,
			col: 'PERSONAL_AWARDS'
		},
		{
			label: 'How many hours do you spend every day doing what you are passionate about?',
			value: -1,
			options: ten,
			col: 'TIME_FOR_PASSION'
		},
		{
			label:
				'In a typical week, how many times do you have the opportunity to think about yourself?',
			value: -1,
			options: ten,
			col: 'WEEKLY_MEDITATION'
		},
		{
			label: 'Age group',
			value: -1,
			options: ['20 or less', '21 to 35', '36 to 50', '51 or more'],
			col: 'AGE'
		},
		{ label: 'Gender', value: -1, options: ['Male', 'Female'], col: 'GENDER' },
		{
			label: 'How is your work-life balance?',
			value: -1,
			options: ten,
			col: 'WORK_LIFE_BALANCE_SCORE'
		}
	].map((question) => ({ ...question, value: question.options[0] }));

	$: answers = questions.map((question) => ({
		col: question.col,
		value: question.value
	}));

	let result: string | null = null;
	export let form;

	function handleSubmit() {
		result = 'Processing...';
		setTimeout(() => {
			result = form?.verdict === 1 ? 'You are stressed...' : 'You are not stressed!';
		}, 1000);
		answers = questions.map((question) => ({
			col: question.col,
			value: question.options[0]
		}));
	}

	const enhanceOptions = ({ formData }) => {
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
	<form
		class="flex flex-col gap-3 items-center"
		on:submit|preventDefault={handleSubmit}
		method="POST"
		use:enhance={enhanceOptions}
	>
		<div class="grid grid-cols-4 gap-3 items-start bg-orange-100 p-3 rounded-lg">
			{#each questions as question, i}
				<div class="question">
					{question.label}
					<select bind:value={answers[i].value} class="input" required>
						{#each question.options as option}
							<option value={option}>{option}</option>
						{/each}
					</select>
				</div>
			{/each}
		</div>
		<button
			type="submit"
			class="bg-orange-100 rounded-md px-3 py-2 border-2 border-solid border-orange-400 hover:bg-orange-400 hover:text-white transition-all"
			>Submit</button
		>
	</form>
</div>
