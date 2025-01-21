Name:           xpad
Version:        5.8.0
Release:        9%{?dist}
Summary:        Sticky notepad for GTK

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://launchpad.net/xpad
Source0:        https://launchpad.net/xpad/trunk/%{version}/+download/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libSM-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  gtksourceview4-devel
BuildRequires:  libayatana-appindicator-gtk3-devel
BuildRequires:  autoconf
BuildRequires:  libappstream-glib

%description
Xpad is a sticky note application that strives to be simple, fault-tolerant, 
and customizable. It consists of independent pad windows; each is basically a 
text box in which notes can be written. Despite being called xpad, all that is
needed to run or compile it is the GTK+ 2.0 libraries.

%prep
%autosetup -p1

%build
./autogen.sh
%configure

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

# desktop file stuff
desktop-file-install  \
        --delete-original \
        --dir=%{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/xpad
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/xpad.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 5.8.0-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Arthur Bols <arthur@bols.dev> - 5.8.0-6
- Switch to libayatana-appindicator Fixes rhbz#2175545

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 28 2022 Kevin Fenzi <kevin@scrye.com> - 5.8.0-1
- Update to 5.8.0. Fixes rhbz#2049721

* Tue Mar 22 2022 Kevin Fenzi <kevin@scrye.com> - 5.7.0-1
- Update to 5.7.0. Fixes rhbz#2049721

* Sun Feb 20 2022 Kevin Fenzi <kevin@scrye.com> - 5.5.0-8
- Update to 5.5.0. Fixes rhbz#2049721

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Kevin Fenzi <kevin@scrye.com> - 5.3.0-1
- Update to 5.3.0

* Sun Dec 16 2018 Kevin Fenzi <kevin@scrye.com> - 5.2.0-2
- Add patch from upstream to fix bug #1655869

* Sun Nov 18 2018 Kevin Fenzi <kevin@scrye.com> - 5.2.0-1
- Update to 5.2.0.

* Thu Aug 16 2018 Kevin Fenzi <kevin@scrye.com> - 5.1.0-1
- Update to 5.1.0. Fixes bug #1614335

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.0-2
- Remove obsolete scriptlets

* Sun Aug 20 2017 Kevin Fenzi <kevin@scrye.com> - 5.0.0-1
- Update to 5.0.0. Fixes bug #1481254

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 4.8.0-1
- Update to 4.8.0. Fixes bug #1325659

* Mon Mar 14 2016 Kevin Fenzi <kevin@scrye.com> - 4.7.0-1
- Update to 4.7.0. Fixes bugs: #1317140 and #1299088

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Kevin Fenzi <kevin@scrye.com> - 4.6.0-1
- Update to 4.6.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 4.1-2
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Tue Nov 27 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.1-1
- Update to 4.1
- Remove obsolete GTK_WINDOW_TOPLEVEL.patch
- Add patch to compile with recent glibc versions

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 4.0-8
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.0-6
- Fix for GTK_WINDOW_TOPLEVEL by Bart Martens (Debian #576770)

* Sat Oct 24 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.0-5
- Remove autostart again. Doesn't work properly and is annoying on Live CDs
- Spec file clean-ups

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 4.0-3
- Add autostart
- Add new icon cache scriptlets
- Fix macros

* Sat May 30 2009 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 4.0-2
- Add BR intltool

* Sat May 30 2009 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 4.0-1
- Update to new upstream version 4.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 10 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 3.0-1
- Update to new upstream version 3.0
- Upstream: Doesn't wake up every 20 milliseconds
- Upstream: Added some command line options (--hide, --show)
- Upstream: Update icon a bit
- Change license to GPLv3+

* Fri Jul 18 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 2.14-2
- description fixed
- Add doc NEWS, THANKS and TODO
- Add Requires: hicolor-icon-theme
- Remove BuildRequires: libICE-devel

* Fri Jul 11 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 2.14-1
- Initial SPEC file
