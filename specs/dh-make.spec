Name:           dh-make
# Squeeze
Version:        2.202402

Release:        4%{?dist}
Summary:        Tool that converts source archives into Debian package source

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://tracker.debian.org/pkg/dh-make
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
BuildArch:      noarch
BuildRequires:      perl-generators

Requires:       debhelper
Requires:       dpkg-dev
Requires:       %{_bindir}/make

%description
This package allows you to take a standard (or upstream) source
package and convert it into a format that will allow you to build
Debian packages.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/debhelper/dh_make/
install -m 755 dh_make.py %{buildroot}/%{_bindir}/dh_make
install -m 755 dh_makefont %{buildroot}/%{_bindir}
cp -a lib/* %{buildroot}/%{_datadir}/debhelper/dh_make/

# Fix permissions of rules files
find %{buildroot}/%{_datadir}/debhelper/dh_make \
	-type f -name 'rules*' \
	-exec chmod 755 '{}' ';'

find %{buildroot}/%{_datadir}/debhelper/dh_make/debian \
	-type f -name '*.ex' \
	-exec chmod 755 '{}' ';'

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 -p dh_make.1 %{buildroot}/%{_mandir}/man1

%files
%doc debian/README.Debian
%{_bindir}/dh_make
%{_bindir}/dh_makefont
%{_mandir}/man1/*.1*
%dir %{_datadir}/debhelper
%{_datadir}/debhelper/dh_make

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.202402-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.202402-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.202402-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 27 2024 Packit <hello@packit.dev> - 2.202402-1
- Update to version 2.202402
- Resolves: rhbz#2283566

* Fri May 10 2024 Packit <hello@packit.dev> - 2.202401-1
- Update to version 2.202401
- Resolves: rhbz#2273872

* Tue Feb 20 2024 Sérgio Basto <sergio@serjux.com> - 2.202304-1
- Update dh-make to 2.202304 (#2247136)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.202302-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.202302-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 03 2023 Sérgio Basto <sergio@serjux.com> - 2.202302-1
- Update dh-make to 2.202302 (#2229051)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.202301-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Sérgio Basto <sergio@serjux.com> - 2.202301-1
- Update dh-make to 2.202301 (#2156634)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.202204-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Sérgio Basto <sergio@serjux.com> - 2.202204-1
- Update dh-make to 2.202204 (#2135135)

* Thu Sep 29 2022 Sérgio Basto <sergio@serjux.com> - 2.202203-1
- Update dh-make to 2.202203 (#2127660)

* Tue Aug 09 2022 Sérgio Basto <sergio@serjux.com> - 2.202202-1
- Update dh-make to 2.202202 (#2106157)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.202201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 05 2022 Sérgio Basto <sergio@serjux.com> - 2.202201-1
- Update dh-make to 2.202201 (#2085522)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.202102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 01 2021 Sérgio Basto <sergio@serjux.com> - 2.202102-1
- Update dh-make to 2.202102 (#1997830)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.202003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.202003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.202003-1
- Update to 2.202003 (#1869057)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.202001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 29 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.202001-1
- Update to 2.202001 (#1808626)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.201903-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.201903-1
- Update to 2.201903 (#1771187)

* Sun Oct 13 2019 Sérgio Basto <sergio@serjux.com> - 2.201902-1
- Update to dh-make-2.201902 (#1742709)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.201801-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.201801-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Sérgio Basto <sergio@serjux.com> - 2.201801-1
- Update to 2.201801 (#1589433)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.201701-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.201701-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Sérgio Basto <sergio@serjux.com> - 2.201701-1
- Update to 2.201701 (#1527706)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.201608-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.201608-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Sérgio Basto <sergio@serjux.com> - 2.201608-1
- Update dh-make to 2.201608 (#1297114)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20140617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 27 2015 Sérgio Basto <sergio@serjux.com> - 1.20140617-1
- Update to dh-make_1.20140617 (Debian 8 stable).
- Some spec clean up.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.61-2
- Perl 5.18 rebuild

* Thu May 23 2013 Oron Peled <oron@actcom.co.il> - 0.61-1
- Upstream bumped to latest Debian/wheezy version
- Update for 'dpkg >= 1.16.x' (Requires: dpkg-dev)
- Don't install the whole ./debian/ directory as doc, only README.Debian
- Fix permissions of all 'rules*' templates

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Oron Peled <oron@actcom.co.il> - 0.55-2
- Minor changes to spec file: glob man pages, don't specify compression.

* Sun Oct 10 2010 Oron Peled <oron@actcom.co.il> - 0.55-1
- Bump to Squeeze version (0.55) as per review.

* Sat Jul 17 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.46-2
- Fix package during review (#591192)

* Tue May 11 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.46-1
- First package
