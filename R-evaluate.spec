%global packname  evaluate
%global rlibdir  %{_datadir}/R/library

# Heavy dependencies.
%global with_suggests 0

Name:             R-%{packname}
Version:          0.23
Release:          %autorelease
Summary:          Parsing and Evaluation Tools that Provide More Details than the Default

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods
# Suggests:  R-ggplot2, R-lattice, R-rlang, R-testthat >= 3.0.0, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
%if %{with_suggests}
BuildRequires:    R-ggplot2
BuildRequires:    R-lattice
BuildRequires:    R-rlang
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-withr
%endif

%description
Parsing and evaluation tools that make it easy to recreate the command line
behaviour of R.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
%autochangelog
