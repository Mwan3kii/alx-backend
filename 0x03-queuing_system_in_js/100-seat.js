import express from 'express';
import { promisify } from 'util';
import redis from 'redis';
import kue from 'kue';

const redisClient = redis.createClient();
const reserveSeatAsync = promisify(redisClient.set).bind(redisClient);
const getCurrentAvailableSeatsAsync = promisify(redisClient.get).bind(redisClient);
const queue = kue.createQueue();
const app = express();
const PORT = 1245;
const INITIAL_SEATS = 50;

redisClient.set('available_seats', INITIAL_SEATS);
let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeatsAsync('available_seats');
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeatsAsync('available_seats');
    const currentSeats = parseInt(availableSeats, 10);
    if (currentSeats > 0) {
      await reserveSeatAsync('available_seats', currentSeats - 1);
      if (currentSeats - 1 === 0) {
        reservationEnabled = false;
      }
      done();
      console.log(`Seat reservation job ${job.id} completed`);
    } else {
      done(new Error('Not enough seats available'));
      console.log(`Seat reservation job ${job.id} failed: Not enough seats available`);
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});