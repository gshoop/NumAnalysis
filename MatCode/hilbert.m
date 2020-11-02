% Creates n x n hilbert matrix where the H(i,j) entry of the
% hilbert matrix is equal to 1/(i + j - 1)
function H = hilbert(n)

H = zeros(n);

for i = 1 : n
    for j = 1 : n
        H(i,j) = 1/(i + j - 1);
    end
end
end