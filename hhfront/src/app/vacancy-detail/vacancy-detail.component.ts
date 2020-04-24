import { Component, OnInit } from '@angular/core';
import {observable} from "rxjs";
import {Vacancy} from "../models";
import {ActivatedRoute, Router} from "@angular/router";
import {VacancyService} from "../service/vacancy.service";


@Component({
  selector: 'app-vacancy-detail',
  templateUrl: './vacancy-detail.component.html',
  styleUrls: ['./vacancy-detail.component.css']
})
export class VacancyDetailComponent implements OnInit {

  vacancy: Vacancy;

  constructor(public vacancyService: VacancyService , private route: ActivatedRoute, private router: Router) {
  }

  ngOnInit(): void {
    this.getVacancyDetail();
  }

  getVacancyDetail() {
    const id = +this.route.snapshot.paramMap.get('vacancy_id');
    const vacancyObservable = this.vacancyService.getVacancyDetail(id)
    vacancyObservable.subscribe(vacancy => this.vacancy = vacancy)
    console.log(this.vacancy);
  }


}
