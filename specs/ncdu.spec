# Fix FTBFS due to `zig build` being called with non-existent system package directory:
#
#   + /usr/bin/zig build [...] --system /builddir/build/BUILD/ncdu-2.7-build/zig-cache/p [...]
#   error: unable to open system package directory '/builddir/build/BUILD/ncdu-2.7-build/zig-cache/p': FileNotFound
#
# See:
#
#   https://src.fedoraproject.org/rpms/zig/c/c8cfc2b53dd82650111a94a5facd984f9251b15c?branch=rawhide
#
%undefine _zig_system_integration

Name:           ncdu
Version:        2.7
Release:        2%{?dist}
Summary:        Text-based disk usage viewer

License:        MIT
URL:            https://dev.yorhel.nl/ncdu/
Source0:        https://dev.yorhel.nl/download/ncdu-%{version}.tar.gz
Source1:        https://dev.yorhel.nl/download/ncdu-%{version}.tar.gz.asc
Source2:        https://yorhel.nl/key.asc

Patch0:         ncdu-allow-shlib-undefined.patch

ExclusiveArch:  %{zig_arches}

BuildRequires:  make
BuildRequires:  zig
BuildRequires:  zig-rpm-macros
BuildRequires:  gnupg2
BuildRequires:  ncurses-devel
BuildRequires:  libzstd-devel

%description
ncdu (NCurses Disk Usage) is a curses-based version of the well-known 'du',
and provides a fast way to see what directories are using your disk space.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n ncdu-%{version}
%patch -P0 -p1

%build
%zig_build -Dpie

%install
%zig_install -Dpie
%{__make} install-doc PREFIX=%{buildroot}%{_prefix}

%files
%{_mandir}/man1/ncdu.1*
%doc ChangeLog
%license LICENSES/MIT.txt
%{_bindir}/ncdu

%changelog
* Fri Jan 03 2025 Richard Fearn <richardfearn@gmail.com> - 2.7-2
- Fix FTBFS due to `zig build` being called with non-existent system package directory

* Fri Nov 29 2024 Richard Fearn <richardfearn@gmail.com> - 2.7-1
- Update to 2.7

* Sat Nov 23 2024 Richard Fearn <richardfearn@gmail.com> - 1.21-1
- Update to 1.21

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 21 2024 Richard Fearn <richardfearn@gmail.com> - 1.20-1
- Update to 1.20

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Richard Fearn <richardfearn@gmail.com> - 1.19-1
- Update to 1.19

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Todd Zullinger <tmz@pobox.com> - 1.18-3
- verify upstream signatures in %%prep
- use %%make_build and %%make_install macros

* Tue Dec 27 2022 Richard Fearn <richardfearn@gmail.com> - 1.18-2
- Use SPDX license identifier

* Fri Dec 09 2022 Richard Fearn <richardfearn@gmail.com> - 1.18-1
- Update to 1.18 (#2151357)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 02 2022 Richard Fearn <richardfearn@gmail.com> - 1.17-1
- Update to 1.17

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Richard Fearn <richardfearn@gmail.com> - 1.16-1
- Update to 1.16 (#1978657)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Richard Fearn <richardfearn@gmail.com> - 1.15.1-1
- Update to new upstream version 1.15.1 (#1842015)

* Sat May 30 2020 Richard Fearn <richardfearn@gmail.com> - 1.15-1
- Update to new upstream version 1.15 (#1842015)

* Tue Feb 11 2020 Richard Fearn <richardfearn@gmail.com> - 1.14.2-1
- Update to new upstream version 1.14.2
- Drop gcc 10 patch

* Sun Feb 02 2020 Richard Fearn <richardfearn@gmail.com> - 1.14.1-4
- Use %%license

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Richard Fearn <richardfearn@gmail.com> - 1.14.1-2
- Enable compilation with gcc 10

* Sun Aug 11 2019 Richard Fearn <richardfearn@gmail.com> - 1.14.1-1
- Update to new upstream version 1.14.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Richard Fearn <richardfearn@gmail.com> - 1.14-1
- Update to new upstream version 1.14 (#1672365)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Richard Fearn <richardfearn@gmail.com> - 1.13-3
- Add BuildRequires: gcc
  (see https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Richard Fearn <richardfearn@gmail.com> - 1.13-1
- Update to new upstream version 1.13 (#1539676)
- Use %%{version} macro in source URL

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 1.12-6
- Remove unnecessary Group: tag

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Richard Fearn <richardfearn@gmail.com> - 1.12-2
- Don't assume man page compression method will be gzip

* Sat Aug 27 2016 Richard Fearn <richardfearn@gmail.com> - 1.12-1
- Update to new upstream version 1.12 (#1370824)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 07 2015 Richard Fearn <richardfearn@gmail.com> - 1.11-1
- Update to new upstream version 1.11 (#1209036)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Richard Fearn <richardfearn@gmail.com> - 1.10-1
- update to new upstream version 1.10 (#962116)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 30 2012 Richard Fearn <richardfearn@gmail.com> - 1.9-1
- update to new upstream version 1.9

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Richard Fearn <richardfearn@gmail.com> - 1.8-1
- update to new upstream version 1.8

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 04 2011 Richard Fearn <richardfearn@gmail.com> - 1.7-1
- update to new upstream version 1.7
- remove unnecessary bits from spec

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 28 2009 Richard Fearn <richardfearn@gmail.com> - 1.6-1
- update to new upstream version 1.6

* Sun Jul 26 2009 Richard Fearn <richardfearn@gmail.com> - 1.5-1
- update to new upstream version 1.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Richard Fearn <richardfearn@gmail.com> - 1.4-1
- new upstream version

* Fri Apr 25 2008 Richard Fearn <richardfearn@gmail.com> - 1.3-2
- remove unnecessary Requires:
- use %%configure macro instead of ./configure
- don't need to mark man page as %%doc
- make package summary more descriptive

* Sat Mar  1 2008 Richard Fearn <richardfearn@gmail.com> - 1.3-1
- initial package for Fedora
