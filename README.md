# CrySense

Submission to University of Florida's 2024 WiNGHacks hackathon by Lydia Chung, Grace Cavarretta, and Claire Wang.

Demo video: [https://youtu.be/2e2FrYw-Xys](https://youtu.be/2e2FrYw-Xys)

## Inspiration
Understanding and responding to a baby's physiological and emotional needs is crucial for all caregivers, including women and non-binary individuals, who often take on primary caregiving roles in families. With CrySense, caregivers can quickly and accurately identify their baby's needs, providing reassurance and support for both. This not only enhances the parenting experience but also fosters stronger bonds between moms, dads, and their children, regardless of gender identity. By developing a tool like CrySense that helps decipher infant cries, we empower women, non-binary people, and all parents to navigate the challenges of childcare with confidence and ease. 

## What it does
Our project, CrySense, uses an AI trained model to analyze and interpret the meaning behind cries from infants. Based on the interpreted result, it sends a notification to the parent's phone via a WiFi connection to alert them about why their baby is crying.

When parents and caregivers hear the cry of an infant, it can be difficult for them to decipher what exactly what they are communicating as babies tend to have different cries to express different needs or emotions. Our project's combination of hardware and AI resolves these challenges by helping caregivers identify when an infant is crying due to hunger or discomfort.

## How we built it
We trained and tested our AI model through Edge Impulse, where we gathered data from an open source dataset containing audio files of infant cries. We then listened to each audio file to minimize the amount of background noise that would appear in our training dataset, as some of the files included sounds of people talking or no sound at all. By doing this, each iteration of our training was able to produce a higher accuracy of prediction. 

We got this data from [https://data.mendeley.com/datasets/hbppd883sd/1](https://data.mendeley.com/datasets/hbppd883sd/1) and [https://github.com/gveres/donateacry-corpus](https://github.com/gveres/donateacry-corpus). These datasets were chosen because they contained distinct infant cries, and we used them to help parents bond with their children by understanding their emotions.

To notify the caregiver, we used an API called PushOver that sends the results from the AI model as a push notification to a mobile device. We used the Arduino IDE to program a wireless microcontroller using the PushOver API and send signals remotely to a user's phone.

## Challenges we ran into
One of the main challenges we encountered was that our microprocessor broke in the middle of testing, which prevented us from being able to run the AI model on our board (Arduino Nano 33 BLE Sense Rev2). To demonstrate the functionality of our wireless connectivity work, we used a different microcontroller to send push notifications to our phones, using a button circuit to simulate the AI model outputs.

Another challenge was training the AI model with the datasets, which turned out to be more time-consuming and demanding than we originally expected. It required careful selection and organization on our part from a wide range of audio data.

## Accomplishments that we're proud of
While training the AI model, we managed to boost the accuracy of said model from (at lowest), 7.32% to 95.1%. We were also able to overcome the hardware problem of our microcontroller breaking.

## What we learned
The process of training AI models, particularly for nuanced tasks like interpreting infant cries, can be more challenging and time-consuming than initially anticipated. This underscores the importance of thorough planning, meticulous data curation, and innovative methodologies to achieve desired outcomes. Additionally, we learned more about the daily challenges that caregivers experience, particularly in the intricate nature of infant communication and deciphering their needs. This project gave us some insight into the value of leveraging AI to bridge communication gaps.

## What's next for CrySense
We would like to enhance CrySense's capability to discern a broader spectrum of emotions from babies' cries, including fatigue, pain, and overstimulation. We would also like to program the AI model onto the Arduino Nano 33 BLE Sense as we originally intended, but this would require the purchase of a new microcontroller. This would remove the need for the button circuit simulation.
