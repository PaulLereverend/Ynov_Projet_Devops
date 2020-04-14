import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-charts',
  templateUrl: './charts.component.html',
  styleUrls: ['./charts.component.css']
})

export class ChartsComponent implements OnInit {

  private configUrl = 'http://localhost:5000';
  nums_unites;
  current_unite;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getUnites().subscribe((data) => {
      this.nums_unites = data;
    });
  }

  getUnites() {
    return this.http.get(this.configUrl + '/unites');
  }
  setCurrentUnite(event) {
    console.log(event);
    this.current_unite = event.value;
  }
}
