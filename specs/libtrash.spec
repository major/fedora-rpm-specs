Summary:       Libraries to move files to a trash-folder on delete
Name:          libtrash
Version:       3.8
Release:       5%{?dist}
License:       GPL-2.0-or-later

URL:           https://pages.stern.nyu.edu/~marriaga/software/libtrash
Source:        https://pages.stern.nyu.edu/~marriaga/software/libtrash/%{name}-%{version}.tgz

Patch0:        libtrash-3.2-defaults.patch
Patch1:        libtrash-3.3-license.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make

%description
Libtrash is the shared library which, when preloaded, implements a trash
can under GNU/Linux. Through the interception of function calls which
might lead to accidental data loss libtrash effectively ensures that your
data remains protected from your own mistakes.

%package devel
Summary: Libraries to move files to a trash-folder on delete
Requires: libtrash%{?_isa} = %{version}-%{release}

%description devel
This package contains the libtrash.so dynamic library which, when preloaded,
implements a trash can under GNU/Linux.

%prep
%autosetup -p1
mkdir -p m4

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

# remove useless *.la files
rm -f %{buildroot}%{_libdir}/libtrash.la

# remove empty file
rm -f %{buildroot}%{_docdir}/%{name}/AUTHORS

# remove installed build documentation
rm -f %{buildroot}%{_docdir}/%{name}/{BUILD,INSTALL}

%files
%doc ChangeLog config.txt NEWS README.md TODO
%license COPYING
%config(noreplace) %{_sysconfdir}/libtrash.conf
%{_libdir}/libtrash.so.*

%files devel
%{_libdir}/libtrash.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Lukáš Zaoral <lzaoral@redhat.com> - 3.8-1
- rebase to latest version (rhbz#2257191)

* Wed Jan 03 2024 Florian Weimer <fweimer@redhat.com> - 3.7-5
- Fix C compatibility issue (#2256620)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Lukáš Zaoral <lzaoral@redhat.com> - 3.7-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Lukáš Zaoral <lzaoral@redhat.com> - 3.7-1
- Update to the latest upstream release
  * Replace custom build scripts with autotools (new in 3.7)
  * Drop unused patches
  * Update BuildRequires
- Fix requires for the devel subpackage
- Install license to the right place
- Use correct release tag
- Use https in links

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Kamil Dudka <kdudka@redhat.com> - 3.6-1
- update to new upstream release

* Tue Aug 04 2020 Kamil Dudka <kdudka@redhat.com> - 3.5-1
- use `readelf -s -W` to avoid truncation of long symbol names (#1864057)
- update to new upstream release

* Tue Aug 04 2020 Kamil Dudka <kdudka@redhat.com> - 3.3-17
- require perl(English) for build (#1864057)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com> - 3.3-10
- enforce use of python3 during the build
- add explicit BR for the gcc compiler

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 08 2016 Kamil Dudka <kdudka@redhat.com> - 3.3-5
- update FSF addresss in the license file to silence rpmlint

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Kamil Dudka <kdudka@redhat.com> - 3.3-1
- update to new upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Kamil Dudka <kdudka@redhat.com> - 3.2-14
- avoid symbol clashes when loading audacious plug-ins (#1096443)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 22 2009 Zdenek Prikryl <zprikryl@redhat.com> 3.2-7
- Fixed usage of RPM_OPT_FLAGS

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-5
- Fixed permissions on config file

* Wed Jul 09 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-4
- Added documentation to devel package
- Minor spec clean up

* Wed Jul 02 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-3
- Create devel package

* Tue Jul 01 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-2
- Package for Fedora 10

* Thu Mar 06 2008 Zdenek Prikryl <zprikryl@redhat.com> 3.2-1
- Package for Fedora 9

