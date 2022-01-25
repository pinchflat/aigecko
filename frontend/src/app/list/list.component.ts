import { Component, OnInit } from '@angular/core';
import { ImageSize } from '../image-size';
import { ImageService } from '../image.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {

  constructor(private imageService: ImageService) { }
  
   images: Array<string> = new Array<string>(0);
   imageSizes: Map<string,ImageSize> = new Map<string,ImageSize>();
   isUploadFormVisible: Boolean =false;
   fileName: string = '';
   loading: Boolean = false;

  ngOnInit(): void {
    this.loading = true;
    this.imageService.listImages().subscribe(images => {
      this.images = images;
      this.loading = false;
    })
  }

  analyseImage(imageId:string): void {
    if (this.imageSizes.get(imageId) === undefined){
      this.loading = true;
      this.imageService.analyseImage(imageId).subscribe(imageData => {
        this.imageSizes.set(imageId,imageData);
        this.loading = false;
      })
    }
  }

  getImageSize(imageId:string): string {
    var im = this.imageSizes.get(imageId);
    if (im === undefined){
      return '';
    }
    return '('+ im.width+'x'+im.height+')';
  }
  
  showUploadForm() : void {
    this.isUploadFormVisible = true;
  }

  onFileSelected(event: any) {
    const file:File = event.target.files[0];
    if (file) {
        this.loading = true;
        this.fileName = file.name;
        
        var reader = new FileReader();
        
        reader.onload = () => {
          if (reader.result !== undefined){
            this.imageService.uploadImage(reader).subscribe(uploadedImageId => {
              this.imageService.listImages().subscribe(images => {
                this.images = images;
                this.isUploadFormVisible =false;
                this.loading = false;
              })
            });
          }
        }

        reader.readAsArrayBuffer(file);
    }
  }
}
