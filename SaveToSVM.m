datap = '\\taka2new\dataT0\Free\chwang\Moonshot\kikou\images\train\';
imgs = dir([datap '*.jpg']);
% movieFrame = struct;
% movieFrame.cdata = [];
% movieFrame.colormap = [];
cnt =1;
for i = 1: length(imgs)
   img = imread([datap imgs(i).name]);
   txts = load([replace(datap,'images','labels') replace(imgs(i).name,'jpg','txt')]);
   [h,w,c]= size(img);
   for j = 1:size(txts,1)
      center_x = txts(j,2)*w;center_y = txts(j,3)*h; 
      ww = txts(j,4)*w;hh = txts(j,5)*h;
      t = max(ww,hh);
      %roi = imcrop(img,[center_x - ww/2 center_y- hh/2 ww hh]);
      roi = imcrop(img,[center_x - ww/2 center_y- hh/2 t t]);
      %imshow(roi)
      im = imresize(roi,[128,128]);
      
      imwrite(im,['images\' replace(imgs(i).name, '.jpg','') '-' num2str(j) '.jpg']);
      % '-' num2str(txts(j,1))
      disp([pwd '\images\' replace(imgs(i).name, '.jpg','') '-' num2str(j) '.jpg,',num2str(txts(j,1))])
      %movieFrame(cnt) = im2frame(im); 
      
      cnt= cnt+1;
   end
end
% writerObj =VideoWriter([datap 'movie.avi']); 
% writerObj.FrameRate=1; 
% open(writerObj); 
% writeVideo(writerObj,movieFrame);
% close(writerObj);
%disp(['saved ' num2str(cnt) ' images']);