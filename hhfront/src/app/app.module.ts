import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CompanyListComponent } from './company-list/company-list.component';
import {HttpClientModule} from "@angular/common/http";
import { CompanyDetailComponent } from './company-detail/company-detail.component';
import {FormsModule} from "@angular/forms";
import { VacancyListComponent } from './vacancy-list/vacancy-list.component';
import { VacancyDetailComponent } from './vacancy-detail/vacancy-detail.component';


@NgModule({
  declarations: [
    AppComponent,
    CompanyListComponent,
    CompanyDetailComponent,
    VacancyListComponent,
    VacancyDetailComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
