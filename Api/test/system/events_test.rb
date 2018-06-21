require "application_system_test_case"

class EventsTest < ApplicationSystemTestCase
  setup do
    @event = events(:one)
  end

  test "visiting the index" do
    visit events_url
    assert_selector "h1", text: "Events"
  end

  test "creating a Event" do
    visit events_url
    click_on "New Event"

    fill_in "Address", with: @event.address
    fill_in "Catch", with: @event.catch
    fill_in "Ended At", with: @event.ended_at
    fill_in "Event", with: @event.event_id
    fill_in "Event Url", with: @event.event_url
    fill_in "Img Url", with: @event.img_url
    fill_in "Started At", with: @event.started_at
    fill_in "Title", with: @event.title
    click_on "Create Event"

    assert_text "Event was successfully created"
    click_on "Back"
  end

  test "updating a Event" do
    visit events_url
    click_on "Edit", match: :first

    fill_in "Address", with: @event.address
    fill_in "Catch", with: @event.catch
    fill_in "Ended At", with: @event.ended_at
    fill_in "Event", with: @event.event_id
    fill_in "Event Url", with: @event.event_url
    fill_in "Img Url", with: @event.img_url
    fill_in "Started At", with: @event.started_at
    fill_in "Title", with: @event.title
    click_on "Update Event"

    assert_text "Event was successfully updated"
    click_on "Back"
  end

  test "destroying a Event" do
    visit events_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Event was successfully destroyed"
  end
end
