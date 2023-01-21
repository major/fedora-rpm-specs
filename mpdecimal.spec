# versioned documentation for old releases
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           mpdecimal
Version:        2.5.1
Release:        5%{?dist}
Summary:        Library for general decimal arithmetic
License:        BSD-2-Clause

URL:            http://www.bytereef.org/mpdecimal/index.html
Source0:        http://www.bytereef.org/software/mpdecimal/releases/mpdecimal-%{version}.tar.gz
Source1:        http://speleotrove.com/decimal/dectest.zip

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  unzip

%description
The package contains a library limpdec implementing General Decimal Arithmetic
Specification. The specification, written by Mike Cowlishaw from IBM, defines
a general purpose arbitrary precision data type together with rigorously
specified functions and rounding behavior.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Development headers for mpdecimal library

%description devel
The package contains development headers for the mpdecimal library.

%package        doc
Summary:        Documentation for mpdecimal library
# docs is FreeBSD-DOC
# bundles underscore.js: MIT
# bundles jquery: MIT
# jquery bundles sizzle.js: MIT
License:        FreeBSD-DOC AND MIT
BuildArch:      noarch
Provides:       bundled(js-jquery) = 3.4.1
Provides:       bundled(js-underscore) = 1.3.1

%description doc
The package contains documentation for the mpdecimal library.

%prep
%autosetup
unzip -d tests/testdata %{SOURCE1}

%build
# Force -ffat-lto-objects so that configure tests are assembled which
# is required for ASM configure tests.  -ffat-lto-objects is the default
# for F33, but will not be the default in F34
#define _lto_cflags -flto=auto -ffat-lto-objects

%configure
make %{?_smp_mflags}

%check
make check

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.a

# license will go into dedicated directory
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE.txt

# relocate documentation if versioned documentation is used
if [ "%{_pkgdocdir}" != "%{_docdir}/%{name}" ]; then
  install -d -m 0755 %{buildroot}%{_pkgdocdir}
  mv -v %{buildroot}%{_docdir}/%{name}/* %{buildroot}%{_pkgdocdir}/
fi

%files
%license LICENSE.txt
%{_libdir}/libmpdec.so.%{version}
%{_libdir}/libmpdec.so.3
%{_libdir}/libmpdec++.so.%{version}
%{_libdir}/libmpdec++.so.3

%files devel
%{_libdir}/libmpdec.so
%{_libdir}/libmpdec++.so
%{_includedir}/mpdecimal.h
%{_includedir}/decimal.hh

%files doc
%license doc/LICENSE.txt
%doc %{_pkgdocdir}

%ldconfig_scriptlets

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb  1 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.1-1
- New version
  Resolves: rhbz#1921929

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Jeff Law <law@redhat.com> - 2.5.0-3
- Force -ffat-lto-objects and re-enable LTO

* Thu Aug  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-2
- Re-enabled tests

* Wed Aug  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-1
- New version
  Resolves: rhbz#1851761
- Fixed changelog

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 2.4.2-14
- Disable LTO

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 30 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.4.2-5
- fix build on EPEL 7

* Tue Aug 30 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.4.2-4
- doc: use versioned Provides for bundled libraries

* Mon Aug 22 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.4.2-3
- add ldconfig in post and postun
- doc: add license file and fix License field
- doc: add Provides for bundled JavaScript libraries

* Fri Aug 12 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.4.2-2
- fix build on EPEL 7

* Fri Jul 15 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 2.4.2-1
- initial package
