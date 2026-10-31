# Marketing tactics for each (churn risk, customer value) segment, based on the project paper.

MARKETING_STRATEGIES = {
    ("High", "High"): [
        "📨 Personalized Communication: Tailored emails, usage-based recommendations.",
        "🎯 Targeted Incentives: Discounts for switching to longer contracts, free service upgrades.",
        "🎥 Exclusive Streaming Benefits",
        "🚀 Fiber Optic Internet Perks: Free speed upgrades, highlighting benefits for streaming.",
        "📦 Personalized Bundles: Custom bundles, free trials of complementary services.",
        "💳 Payment Method Incentives: Discounts for automatic payments, flexible payment plans.",
        "🎁 Personalized Loyalty Rewards: Points for streaming usage, thank-you gifts.",
        "🔙 Win-Back Offers: Discounts or free months to prevent churn.",
        "📝 Feedback and Co-Creation: Surveys, beta testing rewards."
    ],
    ("Low", "High"): [
        "📨 Automated Communication: Thank-you emails, renewal reminders, service updates",
        "🎁 Low-Cost Incentives: Free month of service, loyalty discounts, exclusive access",
        "💳 Highlight Automatic Payments: Emphasize convenience, offer small rewards for switching",
        "📦 Bundle Services: Custom bundles, free add-ons for renewals",
        "🎥 Exclusive Streaming Benefits",
        "🎉 Celebrate Milestones: Anniversary messages, small gifts for loyalty",
        "📝 Simplify Contract Upgrades: Discounted long-term contracts, free service upgrades",
        "🎮 Gamify Loyalty: Points system, loyalty contests"
    ],
    ("ALL", "High") : [
        "No specific strategies defined for this segment combination, Check Personalized Retention methods for High-risk customers and Cost-conscious Retention methods for Low-risk customers."
    ],
    ("ALL", "Medium"): [
        "📈 Tiered incentives: Discounts for high-risk customers, loyalty rewards for low-risk customers.",
        "🎬 Exclusive Streaming Benefits",
        "📦 Bundle streaming services (e.g., fiber internet + streaming TV + movies) at a discounted rate",
        "💳 Provide payment method incentives (e.g., 'Switch to automatic payments and get a $10 credit!').",
        "🚀 Offer fiber optic perks (e.g., 'Enjoy buffer-free streaming with our fiber optic service!')",
        "🎁 Reward low-risk customers with loyalty points or thank-you gifts (e.g., free movie rentals)",
        "🛡️ Promote underutilized services (e.g., 'Try our online security service—free for 30 days!').",
        "🎮 Launch gamified campaigns (e.g., 'Watch 5 movies this month and earn a free rental!').",
        "📝 Personalize communication (e.g., 'We noticed you love action movies—here’s a list of new releases!')."
    ],

    ("High", "Medium"): [
        "📈 Tiered incentives",
        "🎬 Exclusive Streaming Benefits",
        "📦 Bundle streaming services (e.g., fiber internet + streaming TV + movies) at a discounted rate",
        "💳 Provide payment method incentives (e.g., 'Switch to automatic payments and get a $10 credit!').",
        "🚀 Offer fiber optic perks (e.g., 'Enjoy buffer-free streaming with our fiber optic service!')",
        "🛡️ Promote underutilized services (e.g., 'Try our online security service—free for 30 days!').",
        "🎮 Launch gamified campaigns (e.g., 'Watch 5 movies this month and earn a free rental!').",
    ],
        ("Low", "Medium"): [
        "📈 Tiered incentives",
        "🎬 Exclusive Streaming Benefits",
        "📦 Bundle streaming services (e.g., fiber internet + streaming TV + movies) at a discounted rate",
        "💳 Provide payment method incentives (e.g., 'Switch to automatic payments and get a $10 credit!').",
        "🚀 Offer fiber optic perks (e.g., 'Enjoy buffer-free streaming with our fiber optic service!')",
        "🎁 Reward low-risk customers with loyalty points or thank-you gifts (e.g., free movie rentals)",
        "🛡️ Promote underutilized services (e.g., 'Try our online security service—free for 30 days!').",
        "🎮 Launch gamified campaigns (e.g., 'Watch 5 movies this month and earn a free rental!').",
        "📝 Personalize communication (e.g., 'We noticed you love action movies—here’s a list of new releases!')."
    ],
    ("Low", "Low"): [
        "🏷️ Offer a small discount for retention",
        "📺 Offer a free month of streaming services",
        "👥 Encourage customer engagement with a referral program",
        "👨‍👩‍👧‍👦 Promote family bundle offers",
        "💰 Encourage more frequent payments with a rewards program",
        "📊 Engage with customer satisfaction surveys and promotions",
        "🎯 Engage with a personalized loyalty program"
    ],
    ("High", "Low"): [
        "🏷️ Offer a small discount for retention",
        "📺 Offer a free month of streaming services",
        "👥 Encourage customer engagement with a referral program",
        "👨‍👩‍👧‍👦 Promote family bundle offers",
        "💰 Encourage more frequent payments with a rewards program",
        "📊 Engage with customer satisfaction surveys and promotions",
        "🎯 Engage with a personalized loyalty program"
    ],
    ("ALL", "Low"): [
        "🏷️ Offer a small discount for retention",
        "📺 Offer a free month of streaming services",
        "👥 Encourage customer engagement with a referral program",
        "👨‍👩‍👧‍👦 Promote family bundle offers",
        "💰 Encourage more frequent payments with a rewards program",
        "📊 Engage with customer satisfaction surveys and promotions",
        "🎯 Engage with a personalized loyalty program"
    ],
    ("High", "ALL"): [
        "✨ Offer long-term contract discounts",
        "🎁 Provide onboarding incentives (e.g., free months, upgrades)",
        "🎬 Offer free streaming upgrades for 3 months",
        "💰 Offer early termination fee waiver",
        "🛠️ Provide personalized tech support or exclusive deals",
        "🌟 Offer a one-time loyalty bonus",
        "📱 Send an exclusive 'We value you' retention package"
    ],
    ("Low", "ALL"): [
        "📺 Promote premium content bundles",
        "🔒 Upsell security service add-ons",
        "👑 Offer exclusive VIP rewards",
        "🎯 Offer a special loyalty bundle",
        "💎 Provide personalized discounts for high spenders",
        "⚡ Offer a free upgrade or enhanced service",
        "🌟 Offer a premium plan upgrade with additional features"
    ]
}