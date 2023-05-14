%global packname haven
%global packver  2.5.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Import and Export 'SPSS', 'Stata' and 'SAS' Files

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli >= 3.0.0, R-forcats >= 0.2.0, R-hms, R-lifecycle, R-methods, R-readr >= 0.1.0, R-rlang >= 0.4.0, R-tibble, R-tidyselect, R-vctrs >= 0.3.0
# Suggests:  R-covr, R-crayon, R-fs, R-knitr, R-pillar >= 1.4.0, R-rmarkdown, R-testthat >= 3.0.0, R-utf8
# LinkingTo: R-cpp11
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 3.0.0
BuildRequires:    R-forcats >= 0.2.0
BuildRequires:    R-hms
BuildRequires:    R-lifecycle
BuildRequires:    R-methods
BuildRequires:    R-readr >= 0.1.0
BuildRequires:    R-rlang >= 0.4.0
BuildRequires:    R-tibble
BuildRequires:    R-tidyselect
BuildRequires:    R-vctrs >= 0.3.0
BuildRequires:    R-cpp11-devel
BuildRequires:    R-crayon
BuildRequires:    R-fs
BuildRequires:    R-knitr
BuildRequires:    R-pillar >= 1.4.0
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-utf8

%description
Import foreign statistical formats into R via the embedded 'ReadStat' C
library, <https://github.com/WizardMac/ReadStat>.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%ifnarch ppc64le
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
