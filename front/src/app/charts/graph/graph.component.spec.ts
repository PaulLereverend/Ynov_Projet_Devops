import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GraphComponent } from './graph.component';
import { ChartsModule } from 'ng2-charts';
import { MatSelectModule } from '@angular/material/select';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

describe('GraphComponent', () => {

    beforeEach(async(() => {
        TestBed.configureTestingModule({
            imports: [
                MatSelectModule,
                ChartsModule,
                HttpClientModule,
                BrowserAnimationsModule,
            ],
            declarations: [ GraphComponent ]
        })
        .compileComponents();
    }));

    it('should create the GraphComponent', () => {
        const fixture = TestBed.createComponent(GraphComponent);
        const gc = fixture.debugElement.componentInstance;
        expect(gc).toBeTruthy();
    });
});
