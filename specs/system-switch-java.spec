# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global py_byte_compile 1

Name: system-switch-java
Version: 1.1.8
Release: 14%{?dist}
Summary: A tool for changing the default Java toolset


# Automatically converted from old format: GPLv2+ and BSD - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL: https://pagure.io/%{name}
Source0: http://releases.pagure.org/%{name}/%{name}-%{name}-%{version}.tar.gz
Patch0: pythonversion.bad.patch
# ask autopoint to use gettext installed on the system to prevent mismatch in version
Patch1: configure.patch

BuildArch: noarch

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: autoconf
BuildRequires: automake

Requires: /usr/sbin/alternatives
Requires: libglade2
Requires: python3-newt
Requires: python3-gobject-base
Requires: python3
Requires: usermode
Requires: usermode-gtk

%description
The system-switch-java package provides an easy-to-use tool to select
the default Java toolset for the system.

%prep
%setup -q -n system-switch-java-system-switch-java-1.1.8
%patch -P0
%patch -P1

%build
sh ./autogen.sh
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/system-switch-java/__pycache__/*
%find_lang %{name}
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%license COPYING COPYING.icon
%doc AUTHORS README
%{_bindir}/%{name}
%{_sbindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/switch_java_functions.py*
%{_datadir}/%{name}/switch_java_gui.py*
%{_datadir}/%{name}/switch_java_tui.py*
%{_datadir}/%{name}/switch_java_globals.py*
%{_datadir}/%{name}/switch_java_boot.py*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/system-switch-java.glade
%config(noreplace) /etc/pam.d/%{name}
%config(noreplace) /etc/security/console.apps/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.8-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Petra Alice Mikova <pmikova@redhat.com> - 1.1.8-4
- replace %_python_bytecompile_extra with %py_byte_compile 

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Petra Alice Mikova <pmikova@redhat.com> - 1.1.8-1
- updated to new sources
- autogen.sh is now run during the build instead prior
- configure.patch to avoid gettext version mismatch

* Fri Oct 11 2019 Lumír Balhar <lbalhar@redhat.com> - 1.1.7.2-7
- Fixed unversioned Python dependencies

* Fri Oct 04 2019 Jiri Vanek <jvanek@redhat.com> - 1.1.7.2-6
- pathced out python2 shebang

* Thu Oct 03 2019 Jiri Vanek <jvanek@redhat.com> - 1.1.7.2-5
- bumped to python instead of python2
- the sources are not 100% working with python 3 now, but patch will be upstreamed, and sources bumped

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 5 2019 akurtakov <akurtakov@localhost.localdomain> 1.1.7.2-3
- Switch requires from pygtk2 (no longer needed) to python2-gobject to reflect new deps.

* Fri Mar 01 2019 - Jiri Vanek <jvanek@redhat.com> - 1.1.7.2-1
- bumped to 1.7.2 with gtk3 support (https://pagure.io/system-switch-java/c/801cd26e46075fa822b789ff79e775bc9079ea53?branch=master)
- removed BR of intltool
- added BR of gettext-devel

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.7.1-8
- Spec cleanups, use %%license

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.7.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 20 2018 - Jiri Vanek <jvanek@redhat.com> - 1.1.7.1-5
- added buildrequires on gcc/gcc-c++
- to follow new packaging guidelines which no longer automatically pulls gcc/c++ to build root

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7.1-3
- updated url to current package upstrem

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Jiri Vanek <jvanek@redhat.com> - 1.1.7.1-1
- updated to latest upstream, removed upstreamed patches

* Tue Apr 26 2016 Jiri Vanek <jvanek@redhat.com> - 1.1.6-3
- added upsteam patch 107 for better jdk9 support

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Jiri Vanek <jvanek@redhat.com> - 1.1.6-1
- updated to upstream release of 1.1.6
- removed all upstreamed patches

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Jiri Vanek <jvanek@redhat.com> - 1.1.5-10
- Renamed (to baseurl) url macro to prevent shadowing
- Added BSD license to list of Licenses
 - (COPYING.icon says it's a 2-clause BSD license)
- removed buildroot definition and manual removing of it

* Fri Feb 21 2014 Omair Majid <omajid@redhat.com> - 1.1.5-9
- Remove libuser-python dependency

* Mon Feb 10 2014 Omair Majid <omajid@redhat.com> - 1.1.5-8
- Update to work with newer alternatives

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 1.1.5-2
- recompiling .py files against Python 2.7 (rhbz#623409)

* Wed Aug 19 2009 Deepak Bhole <dbhole@redhat.com>  - 1.1.5-1-1
- Update to 1.1.5 which fixes rhbz 493898 and adds more translations

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1.4-2
- Rebuild for Python 2.6

* Tue Oct 28 2008 Deepak Bhole <dbhole@redhat.com> - 1.1.4-1
- Update to 1.1.4, which contains new translations

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1.3-2
- fix license tag

* Thu Jul  3 2008 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.3-1
- Import system-switch-java 1.1.3.
- Remove desktop file patch.
- Remove Fedora 7 obsoletes.
- Resolves: rhbz#453625

* Wed Jun 11 2008 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.2-3
- Update URL and source tags to point to Fedora Hosted.

* Mon Apr 14 2008 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.2-2
- Require libuser-python in place of libuser.
- Require newt-python in place of newt.
- Resolves: rhbz#251352

* Tue Oct  2 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.2-1
- Import system-switch-java 1.1.2.
- Resolves: rhbz#312321

* Fri Sep 28 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.1-1
- Import system-switch-java 1.1.1.

* Sat Jul 21 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-4
- Tolerate trailing newlines in alternatives file.
- Bump release number.

* Sat Jul 14 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-3
- Use Fedora 8 desktop file categories.
- Use desktop-file-install.
- Bump release number.

* Thu Jul  5 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-2
- Bump release number.

* Thu Jul  5 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-1
- Do not use desktop-file-install.

* Wed Jul  4 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-1
- Add categories when installing desktop file.

* Wed Jun 27 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-1
- Import system-switch-java 1.1.0.
- Merge gui subpackage into base package.

* Tue Jan 23 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.0.0-1
- Initial release.
