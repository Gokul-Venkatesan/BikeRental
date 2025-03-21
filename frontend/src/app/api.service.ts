/*
  API Service to Python Program
  Gokul, 19-Mar-2025
  Added to capture inputs and modified to POST method call, 20-Mar-2025
  */

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PythonApiService {

  private apiUrl = 'http://localhost:5000/BikeRental'; // URL of your Python Flask API

  constructor(private http: HttpClient) { }

  /*runAlgorithm(data: string): Observable<any> {
    return this.http.get(this.apiUrl, { });*/

  runAlgorithm(temperature: number, humidity: number, windSpeed: number): Observable<any> {
    const body = {
      temperature: temperature,
      humidity: humidity,
      windspeed: windSpeed
    }

    const headers = new HttpHeaders().set('Content-Type', 'application/json');

    return this.http.post<any>(this.apiUrl, body);
}
}
