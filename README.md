# Watson Meeting Summarizer API

## Overview

The Watson Meeting Summarizer API leverages IBM Watson to automatically generate detailed meeting summaries. This API is integrated with ConnectX to enhance real-time collaboration, scheduling, and post-meeting follow-ups by producing structured, clear, and concise meeting summaries in JSON format.

## Features

- **Automated Meeting Summarization**: Creates structured summaries of meeting discussions, including titles, summaries, attendees, action items, and decisions.
- **Integration with ConnectX**: Enhances meeting management by suggesting optimal meeting times, resolving conflicts, and automating follow-ups.
- **Real-Time Collaboration**: Supports live document collaboration and interactive whiteboarding.

## Files

- **`meetsumm.py`**: Main application script. Implements the API using Flask and IBM Watson.
- **`requirements.txt`**: Lists the dependencies required to run the API.
- **`test.html`**: A simple HTML page for testing the API.
- **`Meeting Summarization Model.ipynb`**: Jupyter notebook explaining how to create and deploy the API using IBM Watson.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/IBMTechXChange/Watson-Meeting-Summarizer-API.git
   cd Watson-Meeting-Summarizer-API
   ```
2. **Install Dependencies**

   Ensure you have Python 3.7 or higher installed. Install the required packages using:

   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables**

   Create a `.env` file in the root directory with the following content:

   ```env
   API_KEY=your_ibm_watson_api_key
   PROJECT_ID=your_ibm_watson_project_id
   ```
4. **Run the Application**

   Start the Flask application using:

   ```bash
   python meetsumm.py
   ```

   The API will be available at `http://localhost:8000`.

## API Endpoints

- **`GET /`**: Check the status of the API.

  - **Response**: `{ "message": "Meeting Summarization using Watson API" }`
- **`POST /generate`**: Generate a meeting summary.

  - **Request Body**:
    ```json
    {
      "question": "Attendee 1 (with their designation): [Statement]\nAttendee 2 (with their designation): [Statement]"
    }
    ```
  - **Response**:
    ```json
    {
      "response": {
        "title": "Meeting Title",
        "summary": "A concise overview of the meeting discussion.",
        "attendees": [
          {
            "name": "Attendee 1",
            "designation": "Attendee 1's designation"
          },
          {
            "name": "Attendee 2",
            "designation": "Attendee 2's designation"
          }
        ],
        "date": "YYYY-MM-DD",
        "action_items": [
          {
            "task": "Description of the task",
            "owner": "Assigned person",
            "due_date": "YYYY-MM-DD"
          }
        ],
        "decisions": [
          {
            "decision": "Description of the decision made",
            "made_by": "Person or group who made the decision"
          }
        ]
      }
    }
    ```

## Testing the API

Open `test.html` in your web browser, enter meeting input, and submit to test the API. The response will be displayed on the same page.

## Creating the API with Watson

Refer to **`Meeting Summarization Model.ipynb`** for a step-by-step guide on how to create and deploy the API using IBM Watson.

## Contact

For questions or support, please contact [IBMTechXChange](https://github.com/IBMTechXChange).
