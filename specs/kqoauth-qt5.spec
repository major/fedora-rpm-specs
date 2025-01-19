# https://github.com/kypeli/kQOAuth/commit/7c31a120f86f3351a9eb0bafd321f2a977b3e0a5
%global commit0 7c31a120f86f3351a9eb0bafd321f2a977b3e0a5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate 20140122
%global sname kqoauth

Name:           %{sname}-qt5
Version:        0.98
Release:        0.20.%{commitdate}git%{shortcommit0}%{?dist}
Summary:        Qt OAuth support library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
Url:            https://github.com/kypeli/kQOAuth
Source0:        https://github.com/kypeli/kQOAuth/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  gcc-c++ 
BuildRequires:  openssl-devel
BuildRequires: make

%description
kQOAuth is a OAuth 1.0 library written for Qt in C++. The goals for the
library have been to provide easy integration to existing Qt5 applications
utilizing Qt5 signals describing the OAuth process, and to provide a
convenient approach to OAuth authentication.

kQOAuth has support for retrieving the user authorization from the service
provider's website. kQOAuth will open the user's web browser to the
authorization page, give a local URL as the callback URL and setup a HTTP
server on this address to listen for the reply from the service and then
process it.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn kQOAuth-%{commit0}
sed -i -e 's|\/usr\/lib|"%{_libdir}"|' kqoauth.prf
find ./ -name "*.pro" -print0| xargs -r0 sed -i -e 's|\/lib|/"%{_lib}"|' --

# Fix pkgconfig file
sed -i 's|QtCore QtNetwork|Qt5Core Qt5Network|g' src/pcfile.sh

%build
%{qmake_qt5} KQOAUTH_LIBDIR=%{_libdir} \
  QMAKE_LFLAGS="${RPM_LD_FLAGS} -Wl,--as-needed"
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check

%ldconfig_scriptlets

%files
%doc CHANGELOG README
%license COPYING
%{_libdir}/lib%{sname}.so.*

%files devel
%{_includedir}/QtKOAuth/
%{_libdir}/lib%{sname}.so
%{_libdir}/pkgconfig/%{sname}.pc
%exclude %{_libdir}/lib%{sname}.prl
%exclude %{_libdir}/qt5/mkspecs/features/%{sname}.prf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.20.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.98-0.19.20140122git7c31a12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.18.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.17.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.16.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.15.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.14.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.13.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.12.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.98-0.11.20140122git7c31a12
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.10.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.9.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.98-0.8.20140122git7c31a12
- Migrate to modern openssl.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.7.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.6.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.5.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.4.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.3.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.2.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.98-0.1.20140122git7c31a12
- inital build
