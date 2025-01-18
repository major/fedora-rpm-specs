%global _hardened_build 1
%global beta    beta15

Name:           hddtemp
Version:        0.3
Release:        0.58.%{beta}%{?dist}
Summary:        Hard disk temperature tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://savannah.nongnu.org/projects/hddtemp/

Source0:        http://download.savannah.nongnu.org/releases/hddtemp/%{name}-%{version}-%{beta}.tar.bz2
Source1:        %{name}.db
Source2:        %{name}.service
Source3:        %{name}.sysconfig
Source4:        %{name}.pam
Source5:        %{name}.consoleapp

Patch0:         0001-Try-attribute-190-if-194-doesn-t-exist.patch
Patch1:         http://ftp.debian.org/debian/pool/main/h/hddtemp/hddtemp_0.3-beta15-53.diff.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=717479
# https://bugzilla.redhat.com/show_bug.cgi?id=710055
Patch2:         %{name}-0.3-beta15-autodetect-717479.patch
Patch3:         0001-Allow-binding-to-a-listen-address-that-doesn-t-exist.patch
Patch4:         fix-model-length.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1634377
Patch5:         ru.po.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1801116
Patch6:         %{name}-nvme.patch
Patch7:         hddtemp-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros
BuildRequires: make
Requires:       %{_bindir}/consolehelper


%description
hddtemp is a tool that gives you the temperature of your hard drive by
reading S.M.A.R.T. information.


%prep
%setup -q -n %{name}-%{version}-%{beta}

%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P0 -p1
%patch -P4 -p1
%patch -P5 -p0
%patch -P6 -p1
%patch -P7 -p1

sed -i -e 's|/etc/hddtemp.db|%{_datadir}/misc/hddtemp.db|' doc/hddtemp.8
chmod -x contribs/analyze/*
rm COPYING ; cp -p GPL-2 COPYING
cp -p debian/changelog changelog.debian


%build
%configure --disable-dependency-tracking
%make_build


%install
%make_install
# the real executable cannot go in %_sbindir since
# https://fedoraproject.org/wiki//Changes/Unify_bin_and_sbin
# as sbindir and bindir are now the same directory
mkdir -p %{buildroot}%{_libexecdir}
mv %{buildroot}%{_sbindir}/hddtemp %{buildroot}%{_libexecdir}
install -Dpm 644 %{S:1} %{buildroot}%{_datadir}/misc/hddtemp.db
install -Dpm 644 %{S:2} %{buildroot}%{_unitdir}/hddtemp.service
install -Dpm 644 %{S:3} %{buildroot}%{_sysconfdir}/sysconfig/hddtemp
install -dm 755 %{buildroot}%{_bindir}
ln -s consolehelper %{buildroot}%{_bindir}/hddtemp
install -Dpm 644 %{S:4} %{buildroot}%{_sysconfdir}/pam.d/hddtemp
install -Dpm 644 %{S:5} %{buildroot}%{_sysconfdir}/security/console.apps/hddtemp
%find_lang %{name}


%post
%systemd_post hddtemp.service

%preun
%systemd_preun hddtemp.service

%postun
%systemd_postun_with_restart hddtemp.service


%files -f %{name}.lang
%doc ChangeLog changelog.debian COPYING README TODO contribs/
%config(noreplace) %{_sysconfdir}/sysconfig/hddtemp
%config(noreplace) %{_sysconfdir}/pam.d/hddtemp
%config(noreplace) %{_sysconfdir}/security/console.apps/hddtemp
%{_unitdir}/hddtemp.service
%{_bindir}/hddtemp
%{_libexecdir}/hddtemp
%config(noreplace) %{_datadir}/misc/hddtemp.db
%{_mandir}/man8/hddtemp.8*


%changelog
* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3-0.58.beta15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.57.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.56.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.55.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.54.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.53.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  8 2022 Florian Weimer <fweimer@redhat.com> - 0.3-0.52.beta15
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.51.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.50.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.49.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-0.48.beta15
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.47.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 22 2020 Dominik Mierzejewski <rpm@greysector.net> - 0.3-0.46.beta15
- update Debian patch to latest
- drop obsolete patch
- fix Russian translation (#1634377)
- add support for NVME drives (#1801116)
- correct build depdendency for systemd macros
- use modern macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.45.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.44.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.43.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.42.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.41.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Dominik Mierzejewski <rpm@greysector.net> - 0.3-0.40.beta15
- use correct user context type to fix FTBFS (#1555871)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.39.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.38.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.37.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.36.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-0.35.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.34.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.33.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.32.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 07 2014 Jaromir Capik <jcapik@redhat.com> - 0.3-0.31.beta15
- Fixing the model string size [24 -> 40] (#1061649)

* Sat Jan 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.30.beta15
- Improve comments in database (#1054593, Edward Kuns).

* Sat Jan 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.29.beta15
- Patch to try attribute 190 if 194 doesn't exist for defaults (#1054593).
- Trim down database to just entries not covered by defaults.
- Add some Samsung SSD's lacking a sensor to the database.

* Thu Jan  9 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.28.beta15
- Patch to allow binding to a listen address that doesn't exist yet.
- Use systemd macros in scriptlets (#850145).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.27.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.26.beta15
- Drop obsolete After=syslog.target from systemd unit, add Documentation.
- Drop obsolete sysv to systemd migration scriptlets.
- Drop obsolete specfile constructs.
- Update Debian patch set to 0.3-beta15-52.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.25.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.23.beta15
- Build with hardening flags on.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.23.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 18 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.22.beta15
- Migrate to systemd, patch to glob usual device names w/o arguments (#717479).
- Update Debian patch set to 0.3-beta15-48, ship its changelog in docs.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.21.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.20.beta15
- Patch to fix ix86 build if sys/ucontext.h is pulled in by signal.h (#564857).

* Thu Aug 20 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.19.beta15
- Try to start daemon for all disks if none are specified in sysconfig.
- Update URLs.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.18.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.17.beta15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct  1 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.16.beta15
- Sync with Debian's 0.3-beta15-45 for a fix for undesired spin-ups with
  most current drives (#464912).

* Sat Feb  9 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.15.beta15
- Sync with Debian's 0.3-beta15-38.
- Update drive database to 2007-09-14.
- Trim pre-2006 changelog entries.

* Wed Sep  5 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.14.beta15
- Adjust server chkconfig start/stop priorities to start before gkrellmd,
  other cosmetic init script tweaks.
- Mark hddtemp.db as %%config(noreplace).

* Mon Aug  6 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.13.beta15
- License: GPLv2+

* Tue Jul 10 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.12.beta15
- Improve init script LSB compliance.

* Tue Jan  9 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.11.beta15
- SATA sense fix (#221100, Jens Axboe).

* Sun Dec 31 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.10.beta15
- Apply patches from Debian containing bunch of hddtemp.db updates and
  guess mode improvements for drives not in the database.

* Wed Aug 30 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.9.beta15
- Rebuild.

* Wed May  3 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.8.beta15
- 0.3-beta15, drive database 2006-04-26.
- Specfile cleanups.

* Wed Feb  8 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.8.beta14
- Update drive database to 2006-02-07.

* Wed Jan 18 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.3-0.7.beta14
- Update drive database to 2006-01-18.
- Init script is not a config file.
- Mark console.perms snippet as noreplace.
