-- SQL INSERT statements for Work Experience
-- Table: pages_experience
-- 
-- Execute these commands in your PostgreSQL database

INSERT INTO pages_experience (title, company, start_date, end_date, description, display_order, created_at, updated_at)
VALUES 
    (
        'Software Engineer',
        'Stepscale.ai',
        '2024-11-01',
        NULL,  -- NULL for current position (change to '2025-08-31' if it has ended)
        'Built and optimized agentic AI systems tailored for real estate developers, including features such as Project Knowledge, SiteKnowledge, SiteChat, and Project Agents. Integrated external services (Google Drive, Gmail, DocuSign, Pipedream) into workflows, enabling smarter automation and knowledge management. Designed and developed the company''s complete website from scratch in Framer, creating professional UI/UX flows and interactive product demos that improved client engagement.',
        0,
        NOW(),
        NOW()
    ),
    (
        'Research Assistant',
        'Soft Matter & Interfaces Research Group, University of Alberta',
        '2024-05-01',
        '2024-08-31',
        'Collaborated with chemical engineering post-doctoral researchers to develop machine learning models that dramatically reduced computational times for complex CFD simulations. Led a project utilizing proprietary data from Imperial Oil to develop predictive artificial neural network (ANN) models for pressure drop in slurry waste pipelines, enhancing operational efficiency and predictive accuracy.',
        1,
        NOW(),
        NOW()
    ),
    (
        'Vice President of Finance',
        'Engineering Students Society, University of Alberta',
        '2024-05-01',
        '2024-07-31',
        'Treasurer and the signing authority for the Engineering Students Society managing the money flow for the club. Responsible for the annual budget, Sponsorships and managing the advertisements for the sponsors.',
        2,
        NOW(),
        NOW()
    );
