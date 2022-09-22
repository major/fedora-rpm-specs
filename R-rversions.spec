%global packname rversions
%global packver  2.1.2
%global rlibdir  %{_datadir}/R/library

%bcond_with network

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Query 'R' Versions, Including 'r-release' and 'r-oldrel'

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-curl, R-utils, R-xml2 >= 1.0.0
# Suggests:  R-mockery, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-curl
BuildRequires:    R-utils
BuildRequires:    R-xml2 >= 1.0.0
BuildRequires:    R-mockery
BuildRequires:    R-testthat

%description
Query the main 'R' 'SVN' repository to find the versions 'r-release' and
'r-oldrel' refer to, and also all previous 'R' versions and their release
dates.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Take out coverage
sed -i 's/covr, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
%{_bindir}/R CMD check %{packname} --no-examples --no-tests
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
# %%doc %%{rlibdir}/%%{packname}/README.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
%autochangelog
