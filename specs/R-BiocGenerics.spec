%global packname  BiocGenerics
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.54.0
Release:          %autorelease
Summary:          Generic functions for Bioconductor

License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch

BuildRequires:    R-devel >= 4.0.0 tex(latex)
BuildRequires:    R-methods R-utils R-graphics R-stats R-generics

%description
S4 generic functions needed by many other Bioconductor packages.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

## Tests fails because of a circular dependency with the 'suggested'
## requirement in the DESCRIPTION file.
#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests

%changelog
%autochangelog
