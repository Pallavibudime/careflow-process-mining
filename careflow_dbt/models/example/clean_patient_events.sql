SELECT
    patient_id,
    activity,
    PARSE_TIME('%H:%M', event_time) AS event_time
FROM `careflow-process-mining-507415.careflow.patient_events`
ORDER BY patient_id, event_time