import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {environment} from "../../../../environments/environment";
import {Observable} from "rxjs";
import {BalanceSheetStatementDTO} from "./BalanceSheetStatementDTO";

@Injectable({
  providedIn: 'root'
})
export class BalanceSheetStatementsService {

  private BALANCE_SHEET_STATEMENTS_URL: string =  `${environment.apiUrl}/api/annual-reports/`;

  constructor(
    private http: HttpClient
  ) { }

  getBalanceSheetStatements(symbol: string): Observable<BalanceSheetStatementDTO[]> {
    return this.http.get<BalanceSheetStatementDTO[]>(`${this.BALANCE_SHEET_STATEMENTS_URL}${symbol}/balance-sheet-statements`);
  }
}
