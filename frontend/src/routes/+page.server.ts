export const actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const answers = formData.get('answers')?.toString() || '';

		// const res = await fetch('https://pillhealth-1.onrender.com/api/time');
		// const hi = await res.json();
		// console.log(hi);

		// const response = await fetch('https://stress-predictor-180.vercel.com/api/point', {
		// 	method: 'POST',
		// 	headers: {
		// 		'Content-Type': 'application/json'
		// 	},
		// 	body: JSON.stringify(answers)
		// });
		// const contents = await response.json();

		return { verdict: Math.random() < 0.5 ? 1 : 0 };
		// return { verdict: Number(contents.verdict) };
	}
};
