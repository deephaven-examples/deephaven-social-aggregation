"""
write.py

An extension to the scheduler to write the tables to parquet files, this is a workaround
for the DynamicTableWriter update lock.
"""
import os

if not bool_converter(os.environ.get("SCHEDULED", "false")):
    print("SCHEDULED needs to be set to \"true\" to run the scheduler. Skipping the scheduler...")
else:
    ###Write tables
    if bool_converter(os.environ.get("ENABLE_GA", "false")):
        write_tables(tables=ga_tables, path=f"/data/{start_date.toDateString()}/google/")
    if bool_converter(os.environ.get("ENABLE_TWITTER", "false")):
        write_tables(table=twitter_analytics_table, path=f"/data/{start_date.toDateString()}/twitter/")
        write_tables(table=twitter_metadata, path=f"/data/{start_date.toDateString()}/twitter-metadata/")
    if bool_converter(os.environ.get("ENABLE_SLACK", "false")):
        write_tables(table=slack_channels, path=f"/data/{start_date.toDateString()}/slack-channels/")
        write_tables(table=slack_messages, path=f"/data/{start_date.toDateString()}/slack-messages/")
