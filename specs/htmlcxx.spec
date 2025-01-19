Name:           htmlcxx
Version:        0.86
Release:        26%{?dist}
# Automatically converted from old format: LGPLv2 and GPLv2+ and ASL 2.0 and MIT - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 AND GPL-2.0-or-later AND Apache-2.0 AND LicenseRef-Callaway-MIT
Summary:        A simple non-validating CSS1 and HTML parser for C++
Url:            http://htmlcxx.sourceforge.net/
Source0:        http://sourceforge.net/projects/htmlcxx/files/htmlcxx/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  chrpath

%description
htmlcxx is a simple non-validating html parser library for C++. 
It allows to fully dump the original html document, character by character, 
from the parse tree. It also has an intuitive tree traversal API.


%package devel
Summary:        Headers and Static Library for htmlcxx
BuildRequires:  pkgconfig
BuildRequires: make
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The htmlcxx-devel package contains libraries and header files for
developing applications that use htmlcxx.

%prep
%setup -q

# convert to utf8 due rpmlint warning W: file-not-utf8 /usr/share/doc/htmlcxx/AUTHORS
# convert to utf8 due rpmlint warning W: file-not-utf8 /usr/share/doc/htmlcxx/README
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README

%build
# Build in C89 mode because the lexer/parser integration relies on implicit
# function declarations.
%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --disable-static --enable-shared

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} 
chrpath --delete %{buildroot}%{_bindir}/htmlcxx

# remove all '*.la' files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
make check

%ldconfig_scriptlets -n %{name}

%files
%doc AUTHORS ChangeLog README
%license COPYING LGPL_V2 ASF-2.0
%{_bindir}/*
%{_datadir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.86-25
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 0.86-21
- Set build_type_safety_c to 0 (#2168170)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Florian Weimer <fweimer@redhat.com> - 0.86-19
- Build in C89 mode (#2168170)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 0.86-13
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.86-3
- Rebuilt

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.86-1
- Update to 0.86
- removed missing-header.patch

* Mon Dec 07 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.85-2
- removed BR gcc-c++
- replaced %%RPM_BUILD_ROOT by %%{buildroot}
- removed Buildroot tag
- use %%{?_smp_mflags} in make
- corrected license tag
- removed unrecognized configure options and added correct one
- added isa to requires tag
- removed all '*.la' files
- Mark license files as %%license where available

* Mon Dec 07 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.85-1
- initial build
