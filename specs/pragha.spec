# Review request: https://bugzilla.redhat.com/show_bug.cgi?id=721043

# As pragha is building real plugins the following is needed, else the build fails:
%undefine _strict_symbol_defs_build

Name:           pragha
Version:        1.3.3
Release:        31%{?dist}
Summary:        Lightweight GTK+ music manager

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/pragha-music-player/pragha
#VCS: git:https://github.com/pragha-music-player/pragha.git
Source0:        https://github.com/pragha-music-player/pragha/releases/download/v%{version}/pragha-%{version}.tar.bz2
Patch0: pragha-c99-1.patch
Patch1: pragha-c99-2.patch

BuildRequires: make
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.8.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(keybinder-3.0) >= 0.2.0
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(libmtp) >= 1.1.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.38
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(libclastfm) >= 0.5

%if (0%{?fedora} && 0%{?fedora} >= 21) || (0%{?rhel} && 0%{?rhel} >= 7)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.90
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 0.11.90
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 0.11.90
# N/A. Error in configure or not yet packaged?
#BuildRequires:  pkgconfig(gstreamer-interfaces-1.0) >= 0.11.90
%else
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.90
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 0.11.90
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 0.10
BuildRequires:  pkgconfig(gstreamer-interfaces-1.0) >= 0.10
%endif

BuildRequires:  pkgconfig(libcddb) >= 1.3.0
BuildRequires:  pkgconfig(libcdio_paranoia) >= 0.90
BuildRequires:  pkgconfig(libcdio) >= 0.80
#BuildRequires:  libcurl-devel >= 7.18
# libglyr is not yet in Fedora
#BuildRequires:  pkgconfig(libglyr) >= 1.0.1
BuildRequires:  pkgconfig(libclastfm) >= 0.5
BuildRequires:  pkgconfig(libnotify) >= 0.7.5
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.10.0
BuildRequires:  pkgconfig(sqlite3) >= 3.4
BuildRequires:  pkgconfig(taglib_c) >= 1.8
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.0.0
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.0.0
BuildRequires:  totem-pl-parser-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       gstreamer1-plugins-base

%description
Pragha is is a lightweight GTK+ music manager that aims to be fast, bloat-free,
and light on memory consumption. It is written completely in C and GTK+.

Pragha is a fork of Consonance Music Manager, discontinued by the original
author.


%prep
%autosetup -p1

# Hack to support grilo 0.3
sed -i -e 's/grilo-0\.2/grilo-0.3/g' configure

%build
%configure

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
desktop-file-install                                       \
  --delete-original                                        \
  --add-category=Audio                                     \
  --dir=%{buildroot}%{_datadir}/applications          \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
# remove duplicate docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}

find %{buildroot}%{_libdir}/pragha -name \*.ls -exec rm -f {} \;

%files -f %{name}.lang
%doc ChangeLog COPYING FAQ NEWS README
%{_bindir}/pragha
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}/
%{_mandir}/man1/pragha.1.*
# One include file for plugins. Not sure if its worth splitting into -devel
%{_includedir}/pragha
# All the plugins
%{_libdir}/pragha

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.3-30
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Florian Weimer <fweimer@redhat.com> - 1.3.3-25
- Apply upstream patches to fix C99 compatibility issues

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Adrian Reber <adrian@lisas.de> - 1.3.3-18
- Rebuilt for libcdio-2.1.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Adrian Reber <adrian@lisas.de> - 1.3.3-12
- Rebuilt for libcdio-2.0.0
- Fix build by undefining _strict_symbol_defs_build

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.3-11
- Remove obsolete scriptlets

* Fri Nov 24 2017 Dan Horák <dan[at]danny.cz> - 1.3.3-10
- Require gstreamer1 plugins
- Little spec cleanup

* Thu Aug 10 2017 Kalev Lember <klember@redhat.com> - 1.3.3-9
- Rebuilt for libtotem-plparser soname bump

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 1.3.3-8
- Rebuilt for libtotem-plparser soname bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Adrian Reber <adrian@lisas.de> - 1.3.3-5
- Rebuild for libcdio-0.94

* Mon Oct 17 2016 Kalev Lember <klember@redhat.com> - 1.3.3-4
- Fix FTBFS with grilo 0.3 (#1307875)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Matias De lellis <mati86dl@hotmail.com> 1.3.3-1
- Update some deps.

* Thu Sep 24 2015 Kevin Fenzi <kevin@scrye.com> 1.3.3-1
- Update to 1.3.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 07 2015 Kevin Fenzi <kevin@scrye.com> 1.3.2.1-1
- Update to 1.3.2.1
- Switch to gstreamer1
- Enable support for a bunch of plugins

* Sun Mar 01 2015 Kevin Fenzi <kevin@scrye.com> 1.2.2-5
- Rebuild for Xfce 4.12

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.2.2-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Tue Nov 11 2014 Adrian Reber <adrian@lisas.de> - 1.2.2-3
- Rebuild for libcdio-0.93

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2 (fixes #1079743 and #1094542)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.2-2
- Fix conditional to build against gstreamer 0.10 only in Fedora > 20

* Thu Feb 13 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.2-1
- Update to 1.2 (fixes #1013020)
- Build against gstreamer 1.0 on Fedora > 20

* Mon Oct 21 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.2.2-1
- Update to 1.1.2.2 (fixes #1016264)

* Sat Sep 28 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.2.1-2
- Build require gstreamer-interfaces-0.10 and gstreamer-audio-0.10

* Fri Sep 27 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.2.1-1
- Update to 1.1.2.1 (#946963, fixes #957252 and #892283)

* Fri Sep 27 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2
- Fix and update build requirements 

* Thu Sep 19 2013 Kalev Lember <kalevlember@gmail.com> - 1.1.1-5
- Rebuilt for totem-pl-parser soname bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Adrian Reber <adrian@lisas.de> - 1.1.1-2
- Rebuild for libcdio-0.90

* Wed Aug 22 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0.1-1
- Update to 1.1.0.1

* Sun Jun 17 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Sat May 05 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.2-2
- Enable totem-pl-parser

* Fri May 04 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2
- Drop upstreamed patches
- Add README
- Add VCS key

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.1-2
- Rebuild for Xfce 4.10

* Wed Mar 14 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Feb 02 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0-1
- Update to 1.0 Final
- Enable Last.fm support

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.0-0.2.cr3
- Apply the cflags patch again

* Wed Dec 14 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.0-0.1.rc3
- Update to 1.0.rc3
- Require exo-devel for playlist saving throughout sessions

* Sun Dec 11 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.99.0-2
- Rebuild for libcdio-0.83
- Compile with '-Wno-error=deprecated-declarations' (#760960)

* Wed Sep 07 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.99.0-1
- Update to 0.99.0

* Mon Aug 22 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.98.0-1
- Update to 0.98.0

* Sat Jul 30 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.97.0-2
- Don't compile with -O3

* Wed Jul 13 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.97.0-1
- Update to 0.97.0: This version is gstreamer-based. It no longer requires
  libmad, libmodplug, libsndfile or libvorbis but gstreamer and gstreamer-
  plugins-base

* Tue Jul 12 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.8-2
- Build with keybinder support

* Tue Jul 12 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.8-1
- Update to 0.8.8

* Thu Mar 17 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.6-1
- Update to 0.8.6
- Drop libnotify-patch, no longer required

* Thu Dec 09 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4

* Sun Oct 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Sat Aug 21 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.8.0.2-3
- rebuilt

* Mon Aug 02 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0.2-2
- Fix desktop file

* Fri Jul 30 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0.2-1
- Update to 0.8.0.2
- Drop de.po patch, included upstream

* Fri Jul 30 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0.1-1
- Update to 0.8.0.1
- Add COPYING and NEWS to docs

* Thu Jul 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Fri Jun 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.7.1-1
- Update to 0.7.7.1

* Fri Jun 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.7-1
- Update to 0.7.7

* Sat Jun 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.6-1
- Update to 0.7.6
- Remove upstreamed use-software-mixer.patch

* Fri Apr 23 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Mon Mar 22 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.3-2
- Use software mixer by default to cope with pulseaudio
- Remove executable bits from docs

* Tue Mar 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3

* Sat Feb 20 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Wed Oct 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.1-1
- Upadte to 0.7.1

* Sat Oct 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.0-1
- Upadte to 0.7.0

* Sun Aug 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.3-1
- Upadte to 0.6.3

* Mon Jul 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2.2-1
- Initial Fedora package
