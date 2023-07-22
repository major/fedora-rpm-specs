Name:           ksensors
Version:        0.7.3
Release:        52%{?dist}
Summary:        KDE frontend to lm_sensors
License:        GPLv2+
URL:            http://ksensors.sourceforge.net/
Source0:        http://downloads.sourceforge.net/ksensors/%{name}-%{version}.tar.gz
Patch1:         %{name}-desktop.patch
Patch2:         http://ftp.debian.org/debian/pool/main/k/ksensors/ksensors_0.7.3-15.diff.gz
Patch3:         %{name}-0.7.3-po.patch
Patch4:         %{name}-0.7.3-fix-min-max.patch
Patch5:         %{name}-0.7.3-lm_sensors-3.x.patch
# Add an --autostart parameter that starts KSensors only if autostart is enabled
Patch6:         %{name}-0.7.3-autostart.patch
BuildRequires:  gcc
BuildRequires:  kdelibs3-devel lm_sensors-devel gettext desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme
# Keep archs in sync with lm_sensors
ExcludeArch:    s390 s390x

%description
KSensors is a nice lm-sensors frontend for the K Desktop Environment.
Install the hddtemp package if you wish to monitor hard disk
temperatures with KSensors.


%prep
%setup -q
%patch1 -p1 -z .desktop
%patch2 -p1
%patch3 -p1 -z .po
%patch4 -p1 -z .minmax
%patch5 -p1 -z .lm_sensors3x
%patch6 -p1 -z .autostart
sed -i -e 's|$(kde_datadir)/sounds|$(kde_sounddir)|' src/sounds/Makefile.*
for f in ChangeLog LIESMICH LISEZMOI ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
done


%build
unset QTDIR ; . %{_sysconfdir}/profile.d/qt.sh
%configure --disable-dependency-tracking --disable-rpath
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install \
    --mode 644 --delete-original \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/ksensors.desktop
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart
sed -e 's/^Exec=ksensors$/Exec=ksensors --autostart/g' \
    $RPM_BUILD_ROOT%{_datadir}/applications/ksensors.desktop \
    >$RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/ksensors.desktop

rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/locolor
rm -rf $RPM_BUILD_ROOT%{_docdir}/HTML
%find_lang %{name} --with-kde



%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog FAQ README TODO
%lang(es) %doc LEEME
%lang(de) %doc LIESMICH
%lang(fr) %doc LISEZMOI
%{_bindir}/ksensors
%{_datadir}/applications/ksensors.desktop
%{_datadir}/apps/ksensors/
%{_datadir}/icons/hicolor/*/apps/ksensors.*
%{_datadir}/sounds/ksensors_alert.wav
%{_sysconfdir}/xdg/autostart/ksensors.desktop


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.3-44
- Readd Requires: hicolor-icon-theme, required for directory ownership

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.3-39
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 30 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.3-36
- Fix autostart race condition in Plasma 5 by setting the autostart phase

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.3-34
- Add an --autostart parameter that starts KSensors only if autostart is enabled
- Make the .desktop file in /etc/xdg/autostart pass it (use sed instead of ln)

* Thu Sep 08 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.3-33
- Use /etc/xdg/autostart instead of the obsolete /usr/share/autostart
- Specfile cleanup: remove obsolete Fedora <= 18 support
- Specfile cleanup: remove obsolete specfile constructs, use %%license

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Rex Dieter <rdieter@fedoraproject.org> 0.7.3-31
- fix %%postun scriptlet (#1187994)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.3-29
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.7.3-26
- fix/optimize icon scriptlets
- omit locolor icons
- omit uneeded dep on hicolor-icon-theme

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.3-24
- Fix desktop vendor tag handling.

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.3-23
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.3-16
- Update Debian patch to -15 release

* Thu Jan  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.3-15
- Change BuildRequires: kdelibs-devel into kdelibs3-devel

* Sun Nov 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.3-14
- Patch for and Rebuild against lm_sensors-3.0.0

* Sun Nov 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.3-13
- Fix reading of min and max tresholds from libsensors

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.3-12
- Update License tag for new Licensing Guidelines compliance

* Fri Jul 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.3-11
- Remove OnlyShowIn=KDE; from .desktop file (I like using ksensors under GNOME,
  works fine grumbel) 

* Fri Jul 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.3-10
- Add icon-cache update scriptlets
- Add Requires: hicolor-icon-theme for dir ownership

* Fri Jul 20 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.7.3-9
- Sync Exclu(de|sive)Arch with new lm_sensors (#249060).

* Tue Jun 26 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.7.3-8
- Update Debian patchset to -14 for additional fixes and translations;
  drop our hddtemp detection patch in favour of the one included in it.
- Drop Application and X-Fedora categories from .desktop file, add GenericName.
- Make autostart checkbox effective again (#242570).
- Convert docs to UTF-8.

* Sat Sep 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.3-7
- Apply Debian -11 patchset for upstream radio button state fix,
  support for hddtemp with SCSI disks and more translations.

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.3-6
- Rebuild.

* Wed Feb 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.3-5
- Rebuild.

* Thu Nov  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.7.3-4
- Clean up build dependencies.

* Thu May 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.7.3-3
- Sync arch availability with FC4 lm_sensors (%%{ix86}, x86_64, alpha).
- Reduce directory ownership bloat.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.7.3-2
- rebuilt

* Sat Aug 21 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.3-0.fdr.1
- Update to 0.7.3, most patches applied upstream.
- Disable dependency tracking to speed up the build.

* Tue Jul 20 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.2-0.fdr.4
- Force use of multithreaded Qt with --enable-mt to fix build on FC2.
- Sync Debian patch to 0.7.2-16 to get a fix for freeze with hddtemp.
- Apply upstream patches #913569 and #915725.
- Disable RPATH.
- Don't ship the "handbook", it's just a template.
- Other minor improvements here and there.

* Sat Aug  2 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.2-0.fdr.3
- Own dirs under %%{_datadir}/icons and %%{_docdir}/HTML (bug 21).
- Don't tweak path to hddtemp.
- Patch to fix hddtemp detection.
- s/--enable-xinerama/--with-xinerama/
- Borrow man page from Debian.

* Sat May 31 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.2-0.fdr.2
- Spec cleanups.

* Fri Apr  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.2-0.fdr.1
- Update to current Fedora guidelines.
- Move desktop entry to %%{_datadir}/applications using desktop-file-install.

* Sun Feb 23 2003 Warren Togami <warren@togami.com> - 0.7.2-1.fedora.2
- BuildRequires libart_lgpl-devel needed for Red Hat 8.1

* Sun Feb 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.7.2-1.fedora.1
- Update to 0.7.2.
- Don't apply startup crash patch, but keep it around for now.

* Sat Feb 15 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.7-1.fedora.2
- Include startup crash patch from upstream SRPM.

* Sun Feb  9 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.7-1.fedora.1
- First Fedora release.
