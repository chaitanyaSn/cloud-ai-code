class Job:
  def __init__(self,id,deadline,profit):
    self.id=id
    self.deadline=deadline
    self.profit=profit


class Solution:
  def jobScheduling(self,jobs):
    jobs.sort(key=lambda x:x.profit,reverse=True)
    maxi=max(job.deadline for job in jobs)
    slot=[-1]*(maxi+1)
    count=0
    jobP=0
    for i in range(len(jobs)):
      for j in range(jobs[i].deadline,0,-1):
        if slot[j]==-1:
          slot[j]=i
          count+=1
          jobP+=jobs[i].profit
          break
    return count,jobP
  
if __name__ == "__main__":
    jobs = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 2, 40), Job(4, 2, 30)]
    count, profit = Solution().jobScheduling(jobs)
    print(count, profit)
