# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%global sub_version                     1.0
%global require_ibus_version            1.5.3
%global have_default_layout             1
%global have_bridge_hotkey              1
%global with_python3                    1

%if (0%{?fedora} > 33 || 0%{?rhel} > 8)
%bcond_without kasumi_unicode
%else
%bcond_with    kasumi_unicode
%endif

%if %with_python3
# for bytecompile in %%{_datadir}/ibus-anthy
%global __python %{__python3}
%endif

Name:           ibus-anthy
Version:        1.5.14
Release:        14%{?dist}
Summary:        The Anthy engine for IBus input platform
License:        GPL-2.0-or-later
URL:            https://github.com/ibus/ibus/wiki
Source0:        https://github.com/ibus/ibus-anthy/releases/download/%{version}/%{name}-%{version}.tar.gz

# Upstreamed patches.
# Patch0:         %%{name}-HEAD.patch
Patch0:         %{name}-HEAD.patch
Patch1:         %{name}-1938129-default-hiragana.patch

BuildRequires:  anthy-unicode-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  ibus 
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-gobject

Requires:       ibus >= %{require_ibus_version}
%if %{with kasumi_unicode}
Requires:       kasumi-unicode
%else
Requires:       kasumi
%endif
Requires:       anthy-unicode
Requires:       %{name}-python = %{version}-%{release}

%description
The Anthy engine for IBus platform. It provides Japanese input method from
a library of the Anthy.

%package python
Summary:        Anthy Python files for IBus
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gtk3
Requires:       python3-cairo
Requires:       python3-gobject

%description python
This package contains the Anthy Python files for IBus

%package devel
Summary:        Development tools for IBus
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       anthy-unicode-devel

%description devel
The ibus-anthy-devel package contains .so file and .gir files
for developers.

%package  tests
Summary:        Tests for the %{name} package
BuildRequires:  python3-pycotap
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-pycotap

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.


%prep
%autosetup -S git

%build
#autoreconf -f -i -v
autoreconf -f -i -v
%configure \
%if %have_default_layout
  --with-layout='default' \
%endif
%if %have_bridge_hotkey
  --with-hotkeys \
%endif
%if %{with kasumi_unicode}
  --with-kasumi-exec=/usr/bin/kasumi-unicode \
%endif
  --with-on-off-keys="'Zenkaku_Hankaku', 'Ctrl+space', 'Ctrl+J'" \
  --with-python=python3 \
  --enable-installed-tests \
  --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm -f $RPM_BUILD_ROOT%{_libdir}/libanthygobject-%{sub_version}.la


%find_lang %{name}

%check
desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-anthy.desktop
export LANG=C.UTF-8
locale
make -C data check

%ldconfig_scriptlets libs


%files -f %{name}.lang
%doc AUTHORS COPYING README
# dir {python2_sitearch}/ibus
%{_libdir}/libanthygobject-%{sub_version}.so.*
%{_libdir}/girepository-1.0/Anthy*.typelib
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.anthy.gschema.xml
%dir %{_datadir}/ibus-anthy
%{_datadir}/applications/ibus-setup-anthy.desktop
%{_datadir}/ibus-anthy/dicts
%{_datadir}/icons/hicolor/scalable/apps/ibus-anthy.svg 

%files python
%{_libexecdir}/ibus-*-anthy
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/ibus-anthy/engine
%{_datadir}/ibus-anthy/setup
%{_datadir}/ibus/component/*

%files devel
%{_datadir}/gir-1.0/Anthy*.gir
%{_includedir}/ibus-anthy-%{sub_version}
%{_libdir}/libanthygobject-%{sub_version}.so

%files tests
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/%{name}
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/%{name}

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.14-13
- Resolves #2015149 Commit candidate text with clicking on candidate list in OSK

* Fri Feb 17 2023 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.14-11
- Fix to load EN compose table

* Thu Jan 26 2023 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.14-10
- Add 2023 Era
- Fix PageDown/PageUp

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.14-8
- Migrate license tag to SPDX

* Wed Aug 03 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.14-7
- Change metainfo icon from SVG to PNG file

* Wed Aug 03 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.14-6
- Add icon tag in ibus-anthy.appdata.xml.in
- Enable IBus.Engine::has-focus-id property
- Add the escape_to_latin command as a vi-cooperative cancel

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 14 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.14-4
- Resolves #2064261 assertion error with page size 0

* Thu Jan 27 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.14-3
- Add 2022 Era

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.14-1
- Bump to 1.5.14

* Fri Oct 22 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.13-3
- export C.UTF-8 for make check

* Fri Oct 22 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.13-2
- Update era.t with 2021
- Check python3-pycotap.rpm in Fedora instead of pip

* Fri Aug 20 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.13-1
- Bump to 1.5.13

* Thu Aug 12 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.12-10
- Remove Ctrl+period in circle_kana_mode

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.12-8
- Delete postscript for ibus write-cache

* Tue Apr 27 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.12-7
- Move .desktop file from ibus-anthy-python to ibus-anthy
- Fix covscan

* Wed Apr 21 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.12-6
- Resolves: #1948197 Move post to posttrans

* Tue Apr 20 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.12-5
- Delete postscripts

* Sun Mar 21 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.12-4
- Output info to stderr instead of StringIO

* Tue Mar 16 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.12-2
- Change default input mode to Hiragana

* Mon Feb 22 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.12-1
- Bump to 1.5.12

* Wed Feb 10 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.11-10
- Replace kasumi with kausmi-unicode
- Delete to require intltool
- Delete to call gettext.bind_textdomain_codeset()

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.11-7
- Use pycotap instead of tappy in CI
- Revise CI from ibus-typing-booster
- Delete _python_bytecompile_extra

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.11-5
- Bug 1779129- Fix to install zipcode dict with anthy-unicode

* Thu Oct 17 2019 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.11-4
- Add CI

* Wed Oct 16 2019 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.11-3
- Replace anthy with anthy-unicode
- Install ibus-anthy-tests sub package

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.11-1
- Bump to 1.5.11

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.10-4
- Rebuilt for Python 3.7

* Mon Mar 19 2018 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.10-3
- Reverted scriptlets for f27

* Mon Mar 19 2018 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.10-2
- Reverted ldconfig for f27

* Mon Mar 19 2018 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.10-1
- Bumped to 1.5.10

* Tue Feb 20 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.9-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.9-2
- Rebuild for Python 3.6

* Thu Oct 20 2016 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.9-1
- Bumped to 1.5.9

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.8-1
- Bumped to 1.5.8

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 03 2015 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.7-2
- Fix URL in anthy.appdata.xml

* Thu Jul 16 2015 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.7-1
- Bumped to 1.5.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.6-6
- Resolved #1214092 Updated ibus-anthy-HEAD.patch
- Added with_appdata macro and removed with_python_pkg macro

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 1.5.6-5
- Add the AppData file to the right built RPM, in this case we have to install
  ibus-anthy-python rather than the main package in gnome-software.
- It turns out adding the AppData file to spec files is a great way to fix these
  kinds of bugs. :)

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 1.5.6-4
- Use an AppStream file compatible with F22 also.

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 1.5.6-3
- Register as an AppStream component.

* Thu Nov 13 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.6-2
- Updated ibus-anthy-HEAD.patch to fix Enter key on setup dialog.
- Use python2 for epel7.

* Tue Sep 16 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.6-1
- Bumped to 1.5.6
- Added ibus-anthy-xx-input-mode.patch from ibus-anthy-HEAD.patch.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.5.5-8
- Rebuilt for gobject-introspection 1.41.4

* Mon Jul 14 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.5-7
- Updated ibus-anthy-HEAD.patch
  Fixed deprecated warnings with python3-gobject 3.13.3.

* Mon Jul 14 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.5-6
- Updated ibus-anthy-HEAD.patch
  Fixed deprecated warnings with python3-gobject 3.13.3.
  Set max-width-chars in ibus-anthy-setup wrapped GtkLabel.
  Set 'IBUS_SETUP_XID' environment variable in setup.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.5-4
- Updated ibus-anthy-HEAD.patch to fix clear() in input mode.

* Mon Apr 21 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.5-3
- Updated ibus-anthy-HEAD.patch to unref pixbuf on destroy.

* Thu Feb 27 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.5-2
- Updated ibus-anthy-HEAD.patch to enable property icon.

* Wed Feb 05 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.5-1
- Bumped to 1.5.5
- Enabled python3.

* Tue Dec 24 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.4-2
- Required ibus-anthy by ibus-anthy-python

* Mon Sep 09 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.4-1
- Bumped to 1.5.4
- Added ibus-anthy-python subpackage for noarch.
- Deleted ibus-anthy-xx-disable-prop-symbol.patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.3-1
- Bumped to 1.5.3

* Mon May 13 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.2-1
- Bumped to 1.5.2

* Sat May 11 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.1-1
- Bumped to 1.5.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.5.0-1
- Bumped to 1.5.0

* Wed Dec 12 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.99.20121006-3
- Resolved #884031. Deleted arch depended files.

* Thu Nov 22 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.99.20121006-2
- Updated to save the spec update.

* Sat Oct 06 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.99.20121006-1
- Bumped to 1.4.99.20121006
- Added ibus-anthy-xx-disable-prop-symbol.patch for Fedora 17

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.99.20120327-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.99.20120327-1
- Bumped to 1.4.99.20120327

* Sun Mar 04 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.99.20120304-1
- Bumped to 1.3.99.20120304

* Mon Feb 06 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.2.6-5
- Added ibus-anthy-xx-layout.patch to set 'default' layout in f17.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 29 2011 Takao Fujiwara <tfujiwar@redhat.com> - 1.2.6-3
- Added ibus-anthy-xx-icon-symbol.patch to enable the engine symbol & hotkeys.

* Mon May 16 2011 Takao Fujiwara <tfujiwar@redhat.com> - 1.2.6-1
- Bumped to 1.2.6
  Fixed Bug 661943 - the latest page_size for ibus.LookupTable.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 01 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.2.5-1
- Updated to 1.2.5
  Fixed Bug 652881 - SEGV when key tables are customized in new gconf.
  Fixed Bug 654322 - new custom keys are not loaded.

* Tue Oct 26 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.2.4-1
- Updated to 1.2.4
- Resolves #644771 ibus-anthy [F7] key cannot work with SEGV

* Sat Oct 16 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.2.3-1
- Updated to 1.2.3
- Updated translations.

* Fri Oct 15 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.2.2.20101015-1
- Updated to 1.2.2.20101015
- Fixed Bug 643291 - ibus-anthy commit_first_segment

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Apr 23 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Mon Apr 05 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100313-3
- Update icon

* Fri Mar 12 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100313-1
- Update to 1.2.0.20100313
- Update fr.po

* Fri Mar 12 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100312.1-1
- Update to 1.2.0.20100312.1
- Minor fix for a translation

* Fri Mar 12 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100312-1
- Update to 1.2.0.20100312
- Fix bug 571728 - ibus-anthy support to switch dicts
- Fix bug 572412 - ibus-anthy: Segment convertion mode

* Fri Mar 05 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100115-2
- Fix bug 564268 - Crash with enabled global input method
- Fix bug 570680 - Support NICOLA-F and NICOLA-A
- Fix romaji_typing_rule. #777
- Fix Shift + char with CapsLock ON in romaji mode.
- Fix chattering bug.

* Fri Jan 15 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20100115-1
- Update to 1.2.0.20100115
- Fix bug 550001 - kasumi should be accessible from ibus-anthy

* Fri Nov 27 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20091127-1
- Update to 1.2.0.20091127
- Fix bug 520989 - ibus-anthy icon enhancement
- Fix bug 531696 - ibus-anthy KeyError is still reported by abrt
- Fix bug 536716 - ibus-anthy: Symbol type change support in ibus-anthy

* Fri Oct 23 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090917-2
- Fix bug 526881 - ibus-anthy backtrace is reported by the latest abrt

* Thu Sep 17 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090917-1
- Update to 1.2.0.20090917
- Fix bug 523642 - ibus-anthy convert_to_char_type_{for,back}ward()

* Mon Sep 07 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090907-2
- Fix a build issue

* Mon Sep 07 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090907-1
- Update to 1.2.0.20090907
- Fix bug 510978 - "Typing Method" configuration doesn't work
- Fix bug 518373 - ibus setup tools need to set gettext textdomain dir.

* Thu Aug 13 2009 Takao Fujiwara <takao.fujiwara1@gmail.com> - 1.2.0.20090813-1
- Update to 1.2.0.20090813
- Fix bug 509483 - reconversion feature doesn't work
- Fix bug 509485 - commit_first_segment feature doesn't work

* Tue Aug 04 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090804-1
- Update to 1.2.0.20090804
- Fix bug 508358 - ANTHY_HISTORY_FILE record only a single word

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090617-1
- Update to 1.2.0.20090617

* Wed Jun 17 2009 Jens Petersen <petersen@redhat.com> - 1.1.0.20090603-2
- require kasumi to pull in dictionary tool

* Wed Jun 03 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090603-1
- Update to 1.1.0.20090603
- Implement setup ui.

* Thu Apr 30 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090402-2
- Update to upstream HEAD version
- Fix bug 498250 - Cannot type zenkaku-space

* Thu Apr 02 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090402-1
- Update to 1.1.0.20090402.
- Fix bug 490747 - Muhenkan (no-conversion) key does not undo conversion
- Fix bug 490750 - Henkan key for candidate conversion doesn't do anything
- Fix bug 490748 - Kana key doesn't do anything

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.20090211-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090211-1
- Update to 1.1.0.20090211.

* Thu Feb 05 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090205-1
- Update to 1.1.0.20090205.

* Tue Feb 03 2009 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20090203-1
- Update to 0.1.1.20090203.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1.20080912-2
- Rebuild for Python 2.6

* Fri Sep 12 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080912-1
- Update to 0.1.1.20080912.

* Mon Sep 01 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080901-1
- Update to 0.1.1.20080901.

* Thu Aug 28 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080828-1
- Update to 0.1.1.20080828.

* Wed Aug 27 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080827-1
- Update to 0.1.1.20080827.

* Tue Aug 26 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080826-1
- Update to 0.1.1.20080826.

* Sat Aug 23 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080823-1
- Update to 0.1.1.20080823.

* Fri Aug 15 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080815-1
- Update to 0.1.1.20080815.

* Tue Aug 12 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080812-1
- Update to 0.1.1.20080812.

* Fri Aug 08 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.0.20080810-1
- The first version.
