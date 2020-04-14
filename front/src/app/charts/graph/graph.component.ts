import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { HttpHeaders, HttpParams, HttpClient } from '@angular/common/http';
import { ChartDataSets, ChartOptions, ChartPoint } from 'chart.js';
import { Color, Label, BaseChartDirective } from 'ng2-charts';
import { interval } from 'rxjs';

@Component({
  selector: 'graph',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.css']
})
export class GraphComponent implements OnInit {
  private configUrl = 'http://localhost:5000';

  @Input() automate: any;
  donnes;
  loaded = false;
  sub;

  public lineChartData: ChartDataSets[] = [];
  public lineChartOptions: (ChartOptions) = {
    responsive: true,
    animation: {
      duration: 0
    },
    maintainAspectRatio: true,
    scales: {
      xAxes: [{
        type: 'time',
        time: {
          unit: 'second',
          displayFormats: {
            second: 'SS'
          }
        }
      }]
    }
  };
  public lineChartLegend = true;
  public lineChartType = 'line';
  public lineChartPlugins = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.loadGraph();
  }
  ngAfterViewInit() {
    this.sub = interval(2000)
      .subscribe((val) => { this.loadGraph(); });
  }
  loadGraph() {
    let newlineChartData: ChartDataSets[] = [];
    this.loadAutomate().subscribe((data: any[]) => {
      let tempCuve: ChartDataSets = { data: [], label: 'Température de la cuve' };
      let tempExterieure: ChartDataSets = { data: [], label: 'Température extérieure' };
      let poidLait: ChartDataSets = { data: [], label: 'Poid du lait' };
      let poidProduitFini: ChartDataSets = { data: [], label: 'Poid du produit fini' };
      let mesurePh: ChartDataSets = { data: [], label: 'Mesure du PH' };
      let mesureK: ChartDataSets = { data: [], label: 'Mesure K+' };
      let concentrationNaCl: ChartDataSets = { data: [], label: 'Concentration NaCl' };
      let niveauSalmonelle: ChartDataSets = { data: [], label: 'Niveau de salmonelle' };
      let niveauEcoli: ChartDataSets = { data: [], label: 'Niveau E-coli' };
      let niveauListeria: ChartDataSets = { data: [], label: 'Niveau bactérien listeria' };

      data = data.sort(function (a, b) {
        return a.date - b.date;
      });
      data.forEach((donnee) => {
        (tempCuve.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.temp_cuve } as ChartPoint);
        (tempExterieure.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.temp_ext } as ChartPoint);
        (poidLait.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.poids_lait } as ChartPoint);
        (poidProduitFini.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.poid_produit_fini } as ChartPoint);
        (mesurePh.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.mesure_ph } as ChartPoint);
        (mesureK.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.mesure_kplus } as ChartPoint);
        (concentrationNaCl.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.mesure_nacl } as ChartPoint);
        (niveauSalmonelle.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.salmonelle } as ChartPoint);
        (niveauEcoli.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.ecoli } as ChartPoint);
        (niveauListeria.data as ChartPoint[]).push({ t: new Date(donnee.date * 1000), y: donnee.listeria } as ChartPoint);

      });
      newlineChartData.push(tempCuve);
      newlineChartData.push(tempExterieure);
      newlineChartData.push(poidLait);
      newlineChartData.push(poidProduitFini);
      newlineChartData.push(mesurePh);
      newlineChartData.push(mesureK);
      newlineChartData.push(concentrationNaCl);
      newlineChartData.push(niveauSalmonelle);
      newlineChartData.push(niveauEcoli);
      newlineChartData.push(niveauListeria);
      this.lineChartData = newlineChartData;
      this.loaded = true;
    });
  }
  loadAutomate() {
    const start = new Date();
    start.setSeconds(start.getSeconds() - 60);
    let headers = new HttpHeaders().set('Content-Type', 'application/json');
    let params = new HttpParams().set("num_automate", this.automate.id).set("date_fin", start.getTime() + '');
    return this.http.get(this.configUrl + '/automate/data', { params: params, headers: headers });
  }

}
