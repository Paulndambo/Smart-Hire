from jobs.models import Job

def filter_jobs_by_primary_skillset(jobs, candidate_primary_skills):
    jobs = jobs.values('id', 'primary_skills')

    job_primary_skills = [x['primary_skills'] for x in jobs]

    job_ids = []

    for job in jobs:
        job_skills = job['primary_skills']
        for job_skill in job_skills:
            if job_skill in candidate_primary_skills:
                job_ids.append(job['id'])

    print(f"Job Ids: {set(job_ids)}")
    print(f"Jobs Requirements: {jobs}")
    print(f"Job Primary Skills: {job_primary_skills}")
    

def job_matching_based_on_experience(candidate):
    candidate_specialty = candidate.specialty.lower()
    candidate_experience = candidate.years_of_experience

    candidate_primary_skills = candidate.skills.filter(skill_category="primary").values_list('title', flat=True)

    """1. Filter Jobs Based On Specialty"""
    jobs_by_specialty = Job.objects.filter(category=candidate_specialty)
    #print(f"Jobs By Specialty: {jobs_by_specialty}")


    """2. Filter Previous Jobs By Years of Experience"""
    excellent_match_ids = jobs_by_specialty.filter(minimum_experience__lte=candidate_experience).values_list('id', flat=True)
    #print(excellent_match_ids)

    """3. Get Candidate Primary Skills in Job Primary Skill Requirements"""
    jobs_by_skillset = jobs_by_specialty.filter(primary_skills__in=candidate_primary_skills)

    filter_jobs_by_primary_skillset(jobs_by_specialty, list(candidate_primary_skills))


    candidate_profile = f"""
    1. Experience: {candidate_experience} Years
    2. Specialty: {candidate_specialty}
    3. Candidate Primary Skills: {list(candidate_primary_skills)}
    4. Job Primary Skills: 
    5. Jobs By Skillset: {jobs_by_skillset}
    """

    print(candidate_profile)

    #candidate_primary_skills = candidate.

    return excellent_match_ids

def job_matching_based_on_skillset(jobs, candidate):
    pass