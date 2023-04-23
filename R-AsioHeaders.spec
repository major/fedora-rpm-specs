%global packname AsioHeaders
%global packver  1.22.1-1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.22.1.1
Release:          4%{?dist}
Summary:          Asio C++ Header Files

License:          Boost
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)

%description
'Asio' is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous model using
a modern C++ approach. It is also included in Boost but requires linking when
used with Boost. Standalone it can be used header-only (provided a recent
compiler). 'Asio' is written and maintained by Christopher M. Kohlhoff, and
released under the 'Boost Software License', Version 1.0.


%package devel
Summary:          Asio C++ Header Files

# Newer than the version that's in Fedora.
# https://bugzilla.redhat.com/show_bug.cgi?id=1551800
Provides: bundled(asio) = 1.16.1

Requires: openssl-devel
Recommends: boost-devel

%description devel
'Asio' is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous model using
a modern C++ approach. It is also included in Boost but requires linking when
used with Boost. Standalone it can be used header-only (provided a recent
compiler). 'Asio' is written and maintained by Christopher M. Kohlhoff, and
released under the 'Boost Software License', Version 1.0.


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


%files devel
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%license %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include


%changelog
* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.22.1.1-4
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.22.1.1-2
- R 4.2

* Tue Aug  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.22.1.1-1
- update to 1.22.1-1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 1.16.1.1-4
- rebuild for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16.1.1-1
- Update to latest version

* Thu Jun 25 2020 José Abílio Matos <jamatos@fedoraproject.org> - 1.12.2.1-3
- bump version to ensure upgrade path (due to a F32 rebuild)

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.12.2.1-2
- rebuild for R 4

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.2.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.1.1-1
- initial package for Fedora
