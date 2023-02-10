%global packname webfakes
%global packver  1.1.7
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Summary:          Fake Web Apps for HTTP Testing

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-stats, R-tools, R-utils
# Suggests:  R-callr, R-covr, R-curl, R-glue, R-httpuv, R-httr, R-jsonlite, R-testthat >= 3.0.0, R-withr, R-xml2
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-callr
BuildRequires:    R-covr
BuildRequires:    R-curl
BuildRequires:    R-glue
BuildRequires:    R-httpuv
BuildRequires:    R-httr
BuildRequires:    R-jsonlite
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-withr
BuildRequires:    R-xml2

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
%{rlibdir}/%{packname}/credits
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/views


%changelog
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
