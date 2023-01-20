%global packname restfulr
%global packver 0.0.15

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Source0:          %{url}&version=%{version}#/%{packname}_%{packver}.tar.gz
License:          Artistic 2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Summary:          R Interface to RESTful Web Services
BuildRequires:    R-devel >= 3.4.0, tetex-latex, R-XML, R-RCurl
BuildRequires:    R-S4Vectors-devel >= 0.13.15, R-yaml, R-rjson
# Suggests
BuildRequires:    R-getPass
BuildRequires:    R-RUnit
# Not in Fedora
# BuildRequires:  R-rsolr

%description
Models a RESTful service as if it were a nested R list.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%check
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/unitTests

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 0.0.15-1
- update to 0.0.15
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.0.13-2
- use buildroot macros
- fix url and source0
- disable examples in check
- drop BR: gcc (R-devel requires R-core-devel requires gcc-c++ requires gcc)

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 0.0.13-1
- initial package
