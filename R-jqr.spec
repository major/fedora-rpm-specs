%global packname jqr
%global packver  1.3.3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3.3
Release:          %autorelease
Summary:          Client for 'jq', a 'JSON' Processor

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-magrittr, R-lazyeval
# Suggests:  R-jsonlite, R-testthat
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    tex(inconsolata.sty)
BuildRequires:    jq-devel
BuildRequires:    R-magrittr
BuildRequires:    R-lazyeval
BuildRequires:    R-jsonlite
BuildRequires:    R-testthat

%description
Client for 'jq', a 'JSON' processor (<https://jqlang.github.io/jq/>),
written in C. 'jq' allows the following with 'JSON' data: index into,
parse, do calculations, cut up and filter, change key names and values,
perform conditionals and comparisons, and more.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/data


%changelog
%autochangelog
