% Make sure t has your t0, which means you should have an odd number of points, symmetric about your t0
t = linspace(-5, 5, 2001);
% # x is the exact solution to the DE, as determined by wolfram alpha
x = 2.*atan(tanh((t.^2)./4));
x0 = 0;
xn = 0*x + x0;
% f is our function in x' = f(t, x). You must verify this f fits the
% conditions of Picard's theorem
f = @(t, x) t.*cos(x);

% Perform 35 iterations of the picard interation.
for i=1:35
    xn = picard(t, 0, 0, xn, f);
end

function out = picard(t, x0, t0, xn, f)
    x = [];
    % Find the index for t0. This should be done outside of the loop (as it
    % will not change), but it is not decreasing performance enough to
    % worry at this point.
    index = 0;
    for i=1:length(t)
        if t(i) == t0
            index = i;
        end
    end
    fs = f(t, xn);
    % Integrating everything to the left of t0
    for i=1:(index)
        x(length(x)+1) = x0 - trapz(t(i:index), fs(i:index), 2);
    end
    
    %integrating everything to the right of t0
    for i=(index + 1):length(t)
        x(length(x)+1) = x0 + trapz(t(index:i), fs(index:i), 2);
    end
    
    out = x;
end