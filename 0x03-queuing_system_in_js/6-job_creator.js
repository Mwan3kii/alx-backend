import kue from 'kue';

const queue = kue.createQueue();

const jobObj = {
  phoneNumber: '0753518780',
  message: 'Notification to verify your account',
};

const job = queue.create('push_notification_code', jobObj)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});