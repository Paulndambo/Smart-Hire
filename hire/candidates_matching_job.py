from hire.models import Candidate

def filter_candidates_by_skillsets(candidates, job_primary_skills):
    candidates_matching_ids = []
    for candidate in candidates:
        candidate_primary_skills = candidate.skills.filter(skill_category="primary").values_list('title', flat=True)
      
        matching_candidate_skills = [x for x in candidate_primary_skills if x in job_primary_skills]
        if len(matching_candidate_skills) == len(candidate_primary_skills):
            #candidates_matching_ids.append(candidate.id)
            print(f"Candidate Matching: {candidate.id}")
        
    return [1, 2]

def candidates_matching_job(job):
    job_type = job.category
    job_seniority = job.seniority
    job_years_experience = job.minimum_experience
    job_primary_skills = job.primary_skills

    """1. Filter Candidate Based on Job Type/Specialty"""
    candidates_based_on_specialty = Candidate.objects.filter(specialty=job_type)#.values_list('id', flat=True)
   
    """2. Filter Candidate Based on Seniority"""
    candidates_based_on_seniority = candidates_based_on_specialty.filter(seniority=job_seniority)

    """3. Filter Candidate Based on Years of Experience"""
    candidates_based_on_experience = candidates_based_on_seniority.filter(years_of_experience__gte=job_years_experience).values_list('id', flat=True)
    

    """3. Filter Candidates Based on Skills"""
    #candidate_ids = filter_candidates_by_skillsets(candidates_based_on_experience, job_primary_skills)

    job_details = f"""
    1. Job Title: {job.title}
    2. Job Type: {job_type}
    3. Minimum Years of Exp. {job_years_experience}
    4. Job Pri. Skills: {job_primary_skills}
    """
    print(job_details)
    return candidates_based_on_experience   # [1, 2]
