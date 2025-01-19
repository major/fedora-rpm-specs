Name:           mujs
Version:        1.3.3
Release:        7%{?dist}
Summary:        An embeddable Javascript interpreter
License:        ISC
URL:            https://mujs.com/
Source0:        https://mujs.com/downloads/%{name}-%{version}.tar.gz

# https://github.com/ccxvii/mujs/pull/187
Patch0:         set-library-soname-version.patch

# use custom soname version until it lands upstream to avoid future potential conflict
Patch1:         downstream-soname-version.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  readline-devel

%description
MuJS is a lightweight Javascript interpreter designed for embedding in
other software to extend them with scripting capabilities.

%package devel
Summary:        MuJS development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the MuJS shared library.

%package static
Summary:        MuJS development files using static lib
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package provides the MuJS static library.


%prep
%autosetup -p1
chmod a-x -v docs/*

%build
%make_build release prefix="%{_prefix}" libdir="%{_libdir}" CFLAGS="%{build_cflags} %{build_ldflags}"

%install
%make_install prefix="%{_prefix}" libdir="%{_libdir}"
%{__make} install-shared DESTDIR=%{?buildroot} INSTALL="%{__install} -p" prefix="%{_prefix}" libdir="%{_libdir}"


%files
%license COPYING
%doc AUTHORS README docs
%{_bindir}/%{name}
%{_bindir}/%{name}-pp
%{_libdir}/lib%{name}.so.0{,.*}

%files devel
%license COPYING
%doc AUTHORS README
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files static
%{_libdir}/lib%{name}.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Alessandro Astone <ales.astone@gmail.com> - 1.3.3-5
- Fix paths in pkgconfig file
- Make shared library versioned

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 30 2023 Alain Vigne <avigne@fedoraproject.org> 1.3.3-2
- Install the shared library instead of default static one. Solve RHBZ#2241358
- Add a -static subpackage

* Tue Sep 19 2023 Alain Vigne <avigne@fedoraproject.org> 1.3.3-1
- upstream release 1.3.3
- migrated to SPDX license

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Alain Vigne <avigne@fedoraproject.org> 1.3.2-1
- upstream release 1.3.2
- Fix CVE-2022-44789 (rhbz#2148261)
- Fix CVE-2022-30975 (rhbz#2088596)
- Fix CVE-2022-30974 (rhbz#2088591)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 Alain Vigne <avigne@fedoraproject.org> 1.2.0-1
- upstream release 1.2.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Petr Šabata <contyk@redhat.com> - 1.0.9-1
- 1.0.9 bump
- Addresses CVE-2019-11411, CVE-2019-11412 and CVE-2019-11413

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-2
- Fix build flags so debuginfo is generated
- Compile with fPIC

* Thu Sep 27 2018 Michael J Gruber <mjg@fedoraproject.org> - 1.0.4-1
* Upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20180129git25821e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20180129git25821e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Petr Šabata <contyk@redhat.com> - 0-11.20180129git25821e6
- Fix CVE-2018-5759, rhbz#1539514

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20170124git4006739
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20170124git4006739
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Petr Šabata <contyk@redhat.com> - 0-8.20170124git4006739
- Include the latest upstream Fixes
- Fixes CVE-2016-10132, CVE-2016-10133, CVE-2016-10141, CVE-2017-5627 and
  CVE-2017-5628

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20161031gita0ceaf5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Petr Šabata <contyk@redhat.com> - 0-6.20161031gita0ceaf5
- Include the latest upstream fixes
- Fixes CVE-2016-9108, CVE-2016-9109, CVE-2016-9017 and CVE-2016-9294

* Thu Sep 29 2016 Petr Šabata <contyk@redhat.com> - 0-5.20160921git5c337af
- Update to the upstream master HEAD
- Fixes CVE-2016-7563 and CVE-2016-7564

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20150929git0827611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Petr Šabata <contyk@redhat.com> - 0-1.20150929git0827611
- Update to 0827611.
- Package the docs directory

* Thu Sep 17 2015 Petr Šabata <contyk@redhat.com> - 0-4.20150202gitc1ad1ba
- Enable full RELRO

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.20150202gitc1ad1ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Petr Šabata <contyk@redhat.com> - 0-2.20150202gitc1ad1ba
- Address the reviewer's concerns

* Thu May 07 2015 Petr Šabata <contyk@redhat.com> - 0-1.20150202gitc1ad1ba
- Initial packaging
