Name:           ecdsautils
Version:        0.4.1
Release:        3%{?dist}
Summary:        Tiny collection of programs used for ECDSA (keygen, sign, verify)

License:        BSD
URL:            https://github.com/freifunk-gluon/ecdsautils
Source0:        https://github.com/freifunk-gluon/ecdsautils/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake3
BuildRequires:  libuecc-devel

%description
This collection of ECDSA utilities can be used to sign and verify data in a
simple manner.


%package        libs
Summary:        Shared libraries for %{name}

%description    libs
The %{name}-libs package contains shared libraries providing
functionality from %{name} to other applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%cmake3
%cmake3_build


%install
%cmake3_install


%{?ldconfig_scriptlets}


%files
%doc README.md
%license COPYRIGHT
%{_bindir}/ecdsakeygen
%{_bindir}/ecdsasign
%{_bindir}/ecdsaverify
%{_bindir}/ecdsautil


%files libs
%doc README.md
%license COPYRIGHT
%{_libdir}/libecdsautil.so.*


%files devel
%doc README.md
%license COPYRIGHT
%{_includedir}/ecdsautil-%{version}
%{_libdir}/libecdsautil.so
%{_libdir}/pkgconfig/ecdsautil.pc


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 05 2022 Felix Kaechele <felix@kaechele.ca> - 0.4.1-2
- use cmake3 BR and macros, they work on both EPEL7 and Fedora
- add ldconfig_scriptlets for EL7

* Thu May 05 2022 Felix Kaechele <felix@kaechele.ca> - 0.4.1-1
- update to 0.4.1
- use new upstream URLs
- drop patch now upstreamed
- added libs and devel subpackages

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Felix Kaechele <heffer@fedoraproject.org> - 0.3.2-15
- update cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.3.2-2
- add dedicated license file

* Tue Feb 10 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.3.2-1
- initial package
