import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from './../environments/environment';
import { ImageSize } from './image-size';
import { UploadedImageId } from './uploaded-image-id';

@Injectable({
  providedIn: 'root'
})
export class ImageService {
  public baseUrl = environment.apiBaseUrl;

  constructor(private httpClient: HttpClient) { }

  public listImages(): Observable<Array<string>> {
    return this.httpClient.get<Array<string>>(this.baseUrl+"/list_images");
  }
  public analyseImage(imageId:string): Observable<ImageSize> {
    return this.httpClient.get<ImageSize>(this.baseUrl+"/analyse_image/"+imageId);
  }
  public uploadImage(imageData:FileReader): Observable<UploadedImageId> {
    return this.httpClient.post<UploadedImageId>(this.baseUrl+"/upload_image",imageData.result);
  }
}
