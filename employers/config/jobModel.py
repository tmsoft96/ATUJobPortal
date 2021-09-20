from ATUJobPortal.config.firebase import Firebase
import timeago, datetime


class JobModel:
    def __init__(self) -> None:
        pass

    def allJob():
        firebase = Firebase()

        now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

        allJobsList = []
        allJobs = firebase.db.child("Jobs").get().val().items()
        
        for key, value in allJobs:
            postDate = datetime.datetime.fromisoformat(value.get("editDate"))
            jobDic = {
                "key": key,
                "jobTitle": value.get("jobTitle"),
                "jobFunction": value.get("jobFunction"),
                "region": value.get("region"),
                "currency": value.get("currency"),
                "salary": value.get("salary"),
                "workType": value.get("workType"),
                "time": timeago.format(postDate, now),
            }
            allJobsList.append(jobDic)

        return allJobsList
