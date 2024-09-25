import kue from 'kue';

const queue = kue.createQueue();

// The blacklisted phone numbers
const blacklistedNums = [
  '4153518780',
  '4153518781'
];
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (blacklistedNums.includes(phoneNumber)) {
    job.progress(100, 100);
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  setTimeout(() => {
    job.progress(100, 100); 
    done();
  }, 1000);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});