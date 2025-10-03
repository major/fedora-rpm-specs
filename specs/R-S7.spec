%global packname  S7
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        0.2.0
Release:        %autorelease
Summary:        An Object Oriented System Meant to Become a Successor to S3 and S4

License:        MIT
URL:            https://cran.r-project.org/package=%{packname}
Source0:        %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel >= 3.5.0
BuildRequires:  R-testthat >= 3.2.0

%description
A new object oriented programming system designed to be a successor to S3
and S4. It includes formal class, generic, and method specification, and
a limited form of multiple dispatch. It has been designed and implemented
collaboratively by the R Consortium Object-Oriented Programming Working
Group, which includes representatives from R-Core, 'Bioconductor',
'Posit'/'tidyverse', and the wider R community.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
export LANG=C.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --no-manual --ignore-vignettes %{packname}

%files
%license %{rlibdir}/%{packname}/LICENSE
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%changelog
%autochangelog
