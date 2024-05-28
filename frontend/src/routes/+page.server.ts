export const actions = {
    default: async ({ request }) => {
        const formData = await request.formData();
        const answers = formData.get('answers')?.toString() || '';

        console.log('answers', answers);

        return;
    },
};