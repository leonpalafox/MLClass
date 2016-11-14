%Linear Regression Example
x = 0:1:10;
y = x.^2;

scatter(x, y)
%%
%This instruction only works in Matlab 2016b
%[Mdl,FitInfo] = fitrlinear(x,y, 'Learner', 'leastsquares'); %This is the matlab function for linear rgeression
mdl = fitlm(x, y);
mdl.Coefficients.Estimate %outputs the value of the coefficients
predict_y = mdl.predict(x');

plot(x, predict_y, 'red')
hold on
scatter(x, y, 'o','blue')

%fit without the intercept
mdl = fitlm(x, y, 'Intercept', false);
mdl.Coefficients.Estimate %outputs the value of the coefficients
predict_y = mdl.predict(x');

plot(x, predict_y, 'green')

%add polynomial information
mdl = fitlm(x, y, 'purequadratic');
mdl.Coefficients.Estimate %outputs the value of the coefficients
predict_y = mdl.predict(x');

plot(x, predict_y, 'blue')

%add polynomial information
mdl = fitlm(x, y, 'poly3');
mdl.Coefficients.Estimate %outputs the value of the coefficients
predict_y = mdl.predict(x');

plot(x, predict_y, 'black')
hold off
%add some noise
y_noise = rand(1,size(y,2))*100;
y_noise = y + y_noise;
%add polynomial information
mdl = fitlm(x, y_noise, 'poly3');
mdl.Coefficients.Estimate %outputs the value of the coefficients
predict_y = mdl.predict(x');
scatter(x, y, 'o','blue')
hold on
scatter(x, y_noise, 'o','red')

%increase the order of the poynomial
mdl = fitlm(x, y_noise, 'poly5');
mdl.Coefficients.Estimate %outputs the value of the coefficients
predict_y = mdl.predict(x');
plot(x, predict_y, 'green')
