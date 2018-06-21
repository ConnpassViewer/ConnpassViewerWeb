class CreateEvents < ActiveRecord::Migration[5.2]
  def change
    create_table :events do |t|
      t.string :title
      t.string :catch
      t.string :img_url
      t.string :event_url
      t.integer :event_id
      t.datetime :started_at
      t.datetime :ended_at
      t.string :address

      t.timestamps
    end
  end
end
