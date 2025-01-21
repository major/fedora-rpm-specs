Name:           zeitgeist
Version:        1.0.4
Release:        18%{?dist}
Summary:        Framework providing Desktop activity awareness

# data/ontology/*.trig	BSD-3-Clause OR CC-BY-SA-3.0 -> main
#   Original: https://sourceforge.net/projects/oscaf/files/shared-desktop-ontologies/0.7/shared-desktop-ontologies-0.7.1.tar.bz2/
#   See: LICENSE.CC-BY in the above tarball
# data/ontology2code	 LGPL-2.0-or-later
# datahub/	 LGPL-3.0-or-later -> main
# doc/libzeitgeist/docs_vala/scripts.js	LGPL-2.0-or-later
# examples/c/	 GPL-3.0-only
# extensions/*.c	LGPL-2.0-or-later
# extensions/fts++/	GPL-2.0-or-later -> main
# libzeitgeist/		LGPL-2.0-or-later
# python/*.py	LGPL-2.0-or-later
# src/	(except for some files) LGPL-2.0-or-later
# src/notify.vala	GPL-2.0-or-later -> main
# test/c/	GPL-3.0-only
# test/	(other files) LGPL-2.0-or-later
# tools/	(except for some files) LGPL-2.0-or-later
# tools/zeitgeist-explorer/	GPL-2.0-or-later

# SPDX confirmed
License:        LGPL-2.0-or-later AND LGPL-3.0-or-later AND GPL-2.0-or-later AND (BSD-3-Clause OR CC-BY-SA-3.0)

URL:            https://launchpad.net/zeitgeist
Source0:        %{url}/1.0/%{version}/+download/%{name}-%{version}.tar.xz
# https://bugzilla.redhat.com/show_bug.cgi?id=1779103
# https://gitlab.freedesktop.org/zeitgeist/zeitgeist/issues/19
Patch1:         %{name}-1.0.4-0001-datahub-Fix-wrong-parameter-for-Event.full-ctor.patch

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-rdflib
BuildRequires:  systemd
BuildRequires:  vala
BuildRequires:  xapian-core-devel

BuildRequires:  pkgconfig(dee-icu-1.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(telepathy-glib)

BuildRequires:	/usr/bin/dbus-run-session

%{?systemd_requires}

Requires:       dbus
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      zeitgeist-datahub < 0.9.5-4
Obsoletes:      python2-%{name} < 1.0.2-1

%description
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and
makes relevant information available to other applications.
Note that this package only contains the daemon, which you can use
together with several different user interfaces.

%package -n python3-zeitgeist
Summary:        Python 3 bindings for zeitgeist
License:        LGPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

# manually specify runtime dependencies (no metadata)
Requires:       python3dist(dbus-python)

%description -n python3-zeitgeist
This package contains the Python 3 bindings for zeitgeist.

%package        libs
Summary:        Client library for interacting with the Zeitgeist daemon
License:        LGPL-2.0-or-later

%description    libs
Libzeitgeist is a client library for interacting with the Zeitgeist
daemon.

%package        devel
Summary:        Development files for %{name}
License:        LGPL-2.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1
# Regenerate C source from vala source
find -name '*.vala' -exec touch {} \;

## nuke unwanted rpaths, see also
## https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure

# The following two are hard to get enabled...
%if 0
sed -i.disable test/direct/Makefile.in \
	-e 's|log-test\$(EXEEXT) \\|\\|'
sed -i.disable test/c/Makefile.in \
	-e 's|test-log\$(EXEEXT) \\|\\|'
%endif

# python 3.11 removes inspect.getargspec (bug 2159916)
# https://gitlab.freedesktop.org/zeitgeist/zeitgeist/-/issues/26
# https://docs.python.org/3.11/whatsnew/3.11.html#removed
sed -i.py311 python/client.py \
	-e 's|inspect.getargspec|inspect.getfullargspec|'

%build
%configure --enable-fts --enable-datahub --disable-silent-rules
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete -print

# We install AUTHORS and NEWS with %%doc instead
rm -frv %{buildroot}%{_datadir}/zeitgeist/doc

%check
cat > test-script <<EOF
#!/bin/bash
set -x

PATH_ORIG=\${PATH}
export PATH=\${PATH_ORIG}:%{buildroot}%{_bindir}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

zeitgeist-daemon &
exec make check
EOF

chmod 0700 ./test-script
dbus-run-session -- ./test-script

%post
%systemd_user_post %{name}.service
%systemd_user_post %{name}-fts.service

%preun
%systemd_user_preun %{name}.service
%systemd_user_preun %{name}-fts.service

%ldconfig_scriptlets libs


%files
%doc AUTHORS
%doc NEWS
%license COPYING
%license COPYING.GPL

%{_bindir}/zeitgeist-daemon
%{_bindir}/zeitgeist-datahub
%dir	%{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/zeitgeist-fts

%dir	%{_datadir}/%{name}/
%dir	%{_datadir}/%{name}/ontology/
%{_datadir}/%{name}/ontology/*.trig
%{_datadir}/dbus-1/services/org.gnome.zeitgeist*.service
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/zeitgeist-daemon
%{_mandir}/man1/zeitgeist-*.*

%config(noreplace) %{_sysconfdir}/xdg/autostart/zeitgeist-datahub.desktop
%{_userunitdir}/%{name}.service
%{_userunitdir}/%{name}-fts.service

%files -n python3-zeitgeist
%{python3_sitelib}/zeitgeist/

%files libs
%license COPYING
%{_libdir}/girepository-1.0/Zeitgeist-2.0.typelib
%{_libdir}/libzeitgeist-2.0.so.*

%files devel
%{_includedir}/zeitgeist-2.0/
%{_libdir}/libzeitgeist-2.0.so
%{_libdir}/pkgconfig/zeitgeist-2.0.pc

%{_datadir}/gir-1.0/Zeitgeist-2.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/zeitgeist-2.0.deps
%{_datadir}/vala/vapi/zeitgeist-2.0.vapi
%{_datadir}/vala/vapi/zeitgeist-datamodel-2.0.vapi

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 16 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-17
- execute test program which require dbus and zeitgeist-daemon

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 1.0.4-15
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-13
- Regenerate C source from Vala source and enable
  -Werror=incompatible-pointer-types again
  (Thanks to Florian Weimer <fweimer@redhat.com>)

* Thu Jan 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-12
- Change -Wincompatible-pointer-types from error to warning

* Sun Dec 10 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-11
- SPDX migration

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.0.4-9
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-7
- F-37+: Replace inspect.getargspec removed on python3.11 (bug 2159916)

* Sat Sep 10 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-6
- Upstream patch: datahub: Fix wrong parameter for Event.full() ctor
  (Upstream bug 19, RH bug 1779103)

* Thu Sep  8 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-5
- Make make check error fatal
- Disable tests currently hard to get passed
- Make main package EVR aware for -libs subpackage

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Fabio Valentini <decathorpe@gmail.com> - 1.0.4-1
- Update to version 1.0.4.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.3-5
- Rebuilt for Python 3.10

* Tue Apr 20 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-4
- Include upstream patches for vala 0.52 support.

* Sun Mar 14 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-3
- Reintroduce Python bindings, they support Python 3 since version 1.0.3.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 David King <amigadave@amigadave.com> - 1.0.3-1
- Update to 1.0.3 (#1888547)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.2-1
- Update to version 1.0.2.
- Drop unused python bindings.
- Drop unnecessary patches.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 David King <amigadave@amigadave.com> - 1.0.1-1
- Update to 1.0.1
- Fix VAPI file for recent Vala (#1668410)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 David King <amigadave@amigadave.com> - 1.0-5
- Fix service file variable substitution (#1464693)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 21 2017 David King <amigadave@amigadave.com> - 1.0-1
- Update to 1.0
- Use pkgconfig for BuildRequires
- Use python_provide macro

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.16-4
- Rebuild (xapian 1.4)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 07 2015 Christopher Meng <rpm@cicku.me> - 0.9.16-1
- Update to 0.9.16

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-0.5.20140808.git.ce9affa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.16-0.4.20140808.git.ce9affa
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-0.3.20140808.git.ce9affa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Christopher Meng <rpm@cicku.me> - 0.9.16-0.2.20140808.git.ce9affa
- Introduce python-zeitgeist subpkg
- Mark xdg autostart file as noreplace for better UX, Fix BZ#863222

* Fri Aug 08 2014 Christopher Meng <rpm@cicku.me> - 0.9.16-0.1.20140808.git.ce9affa
- Update to 0.9.16 snapshot
- Fix BZ#1126461

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.14-4
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  9 2013 Brian Pepple <bpepple@fedoraproject.org> - 0.9.14-1
- Update to 0.9.14.

* Sun Jun 16 2013 Kalev Lember <kalevlember@gmail.com> - 0.9.13-2
- Fix postun script syntax error

* Fri Jun 14 2013 Deji Akingunola <dakingun@gmail.com> - 0.9.13-1
- Update to 0.9.13

* Sun Apr 14 2013 Kalev Lember <kalevlember@gmail.com> - 0.9.12-1
- Update to 0.9.12 (#949286)
- Obsolete zeitgeist-datahub
- Package up the libzeitgeist-2.0 library
- Update the license tag and add a spec file comment with longer explanations

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 23 2012 Deji Akingunola <dakingun@gmail.com> - 0.9.5-1
- Update to 0.9.5

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Deji Akingunola <dakingun@gmail.com> - 0.9.0-1
- Update to 0.9.0
- Apply upstream patch to fix a crasher bug.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.2-2
- Revert post-install script to restart zeitgeist daemon on update

* Tue Oct 18 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.2-1
- Update to 0.8.2
- Restart the zeitgeist daemon on update (BZ #627982)

* Wed Jul 20 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.1-1
- Update to 0.8.1

* Fri May 13 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.0-1
- Update to 0.8.0
- Add a hard requires on zeitgeist-datahub

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Deji Akingunola <dakingun@gmail.com> - 0.7-1
- Update to 0.7

* Fri Aug 06 2010 Deji Akingunola <dakingun@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 Deji Akingunola <dakingun@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3.1-1
- Update to 0.3.3.1 to fix datasource_registry bug (BZ #586238)

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3-1
- Update to 0.3.3

* Wed Jan 20 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Thu Jan 14 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.1-1
- Add missing requires (Package reviews)
- Update license tag (Package reviews)
- Update to latest release

* Tue Dec 01 2009 Deji Akingunola <dakingun@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Wed Nov 04 2009 Deji Akingunola <dakingun@gmail.com> - 0.2.1-1
- Initial Fedora packaging
