import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ChartsComponent } from './charts/charts.component';
import { TemperatureComponent } from './charts/temperature/temperature.component';


const routes: Routes = [
  { path: '', component: ChartsComponent },
  { path: 'test', component: TemperatureComponent }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
