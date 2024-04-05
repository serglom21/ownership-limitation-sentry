import src.bad_ideas as bad_ideas
import sentry_sdk


if __name__ == "__main__":
    sentry_sdk.init(
        dsn="https://98d96ed5f65d466f85eb3094006eb8a4@o4504533099937792.ingest.us.sentry.io/4504710550847488",
    )

    bad_ideas.main()
