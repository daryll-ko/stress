export const actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const answers = formData.get('answers')?.toString() || '';

		console.log(answers);

		try {
			// https://stress-predictor-180.vercel.com/api/point
			const response = await fetch('http://127.0.0.1:5000/api/point', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(answers)
			});
			const contents = await response.json();
			return { verdict: Number(contents.verdict) };
		} catch {
			return { verdict: Math.random() < 0.5 ? 1 : 0 };
		}
	}
};
