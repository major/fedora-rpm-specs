Name: xmp
Version: 4.2.0
Release: 5%{?dist}
Summary: A multi-format module player
Source0: https://downloads.sourceforge.net/project/xmp/xmp/%{version}/xmp-%{version}.tar.gz
# use pulseaudio output by default
Patch0: xmp-pulse.patch
License: GPL-2.0-or-later
URL: http://xmp.sourceforge.net/
BuildRequires: make
Buildrequires: alsa-lib-devel
BuildRequires:  gcc
BuildRequires: libxmp-devel >= 4.4.0
BuildRequires: pulseaudio-libs-devel

%description
This is the Extended Module Player, a portable module player that plays
over 90 mainstream and obscure module formats, including Protracker MOD,
Fasttracker II XM, Scream Tracker 3 S3M and Impulse Tracker IT files.

%prep
%autosetup -p1

%build
%configure \
  --enable-pulseaudio \

%make_build

%install
%make_install

%files
%license COPYING
%doc Changelog CREDITS README girl_from_mars.xm
%dir %{_sysconfdir}/xmp
%config(noreplace) %{_sysconfdir}/xmp/xmp.conf
%config(noreplace) %{_sysconfdir}/xmp/modules.conf
%{_bindir}/xmp
%{_mandir}/man1/xmp.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Dominik Mierzejewski <dominik@greysector.net> - 4.2.0-1
- update to 4.2.0 (#2216922)
- drop obsolete patch
- update License tag with SPDX identifier

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 4.1.0-2
- fix path to xmp.conf (#1365321)
- include the shipped sample module as doc

* Mon Aug 01 2016 Dominik Mierzejewski <rpm@greysector.net> - 4.1.0-1
- update to 4.1.0
- libxmp 4.4.0 is required

* Mon Mar 07 2016 Dominik Mierzejewski <rpm@greysector.net> - 4.0.11-1
- update to 4.0.11
- use https for source URL
- tighten file list and use license macro

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 08 2014 Dominik Mierzejewski <rpm@greysector.net> - 4.0.10-1
- update to 4.0.10
- update minimum libxmp requirement

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Dominik Mierzejewski <rpm@greysector.net> - 4.0.8-1
- update to 4.0.8

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Dominik Mierzejewski <rpm@greysector.net> - 4.0.7-1
- update to 4.0.7
- remove obsolete specfile parts

* Wed Oct 30 2013 Dominik Mierzejewski <rpm@greysector.net> - 4.0.6-1
- update to 4.0.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Dominik Mierzejewski <rpm@greysector.net> - 4.0.5-1
- update to 4.0.5
- drop all patches
- Audacious plugin moved to a separate package
- XMMS plugin no longer available
- patch to use pulseaudio by default

* Sun Apr 28 2013 Dominik Mierzejewski <rpm@greysector.net> - 3.5.0-3
- fix build against audacious 3.4 (empty pkg-config --cflags is not an error)
- backport fix for CVE-2013-1890 (rhbz #954658)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 05 2012 Dominik Mierzejewski <rpm@greysector.net> - 3.5.0-1
- updated to 3.5.0
- rebased 3.3 API patch

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 3.4.0-11
- Rebuild for Audacious 3.3-alpha1 generic plugin API/ABI bump.
- Patch for Audacious 3.3-alpha1 API changes.

* Fri Jun 15 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 3.4.0-10
- Fix untimely g_free(filename) calls in Audacious 3 plugin and
  make module probing thread-safe.

* Mon Jun  4 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 3.4.0-7
- Fix undefined symbol corner-case for Audacious 3.2 API (#825937).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 3.4.0-5
- Rebuild for Audacious 3.2-beta1 generic plugin API/ABI bump.
- Update Audacious 3.1 Preferences API patch for header changes.

* Sat Dec 24 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 3.4.0-4
- Rebuild for Audacious 3.2-alpha1 generic plugin API/ABI bump.

* Wed Oct 26 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 3.4.0-3
- Rebuild for Audacious 3.1-beta3 generic plugin API/ABI bump.

* Wed Oct 12 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 3.4.0-2
- Port to Audacious 3.1 Preferences API.
- Rebuild for Audacious 3.1-beta1 generic plugin API/ABI bump.
- Depend on audacious(plugin-api)%%{?_isa}.

* Wed Aug 10 2011 Dominik Mierzejewski <rpm@greysector.net> 3.4.0-1
- update to 3.4.0
- drop obsolete patches

* Thu Jul  7 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 3.3.0-8
- Rewrite the Audacious plugin for Audacious 3.0 Preferences Widgets.

* Sun Mar 27 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 3.3.0-7
- Rewrite the Audacious plugin for Audacious 2.5.
- Verbose build log with V=1 make.
- Update the audacious(plugin-api) stuff in the spec file for Audacious 2.5.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 3.3.0-5
- No build: wait for mass-rebuild in Rawhide.
- Enhance the audacious(plugin-api) stuff in the spec file.

* Fri Jan 28 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 3.3.0-4
- In audacious-plugin-xmp require a specific audacious(plugin-api).

* Mon Dec 13 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 3.3.0-3
- Rebuild for Audacious 2.4.2 generic plugin API/ABI bump.

* Thu Dec 09 2010 Dominik Mierzejewski <rpm@greysector.net> 3.3.0-2
- apply upstream patches to fix crash in audacious plugins (bug #660507)

* Sat Dec 04 2010 Dominik Mierzejewski <rpm@greysector.net> 3.3.0-1
- updated to 3.3.0
- drop obsolete patches

* Wed Jul 21 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 3.2.0-3
- Patch and rebuild for Audacious 2.4 beta1 generic plugin API/ABI bump.

* Thu Jul 15 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 3.2.0-2
- Rebuild for Audacious 2.4 alpha3 generic plugin API/ABI bump.

* Thu Jul 08 2010 Dominik Mierzejewski <rpm@greysector.net> 3.2.0-1
- updated to 3.2.0
- fixed compilation on rawhide

* Sun Jan 17 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 3.1.0-2
- Rebuild for audacious.pc --libs changes.

* Thu Jan 07 2010 Dominik Mierzejewski <rpm@greysector.net> 3.1.0-1
- updated to 3.1.0
- enabled parallel build
- dropped obsolete patches
- built with pulseaudio output support

* Thu Dec 31 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.7.1-2
- fix FTBFS (#539061), Audacious 2.2 iplugin API change
- fix Audacious plugin dialogs

* Mon Sep 14 2009 Dominik Mierzejewski <rpm@greysector.net> 2.7.1-1
- updated to 2.7.1
- dropped obsolete patch
- fixes CVE-2007-6731 (rhbz#523138) and CVE-2007-6732 (rhbz#523147)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.1-7
- patch further for Audacious 2, because the bmp_cfg_* symbols are gone
  since Audacious 1.5 already

* Sun Jul 19 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.1-6
- patch for Audacious 2 (xmp-2.5.1-audacious2.patch)

* Tue Jun 16 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.1-5
- rebuild for new libmowgli SONAME (audacious-plugin-xmp depends on it
  indirectly because of audacious-devel pkgconfig dep-chain)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 13 2008 Dominik Mierzejewski <rpm@greysector.net> 2.5.1-3
- add a script to create the free tarball
- drop workaround for missing audacious-devel Requires:

* Mon Jul 07 2008 Dominik Mierzejewski <rpm@greysector.net> 2.5.1-2
- repackaged source tarball without the OCL-licensed file

* Wed Jun 25 2008 Dominik Mierzejewski <rpm@greysector.net> 2.5.1-1
- initial build based on upstream spec
- disabled stripping upon install
- renamed player plugins to playername(-plugin)-xmp
- worked around missing BRs in audacious-devel in rawhide
- converted non-UTF8 docs
