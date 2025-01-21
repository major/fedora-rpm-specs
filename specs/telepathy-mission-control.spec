%define tp_glib_ver 0.17.5
%global mc_plugindir %{_libdir}/mission-control-plugins.0

Name:           telepathy-mission-control
Version:        5.16.5
Release:        13%{?dist}
Epoch:          1
Summary:        Central control for Telepathy connection manager

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://telepathy.freedesktop.org/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

# Backported from upstream
# https://github.com/TelepathyIM/telepathy-mission-control/pull/6
Patch0:         6.patch

BuildRequires: make
BuildRequires:  chrpath
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  libxslt-devel
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  pkgconfig
BuildRequires:  telepathy-glib-devel >= %{tp_glib_ver}

%description
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, and to remove the need to have in each program the
account definitions and credentials.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.


%prep
%autosetup -p1


%build
%configure \
  --disable-static \
  --enable-gtk-doc \
  --with-connectivity=nm

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

%{make_build}


%install
%{make_install}

# create/own plugin dir
mkdir -p %{buildroot}%{mc_plugindir}

# Remove rpaths if present
chrpath --list   %{buildroot}%{_libexecdir}/mission-control-5 && \
chrpath --delete %{buildroot}%{_libexecdir}/mission-control-5
# Remove .la files
find %{buildroot} -type f -name "*.la" -delete


%check
%if %{undefined flatpak}
PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "%{?mc_plugindir}" = "$(pkg-config --variable=plugindir mission-control-plugins 2>/dev/null)"
%endif
make check ||:


%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/mc-tool
%{_bindir}/mc-wait-for-name
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.AccountManager.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.MissionControl5.service
%{_datadir}/glib-2.0/schemas/im.telepathy.MissionControl.FromEmpathy.gschema.xml
%{_libdir}/libmission-control-plugins.so.0*
%dir %{mc_plugindir}
%{_libexecdir}/mission-control-5
%{_mandir}/man1/mc-tool.1*
%{_mandir}/man1/mc-wait-for-name.1*

%files devel
%doc %{_datadir}/gtk-doc/html/mission-control-plugins
%{_includedir}/mission-control-5.5/
%{_libdir}/pkgconfig/mission-control-plugins.pc
%{_libdir}/libmission-control-plugins.so
%{_mandir}/man8/mission-control-5.8*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1:5.16.5-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Kalev Lember <klember@redhat.com> - 1:5.16.5-2
- Backport a fix for a crash due to invalid property name

* Sat Feb 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.16.5-1
- Update to 5.16.5

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:5.16.4-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1:5.16.4-1
- Update to 5.16.4

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Rex Dieter <rdieter@fedoraproject.org> 1:5.16.3-5
- hard-code mc_plugindir macro, add %%check to verify correctness

* Wed Oct 14 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:5.16.3-4
- -devel: tighten subpkg dep via %%{?_isa}, rely on pkgconfig auto deps
- tighten file lists, track libsoname
- own /usr/lib*/mission-control-plugins.0
- %%build: drop unused --enable-mcd-plugins option
- .spec cosmetics, drop Group: tags

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1:5.16.3-3
- Use %%license
- Don't fail build on check fail (fix FTBFS)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 29 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1:5.16.3-1
- Update to 5.16.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Debarshi Ray <rishi@fedoraproject.org> - 1:5.16.2-1
- Update to 5.16.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Brian Pepple <bpepple@fedoraproject.org> - 1:5.16.1-1
- Update to 5.16.1.

* Wed Oct 30 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:5.16.0-2
- --disable-upower

* Thu Oct  3 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:5.16.0-1
- Update to 5.16.0.

* Thu Sep 19 2013 Debarshi Ray <rishi@fedoraproject.org> - 1:5.15.1-1
- Update to 5.15.1

* Thu Sep 19 2013 Debarshi Ray <rishi@fedoraproject.org> - 1:5.15.0-4
- Enable the Python tests

* Thu Sep 19 2013 Debarshi Ray <rishi@fedoraproject.org> - 1:5.15.0-3
- Add %%check to run the upstream test suite on each build

* Mon Aug 26 2013 Kalev Lember <kalevlember@gmail.com> - 1:5.15.0-2
- Fix the build

* Sun Aug  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1:5.15.0-1
- Update to 5.15.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Debarshi Ray <rishi@fedoraproject.org> - 1:5.14.1-3
- Remove rpath and omit some unused direct shared library dependencies.

* Thu Jun 20 2013 Matthias Clasen <mclasen@redhat.com> - 1:5.14.1-2
- Install NEWS instead of ChangeLog

* Fri May  3 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:5.14.1-1
- Update to 5.14.1.
- Drop defattr. No longer needed.
- Drop ignore gnome keyring patch. Fixed upstream.

* Thu Jan 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1:5.14.0-2
- Add patch for upstream b.fd.o # 59468

* Wed Oct  3 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.14.0-1
- Update to 5.14.0

* Thu Sep 20 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.13.2-1
- Update to 5.13.2.

* Thu Sep  6 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.13.1-1
- Update to 5.13.1.

* Mon Jul 23 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.13.0-1
- Update to 5.13.0.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.12.1-1
- Update to 5.12.1.

* Mon Apr  2 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.12.0-1
- Update to 5.12.0.

* Wed Feb 22 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.11.0-1
- Update to 5.11.0
- Bump minimum version of tp-glib.
