import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CompanyListComponent} from "./company-list/company-list.component";
import {CompanyDetailComponent} from "./company-detail/company-detail.component";
import {VacancyListComponent} from "./vacancy-list/vacancy-list.component";
import {VacancyDetailComponent} from "./vacancy-detail/vacancy-detail.component";


const routes: Routes = [
  {path: '', component: CompanyListComponent},
  {path: 'companies/:company_id' , component : CompanyDetailComponent },
  {path: 'companies/vacancies/:company_id' , component: VacancyListComponent },
  {path: 'vacancies/:vacancy_id' , component: VacancyDetailComponent}


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
