import { TestBed } from '@angular/core/testing';

import { SymbolsAPIServiceService } from './symbols-apiservice.service';

describe('SymbolsAPIServiceService', () => {
  let service: SymbolsAPIServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SymbolsAPIServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
