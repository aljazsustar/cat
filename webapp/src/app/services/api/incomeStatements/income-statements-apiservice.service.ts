import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {IncomeStatementDTO} from "./IncomeStatementDTO";
import {environment} from "../../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class IncomeStatementsAPIServiceService {

  private INCOME_STATEMENTS_URL: string =  `${environment.apiUrl}/api/annual-reports/`;

  constructor(private http: HttpClient) { }

  getIncomeStatements(symbol: string): Observable<IncomeStatementDTO[]> {
    return this.http.get<IncomeStatementDTO[]>(`${this.INCOME_STATEMENTS_URL}${symbol}/income-statements/`);
  }
}
