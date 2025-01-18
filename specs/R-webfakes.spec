%global packname webfakes
%global packver  1.3.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          4%{?dist}
Summary:          Fake Web Apps for HTTP Testing

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-stats, R-tools, R-utils
# Suggests:  R-brotli, R-callr, R-covr, R-curl, R-digest, R-glue, R-httpuv, R-httr, R-jsonlite, R-testthat >= 3.0.0, R-withr, R-xml2, R-zip >= 2.3.0
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-utils
# Not in Fedora
# BuildRequires:    R-brotli
BuildRequires:    R-callr
BuildRequires:    R-covr
BuildRequires:    R-curl
BuildRequires:    R-digest
BuildRequires:    R-glue
BuildRequires:    R-httpuv
BuildRequires:    R-httr
BuildRequires:    R-jsonlite
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-withr
BuildRequires:    R-xml2
BuildRequires:    R-zip >= 2.3.0

%description
Create a web app that makes it easier to test web clients without using the
internet. It includes a web app framework with path matching, parameters
and templates. Can parse various 'HTTP' request bodies. Can send 'JSON'
data or files from the disk. Includes a web app that implements the
<https://httpbin.org> web service.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-tests


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
%{rlibdir}/%{packname}/credits
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/views


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.0-2
- R-maint-sig mass rebuild

* Sat Feb 10 2024 Tom Callaway <spot@fedoraproject.org> - 1.3.0-1
- update to 1.3.0

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.1.7-2
- R-maint-sig mass rebuild

* Wed Feb  8 2023 Tom Callaway <spot@fedoraproject.org> - 1.1.7-1
- update to 1.1.7

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  8 2022 Tom Callaway <spot@fedoraproject.org> - 1.1.4-1
- update to 1.1.4

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.1.3-5
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.1.3-1
- update to 1.1.3
- Rebuilt for R 4.1.0

* Sun Apr 25 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.2-1
- Update to latest version (#1953276)

* Tue Mar 02 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
