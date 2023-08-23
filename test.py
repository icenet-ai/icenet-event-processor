import EventGridProcessor
import datetime
import logging
import sys

logging.getLogger().setLevel(logging.DEBUG)

import azure.functions as func

# export FORECAST_PROCESSING_CONFIG=/home/jambyr/code/ai-lab/icenet/icenet-caribou-ceas/event-processor/event-processing.yaml
# python test.py /home/jambyr/code/ai-lab/icenet/icenet-pipeline/results/predict/north_daily_forecast.2023-07-24.nc

if __name__ == "__main__":
    # This is just easier to test locally than hooking up event grid in Azure
    subj = sys.argv[1]
    evt = func.EventGridEvent(
        id="1",
        event_time=datetime.datetime.now(),
        subject=subj,
        topic="some_topic_or_other",
        event_type="Microsoft.Storage.BlobCreated",
        data=dict(
            url="http://example.com/test.url"
        ),
        data_version=""
    )
    EventGridProcessor.main(evt)

