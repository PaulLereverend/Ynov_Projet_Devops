import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-charts',
  templateUrl: './charts.component.html',
  styleUrls: ['./charts.component.css']
})

export class ChartsComponent implements OnInit {

  private configUrl = 'back:5000';
  nums_unites;
  current_unite;
  current_automates;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getUnites().subscribe((data) => {
      this.nums_unites = data;
    });
  }

  getUnites() {
    return this.http.get(this.configUrl + '/unites');
  }
  getAutomates() {
    let headers = new HttpHeaders().set('Content-Type', 'application/json');
    let params = new HttpParams().set("num_unite", this.current_unite.id);
    return this.http.get(this.configUrl + '/automates', { params: params, headers: headers });
  }
  setCurrentUnite(event) {
    console.log(event);
    this.current_unite = event.value;
    this.getAutomates().subscribe((data) => {
      this.current_automates = data;
      console.log(this.current_automates);
    })
  }
}
