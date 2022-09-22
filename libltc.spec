Name:       libltc
Version:    1.3.1
Release:    7%{?dist}
Summary:    Linear/Longitudinal Time Code (LTC) Library

License:    LGPLv3+
URL:        http://x42.github.io/libltc/
Source0:    https://github.com/x42/%{name}/releases/download/v%{version}/libltc-%{version}.tar.gz
# Don't timestamp built HTML documentation, probably Fedora specific
Patch0:     libltc-1.1.2-multilib.patch

BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires: make

%description
Linear (or Longitudinal) Timecode (LTC) is an encoding of time code data as a
Manchester-Biphase encoded audio signal. The audio signal is commonly recorded
on a VTR track or other storage media.

libltc provides functionality to encode and decode LTC from/to time code,
including SMPTE date support.

%package devel
Summary:    Development files for libltc
Requires:   %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the libraries and header files needed for
developing with libltc.

%prep
%setup -q
%patch0 -p1 -b .multilib

%build
%configure
make %{?_smp_mflags} all dox

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libltc.{a,la}

%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README.md
%{_libdir}/libltc.so.*

%files devel
%doc doc/html
%{_libdir}/libltc.so
%{_includedir}/ltc.h
%{_libdir}/pkgconfig/ltc.pc
%{_mandir}/man3/ltc.h.3*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Nils Philippsen <nils@tiptoe.de> - 1.3.1-1
- version 1.3.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 1.3.0-6
- require gcc for building

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Nils Philippsen <nils@tiptoe.de> - 1.3.0-1
- version 1.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Nils Philippsen <nils@redhat.com> - 1.2.0-1
- version 1.2.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Nils Philippsen <nils@tiptoe.de> - 1.1.4-1
- version 1.1.4

* Sat Nov 09 2013 Nils Philippsen <nils@tiptoe.de> - 1.1.3-1
- version 1.1.3

* Sat Nov 09 2013 Nils Philippsen <nils@tiptoe.de> - 1.1.2-2
- upstream distributes official tarballs now

* Mon Oct 28 2013 Nils Philippsen <nils@tiptoe.de> - 1.1.2-1
- version 1.1.2
- use github auto-generated tarball
- build HTML development documentation

* Tue Oct 22 2013 Nils Philippsen <nils@tiptoe.de> - 1.1.1-1
- initial release
