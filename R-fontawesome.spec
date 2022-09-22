%global packname  fontawesome
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Easily work with 'Font Awesome' Icons
# Font bits are OFL
# Rest is MIT
License:          MIT and OFL
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports: R-rlang >= 0.4.10, R-htmltools >= 0.5.1.1
# Suggests: R-covr, R-dplyr >= 1.0.8, R-knitr >= 1.31, R-testthat >= 3.0.0, R-rsvg
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core
# This package has a copy of the fontawesome free fonts v6
Provides:         bundled(fontawesome-fonts) = 6.1.1
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-rlang >= 0.4.10
BuildRequires:    R-htmltools >= 0.5.1.1
# Suggests
BuildRequires:    R-dplyr >= 1.0.8
BuildRequires:    R-knitr >= 1.31
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-rsvg

%description
Easily and flexibly insert 'Font Awesome' icons into 'R Markdown' documents
and 'Shiny' apps. These icons can be inserted into HTML content through inline
'SVG' tags or 'i' tags. There is also a utility function for exporting 'Font
Awesome' icons as 'PNG' images for those situations where raster graphics are
needed.

%prep
%setup -q -c -n %{packname}

# it is easier without a covr BR
pushd %{packname}
sed -i 's/covr, //g' DESCRIPTION
popd

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/apps
%{rlibdir}/%{packname}/fontawesome

%changelog
* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 0.3.0-1
- initial package
