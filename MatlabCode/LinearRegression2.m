%Regerssion 102
clear
x = 0:0.5:20;
y = x.^2;
scatter(x, y)
hold on
%add noise
y_noise = rand(1,size(y,2))*300 - 150;
y_noise = y + y_noise;

x_predict = 0:0.5:20;
mdl = lasso(x', y_noise','Lambda', 0);
%mdl.Coefficients.Estimate %outputs the value of the coefficients
%predict_y = mdl.predict(x_predict');
%scatter(x, y_noise)
%plot(x_predict, predict_y, 'green')
%Fitlm toolbox
%https://www.mathworks.com/help/stats/linear-regression-model-workflow.html

