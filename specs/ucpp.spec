Summary: Embeddable, quick, light and fully compliant ISO C99 preprocessor
Name: ucpp
Version: 1.3.5
Release: 15%{?dist}
URL: https://gitlab.com/scarabeusiv/ucpp
Source0: https://gitlab.com/scarabeusiv/ucpp/-/archive/%{version}/ucpp-%{version}.tar.bz2
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
BuildRequires: make
BuildRequires: libtool
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
A C preprocessor is a part of a C compiler responsible for macro replacement,
conditional compilation and inclusion of header files. It is often found as
a stand-alone program on Unix systems.

ucpp is such a preprocessor; it is designed to be quick and light, but anyway
fully compliant to the ISO standard 9899:1999, also known as C99. ucpp can be
compiled as a stand-alone program, or linked to some other code; in the latter
case, ucpp will output tokens, one at a time, on demand, as an integrated lexer.

%package libs
Summary: Library for preprocessing C code compliant with ISO-C99

%description libs
libucpp is an ISO standard 9899:1999 compliant preprocessing library for C
code. It will output tokens, one at a time, on demand, as an integrated lexer.

%package devel
Summary: Development files for libucpp Library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
libucpp is an ISO standard 9899:1999 compliant preprocessing library for C
code. It will output tokens, one at a time, on demand, as an integrated lexer.

This package contains the development files for the library.

%prep
%setup -q
# convert README to UTF-8
iconv -f iso8859-1 -t utf8 README >README.utf8 && \
 touch -r README.utf8 README && \
 mv README.utf8 README
autoreconf -vif

%build
%configure \
           --disable-silent-rules \
           --disable-static \
           --disable-werror \

%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libucpp.la

%files
%{_bindir}/ucpp
%{_mandir}/man1/ucpp.1*

%files libs
%doc AUTHORS ChangeLog* COPYING README
%{_libdir}/libucpp.so.13*

%files devel
%{_includedir}/libucpp
%{_libdir}/libucpp.so
%{_libdir}/pkgconfig/libucpp.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.5-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Dominik Mierzejewski <rpm@greysector.net> 1.3.5-4
- fix FTBFS due to -Werror on s390x

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Dominik Mierzejewski <rpm@greysector.net> 1.3.5-1
- update to 1.3.5
- update upstream location
- include SO version in files list to avoid unexpected bumps
- use modern macros
- drop obsolete comments

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 22 2014 Dominik Mierzejewski <rpm@greysector.net> 1.3.4-3
- add ?_isa to dependencies

* Sun Nov 03 2013 Dominik Mierzejewski <rpm@greysector.net> 1.3.4-2
- make make verbose
- run ldconfig for libs
- convert README to UTF-8

* Wed Oct 30 2013 Dominik Mierzejewski <rpm@greysector.net> 1.3.4-1
- switch to new upstream
- update to 1.3.4
- split libs and devel subpackages
- call autoreconf to fix rpath issue

* Thu Oct 17 2013 Dominik Mierzejewski <rpm@greysector.net> 1.3.2-1
- initial build
