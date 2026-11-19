"""Unit tests for resume parsing and ATS section detection."""
import pytest
from app.services.resume_parser import ResumeParser, InvalidPdfError, ScannedPdfError


@pytest.fixture
def parser():
    return ResumeParser()


def test_detect_standard_sections(parser: ResumeParser):
    sample_resume = """
    Jane Doe
    Software Engineer
    
    Education:
    Bachelor of Technology in Computer Science, 2024
    
    Technical Skills:
    Python, FastAPI, Next.js, PostgreSQL, Docker, Git
    
    Work Experience:
    Software Engineering Intern at TechCorp (2023 - 2024)
    - Developed microservices using FastAPI
    
    Academic Projects:
    - Built an end-to-end placement portal with real-time code editor
    
    Certifications:
    AWS Certified Cloud Practitioner
    """
    sections = parser.detect_sections(sample_resume)
    assert "education" in sections
    assert "skills" in sections
    assert "experience" in sections
    assert "projects" in sections
    assert "certifications" in sections


def test_parse_plain_text(parser: ResumeParser):
    text = "John Smith\n\nExperienced Full Stack Developer with 3 years of experience in React and Node.js."
    result = parser.parse_text(text)
    assert result["word_count"] > 0
    assert result["character_count"] > 0
    assert "John Smith" in result["text"]


def test_invalid_pdf_bytes_raise_error(parser: ResumeParser):
    invalid_pdf_bytes = b"NOT_A_VALID_PDF_HEADER_OR_CONTENT"
    with pytest.raises(InvalidPdfError):
        parser.parse_pdf(invalid_pdf_bytes)
