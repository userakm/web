import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Company} from "../models";
import {LoginResponse} from "../models";
@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  static uri = "http://localhost:8000/api/companies";
  constructor(private http: HttpClient) {
  }

  getCompanyList(): Promise<any> {
    return this.http.get(CompanyService.uri).toPromise().then(res => res);
  }

  getCompany(id: number): Observable<Company> {
    return this.http.get<Company>('http://localhost:8000/api/companies/' + id);
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>('http://localhost:8000/api/login/', {
      username,
      password
    })
  }

}
