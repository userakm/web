import { Component, OnInit } from '@angular/core';
import {Company} from "../models";
import {CompanyService} from "../service/company.service";
import {Observable} from "rxjs";

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];

  constructor(public companyService: CompanyService) {
  }

  ngOnInit(): void {
    this.getCompanyList();
  }

  getCompanyList() {
    this.companyService.getCompanyList().then(res => {
      this.companies = res;
      console.log(res);
    })
  }
  

}
