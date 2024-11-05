-- Create the claims table
CREATE TABLE IF NOT EXISTS claim (
    claim_id UUID PRIMARY KEY,
    provider_npi BIGINT NOT NULL,
    submitted_procedure VARCHAR(10) NOT NULL,
    provider_fees DECIMAL NOT NULL,
    member_coinsurance DECIMAL NOT NULL,
    member_copay DECIMAL NOT NULL,
    allowed_fees DECIMAL NOT NULL,
    quadrant VARCHAR(100),
    plan_group_number VARCHAR(8) NOT NULL,
    subscriber_number BIGINT NOT NULL,
    net_fee DECIMAL NOT NULL
);

-- Insert sample data
INSERT INTO claim (claim_id, provider_npi, submitted_procedure, provider_fees, member_coinsurance, member_copay, allowed_fees, net_fee, plan_group_number, subscriber_number)
VALUES 
    ('bdea9f10-0a16-4cfa-97e2-0b3df4fbc84f', 1497775530, 'D0123', 100.00, 20.00, 10.00, 80.00, 50.00, 'GRP-1000', 3730189502),
    ('cd2a5e5e-f5e6-4e2b-a0f6-3fbf6b6d4b9f', 1234567891, 'D0456', 150.00, 30.00, 15.00, 120.00, 75.00, 'GRP-1000', 3730189502);
