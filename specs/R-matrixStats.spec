%global packname  matrixStats
%global packver   1.5.0

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Functions that Apply to Rows and Columns of Matrices (and to Vectors)
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
BuildRequires:    R-devel >= 3.4.0
# Suggests
# BuildRequires:  R-base64enc
# BuildRequires:  R-ggplot2
# BuildRequires:  R-knitr
# BuildRequires:  R-markdown
# BuildRequires:  R-microbenchmark
# BuildRequires:  R-R.devices
# BuildRequires:  R-R.rsp

%description
High-performing functions operating on rows and columns of matrices, e.g. 
col / rowMedians(), col / rowRanks(), and col / rowSds(). Functions optimized 
per data type and for subsetted calculations such that both memory usage and 
processing time is minimized. There are also optimized vector-based methods, 
e.g. binMeans(), madDiff() and weightedMedian().

%prep
%setup -c -q -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_libdir}/R/library/R.css

%check
# Too many missing deps
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS.md
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/benchmarking
%{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/WORDLIST

%changelog
%autochangelog
