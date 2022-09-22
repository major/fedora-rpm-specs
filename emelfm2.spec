Name:           emelfm2
Version:        0.9.1
Release:        19%{?dist}
Summary:        File manager that implements the popular two-pane design

License:        GPLv3+
URL:            http://emelfm2.net/
Source0:        http://emelfm2.net/rel/%{name}-%{version}.tar.bz2
#VCS svn:http://svn.emelfm2.net/trunk/
Patch0:         emelfm2-0.7.1-dsofix.patch

BuildRequires:  gcc
BuildRequires:  dbus-glib-devel
BuildRequires:  file-devel
BuildRequires:  gtk2-devel
BuildRequires:  libacl-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
Requires:       findutils >= 4.2, grep, sed, bzip2
BuildRequires:  gtkspell-devel
BuildRequires:  udisks-devel
BuildRequires: make
Requires:       udisks


%description
emelFM2 is the GTK+2 port of emelFM. emelFM2 is a file manager that implements 
the popular two-pane design. It features a simple GTK+2 interface, a flexible 
file typing scheme, and a built-in command line for executing commands without 
opening an xterm.


%prep
%setup -q
%patch0 -p1 -b .dsofix

# fix broken icon in emelfm2.desktop
sed -i 's!Icon=emelfm2!Icon=%{_datadir}/pixmaps/emelfm2/emelfm2_48.png!' \
    po/%{name}.desktop.in

# get more useful build logs (verify CFLAGS etc)
sed -i 's!^\(\t\+\)@!\1!' Makefile


%build
# Build with -fcommon for now, the source is not written to use -fno-common
%global optflags %optflags -fcommon
# This package doesn't have a configure script. Instead, one needs to edit
# Makefile.config or pass options to the make command. When adding a new
# option, please use the same ordering as in Makefile.config
make %{?_smp_mflags} \
    DOC_DIR=%{_docdir}/%{name} \
    XDG_DESKTOP_DIR=%{_datadir}/applications \
    XDG_APPLICATION_DIR=%{_datadir}/application-registry \
    %if (0%{?fedora} && 0%{?fedora} < 20) || (0%{?rhel} && 0%{?rhel} < 7)
        DOCS_VERSION=1 \
    %endif
    WITH_TRANSPARENCY=1 \
    WITH_KERNELFAM=1 \
    USE_INOTIFY=1 \
    EDITOR_SPELLCHECK=1 \
    WITH_OUTPUTSTYLES=1 \
    WITH_CUSTOMMOUSE=1 \
    WITH_GTK2=1 \
    NEW_COMMAND=1 \
    WITH_UDISKS=1 \
    WITH_TRACKER=1 \
    WITH_ACL=1 \
    WITH_POLKIT=1 \
    PREFIX=%{_prefix} \
    BIN_DIR=%{_bindir} \
    LIB_DIR=%{_libdir} \
    PLUGINS_DIR=%{_libdir}/%{name}/plugins \
    ICON_DIR=%{_datadir}/pixmaps/%{name} \
    LOCALE_DIR=%{_datadir}/locale \
    MAN_DIR=%{_mandir}/man1 \
    CFLAGS="%{optflags}" \
    STRIP=0 \


%install
make install install_i18n \
    %if (0%{?fedora} && 0%{?fedora} < 20) || (0%{?rhel} && 0%{?rhel} < 7)
        DOCS_VERSION=1 \
    %endif
    PREFIX=%{buildroot}%{_prefix} \
    BIN_DIR=%{buildroot}%{_bindir} \
    LIB_DIR=%{buildroot}%{_libdir} \
    PLUGINS_DIR=%{buildroot}%{_libdir}/%{name}/plugins \
    ICON_DIR=%{buildroot}%{_datadir}/pixmaps/%{name} \
    LOCALE_DIR=%{buildroot}%{_datadir}/locale \
    MAN_DIR=%{buildroot}%{_mandir}/man1 \

%find_lang %{name}

desktop-file-install  \
    %if (0%{?fedora} && 0%{?fedora} < 19)
        --vendor fedora
    %endif
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

rm -f ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}/INSTALL
rm -f ${RPM_BUILD_ROOT}%{_docdir}/%{name}/INSTALL
rm -f ${RPM_BUILD_ROOT}%{_docdir}/%{name}/EBUILD
rm -f ${RPM_BUILD_ROOT}%{_docdir}/%{name}/SPEC


%files -f %{name}.lang
%doc docs/ACTIONS docs/CONFIGURATION docs/CREDITS docs/HACKING 
%doc docs/NEWS docs/README docs/TODO docs/USAGE docs/WARNING 
%doc docs/GPL docs/LGPL
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_mandir}/man1/emelfm2.1.gz


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.1-14
- gcc10: build with -fcommon for now

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.1-6
- Fix FTBFS rhbz #1307450

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Sat Oct 26 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Wed Aug 07 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
- Install docs unversioned on Fedora >= 20 (#992210)
- Make desktop vendor conditional

* Mon Mar 04 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.2-3
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- drop obsolete conditionals and version requirements
- drop INSTALL file
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2
- Drop upstreamed cursor-position.patch
- Enable processing of escape sequences in terminal output
- Improve build system and clean up spec file

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
- Patch editor to position cursor at start of opened file (instead of end)
- Explicitly build GTK2 version for now
- Add VCS key

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.5-1
- Update to 0.7.5

* Sun Nov 28 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Fri Jun 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3
- Add udisks support

* Thu Feb 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.1-2
- Add patch to fix DSO linking (#564729)

* Mon Dec 21 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Sun Nov 22 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2-2
- Fix a typo that prefented the debuginfo from being built (#513031)

* Mon Jul 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Fri Jul 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-2
- Build with ACL plugin again, got dropped accidentially.

* Fri Jul 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-1
- Update 0.6.1
- Enable auto (un)mounting using devicekit-disks
- Use new LIB_DIR option instead of PLUGINS_DIR
- Build with "STRIP=0" instead of using nostrip.patch

* Sat May 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-1
- Update 0.6.0
- Patch to fix segfault in e2_upgrade.so
- Enable the tracker plugin

* Fri May  8 2009 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-2
- Patch to not strip binaries before rpmbuild creates the -debuginfo subpackage (#499885)

* Wed Feb 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update 0.5.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 30 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update 0.5.0

* Tue Jul 08 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update 0.4.1
- Revove hal_flags.patch (fixed upstream)
- Remove HAL support until it really works. To enable rebuild "--with hal"

* Wed Apr 02 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update 0.4.0
- Enable HAL support, but dont install hal by default
- Add emelfm2-0.4-hal_flags.patch (Thanks to Uwe Helm)
- Require bzip2 for the unpack-plugin

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.6-2
- Autorebuild for GCC 4.3

* Sun Dec 02 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.6-1
- Update 0.3.6 with upstream's e2-0.3.6-07-12-01.patch
- Enable the ACL plugin

* Tue Aug 21 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-2
- Rebuild to fix SELinux issues on PPC32 and to include BuildID feature

* Sun Jul 29 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-1
- Update 0.3.5.

* Sat Jun 09 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.4-1
- Update 0.3.4.
- Enable support for inotify

* Wed Mar 21 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.3-1
- Update 0.3.3.

* Sat Feb 24 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-2
- Include upstream's e2-0.3.2-07-02-01.patch fixing some bugs.

* Fri Jan 19 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-1
- Update 0.3.2.
- Remove Category "Application" from emelfm2.desktop.

* Sat Dec 16 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.1-1
- Update 0.3.1.
- Remove Category "X-Fedora" from emelfm2.desktop.

* Mon Aug 28 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update 0.3.

* Mon Aug 28 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update 0.2.0.

* Fri Aug 11 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.8-2
- Include upstream's e2-0.1.8-06-08-09.patch to fix two serious bugs.

* Sun Aug 06 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8.

* Thu Apr 20 2006 Christoph Wickert <fedora wickert arcor de> - 0.1.7-1
- Update to 0.1.7.

* Tue Mar 14 2006 Christoph Wickert <fedora wickert arcor de> - 0.1.6-1
- Update to 0.1.6.
- Add Requires for plugins.

* Sat Feb 18 2006 Christoph Wickert <fedora wickert arcor de> - 0.1.5-2
- Rebuild for Fedora Extras 5.

* Thu Jan 26 2006 Christoph Wickert <fedora wickert arcor de> - 0.1.5-1
- Update to 0.1.5.

* Thu Dec 29 2005 Christoph Wickert <fedora wickert arcor de> - 0.1.4-1
- Update to 0.1.4.

* Mon Nov 21 2005 Christoph Wickert <fedora wickert arcor de> - 0.1.3-2
- Removed nonexistant ROADMAP from %%doc.

* Mon Nov 21 2005 Christoph Wickert <fedora wickert arcor de> - 0.1.3-1
- Update to 0.1.3.

* Tue Sep 27 2005 Christoph Wickert <fedora wickert acror de> - 0.1.2-3
- Fix for x86_64.

* Mon Sep 26 2005 Christoph Wickert <fedora wickert acror de> - 0.1.2-2
- Removed broken-icon.patch (using sed instead).
- Removed hardcoded /usr from makefile.config-patch.
- Minor specfile changes (#168608).

* Sun Sep 18 2005 Christoph Wickert <fedora wickert acror de> - 0.1.2-1
- Update to 0.1.2.

* Sun Sep 11 2005 Christoph Wickert <fedora wickert acror de> - 0.1.1-2
- Using destop-file-install.
- Several fixes for FE.

* Sun Aug 21 2005 Christoph Wickert <fedora wickert acror de> - 0.1.1-1.fc4.cw
- Initial RPM release.
