# Women's Therapy Group Form Analysis

## Project Overview

This project analyzes data from an online form used by a women's therapy group company. The form collects information about potential clients' problems, desired changes, and expectations from therapy. The analysis aims to understand the differences between respondents who attended informational sessions (indicating higher commitment) and those who did not.

The therapy group speaks is from Spain, so that's why all inputs are in spanish and the variables are in the same language. Also, at the end of the `EDA+keyword_impact.ipynb`, you will find a deep interpretation of the keywords impact scores in Spanish.

## Repository Contents

- `cleaning_typeform.ipynb`: Data cleaning and preprocessing notebook
- `EDA+keyword_impact.ipynb`: Exploratory Data Analysis and NLP-based keyword impact analysis
- `clean_typeform.csv`: Cleaned and anonymized dataset (not included in repository for privacy reasons)
- `Calendly 15 sp 2024.xlsx`: Supplementary data for session attendance (not included in repository)

## Methodology

### Data Cleaning and Preprocessing

1. Load raw data from the online form responses
2. Clean and preprocess the data
3. Anonymize personal information (names, emails, phone numbers)
4. Merge additional data to track session completion
5. Create new categorical variables for analysis

### Natural Language Processing (NLP) Analysis

1. Use NLTK for text processing
2. Analyze key input fields:
   - Main problem (problema_principal)
   - Desired changes (cambios_deseados)
   - Expectations from therapy (busqueda_en_terapia)
3. Generate word clouds and frequency distributions of keywords
4. Compare keyword usage between session attendees and non-attendees
5. Calculate "impact scores" to identify significant differences in keyword usage between groups

## Key Findings

The analysis reveals differences in language and focus between respondents who attended informational sessions and those who did not. Key findings are summarized in the `EDA+keyword_impact.ipynb` notebook, including:

- Most impactful keywords for each input field
- Differences in problem framing and goal setting between groups
- Insights into the motivations and expectations of potential clients

## Usage

To reproduce the analysis:

1. Ensure you have the required dependencies installed (see `requirements.txt`)
2. Run `cleaning_typeform.ipynb` to clean and preprocess the data
3. Run `EDA+keyword_impact.ipynb` to perform the NLP analysis and generate insights

Note: The raw data files are not included in this repository to protect privacy. You'll need to supply your own data in a similar format to run the analysis.

## Future Work

Potential areas for expanding this analysis include:

- Sentiment analysis of responses
- Topic modeling to identify common themes
- Predictive modeling to forecast session attendance or client engagement
