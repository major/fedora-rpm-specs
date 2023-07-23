%global commit0 a0763a246a81188f60b0f9810143e49224dc752f
%global date 20170423
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: PolicyKit integration for the GNOME desktop
Name:    polkit-gnome
Version: 0.106
Release: 0.14%{?commit0:.%{date}git%{shortcommit0}}%{?dist}
License: LGPLv2+
URL:     http://www.freedesktop.org/wiki/Software/PolicyKit
Source0: https://github.com/GNOME/PolicyKit-gnome/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
#Source0: https://ftp.gnome.org/pub/gnome/sources/polkit-gnome/%{version}/%{name}-%{version}.tar.xz
Patch0:  02-select-default-user.patch
Patch1:  04-autorestart.patch
Patch2:  06-authentication-failure-string.patch
Patch3:  07-use-accountsservice.patch
Patch4:  08-fresh-x11-timestamps.patch
Patch5:  0001-auth-dialog-make-the-label-wrap-at-70-chars.patch
Patch6:  remove_g_type_init.patch

BuildRequires: make
BuildRequires: gtk3-devel
BuildRequires: glib2-devel >= 2.25.11
BuildRequires: polkit-devel >= 0.97-1
BuildRequires: intltool
BuildRequires: gobject-introspection-devel
BuildRequires: gnome-common
BuildRequires: gtk-doc

Obsoletes: PolicyKit-gnome <= 0.10
Provides:  PolicyKit-gnome = 0.11
Obsoletes: PolicyKit-gnome-libs <= 0.10
Provides:  PolicyKit-gnome-libs = 0.11
Obsoletes: polkit-gnome-devel < 0.102-2
Provides:  polkit-gnome-devel = 0.102-2
Obsoletes: polkit-gnome-docs < 0.102-2
Provides:  polkit-gnome-docs = 0.102-2

Provides:  PolicyKit-authentication-agent = %{version}

Requires:  polkit >= 0.97

%description
polkit-gnome provides an authentication agent for PolicyKit
that matches the look and feel of the GNOME desktop.

%prep
%autosetup -p1 -n PolicyKit-gnome-%{?commit0}%{?!commit0:%{version}}
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static --enable-compile-warnings=no
%{make_build} V=1

%install
%{make_install}

%find_lang polkit-gnome-1

%ldconfig_scriptlets

%files -f polkit-gnome-1.lang
%doc AUTHORS README NEWS 
%license COPYING
%{_libexecdir}/*


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.14.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.13.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.12.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.11.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 5 2022 Alexej Kowalew <616b2f@gmail.com> - 0.106-0.10
- fix crashes under wayland

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.9.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.8.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.7.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.6.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.5.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.4.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.3.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.106-0.2.20170423gita0763a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.106-0.1.20170423gita0763a2
- Switch to git for improved locale support

* Thu Sep 14 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.105-14
- Fix source url
- Remove build requires desktop-file-utils
- Add version to PolicyKit-authentication-agent provides
- Spec file clean up

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.105-9
- add ububtu fixes as upstream is dead

* Thu Jun 18 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.105-8
- use license tag for COPYING

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 0.105-1
- Update to 0.105

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.104-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 0.104-1
- Update to 0.104

* Tue Oct 11 2011 Matthias Clasen <mclasen@redhat.com> - 0.103-2
- Try to fix Obsoletes/Provides

* Mon Sep 19 2011 Matthias Clasen <mclasen@redhat.com> - 0.103-1
- Update to 0.103
- Build against gtk3
- Drop no-longer-needed subpackages

* Tue Aug 16 2011 Matthias Clasen <mclasen@redhat.com> - 0.102-1
- Update to 0.102

* Thu Mar 03 2011 David Zeuthen <davidz@redhat.com> - 0.101-1
- New upstream version

* Mon Feb 21 2011 David Zeuthen <davidz@redhat.com> - 0.100-1
- New upstream version
- Note: The auto-start desktop file for the authentication agent is no
  longer shipped with this package. This is now the responsibility of
  each desktop environment.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 10 2010 Dan Horák <dan[at]danny.cz> - 0.97-7
- Add gtk-doc as BR

* Mon Aug 23 2010 Matthias Clasen <mclasen@redhat.com> - 0.97-6
- Co-own /usr/share/gtk-doc (#604411)

* Wed Aug 18 2010 Matthias Clasen <mclasen@redhat.com> - 0.97-5
- Rebuild to work around bodhi limitations

* Mon Aug 09 2010 David Zeuthen <davidz@redhat.com> - 0.97-4
- Bump polkit req to 0.97 since we have to chainbuild anyway. Sigh.

* Mon Aug 09 2010 David Zeuthen <davidz@redhat.com> - 0.97-3
- Nuke patch that was committed upstream

* Mon Aug 09 2010 David Zeuthen <davidz@redhat.com> - 0.97-2
- Fix up BRs

* Mon Aug 09 2010 David Zeuthen <davidz@redhat.com> - 0.97-1
- Update to 0.97

* Mon Jun 14 2010 Matthias Clasen <mclasen@redhat.com> - 0.96-2
- Use lock icons that exist in current icon theme
- Minor spec file fixes

* Fri Jan 15 2010 David Zeuthen <davidz@redhat.com> - 0.96-1
- Update to release 0.96
- Disable introspection support for the time being

* Tue Jan  5 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.95-2
- Don't autostart in KDE on F13+

* Fri Nov 13 2009 David Zeuthen <davidz@redhat.com> - 0.95-1
- Update to release 0.95
- Drop upstreamed patches

* Wed Oct  7 2009 Matthias Clasen <mclasen@redhat.com> - 0.95.0.git20090913.6
- Prevent the statusicon from eating whitespace

* Mon Sep 14 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.5
- add Provides: PolicyKit-authentication-agent to satify what PolicyKit-gnome
  also provided

* Mon Sep 14 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.4
- Refine how Obsolete: is used and also add Provides: (thanks Jesse
  Keating and nim-nim)

* Mon Sep 14 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.3
- Obsolete old PolicyKit-gnome packages

* Sun Sep 13 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.2
- Update BR

* Sun Sep 13 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.1
- Update BR

* Sun Sep 13 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913
- Update to git snapshot
- Turn on GObject introspection

* Wed Sep  2 2009 Matthias Clasen <mclasen@redhat.com> - 0.94-4
- Just remove the OnlyShowIn, it turns out everybody wants this

* Sat Aug 29 2009 Matthias Clasen <mclasen@redhat.com> - 0.94-3
- Require a new enough polkit (#517479)

* Sat Aug 29 2009 Matthias Clasen <mclasen@redhat.com> - 0.94-2
- Show in KDE, too (#519674)

* Wed Aug 12 2009 David Zeuthen <davidz@redhat.com> - 0.94-1
- Update to upstream release 0.94

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 David Zeuthen <davidz@redhat.com> - 0.93-2
- Rebuild

* Mon Jul 20 2009 David Zeuthen <davidz@redhat.com> - 0.93-1
- Update to 0.93

* Tue Jun  9 2009 Matthias Clasen <mclasen@redhat.com> - 0.9.2-3
- Fix BuildRequires

* Tue Jun 09 2009 David Zeuthen <davidz@redhat.com> - 0.92-2
- Change license to LGPLv2+
- Remove Requires: gnome-session

* Mon Jun 08 2009 David Zeuthen <davidz@redhat.com> - 0.92-1
- Update to 0.92 release

* Wed May 27 2009 David Zeuthen <davidz@redhat.com> - 0.92-0.git20090527
- Update to 0.92 snapshot

* Mon Feb  9 2009 David Zeuthen <davidz@redhat.com> - 0.91-1
- Initial spec file.
