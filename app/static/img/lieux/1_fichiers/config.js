window.orejimeConfig = {
	appElement: '#page',
	implicitConsent: true,
	lang: 'fr',
	translations: {
		'fr': {
			purposes: {
				analytics: 'mesure de l\'audience'
			},
			'google-analytics': {
				description: 'statistiques de visites'
			},
			consentModal: {
				description: 'Ici, vous pouvez voir et personnaliser les informations que nous collectons.'
			}
		},
	},
	apps : [
		{
			name : 'google-analytics',
			title : 'Google Analytics',
			purposes : ['analytics'],
			optOut : false,
			cookies: [
				'_ga',
				'_gat',
				'_gid',
				'__utma',
				'__utmb',
				'__utmc',
				'__utmt',
				'__utmz'
			]
		}
	]
};
