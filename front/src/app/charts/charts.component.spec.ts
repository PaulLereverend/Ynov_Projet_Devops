import { async, TestBed } from '@angular/core/testing';

import { ChartsComponent } from './charts.component';
import { MatSelectModule } from '@angular/material/select';
import { ChartsModule } from 'ng2-charts';
import { GraphComponent } from './graph/graph.component';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

describe('ChartsComponent', () => {

    beforeEach(async(() => {
        TestBed.configureTestingModule({
            imports: [
                MatSelectModule,
                ChartsModule,
                HttpClientModule,
                BrowserAnimationsModule,
            ],
            declarations: [ ChartsComponent, GraphComponent ]
        })
        .compileComponents();
    }));

    it('should create the ChartsComponent', () => {
        const fixture = TestBed.createComponent(ChartsComponent);
        const cc = fixture.debugElement.componentInstance;
        expect(cc).toBeTruthy();
    });
});
