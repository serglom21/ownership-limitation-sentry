import src.bad_ideas as bad_ideas
import sentry_sdk


if __name__ == "__main__":
    sentry_sdk.init(
        dsn="[]",
    )

    bad_ideas.main()
