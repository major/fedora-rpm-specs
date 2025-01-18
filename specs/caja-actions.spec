Summary: Caja extension for customizing the context menu
Name:    caja-actions
Version: 1.28.0
Release: 4%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+

URL: https://github.com/raveit65/%{name}
Source0: https://github.com/raveit65/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires: caja-devel
BuildRequires: dblatex
BuildRequires: desktop-file-utils
BuildRequires: libgtop2-devel
BuildRequires: libSM-devel
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: yelp-tools

Requires:       %{name}-doc = %{version}-%{release}


%description
Caja actions is an extension for Caja, the MATE file manager.
It provides an easy way to configure programs to be launch on files 
selected in Caja interface

%package doc
Summary: Documentations for %{name}
BuildArch: noarch

%description doc
This package contains the documentation for %{name}

%package devel
Summary: Development tools for the caja-actions
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and shared libraries needed for development
with caja-actions.

%prep
%autosetup -p1

%build
%configure \
    --disable-gtk-doc \
    --enable-html-manuals \
    --enable-pdf-manuals \
    --enable-deprecated

make %{?_smp_mflags} V=1

%install
%{make_install}

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

# clean docs dirs
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/INSTALL
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2008
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2009
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2010
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2011
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2012
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/MAINTAINERS

%find_lang %{name} --with-gnome --all-name


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/cact.desktop


%ldconfig_scriptlets


%files
%doc AUTHORS COPYING COPYING-DOCS ChangeLog NEWS README
%{_bindir}/caja-actions-run
%{_bindir}/caja-actions-config-tool
%{_bindir}/caja-actions-new
%{_bindir}/caja-actions-print
%{_libexecdir}/caja-actions/
%{_libdir}/caja-actions/
%{_libdir}/caja/extensions-2.0/libcaja-actions-menu.so
%{_libdir}/caja/extensions-2.0/libcaja-actions-tracker.so
%{_datadir}/caja-actions/
%{_datadir}/icons/hicolor/*/apps/caja-actions.*
%{_datadir}/applications/cact.desktop

%files doc -f %{name}.lang
%{_docdir}/caja-actions/html/
%{_docdir}/caja-actions/pdf/
%{_docdir}/caja-actions/objects-hierarchy.odg

%files devel
%{_includedir}/caja-actions/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 23 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-3
- use https://github.com/mate-desktop/caja-actions/commit/04d965a
- add BR desktop-file-utils

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0 release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.8.3-12
- clean up spec file, drop non working rhel7 macros for f32 branch
- fix building for f32

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Thomas Batten <stenstorpmc@gmail.com> - 1.8.3-10
- Disable doc path patch for el > 7

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.3-6
- Rebuilt for fixing rhbz (#1555660) (f28)
- switch to using autosetup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.3-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.3-1
- update to 1.8.3

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 1.8.2-2
- Rebuilt for libgtop2 soname bump

* Mon Feb 13 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.2-1
- update to 1.8.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.1-3
- switch to gtk3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.1-1
- update to 1.8.1 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 30 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-1
- update to 1.8.0 release
- fix english and non translated help

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 Kalev Lember <kalevlember@gmail.com> - 1.7.1-2
- Rebuilt for libgtop2 soname bump

* Sun Mar 16 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-1
- update to 1.7.1 release
- improve help documents
- move docs to main package

* Sun Mar 16 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-1
- add 1.7.0 release
- use yelp-tools, help is working now
- use --enable-gtk-docs, remove --disable-srollkepper
- use --enable-deprecated
- move find language to -doc subpackage, and use --with-gnome --all-name
- move gtk-docs to -devel subpackage
- remove changelog-2012
- add BR dblatex
- update configure flags

* Wed Dec 18 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-2
- update for rename caja in f21

* Sat Aug 17 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-1
- update to 1.6.2
- fix wrong-file-end-of-line-encoding in COPYING-DOCS
- remove obsolete sed command to fix desktop file

* Fri Aug 16 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-2
- move doc dirs to a -doc subpackage

* Thu Aug 15 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-1
- update to 1.6.1 release
- improve debug usage
- remove require hicolor-icon-theme
- fix bogus date in changelog

* Thu Nov 29 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-1
- removal of mate-conf usage
- add require hicolor-icon-theme

* Wed Nov 21 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.5.0-0101
- update version to 1.5.0
- disable mateconf
- remove desktop file fixes
- change configure flags
- update BR
- build against official fedora mate-desktop
- remove epoch

* Fri Nov 16 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:1.4.0-0102
- testbuild
- build for fedora
- add libxml2-devel BR

* Mon Nov 05 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:1.4.0-0101
- add epoch

* Thu Oct 04 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.4.0-0100
- udate vsersion to 1.4.0
- fix desktop files

* Mon Aug 27 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.4.0-0100
- build for f18

* Tue Aug 14 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.2.0-2
- switch to mate-filemanager

* Sat Apr 07 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.2.0-1
- rename nact to cact

* Tue Mar 27 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.1.0-2
- fix dso linking ICE error for fc17

* Sun Feb 12 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.1.0-1
- change version to mate release version

* Wed Jan 04 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 2.30.3-1
- start building for the MATE-Desktop
- caja-actions.spec based on nautilus-actions-2.30.3-1.fc14 spec

