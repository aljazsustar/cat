import { TestBed } from '@angular/core/testing';

import { BalanceSheetStatementsService } from './balance-sheet-statements.service';

describe('BalanceSheetStatementsService', () => {
  let service: BalanceSheetStatementsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BalanceSheetStatementsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
