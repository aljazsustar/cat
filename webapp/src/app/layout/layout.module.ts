import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TopbarComponent } from './topbar/topbar.component';
import {RouterLinkWithHref, RouterOutlet} from "@angular/router";
import {NgbCollapseModule} from "@ng-bootstrap/ng-bootstrap";



@NgModule({
  declarations: [
    TopbarComponent
  ],
  exports: [
    TopbarComponent
  ],
  imports: [
    CommonModule,
    RouterLinkWithHref,
    NgbCollapseModule,
    RouterOutlet
  ]
})
export class LayoutModule { }
