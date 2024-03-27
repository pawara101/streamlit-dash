import streamlit as st

import requests
import json
import pandas as pd
from datetime import datetime, timedelta, timezone
import numpy as np

from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthDeviceCode,OAuthClientCredentials

##------INTERACTIVE LOGIN

TENANT_ID = "48d5043c-cf70-4c49-881c-c638f5796997"
CLIENT_ID = "1b90ede3-271e-401b-81a0-a4d52bea3273"
BASE_URL = "https://api.cognitedata.com"

oauth_provider = OAuthDeviceCode(
    authority_url=f"https://login.microsoftonline.com/{TENANT_ID}",
    client_id=CLIENT_ID,
    scopes=[f"{BASE_URL}/.default"],
)
client = CogniteClient(
    ClientConfig(
        client_name="Cognite Academy: Intro to PySDK",
        base_url=BASE_URL,
        project="publicdata",
        credentials=oauth_provider,
    )
)


token_info = client.iam.token.inspect()  # 'iam' stands for: Identity and Access Management

print([project.url_name for project in token_info.projects])


## Time series
time_series_data_list =  client.time_series.list()

train_start_date = datetime(2019,1, 1, tzinfo=timezone.utc)
train_end_date = train_start_date + timedelta(days=90)

ts_exids = ["pi:160697", "pi:160882","pi:160623"]

datapoints_df_ts = client.time_series.data.retrieve_dataframe(
    external_id=ts_exids,
    aggregates="average",
    granularity="1m",
    start=train_start_date,
    end=train_end_date,
    include_aggregate_name=False,
    uniform_index=True,
)

# st.dataframe(datapoints_df_ts)
# print(datapoints_df_ts["pi:160697"].head())



st.markdown("Datapoints")
sensor = st.selectbox(label="Sensor ID",options=tuple(ts_exids))
print(f"Selected : {sensor}")

# print("======")
# print([f"{sensor}"])

# select_sensor = [sensor]

# datapoints_df_ts_sensor = client.time_series.data.retrieve_dataframe(
#     external_id=select_sensor,
#     aggregates="average",
#     granularity="1m",
#     start=train_start_date,
#     end=train_end_date,
#     include_aggregate_name=False,
#     uniform_index=True,
# )

# st.line_chart(datapoints_df_ts_sensor)

sensor_data = datapoints_df_ts[datapoints_df_ts['external_id'] == sensor]

# Plot the data using Altair
st.line_chart(sensor_data)