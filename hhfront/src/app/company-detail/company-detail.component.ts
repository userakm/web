import { Component, OnInit } from '@angular/core';
import {Company} from "../models";
import { Vacancy} from "../models";
import {CompanyService} from "../service/company.service";
import {ActivatedRoute , Router} from "@angular/router";
import { Observable} from "rxjs";

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {

  company: Company;

  constructor(public companyService: CompanyService , private route: ActivatedRoute, private router: Router) {
  }

  ngOnInit(): void {
    this.getCompanyDetail();
  }

  getCompanyDetail() {
    const id = +this.route.snapshot.paramMap.get('company_id');
    const companyObservable = this.companyService.getCompany(id)
    companyObservable.subscribe(company => this.company = company)
  }

}
