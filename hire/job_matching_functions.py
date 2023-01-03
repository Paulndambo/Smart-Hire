from jobs.models import Job

def job_matching_based_on_experience(candidate):
    candidate_experience = candidate.years_of_experience

    excellent_match_ids = Job.objects.filter(minimum_experience=candidate_experience).values_list('id', flat=True)
    print(excellent_match_ids)

    return excellent_match_ids

def job_matching_based_on_skillset(jobs, candidate):
    pass