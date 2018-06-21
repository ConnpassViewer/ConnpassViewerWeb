json.extract! event, :id, :title, :catch, :img_url, :event_url, :event_id, :started_at, :ended_at, :address, :created_at, :updated_at
json.url event_url(event, format: :json)
