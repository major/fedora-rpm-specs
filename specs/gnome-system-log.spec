Name:           gnome-system-log
Version:        3.9.90
Release:        28%{?dist}
Epoch:          1
Summary:        A log file viewer for GNOME

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/gnome-system-log/3.9/gnome-system-log-%{version}.tar.xz
Source1:        gnome-system-log
Source2:        org.gnome.logview.policy

BuildRequires:  gcc
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: docbook-dtds
BuildRequires: desktop-file-utils
BuildRequires: itstool
BuildRequires: make

Obsoletes: gnome-utils < 1:3.3
Obsoletes: gnome-utils-devel < 1:3.3
Obsoletes: gnome-utils-libs < 1:3.3

%description
gnome-system-log lets you view various log files on your system.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-system-log.desktop

mv $RPM_BUILD_ROOT%{_bindir}/gnome-system-log $RPM_BUILD_ROOT%{_bindir}/logview
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
chmod a+x $RPM_BUILD_ROOT%{_bindir}/gnome-system-log
mkdir -p $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=730871
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">gnome-system-log.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>View system logs</summary>
  <description>
    <p>
      System Logs is an application for viewing the system logs on your 
      computer.
      It provides a graphical viewer for the logs that one would
      typically view in a terminal, such as the boot.log or the system
      messages.
    </p>
  </description>
  <url type="homepage">https://git.gnome.org/browse/gnome-system-log/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gnome-system-log/a.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name} --with-gnome

# https://bugzilla.redhat.com/show_bug.cgi?id=736523
#echo "%%dir %%{_datadir}/help/C" >> aisleriot.lang
#echo "%%{_datadir}/help/C/%%{name}" >> aisleriot.lang
#for l in ca cs de el en_GB es eu fi fr it ja ko oc ru sl sv uk zh_CN; do
#  echo "%%dir %%{_datadir}/help/$l"
#  echo "%%lang($l) %%{_datadir}/help/$l/%%{name}"
#done >> %{name}.lang

%files -f %{name}.lang
%doc COPYING COPYING.docs
%{_bindir}/gnome-system-log
%{_bindir}/logview
%{_datadir}/GConf/gsettings/logview.convert
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/gnome-system-log.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-log.gschema.xml
%{_datadir}/icons/hicolor/*/apps/logview.png
%{_datadir}/icons/HighContrast/*/apps/logview.png
%{_datadir}/polkit-1/actions/org.gnome.logview.policy
%doc %{_mandir}/man1/gnome-system-log.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:3.9.90-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.9.90-10
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.9.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.9.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:3.9.90-4
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.9.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.9.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.3-1
- Update to 3.9.3

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.0-1
- Update to 3.8.0

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 1:3.7.90-1
- Update to 3.7.90

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.6.1-2
- Use auth_admin instead of auth_self (#878115)

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.1-1
- Update to 3.6.1
- Remove unused BRs

* Tue Sep 25 2012 Cosimo Cecchi <cosimoc@redhat.com> - 1:3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.92-1
- Update to 3.5.92

* Wed Sep 05 2012 Cosimo Cecchi <cosimoc@redhat.com> - 1:3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.90-1
- Update to 3.5.90

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.4-1
- Update to 3.5.4

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.4.1-2
- Silence rpm scriptlet output

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.1-1
- Update to 3.4.1

* Thu Apr  5 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.4.0-2
- Use pkexec to run privileged

* Mon Mar 26 2012 Cosimo Cecchi <cosimoc@redhat.com> - 1:3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.3.92-1
- Update to 3.3.92

* Mon Mar 19 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.3.1-4
- Use epoch to fix the upgrade path from the old gnome-system-log package that
  was built as part of gnome-utils

* Sat Mar 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.1-3
- Obsolete gnome-utils and subpackages

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011  Matthias Clasen <mclasen@redhat.com> - 3.3.1-1
- Initial packaging
