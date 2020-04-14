import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-charts',
  templateUrl: './charts.component.html',
  styleUrls: ['./charts.component.css']
})

export class ChartsComponent implements OnInit {

  private configUrl = 'http://localhost:5000';
  num_unite;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getUnites().subscribe((data) => {
      this.num_unite = data;
      console.log(this.num_unite);
    });
  }

  getUnites() {
    return this.http.get(this.configUrl + '/unites');
  }
}
