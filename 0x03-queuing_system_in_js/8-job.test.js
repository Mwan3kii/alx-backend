import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('create new jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is code 5678 to verify your account'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    const queuedJobs = queue.testMode.jobs;
    expect(queuedJobs).to.have.lengthOf(2);
    queuedJobs.forEach((job, index) => {
        expect(job.data).to.deep.equal(jobs[index]);
        expect(job.type).to.equal('push_notification_code_3');
    });
  });
});