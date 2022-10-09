import { TestBed } from '@angular/core/testing';

import { IncomeStatementsAPIServiceService } from './income-statements-apiservice.service';

describe('IncomeStatementsAPIServiceService', () => {
  let service: IncomeStatementsAPIServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(IncomeStatementsAPIServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
