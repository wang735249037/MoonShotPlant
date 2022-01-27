clear
close
clc
path = '\\taka2\chwang\pywork\RA\data\leaf\Stomata_Photo-20211022T082401Z-001\Close-11-86';
fnames = dir([path '\*txt']);
x=1:length(fnames);
y=zeros(4,length(fnames));
for i =1:length(fnames)
   one = load([path '\' fnames(i).name]);
   for m = 1:size(one,1)
       t =one(m,1)+1;
       y(t,i) =y(t,i)+1;
   end
end
sum= zeros(4,length(fnames)-2);
for i =3:length(fnames)
   sum(1,i) = trapz(2:i,y(1,2:i));
   sum(2,i) = trapz(2:i,y(2,2:i));
   sum(3,i) = trapz(2:i,y(3,2:i));
   sum(4,i) = trapz(2:i,y(4,2:i));
end
