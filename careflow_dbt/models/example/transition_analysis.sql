WITH events AS (
    SELECT
        patient_id,
        activity,
        SAFE.PARSE_TIME('%H:%M', event_time) AS event_time
    FROM `careflow-process-mining-507415.careflow.patient_events`
    WHERE SAFE.PARSE_TIME('%H:%M', event_time) IS NOT NULL
),

transitions AS (
    SELECT
        patient_id,
        activity AS from_activity,
        LEAD(activity) OVER (
            PARTITION BY patient_id
            ORDER BY event_time
        ) AS to_activity,
        event_time AS start_time,
        LEAD(event_time) OVER (
            PARTITION BY patient_id
            ORDER BY event_time
        ) AS end_time
    FROM events
)

SELECT
    from_activity,
    to_activity,
    AVG(TIME_DIFF(end_time, start_time, MINUTE)) AS average_minutes
FROM transitions
WHERE to_activity IS NOT NULL
GROUP BY from_activity, to_activity
ORDER BY average_minutes DESC