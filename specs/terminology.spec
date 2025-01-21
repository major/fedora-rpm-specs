Name:           terminology
Version:        1.13.0
Release:        8%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Summary:        EFL based terminal emulator
Url:            http://www.enlightenment.org
Source0:        https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  desktop-file-utils
BuildRequires:  efl-devel >= 1.26
BuildRequires:  gettext-devel autoconf automake libtool
BuildRequires:  meson
BuildRequires:  ninja-build
Suggests:       terminus-fonts
Suggests:       xorg-x11-fonts-misc

%if 0%{?el8} > 0
ExcludeArch: s390x
%endif

%description
Fast and lightweight terminal emulator using EFL libraries.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

#Remove fonts that already exist in Fedora
rm -rf %{buildroot}%{_datadir}/terminology/fonts/10x20.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/4x6.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/5x7.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/5x8.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/6x10.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/6x12.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/6x13.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/6x9.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/7x13.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/7x14.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/8x13.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/9x15.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/9x18.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/terminus-*

desktop-file-validate %{buildroot}/%{_datadir}/applications/terminology.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc README.md COPYING
%{_mandir}/man1/*
%{_bindir}/tyalpha
%{_bindir}/tybg
%{_bindir}/tycat
%{_bindir}/tyls
%{_bindir}/typop
%{_bindir}/tyq
%{_bindir}/tysend
%{_bindir}/terminology
%{_datadir}/applications/terminology.desktop
%{_datadir}/icons/hicolor/128x128/apps/terminology.png
%{_datadir}/terminology


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.13.0-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Ding-Yi Chen <dchen@redhat.com> -1.13.0-4
- Build for EPEL 9
- The fonts packages are optional, thus change them to Suggests.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0 (#2150085)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Conrad Meyer <cem@FreeBSD.org> - 1.12.1-1
- Update to 1.12.1 (#2022499)

* Mon Jan 03 2022 Conrad Meyer <cem@FreeBSD.org> - 1.12.0-1
- Update to 1.12.0 (#2022499)
- Bump EFL depend to 1.26 per upstream

* Thu Oct 21 2021 Ding-Yi Chen <dchen@redhat.com> - 1.10.0-2
- ExcludeArch s390x because of missing dependencies

* Wed Oct 20 2021 Ding-Yi Chen <dchen@redhat.com> - 1.10.0-1
- Upstream update to 1.10.0
- Fixes RHBZ #1917603 - terminology-1.10.0 is available
- Remove BuildRequired elementary-devel because it is merged into efl-devel

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Tom Callaway <spot@fedoraproject.org> - 1.9.0-1
- update to 1.9.0

* Mon Aug 17 2020 Tom Callaway <spot@fedoraproject.org> - 1.8.1-1
- update to 1.8.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Conrad Meyer <cem@FreeBSD.org> - 1.7.0-1
- update to 1.7.0 (#1833812)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Tom Callaway <spot@fedoraproject.org> - 1.6.0-1
- update to 1.6.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Conrad Meyer <cemeyer@uw.edu> - 1.4.1-1
- Update to latest upstream 1.4.1
- Fix rhbz# 1713806

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.4.0-2
- Rebuild with Meson fix for #1699099

* Mon Apr 08 2019 Conrad Meyer <cemeyer@uw.edu> - 1.4.0-1
- Update to latest upstream
- Fix rhbz# 1694425

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Conrad Meyer <cemeyer@uw.edu> - 1.3.2-1
- Update to latest upstream
- Fix rhbz# 1659977 (CVE)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Conrad Meyer <cemeyer@uw.edu> - 1.2.1-1
- Update to 1.2.1
- rhbz# 1578178

* Sun Apr 15 2018 Conrad Meyer <cemeyer@uw.edu> - 1.2.0-1
- Update to 1.2.0
- Buildsystem has changed to use meson.  Adapt, following https://fedoraproject.org/wiki/Packaging:Meson .

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.0-3
- apply upstream fix for font sizing issue (T5012)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.0-1
- update to 1.0.0

* Thu Dec  1 2016 Tom Callaway <spot@fedoraproject.org> - 0.9.1-8.20161129git6cc0abd
- Update to git latest, since upstream has forgotten how to do a proper release

* Fri Jul 15 2016 Ding-Yi Chen <dchen@redhat.com> - 0.9.1-7
- Rebuild for efl-1.17.2

* Mon Mar 14 2016 Ding-Yi Chen <dchen@redhat.com> - 0.9.1-6
- Rebuild for efl-1.17.0

* Fri Mar 04 2016 Conrad Meyer <cemeyer@uw.edu> - 0.9.1-5
- Pull bugfix from terminology git to fix issue users may be hitting in the
  field: https://retrace.fedoraproject.org/faf/reports/997237/

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Ding-Yi Chen <dchen@redhat.com> - 0.9.1-3
- rebuild for efl-1.16.1

* Tue Nov 10 2015 Tom Callaway <spot@fedoraproject.org> - 0.9.1-2
- rebuild for new EFL

* Mon Sep 28 2015 Tom Callaway <spot@fedoraproject.org> - 0.9.1-1
- update to 0.9.1

* Tue Sep  8 2015 Tom Callaway <spot@fedoraproject.org> - 0.9.0-1
- update to 0.9.0

* Thu Aug 13 2015 Tom Callaway <spot@fedoraproject.org> - 0.8.0-5
- bump to rebuild with new EFL

* Sat Jul 11 2015 Conrad Meyer <cemeyer@uw.edu> - 0.8.0-4
- Bump to rebuild with new EFL (rh #1242166)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  1 2015 Tom Callaway <spot@fedoraproject.org> - 0.8.0-2
- dep on efl-devel

* Sun Feb 15 2015 Conrad Meyer <cemeyer@uw.edu> - 0.8.0-1
- Update to new upstream 0.8.0

* Mon Oct 13 2014 Conrad Meyer <cemeyer@uw.edu> - 0.7.0-1
- Update to new upstream 0.7.0 (now with localization)
- Add gettext BR per packaging guidelines on locale files
- Use %%find_lang per packaging guidelines on locale files

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Conrad Meyer <cemeyer@uw.edu> - 0.6.1-1
- Update to 0.6.1

* Thu Jul 03 2014 Conrad Meyer <cemeyer@uw.edu> - 0.6.0-1
- Update to 0.6.0 for numerous bugfixes, including the annoying T627
  (https://phab.enlightenment.org/T627)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 10 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0 (thanks Conrad Meyer)

* Sun Oct 13 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 0.3.0-3
- Remove post scriptlets as per review.

* Wed Oct 09 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 0.3.0-2
- Remove bundled fonts that already exist in Fedora.
- Add icon and desktop scriptlets

* Tue Oct 08 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
- Fix license
- Update BRs

* Wed Jan 02 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.0-1
- initial spec
