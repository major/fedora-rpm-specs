Name:		gnome-phone-manager
Summary:	Gnome Phone Manager
Version: 	0.69
Release: 	47%{?dist}
License: 	GPL-2.0-or-later
Source:		http://ftp.gnome.org/pub/GNOME/sources/gnome-phone-manager/%{version}/%{name}-%{version}.tar.xz
#Using git clone plus patch from GNOME BZ 680927.
#Source:		gnome-phone-manager-0.68-20120806git16211d.tar.xz
URL: 		https://wiki.gnome.org/PhoneManager/
BuildRequires:	gtk3-devel
BuildRequires:	libcanberra-devel
BuildRequires:	gnome-bluetooth-libs-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	gnokii-devel
BuildRequires:	gstreamer1-devel
BuildRequires:	gnome-icon-theme-devel
BuildRequires:	evolution-data-server-devel >= 3.45.1
BuildRequires:	gtkspell-devel
BuildRequires:	telepathy-glib-devel
BuildRequires:	intltool perl(XML::Parser)
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	GConf2-devel
BuildRequires:	make
BuildRequires:	pkgconfig(gnome-bluetooth-1.0)

#Patch01: gnome-phone-manager-0.66-no-g-thread-init.patch
#Patch02: gnome-phone-manager-0.66-bluetooth-api-change.patch
Patch03: gnome-phone-manager-0.68-eds.patch
Patch04: gnome-phone-manager-0.69-drop-plugin.patch

%description
This program will connect to your mobile phone over a serial port,
either via a cable, infrared (IrDA) or Bluetooth connection.

For example it listens for text messages, and when they arrive,
displays them on the desktop. A visual indicator is displayed in
the notification area, if one is presently added to the panel.

%package telepathy
Summary: Telepathy connection manager to send and receive SMSes

%description telepathy
This program will connect to your mobile phone over a serial port,
either via a cable, infrared (IrDA) or Bluetooth connection.

This plugin to Telepathy allows you to send and receive messages using any
Instant Messaging application that uses Telepathy, such as Empathy.

%prep
%setup -q

#%patch01 -p1 -b .no-g-thread-init
#%patch02 -p1 -b .bluetooth-api-change
%patch -P03 -p1 -b .eds
%patch -P4 -p0 -b .plugin

#rm ./libgsm/phonemgr-listener.lo
#rm ./libgsm/phonemgr-listener.o

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# This should be in empathy instead
install -m0644 -D telepathy/sms.profile $RPM_BUILD_ROOT%{_datadir}/mission-control/profiles/sms.profile

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
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=730849
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">gnome-phone-manager.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Control your mobile phone from your desktop</summary>
  <description>
    <p>
      Phone Manager allows you to control your mobile phone. It uses the
      gnokii backend that typically works with older Nokia devices. Phone
      manager allows you to send SMS messages, view the address book on your
      phone, and receive notifications on the desktop when a new SMS arrives.
    </p>
  </description>
  <url type="homepage">https://live.gnome.org/PhoneManager/</url>
  <screenshots>
    <screenshot type="default">https://wiki.gnome.org/PhoneManager?action=AttachFile&amp;do=get&amp;target=prefs-2.png</screenshot>
  </screenshots>
</application>
EOF

rm $RPM_BUILD_ROOT%{_libdir}/gnome-bluetooth/plugins/libphonemgr.a
rm $RPM_BUILD_ROOT%{_libdir}/gnome-bluetooth/plugins/libphonemgr.la

%find_lang %{name}
desktop-file-install \
  --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category X-Fedora \
  $RPM_BUILD_ROOT%{_datadir}/applications/gnome-phone-manager.desktop

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
        %{_sysconfdir}/gconf/schemas/gnome-phone-manager.schemas 	\
	>& /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule 				\
        %{_sysconfdir}/gconf/schemas/gnome-phone-manager.schemas 	\
	>& /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule 				\
        %{_sysconfdir}/gconf/schemas/gnome-phone-manager.schemas 	\
	>& /dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_sysconfdir}/gconf/schemas/gnome-phone-manager.schemas
%{_bindir}/gnome-phone-manager
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/gnome-phone-manager/
%{_mandir}/man1/gnome-phone-manager.1.gz
%{_libdir}/gnome-bluetooth/plugins/libphonemgr.so

%files telepathy
%{_libexecdir}/telepathy-phoney
%{_datadir}/telepathy/managers/*
%{_datadir}/dbus-1/services/*
%{_datadir}/mission-control/profiles/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.69-42
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Milan Crha <mcrha@redhat.com> - 0.69-39
- Rebuilt for evolution-data-server soname version bump

* Wed Feb 16 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.69-38
- libgnome-bluetooth rebuild.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 0.69-35
- Rebuilt for evolution-data-server soname version bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-33
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 0.69-31
- Rebuilt for evolution-data-server soname version bump

* Fri Mar 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.69-30
- Move to gstreamer1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 0.69-27
- Rebuilt for evolution-data-server soname bump

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 0.69-24
- Rebuilt for evolution-data-server soname bump

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Milan Crha <mcrha@redhat.com> 0.69-20
- Rebuild for newer evolution-data-server

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> 0.69-19
- Rebuild for newer evolution-data-server

* Wed Jun 22 2016 Milan Crha <mcrha@redhat.com> - 0.69-18
- Do not require evolution, when using evolution-data-server libraries

* Tue Jun 21 2016 Jon Ciesla <limburgher@gmail.com> - 0.69-17
- Libcamel rebuild.

* Tue Feb 16 2016 Milan Crha <mcrha@redhat.com> 0.69-16
- Rebuild for newer evolution-data-server

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Milan Crha <mcrha@redhat.com> 0.69-14
- Rebuild for newer evolution-data-server

* Wed Jul 22 2015 Milan Crha <mcrha@redhat.com> 0.69-13
- Rebuild for newer evolution-data-server

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.69-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> 0.69-11
- Rebuild for newer evolution-data-server

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.69-10
- Add an AppData file for the software center

* Tue Feb 17 2015 Milan Crha <mcrha@redhat.com> 0.69-9
- Rebuild against newer evolution-data-server

* Tue Sep 23 2014 Jon Ciesla <limburgher@gmail.com> - 0.69-8
- Libcamel rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.69-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Jon Ciesla <limburgher@gmail.com> 0.69-6
- Rebuild against newer evolution-data-server

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.69-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Milan Crha <mcrha@redhat.com> 0.69-4
- Rebuild against newer evolution-data-server

* Tue Jan 14 2014 Jon Ciesla <limburgher@gmail.com> - 0.69-3
- Libcamel rebuild.

* Thu Dec 19 2013 Jon Ciesla <limburgher@gmail.com> - 0.69-2
- Patch out plugin support, no longer in gnome-bluetooth.

* Wed Dec 18 2013 Jon Ciesla <limburgher@gmail.com> - 0.69-1
- Latest upstream.

* Wed Dec 18 2013 Jon Ciesla <limburgher@gmail.com> - 0.68-18
- gnome-bluetooth rebuild.

* Tue Nov 19 2013 Jon Ciesla <limburgher@gmail.com> - 0.68-17
- Libcamel rebuild.

* Wed Oct 23 2013 Jon Ciesla <limburgher@gmail.com> - 0.68-16
- Libcamel rebuild.

* Mon Aug 19 2013 Jon Ciesla <limburgher@gmail.com> - 0.68-15
- libedata-book rebuild.

* Thu Aug 08 2013 Jon Ciesla <limburgher@gmail.com> - 0.68-14
- gnome-bluetooth rebuild.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Jon Ciesla <limburgher@gmail.com> - 0.68-12
- Libcamel rebuild.

* Fri Jun 28 2013 Kalev Lember <kalevlember@gmail.com> - 0.68-11
- Adapt for gnome-icon-theme packaging changes

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Jon Ciesla <limburgher@gmail.com> - 0.68-9
- Libcamel rebuild.

* Tue Nov 20 2012 Jon Ciesla <limburgher@gmail.com> - 0.68-8
- Libcamel rebuild.

* Tue Oct 30 2012 Matthew Barnes <mbarnes@redhat.com> - 0.68-7
- Remove unnecessary libedataserverui dependency.

* Thu Oct 25 2012 Milan Crha <mcrha@redhat.com> 0.68-6
- Rebuild against newer evolution-data-server

* Wed Aug 29 2012 Milan Crha <mcrha@redhat.com> - 0.68-5
- Remove precompiled files from sources before build

* Fri Jul 20 2012 Jon Ciesla <limburgher@gmail.com> - 0.68-4
- Add GConf2-devel BR to fix FTBFS.
- Fixed URL.
- Patched for includes.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Jon Ciesla <limburgher@gmail.com> - 0.68-2
- Rebuild for gnokii soname bump.

* Sat Mar 24 2012 Kalev Lember <kalevlember@gmail.com> - 0.68-1
- Update to 0.68

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.66-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Milan Crha <mcrha@redhat.com> 0.66-8
- Rebuild against newer evolution-data-server
- Add patch to drop g_thread_init() calls
- Add patch for bluetooth API change

* Sun Oct 30 2011 Bruno Wolff III <bruno@wolff.to> - 0.66-7
- Rebuild against newer evolution-data-server

* Tue Aug 30 2011 Milan Crha <mcrha@redhat.com> 0.66-6
- Sync version with f16 branch

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> 0.66-5
- Rebuild against newer evolution-data-server

* Tue Aug 16 2011 Milan Crha <mcrha@redhat.com> 0.66-4
- Rebuild against new evolution-data-server

* Mon Jun 20 2011 Milan Crha <mcrha@redhat.com> 0.66-3
- Rebuild against new evolution-data-server

* Fri May 20 2011 Kalev Lember <kalev@smartlink.ee> - 0.66-2
- Rebuilt for libcamel soname bump

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> 0.66-1
- Update to 0.66

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> 0.65-15
- Rebuild against newer gtk3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.65-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 0.65-13
- Rebuild against newer gtk3

* Tue Feb 01 2011 Milan Crha <mcrha@redhat.com> 0.65-12
- Rebuild against new evolution-data-server

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> 0.65-11
- Rebuild against newer gtk3

* Thu Dec 30 2010 Robert Scheck <robert@fedoraproject.org> 0.65-10
- Rebuild against new gnokii library

* Fri Dec 10 2010 Bastien Nocera <bnocera@redhat.com> 0.65-9
- Rebuild against GTK2 libraries (#643646)

* Mon Jul 19 2010 Bastien Nocera <bnocera@redhat.com> 0.65-8
- Rebuild against new evolution-data-server

* Mon Jul 12 2010 Matthias Clasen <mclasen@redhat.com> 0.65-7
- Rebuild against new webkit

* Mon Jun  7 2010 Matthias Clasen <mclasen@redhat.com> 0.65-6
- Rebuild against new evolution-data-server

* Tue Sep 08 2009 Bastien Nocera <bnocera@redhat.com> 0.65-5
- Rebuilt for new gnokii

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Bastien Nocera <bnocera@redhat.com> 0.65-3
- Rebuild for new gnome-bluetooth

* Fri Jun 19 2009 Bastien Nocera <bnocera@redhat.com> 0.65-2
- Rebuild for new gnome-bluetooth

* Tue Mar 10 2009 - Bastien Nocera <bnocera@redhat.com> - 0.65-1
- Update to 0.65

* Thu Mar 5 2009 Linus Walleij <triad@df.lth.se> 0.60-6
- Rebuild hoping to pick up libgnomebt i/f bump.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 - Caolán McNamara <caolanm@redhat.com> - 0.60-4
- rebuild for dependencies

* Tue Oct 07 2008 - Bastien Nocera <bnocera@redhat.com> - 0.60-3
- Rebuild for new libgnokii

* Thu Sep 11 2008  Matthias Clasen  <mclasen@redhat.com>
- Rebuild

* Wed Jun 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.60-1
- Update to 0.60
- Remove vendor from desktop file

* Wed May 14 2008 - Bastien Nocera <bnocera@redhat.com> - 0.51-2
- Rebuild

* Fri Mar 21 2008 - Bastien Nocera <bnocera@redhat.com> - 0.51-1
- Update to 0.51

* Fri Mar 14 2008 - Bastien Nocera <bnocera@redhat.com> - 0.50-3
- Add a patch from upstream to fix connection to serial devices (#356861)

* Mon Mar 10 2008 - Bastien Nocera <bnocera@redhat.com> - 0.50-2
- Work-around for telepathy brokeness

* Mon Mar 10 2008 - Bastien Nocera <bnocera@redhat.com> - 0.50-1
- Update to 0.50

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.40-3
- Autorebuild for GCC 4.3

* Wed Dec 12 2007 - Bastien Nocera <bnocera@redhat.com> - 0.40-2
- Rebuild against new release of gnokii

* Wed Nov 14 2007 - Bastien Nocera <bnocera@redhat.com> - 0.40-1
- Update to 0.40
- Add experimental telepathy backend in a subpackage

* Mon Oct 29 2007 - Bastien Nocera <bnocera@redhat.com> - 0.30-1
- Update to 0.30
- Fix sending non-ASCII texts (for real)
- Add debugging improvements

* Wed Oct 17 2007 - Bastien Nocera <bnocera@redhat.com> - 0.20-1
- Update to 0.20

* Sun Aug 19 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10-1
- Update to 0.10 (#253400)
- Remove obsolete work-arounds and dependencies
- Update BRs
- Add GConf scriptlets

* Fri Aug 17 2007 Linus Walleij <triad@df.lth.se> 0.8-6
- Update license field from GPL to GPLv2+

* Wed Nov 15 2006 Linus Walleij <triad@df.lth.se> 0.8-5
- Rebuild to pick up libbtctl i/f bump.

* Sun Oct 29 2006 Linus Walleij <triad@df.lth.se> 0.8-4
- Rebuild to pick up libedataserver i/f bump.

* Sun Oct 8 2006 Linus Walleij <triad@df.lth.se> 0.8-3
- Pick up intltool.

* Sun Oct 8 2006 Linus Walleij <triad@df.lth.se> 0.8-2
- Pick up libtool.

* Sun Oct 8 2006 Linus Walleij <triad@df.lth.se> 0.8-1
- New upstream version including patch.
- The icon is an an even weirder place now!
- Have to run som autotools on this one to get it working.

* Tue Sep 5 2006 Linus Walleij <triad@df.lth.se> 0.7-5
- Patch to compile with new version of E-D-S.

* Thu Aug 10 2006 Linus Walleij <triad@df.lth.se> 0.7-4
- Missing BR

* Thu Aug 3 2006 Linus Walleij <triad@df.lth.se> 0.7-3
- Updated after feedback from Chris Weyl
- Bogus problem with cellphone.png icon image

* Sat Jul 29 2006 Linus Walleij <triad@df.lth.se> 0.7-2
- Updated after feedback from Parag and Paul

* Tue Jun 27 2006 Linus Walleij <triad@df.lth.se> 0.7-1
- 0.7 Release
- Took Matthews nrpm package and Fedora Extrasificated it

* Fri Sep 09 2005 Matthew Hall <matt@nrpms.net> 0.6-1
- 0.6 Release

* Mon Jun 20 2005 Matthew Hall <matt@nrpms.net> 0.4-1
- 0.4 Release
