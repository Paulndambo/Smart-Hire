from jobs.models import Job

def filter_jobs_by_primary_skillset(jobs, candidate_primary_skills):
    matching_jobs_ids = []
    excellent_matching_job_ids = [] ## This is 100% match
    for job in jobs:
        job_primary_skills = job.primary_skills
        print(f"Job P. Skills: {job_primary_skills}")

        matching_skills = [x for x in job_primary_skills if x in candidate_primary_skills]

        if len(matching_skills) == len(job_primary_skills):
            excellent_matching_job_ids.append(job.id)
        matching_jobs_ids.append(job.id)

        print(f"Matching skills: {matching_skills}")

    return matching_jobs_ids, excellent_matching_job_ids

    

def job_matching_candidate(candidate):
    candidate_specialty = candidate.specialty.lower()
    candidate_seniority = candidate.seniority
    candidate_experience = candidate.years_of_experience

    candidate_primary_skills = candidate.skills.filter(skill_category="primary").values_list('title', flat=True)

    """1. Filter Jobs Based On Specialty"""
    jobs_by_specialty = Job.objects.filter(category=candidate_specialty)
    #print(f"Jobs By Specialty: {jobs_by_specialty}")

    """2. Filter Jobs Based On Seniority"""
    jobs_by_seniority = jobs_by_specialty.filter(seniority=candidate_seniority)
    #print(f"Jobs By Seniority: {jobs_by_seniority}")

    """2. Filter Previous Jobs By Years of Experience"""
    jobs_by_experience = jobs_by_seniority.filter(minimum_experience__lte=candidate_experience)
    #print(excellent_match_ids)

    """3. Filter Jobs By Primary Skills"""
    x, y = filter_jobs_by_primary_skillset(jobs_by_experience, list(candidate_primary_skills))


    candidate_profile = f"""
    1. Experience: {candidate_experience} Years
    2. Specialty: {candidate_specialty}
    3. Candidate Primary Skills: {list(candidate_primary_skills)}
    4. Job Primary Skills: 
    """

    print(candidate_profile)

    #candidate_primary_skills = candidate.

    return y

def job_matching_based_on_skillset(jobs, candidate):
    pass