/*
  Component section to invoke the trigger from UI
  Gokul, 19-Mar-2025
  Added to capture the input and display the predictions, 20-Mar-2025
  Simple validation implemented, 21-Mar-2025
  */

import { Component } from '@angular/core';
import { PythonApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  standalone: false,
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'BikeRental';
  //result: any;
  //inputData: string = '';
  temperature: number = 0;
  humidity: number = 0;
  windSpeed: number = 0;
  predictedRent: string = '';
  
  constructor(private pythonApiService: PythonApiService) { }

  // Trigger from the UI will call API service call
  /* runPythonAlgorithm() {
     this.pythonApiService.runAlgorithm(this.inputData).subscribe(response => {
       this.result = response.message;
     });
     }*/

  runPythonAlgorithm() {
    this.pythonApiService.runAlgorithm(this.temperature, this.humidity, this.windSpeed).subscribe
      (response => {
        if (response.predictions == 0) {
          this.predictedRent = "Invalid Inputs";
        }
        else {
          this.predictedRent = "INR " + response.predictions;  // Capture the predicted rental price
        }
        },
          (error) => {
            this.predictedRent = "Invalid Inputs";
            console.error('Error:', error);
          });
    }
  }

