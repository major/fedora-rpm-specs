%global packname websocket
%global packver  1.4.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          5%{?dist}
Summary:          'WebSocket' Client Library

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# https://github.com/rstudio/websocket/issues/59
Patch0001:        0001-Unbundle-websocketpp.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-R6, R-later >= 1.2.0
# Suggests:  R-httpuv, R-testthat, R-knitr, R-rmarkdown
# LinkingTo: R-cpp11, R-AsioHeaders, R-later
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-R6
BuildRequires:    R-later-devel >= 1.2.0
BuildRequires:    R-httpuv
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-cpp11-devel
BuildRequires:    R-AsioHeaders-devel
BuildRequires:    pkgconfig(openssl) >= 1.0.2
BuildRequires:    pkgconfig(websocketpp) >= 0.8.2

%description
Provides a WebSocket client interface for R. WebSocket is a protocol for
low-overhead real-time communication:
<https://en.wikipedia.org/wiki/WebSocket>.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Unbundle websocketpp
%patch0001 -p1

# Fix executable bit
chmod -x man/figures/websocket_logo.svg
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
# i686 segfaults?
%ifnarch i686
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.1-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.4.1-1
- update to 1.4.1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.4.0-4
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.4.0-2
- Rebuilt for R 4.1.0

* Sat Apr 24 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version (#1953110)

* Wed Feb 24 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version (#1927495)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version (#1846157)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
