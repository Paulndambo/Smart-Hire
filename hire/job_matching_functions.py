from jobs.models import Job

def filter_jobs_by_primary_skillset(jobs, candidate_primary_skills):
    matching_jobs = []

    for job in jobs:
        job_primary_skills = job.primary_skills
        if len(job_primary_skills) == 1:
            print("Matching Skills Few")
        elif len(job_primary_skills) > 1:
            matching_skills = [x for x in job_primary_skills if x in candidate_primary_skills]
            if len(matching_skills) == 1:
                print("Matched Very Few Skills")
            matching_jobs.append(job.id)
    
    print(f"Matching Jobs: {matching_jobs}")

    

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