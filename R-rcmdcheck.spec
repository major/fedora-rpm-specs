%global packname  rcmdcheck
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.4.0
Release:          %autorelease
Summary:          Run 'R CMD check' from 'R' and Capture Results

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-callr >= 3.1.1.9000, R-cli >= 1.1.0, R-crayon, R-desc >= 1.2.0, R-digest, R-pkgbuild, R-prettyunits, R-R6, R-rprojroot, R-sessioninfo >= 1.1.1, R-utils, R-withr, R-xopen
# Suggests:  R-covr, R-knitr, R-mockery, R-rmarkdown, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-callr >= 3.1.1.9000
BuildRequires:    R-cli >= 3.0.0
BuildRequires:    R-curl
BuildRequires:    R-desc >= 1.2.0
BuildRequires:    R-digest
BuildRequires:    R-pkgbuild
BuildRequires:    R-prettyunits
BuildRequires:    R-R6
BuildRequires:    R-rprojroot
BuildRequires:    R-sessioninfo >= 1.1.1
BuildRequires:    R-utils
BuildRequires:    R-withr
BuildRequires:    R-xopen
BuildRequires:    R-knitr
BuildRequires:    R-mockery
BuildRequires:    R-processx
BuildRequires:    R-ps
BuildRequires:    R-rmarkdown
BuildRequires:    R-svglite
BuildRequires:    R-testthat
BuildRequires:    R-webfakes

%description
Run 'R CMD check' from 'R' and capture the results of the individual checks.
Supports running checks in the background, timeouts, pretty printing and
comparing check results.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION

# Fix test
sed -i 's/bad3, tempfile(), character()/bad3, tempfile(), "--no-build-vignettes"/' \
    %{packname}/tests/testthat/test-build.R


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
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
%autochangelog
