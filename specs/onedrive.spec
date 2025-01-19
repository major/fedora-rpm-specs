%global project abraunegg
%global repo onedrive

Name:           onedrive
Version:        2.5.3
Release:        4%{?dist}
Summary:        OneDrive Free Client written in D
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/%{project}/%{repo}
Source0:        %{url}/archive/v%{version}/%{repo}-v%{version}.tar.gz
BuildRequires: make
BuildRequires:  ldc
BuildRequires:  libcurl-devel
BuildRequires:  libnotify-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd
Requires(preun): systemd
ExclusiveArch:  %{ldc_arches}
Patch0: Fix-unable-to-parse-SSL-version.patch

%description
Free CLI client for Microsoft OneDrive written in D.

%prep
%setup -q -n %repo-%{version}
%patch -P 0 -p 1
# sed -i 's|version ||g' Makefile
# sed -i '/chown/d' Makefile.in
sed -i 's/-o root -g users//g' Makefile.in
sed -i 's/-o root -g root//g' Makefile.in
# sed -i '/git/d' Makefile
sed -i "s|std\.c\.|core\.stdc\.|" src/sqlite.d
echo %{version} > version

%build
%configure --enable-notifications
export DFLAGS="%{_d_optflags}"
export PREFIX="%{_prefix}"
make DC=ldmd2 %{?_smp_mflags}

%install
%make_install \
    PREFIX="%{_prefix}"
chmod a-x %{buildroot}/%{_mandir}/man1/%{name}*

%preun
%systemd_user_preun %{name}.service
%systemd_preun %{name}@.service

%files
%doc readme.md LICENSE changelog.md
%{_bindir}/%{name}
%if 0%{?el8} || 0%{?el9}
%{_unitdir}/%{name}.service
%else
%{_userunitdir}/%{name}.service
%endif
%{_unitdir}/%{name}@.service
%{_mandir}/man1/%{name}.1.gz
%{_docdir}/%{name}
%config %{_sysconfdir}/logrotate.d/onedrive

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Kalev Lember <klember@redhat.com> - 2.5.3-3
- Rebuilt for ldc 1.40

* Fri Nov 22 2024 Zamir SUN <sztsian@gmail.com> - 2.5.3-2
- Fix unable to parse SSL version

* Fri Nov 15 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3 (#2326647)

* Mon Oct 14 2024 Zamir SUN <sztsian@gmail.com> - 2.5.2-1
- Update to 2.5.2
- Fixes RHBZ#2315073 RHBZ#2258756

* Wed Sep 18 2024 Zamir SUN <sztsian@gmail.com> - 2.5.0-1
- Update to 2.5.0 (#2268779)

* Tue Aug 06 2024 Kalev Lember <klember@redhat.com> - 2.4.25-9
- Rebuilt for ldc 1.39

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.25-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 17 2023 Kalev Lember <klember@redhat.com> - 2.4.25-4
- Rebuilt for ldc 1.35

* Mon Jul 24 2023 Kalev Lember <klember@redhat.com> - 2.4.25-3
- Rebuilt for ldc 1.33

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 21 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.4.25-1
- Update to 2.4.25 (#2216391)

* Wed Mar 15 2023 Kalev Lember <klember@redhat.com> - 2.4.23-3
- Rebuilt for ldc 1.32

* Thu Feb 23 2023 Zamir SUN <sztsian@gmail.com> - 2.4.23-2
- Support EPEL8

* Mon Feb 06 2023 Zamir SUN <sztsian@gmail.com> - 2.4.23-1
- Update to 2.4.23

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 13 2022 Zamir SUN <sztsian@gmail.com> - 2.4.21-1
- Update to 2.4.21

* Sat Aug 13 2022 Zamir SUN <sztsian@gmail.com> - 2.4.20-1
- Update to 2.4.20

* Wed Jul 27 2022 Kalev Lember <klember@redhat.com> - 2.4.19-3
- Rebuilt for ldc 1.30

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Zamir SUN <sztsian@gmail.com> - 2.4.19-1
- Update to 2.4.19

* Fri Jun 03 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.4.18-1
- Update to 2.4.18 (#2093172)

* Sat Apr 30 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.4.17-1
- Update to 2.4.17 (#2080550)

* Thu Mar 10 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.4.16-1
- Update to 2.4.16 (#2036387)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.4.14-1
- Update to 2.4.14 (#2026496)

* Tue Aug 17 2021 Kalev Lember <klember@redhat.com> - 2.4.13-4
- Rebuilt for ldc 1.27

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Zamir SUN <sztsian@gmail.com> - 2.4.13-2
- Fix rpath issue

* Wed Jul 14 2021 Marcel <34819524+MarcelCoding@users.noreply.github.com> - 2.4.13-1
- Update to 2.4.13

* Fri Jul 02 2021 Marcel <34819524+MarcelCoding@users.noreply.github.com> - 2.4.12-1
- Update to 2.4.12

* Mon Feb 22 2021 Kalev Lember <klember@redhat.com> - 2.4.8-3
- Rebuilt for ldc 1.25

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Zamir SUN <sztsian@gmail.com> - 2.4.8-1
- Update to 2.4.8 to apply more fixes

* Sat Nov 28 2020 Zamir SUN <sztsian@gmail.com> - 2.4.7-1
- Update to 2.4.7

* Fri Aug 21 2020 Kalev Lember <klember@redhat.com> - 2.4.5-2
- Rebuilt for ldc 1.23

* Sat Aug 15 2020 Zamir SUN <sztsian@gmail.com> - 2.4.5-1
- Update to 2.4.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Thomas Drake-Brockman <thomas@drake-brockman.id.au> - 2.4.2-1
- Update to 2.4.2 (#1840773)

* Mon May 18 2020 Zamir SUN <sztsian@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Sun Apr 19 2020 Alan Pevec <alan.pevec@redhat.com> 2.4.0-1
- Update to 2.4.0

* Mon Feb 10 2020 Kalev Lember <klember@redhat.com> - 2.3.12-3
- Rebuilt for ldc 1.20

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Thomas Drake-Brockman <thom@sfedb.com> - 2.3.12-1
- Update to 2.3.12

* Wed Oct 02 2019 Zamir SUN <sztsian@gmail.com> - 2.3.10-1
- Update to 2.3.10

* Mon Aug 19 2019 David Va <davidva@tuta.io> - 2.3.8-1
- Update to 2.3.8 for bug fixes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 2019 Thomas Drake-Brockman <thom@sfedb.com> - 2.3.7-1
- Update to 2.3.7 for bug fixes

* Thu Jun 20 2019 Zamir SUN <zsun@fedoraproject.org> - 2.3.5-1
- Update to 2.3.5 to apply some more fixes

* Sat Jun 15 2019 Zamir SUN <zsun@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4 for bug fixes

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 2.3.2-2
- Rebuilt for ldc 1.15

* Wed Apr 03 2019 Zamir SUN <zsun@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2 to bring in bugfixes.
- Resolves: 1695392

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2.2.1-5
- Remove obsolete requirement for %%post scriptlet

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 2.2.1-4
- Rebuilt for ldc 1.14

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Zamir SUN <sztsian@gmail.com> - 2.2.1-2
- Add the source tarball

* Tue Dec 04 2018 Zamir SUN <sztsian@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Fri Nov 30 2018 Zamir SUN <sztsian@gmail.com> - 2.2.0-1
- Switch upstream to more active fork in https://github.com/abraunegg/onedrive
- Update to 2.2.0

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 1.1.1-6
- Rebuilt for ldc 1.12

* Sun Aug 05 2018 Thomas Drake-Brockman <thom@sfedb.com> - 1.1.1-5
- Patch src/sqlite.d to use core.stc instead of std.c

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 1.1.1-3
- Rebuilt for ldc 1.11

* Fri Feb 23 2018 Thomas Drake-Brockman <thom@sfedb.com> - 1.1.1-2
- Bump release for rebuild on f28 branch

* Tue Feb 20 2018 Thomas Drake-Brockman <thom@sfedb.com> - 1.1.1-1
- Update to upstream version 1.1.1
- Remove %check because upstream removed the unittest action from Makefile

* Mon Feb 19 2018 Kalev Lember <klember@redhat.com> - 1.0.1-3
- Rebuilt for ldc 1.8

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Zamir SUN <sztsian@gmail.com> 1.0.1-1
- Update to upstream release version 1.0.1

* Tue Oct 25 2016 mosquito <sensor.wen@gmail.com> 0.1.1-2.giteb8d0fe
- add BReq systemd

* Thu Oct 20 2016 Zamir SUN <sztsian@gmail.com> 0.1.1-1.giteb8d0fe
- initial package
