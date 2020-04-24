import { Component, OnInit } from '@angular/core';
import { Vacancy} from "../models";
import {VacancyService} from "../service/vacancy.service";
import {ActivatedRoute, Router} from "@angular/router";
import {Observable} from "rxjs";


@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css']
})
export class VacancyListComponent implements OnInit {

  vacancies: Vacancy[] = [];


  constructor(public vacancyService: VacancyService, private route: ActivatedRoute, private router: Router) {
  }

  ngOnInit(): void {
    this.getVacancyList();
  }

  getVacancyList() {
    const id = +this.route.snapshot.paramMap.get('company_id');
    const vacancyObservable = this.vacancyService.getVacancy(id)
    vacancyObservable.subscribe(vacancy => this.vacancies = vacancy)
    this.vacancyService.getVacancy(id)
  }


}
