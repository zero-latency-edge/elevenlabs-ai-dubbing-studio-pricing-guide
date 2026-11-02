#!/usr/bin/env python3
"""ElevenLabs AI Dubbing & Studio Localization Pricing Calculator 2026."""
import argparse

DUBBING_RATES = {
    "creator": {"chars_per_min": 1000, "overage_per_1k": 0.30, "base_monthly": 22.0, "quota_chars": 100000},
    "pro": {"chars_per_min": 1000, "overage_per_1k": 0.24, "base_monthly": 99.0, "quota_chars": 500000},
    "scale": {"chars_per_min": 1000, "overage_per_1k": 0.18, "base_monthly": 330.0, "quota_chars": 2000000}
}

def calculate(tier="pro", video_minutes=60, annual=True):
    data = DUBBING_RATES.get(tier.lower(), DUBBING_RATES["pro"])
    base_rate = data["base_monthly"] * (10.0 / 12.0) if annual else data["base_monthly"]
    total_chars_needed = video_minutes * data["chars_per_min"]
    overage_chars = max(0, total_chars_needed - data["quota_chars"])
    overage_cost = (overage_chars / 1000.0) * data["overage_per_1k"]
    monthly_total = base_rate + overage_cost
    cost_per_minute = monthly_total / video_minutes if video_minutes else 0.0

    print("=" * 65)
    print(f"ElevenLabs Dubbing Studio Calculator: Tier {tier.upper()}")
    print("=" * 65)
    print(f"Video Content Volume:      {video_minutes} minutes/month")
    print(f"Estimated Characters:      {total_chars_needed:,} chars")
    print(f"Base Monthly Plan:         ${base_rate:.2f}/mo ({'Annual' if annual else 'Monthly'})")
    print(f"Overage Chars / Cost:      {overage_chars:,} chars -> ${overage_cost:.2f}/mo")
    print(f"Effective Monthly Outlay:  ${monthly_total:.2f}/mo")
    print(f"Effective Cost per Minute: ${cost_per_minute:.2f} per dubbed minute")
    print("=" * 65)
    return monthly_total, cost_per_minute

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ElevenLabs Dubbing Calculator")
    parser.add_argument("--tier", default="pro", choices=["creator", "pro", "scale"])
    parser.add_argument("--minutes", type=int, default=60)
    parser.add_argument("--monthly", action="store_true")
    args = parser.parse_args()
    calculate(tier=args.tier, video_minutes=args.minutes, annual=not args.monthly)
