# Resume Generation API

A FastAPI-based service that generates professional resumes using OpenAI GPT and creates downloadable Word documents stored in Google Cloud Storage.

## Features

- 🤖 AI-powered resume generation using OpenAI GPT
- 📄 Professional Word document (.docx) output
- ☁️ Automatic upload to Google Cloud Storage
- 🎨 Clean, structured resume formatting
- 🚀 Fast and reliable REST API

## Tech Stack

- **Backend**: FastAPI, Python
- **AI**: OpenAI GPT API
- **Document Generation**: python-docx
- **Cloud Storage**: Google Cloud Storage
- **Data Validation**: Pydantic

## Prerequisites

- Python 3.8+
- Google Cloud Storage account and bucket
- OpenAI API access (Azure OpenAI or standard OpenAI)
- Required environment variables

## Installation

1. Clone the repository:
```bash
git clone https://github.com/thirumurugan2001/AI-Resume-Generator.git
cd AI-Resume-Generator
```

2. Install dependencies:
```bash
pip install fastapi uvicorn pydantic google-cloud-storage python-docx openai python-dotenv
```

3. Set up environment variables in `.env` file:
```env
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json
BUCKET_NAME=your-gcs-bucket-name
AZURE_OPENAI_KEY=your-openai-api-key
GPT_URL=your-openai-base-url
MODEL=your-model-name
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to GCS service account JSON file | Yes |
| `BUCKET_NAME` | Google Cloud Storage bucket name | Yes |
| `AZURE_OPENAI_KEY` | OpenAI API key | Yes |
| `GPT_URL` | OpenAI base URL | Yes |
| `MODEL` | OpenAI model name | Yes |

## Project Structure

```
├── main.py              # FastAPI application entry point
├── model.py             # Pydantic models for request validation
├── connectai.py         # Resume generation and document creation logic
├── helper.py            # Google Cloud Storage utilities
├── .env                 # Environment variables (not in repo)
└── README.md           # This file
```

## API Endpoints

### Generate Resume

**POST** `/resume/generation`

Generates a professional resume based on provided user information.

#### Request Body

```json
{
    "name": "string",
    "email": "string", 
    "phone": "string",
    "skills": "string",
    "experience": "string",
    "summary": "string",
    "linked_in": "string",
    "degree": "string",
    "university": "string",
    "grad_year": "string",
    "projects": "string"
}
```

#### Example Request

```json
{
    "name": "Thirumurugan Subramaniyan",
    "email": "thirusubramaniyan2001@gmail.com",
    "phone": "+91 - 7339225958",
    "skills": "Gen AI, RAG & Fine Tuning | Python, JavaScript, React | Azure OpenAI & AWS Bedrock | PyTorch, TensorFlow, LangChain | Web Scraping | MS SQL, PostgreSQL, MongoDB | Git | Prompt Engineer",
    "experience": "2+ years",
    "summary": "As a passionate and driven Software Engineer, I specialize in designing and developing next-generation AI-powered applications...",
    "linked_in": "https://www.linkedin.com/in/thirumurugan-subramaniyan-a62351212/",
    "degree": "B.E.,CSE",
    "university": "Karpagram academy og higher Education",
    "grad_year": "2023",
    "projects": "REAL-TIME EMERGENCY INFORMATION DISSMINATION MOBLIE APPLICATION FOR FIRE SERVICE..."
}
```

#### Success Response

```json
{
    "data": [
        {
            "file_url": "https://storage.cloud.google.com/bucket-name/generated_resume/generated_resume78066.docx"
        }
    ],
    "statusCode": 200,
    "message": "Resume generated successfully",
    "status": true
}
```

#### Error Response

```json
{
    "data": [{}],
    "statusCode": 200,
    "message": "Failed to generate resume",
    "status": false
}
```

## Running the Application

### Development Mode

```bash
python main.py
```

The API will be available at `http://0.0.0.0:8080`

### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: `http://localhost:8080/docs`
- **ReDoc**: `http://localhost:8080/redoc`

## How It Works

1. **Request Validation**: Pydantic models validate incoming resume data
2. **AI Generation**: OpenAI GPT generates professional resume content based on user input
3. **Document Creation**: python-docx creates a formatted Word document
4. **Cloud Upload**: Generated document is uploaded to Google Cloud Storage
5. **Response**: API returns downloadable URL for the generated resume

## Resume Features

The generated resume includes:

- Professional header with contact information
- Executive summary
- Key skills section
- Education details
- Project descriptions
- Work experience
- Clean, professional formatting with color-coded headings

## Error Handling

The API includes comprehensive error handling for:

- OpenAI API failures
- Document generation errors
- Cloud storage upload issues
- Invalid request data

## Security Considerations

- Environment variables for sensitive credentials
- Temporary file cleanup after processing
- Secure cloud storage integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions, please create an issue in the repository or contact thirusubramaniyan.

## Changelog

### v1.0.0
- Initial release
- Basic resume generation functionality
- Google Cloud Storage integration
- OpenAI GPT integration