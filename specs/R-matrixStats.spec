Name:           R-matrixStats
Version:        %R_rpm_version 1.5.0
Release:        %autorelease
Summary:        Functions that Apply to Rows and Columns of Matrices (and to Vectors)

License:        Artistic-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
High-performing functions operating on rows and columns of matrices, e.g. 
col / rowMedians(), col / rowRanks(), and col / rowSds(). Functions optimized 
per data type and for subsetted calculations such that both memory usage and 
processing time is minimized. There are also optimized vector-based methods, 
e.g. binMeans(), madDiff() and weightedMedian().

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
