%Vector Algebra Examples
%Trace

vec_1 = rand(1,4);
vec_2 = rand(4, 4);

%Trace

trace(vec_2)

%Transpose

vec_2'

%diagonal

diag(vec_2)

%matrix multiplication

result = vec_2*vec_2

%elementwise matrix multiplication

result = vec_2.*vec_2 %There is a dot

%inner product in 1D vector

vec_1*vec_1'


%firt element
 vec_1(1)
 
 %last element
 
 vec_1(end)
 
 %find values in vector
 
 find(vec_1>0.5)
 
 
 %horizontal stacking
 
 [vec_1,vec_1]
 
 %vertical stacking
 
 [vec_1;vec_1]
 
 %determinant
 
 det(vec_2)
 
 %%
 %Eigenvalue plot
circle_points = rand(1000,2)*2-1;
scatter(circle_points(:,1), circle_points(:,2))
distances = circle_points(:,1).^2 + circle_points(:,2).^2 ;
distances = sqrt(distances);
index = find(distances<1);
inner_circle = circle_points(index,:);
scatter(inner_circle(:,1), inner_circle(:,2))
axis equal

transf_matrix = [2,1;1,2];
transf_dots = transf_matrix*inner_circle';
scatter(transf_dots(1,:), transf_dots(2,:))
eig(transf_matrix)
 
 
 
 