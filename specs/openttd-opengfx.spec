%global realname opengfx
#global prever   alpha6

Name:           openttd-opengfx
Version:        7.1
Release:        10%{?prever:.%{prever}}%{?dist}
Summary:        OpenGFX replacement graphics for OpenTTD

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/OpenTTD/OpenGFX
Source0:        https://cdn.openttd.org/opengfx-releases/%{version}%{?prever:-%{prever}}/%{realname}-%{version}%{?prever:-%{prever}}-source.tar.xz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gimp
BuildRequires:  grfcodec
BuildRequires:  nml
BuildRequires:  python3
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
BuildRequires:  xwayland-run
%endif
Requires:       openttd


%description
OpenGFX is an open source graphics base set for OpenTTD which can completely
replace the TTD base set. The main goal of OpenGFX therefore is to provide a
set of free base graphics which make it possible to play OpenTTD without
requiring the (copyrighted) files from the TTD CD. This potentially increases
the OpenTTD fan base and makes it a true free game (with "free" as in both
"free beer" and "free speech").

As of version 0.2.0 OpenGFX has a full set of sprites. Future versions will aim
to improve the graphics. 


%prep
%setup -q -n %{realname}-%{version}%{?prever:-%{prever}}-source 

%build
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
# gimp-3 requires a display even in batch mode and additional arguments
xwfb-run -- make grf _V= PYTHON=/usr/bin/python3 GIMP_FLAGS="-n -i --quit --batch-interpreter plug-in-script-fu-eval"
%else
make grf _V= PYTHON=/usr/bin/python3
%endif


%install
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
# gimp-3 requires a display even in batch mode
xwfb-run -- make install _V= PYTHON=/usr/bin/python3 UNIX2DOS= \
    INSTALL_DIR=$RPM_BUILD_ROOT%{_datadir}/openttd/data \
    GIMP_FLAGS="-n -i --quit --batch-interpreter plug-in-script-fu-eval"
%else
make install _V= PYTHON=/usr/bin/python3 UNIX2DOS= INSTALL_DIR=$RPM_BUILD_ROOT%{_datadir}/openttd/data
%endif


%check
cp %{realname}-%{version}.check.md5 %{realname}-%{version}.md5
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
# gimp-3 requires a display even in batch mode
xwfb-run -- make check _V= PYTHON=/usr/bin/python3 GIMP_FLAGS="-n -i --quit --batch-interpreter plug-in-script-fu-eval"
%else
make check _V= PYTHON=/usr/bin/python3
%endif


%files
%license LICENSE
%doc changelog.txt docs/authoroverview.csv extra/ README.md
%{_datadir}/openttd/data/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 7.1-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Felix Kaechele <felix@kaechele.ca> - 7.1-1
- update to 7.1

* Tue Sep 14 2021 Felix Kaechele <felix@kaechele.ca> - 7.0-1
- update to 7.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 01 2021 Felix Kaechele <felix@kaechele.ca> - 0.6.1-1
- update to 0.6.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Felix Kaechele <heffer@fedoraproject.org> - 0.6.0-2
- fix docs
- fix make check

* Wed Apr 01 2020 Felix Kaechele <heffer@fedoraproject.org> - 0.6.0-1
- update to 0.6.0
- update Source and project home URL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Felix Kaechele <heffer@fedoraproject.org> - 0.5.5-4
- add python3 interpreter also to install step

* Sun Jul 28 2019 Felix Kaechele <heffer@fedoraproject.org> - 0.5.5-3
- fix build for F31

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Felix Kaechele <heffer@fedoraproject.org> - 0.5.5-1
- update to 0.5.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Felix Kaechele <heffer@fedoraproject.org> - 0.5.4-6
- add gcc BuildRequires
- some spec file gardening

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 30 2016 Felix Kaechele <heffer@fedoraproject.org> - 0.5.4-1
- update to 0.5.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.5.3-1
- update to 0.5.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.5.2-1
- update to 0.5.2
- Makefile.local is replaced by command line variables

* Sat Jun 21 2014 Felix Kaechele <heffer@fedoraproject.org> - 0.5.1-1
- update to 0.5.1
- upstream now only provides an xz tarball so change Source0 to that

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Felix Kaechele <heffer@fedoraproject.org> - 0.5.0-1
- update to 0.5.0

* Sun Dec 15 2013 Felix Kaechele <heffer@fedoraproject.org> - 0.4.7-1
- update to 0.4.7
- drop patch, it was upstreamed

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Felix Kaechele <heffer@fedoraproject.org> - 0.4.6.1-3
- fix gcc 4.8 patch

* Sat Mar 23 2013 Felix Kaechele <heffer@fedoraproject.org> - 0.4.6.1-2
- fix compilation on F19+
- specfile cleanups

* Thu Mar 14 2013 Felix Kaechele <heffer@fedoraproject.org> - 0.4.6.1-1
- update to 0.4.6.1
- remove unix2dos usage during compilation of docs
- enable verbosity

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Felix Kaechele <heffer@fedoraproject.org> - 0.4.5-1
- update to 0.4.5

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Felix Kaechele <heffer@fedoraproject.org> - 0.4.4-1
- update to 0.4.4
- use clean-gfx target to build completely from source

* Thu Mar 29 2012 Felix Kaechele <heffer@fedoraproject.org> - 0.4.3-1
- update to 0.4.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.3.7-1
- updated river sprites (0.3.6)
- added new sprites for nightly versions of OpenTTD

* Sat Sep 03 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.3.5-1
- update 0.3.5
- many bugfixes
- reworked aircarft sprites

* Sun Jun 12 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.3.4-1
- update to 0.3.4
- switch to xz tarball
- updated description

* Mon Apr 04 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.3.3-1
- bump version

* Wed Feb 09 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.3.2-1
- update to new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Felix Kaechele <heffer@fedoraproject.org> - 0.3.1-1
- new upstream release
- contains mostly packaging fixes and a fix for the load sprite
- removed empty sample.cat, openttd now gives a warning and offers
  to download a sound set
- sprites are complete as of 0.3.0

* Sun May 09 2010 Felix Kaechele <heffer@fedoraproject.org> - 0.2.4-1
- mainly fixes for train alignment
- now relying on 'make check' for data integrity checks

* Mon Mar 29 2010 Felix Kaechele <heffer@fedoraproject.org> - 0.2.2-1
- bugfix release 0.2.2
- major fixes to houses and their alignment
- re-worked maglev and monorail vehicles
- translations into multiple languages

* Sat Jan 02 2010 Felix Kaechele <felix@fetzig.org> - 0.2.1-1
- upstream bugfix release

* Fri Dec 11 2009 Felix Kaechele <felix@fetzig.org> - 0.2.0-1
- update to 0.2.0
- cleaned up docs

* Sat Oct 10 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.1.1-2
- Correct generation of grfs, using nforenum

* Sat Oct 10 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.1.1-1
- New upstream release 0.1.1
- Check md5sums of resulting files

* Sun Aug 23 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.1.0-0.1.alpha6
- new upstream release

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.alpha4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Felix Kaechele <heffer@fedoraproject.org> - 0-0.4.alpha4.2
- added md5 check

* Tue Apr 14 2009 Felix Kaechele <heffer@fedoraproject.org> - 0-0.3.alpha4.2
- now compiles from source

* Sun Mar 29 2009 Felix Kaechele <heffer@fedoraproject.org> - 0-0.2.alpha4.2
- improved macro usage
- touch sample.cat

* Sat Mar 21 2009 Felix Kaechele <heffer@fedoraproject.org> - 0-0.1.alpha4.2
- initial build

