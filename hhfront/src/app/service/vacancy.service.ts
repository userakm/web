import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Vacancy} from "../models";
@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  static uri = "http://localhost:8000/api/companies/vacancies";

  constructor(private http: HttpClient) {
  }

  getVacancyList(): Promise<any> {
    return this.http.get(VacancyService.uri).toPromise().then(res => res);
  }

  getVacancy(id: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>('http://localhost:8000/api/companies/vacancies/' + id);
  }

  getVacancyDetail(id : number) : Observable<Vacancy> {
    return this.http.get<Vacancy>('http://localhost:8000/api/vacancies/' + id);
  }


}
