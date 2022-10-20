import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {SymbolDTO} from "./SymbolDTO";
import {environment} from "../../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class SymbolsAPIServiceService {

  private SYMBOLS_URL: string = `${environment.apiUrl}/api/symbols/`

  constructor(private http: HttpClient) { }

  getSymbols(): Observable<SymbolDTO[]> {
    return this.http.get<SymbolDTO[]>(`${this.SYMBOLS_URL}`);
  }

  getSymbol(symbol: string): Observable<SymbolDTO> {
    return this.http.get<SymbolDTO>(`${this.SYMBOLS_URL}/${symbol}/`)
  }
}
