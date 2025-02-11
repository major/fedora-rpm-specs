Name:           flatpak-rpm-macros
Version:        42
Release:        1%{?dist}
Summary:        Macros for building RPMS for flatpaks
Source0:        macros.flatpak.in
Source1:        distutils.cfg
Source2:        flatpak.xml
Source3:        fontconfig-flatpak.prov
License:        MIT

# Buildrequire these to satisfy Pyton byte-compilation hooks
BuildRequires:  python3-devel

%description
The macros in this package set up the RPM build environment so built
applications install in /app rather than /usr. This package is meant
only for installation in buildroots when rebuilding RPMS to package
in Flatpaks.

%prep

%build
sed -e 's|__LIB__|%{_lib}|g' \
    %{SOURCE0} > macros.flatpak

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
install -t $RPM_BUILD_ROOT%{_sysconfdir}/rpm -p -m 644 macros.flatpak
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/distutils/
install -t $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/distutils/ %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xmvn/config.d
install -t $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xmvn/config.d -m 644 %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}
install -t $RPM_BUILD_ROOT%{_rpmconfigdir} -m 755 %{SOURCE3}

%files
# The location in sysconfdir contradicts
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_of_Additional_RPM_Macros
# but I believe is necessary to properly override macros that are otherwise set.
%{_sysconfdir}/rpm/
%{_libdir}/python%{python3_version}/distutils/distutils.cfg
%{_sysconfdir}/xdg/xmvn/config.d/flatpak.xml
%{_rpmconfigdir}/fontconfig-flatpak.prov

%changelog
* Sun Feb 09 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 42-1
- Bump version

* Mon Sep 23 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 41-2
- Update pandoc_datadir

* Thu Aug 15 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 41-1
- Bump version

* Tue May 14 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 40-3
- Define pandoc_datadir

* Mon Apr 08 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 40-2
- Override jurand macros

* Wed Mar 27 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 40-1
- Version bump for F40
- Define JAVA_HOME, JAVACONFDIRS and %%__maven_path
- Change xmvn configuration location

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 28 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 39-4
- Define %%_localstatedir and %%__git

* Tue Aug 22 2023 Owen Taylor <otaylor@redhat.com> - 39-3
- Fix %%dist tag to be consistent with fedora-release

* Mon Aug 7 2023 Owen Taylor <otaylor@redhat.com> - 39-2
- Bump release for rebuild

* Mon Aug 7 2023 Owen Taylor <otaylor@redhat.com> - 39-1
- Set %%dist to f%%{fedora}app - this is for building without modules

* Fri Aug 04 2023 Kalev Lember <klember@redhat.com> - 39-1
- Update %%python_sitearch for python-3.12 (rhbz#2225806)
- Fix brp-compress search path to correctly compress man pages in /app

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 25 2023 Kalev Lember <klember@redhat.com> - 37-5
- Redefine __perl macro as /usr/bin/perl

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 37-3
- Fix host search paths for noarch builds

* Tue Aug 23 2022 Kalev Lember <klember@redhat.com> - 37-2
- Sync build_ldflags with redhat-rpm-config
- Drop python3_sitelib/sitearch overrides
- Override _fontbasedir to honor /app prefix

* Tue Aug 02 2022 Kalev Lember <klember@redhat.com> - 37-1
- Update %%python_sitearch for python-3.11 (#2113228)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Kalev Lember <klember@redhat.com> - 35-3
- Disable rpath checks as they don't work right for non-/usr prefix

* Fri Oct 01 2021 Kalev Lember <klember@redhat.com> - 35-2
- Sync ___build_pre section with macros from rpm 4.17.0

* Mon Aug 23 2021 Kalev Lember <klember@redhat.com> - 35-1
- Update %%python_sitearch for python-3.10 (#1987478)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Kalev Lember <klember@redhat.com> - 34-1
- Override RPM's fontconfig auto-provide to handle /app/share/fonts

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 2020 Kalev Lember <klember@redhat.com> - 33-2
- Redefine __python2 macro to point to /app/bin/python2

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 33-1
- Update %%python_sitearch for python-3.9

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Kalev Lember <klember@redhat.com> - 32-2
- Remove Python 2 support (#1805232)

* Wed Mar 18 2020 Stephan Bergmann <sbergman@redhat.com> - 32-1
- Let xmvn_install store artifacts under /app

* Thu Feb 06 2020 David King <amigadave@amigadave.com> - 29-12
- Update %%python_sitearch for python-3.8 (#1799346)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Kalev Lember <klember@redhat.com> - 29-9
- Use optflags, rather than __global_compiler_flags

* Thu Apr 04 2019 Stephan Bergmann <sbergman@redhat.com> - 29-8
- Add CFLAGS and CXXFLAGS to macros.flatpak, to match LDFLAGS

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Owen Taylor <otaylor@redhat.com> - 29-6
- Fix accidentally not installing the macro file

* Thu Sep 27 2018 Owen Taylor <otaylor@redhat.com> - 29-5
- Install a distutils.cfg to redirect installation of Python packages to /app
  this makes the package no longer noarch because the file is in
  /usr/lib or /usr/lib64.

* Tue Sep 25 2018 Owen Taylor <otaylor@redhat.com> - 29-4
- Remove space in -L <libdir>

* Thu Sep 20 2018 Owen Taylor <otaylor@redhat.com> - 29-3
- Extend set of overriden Python macros

* Wed Sep 19 2018 Owen Taylor <otaylor@redhat.com> - 29-2
- Improve LDFLAGS flags handling in macros.flatpak

* Sat Sep  8 2018 Owen Taylor <otaylor@redhat.com> - 29-1
- Instead of defining %%app to true, define %%flatpak to 1
- Update %%python_sitearch for python-3.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Owen Taylor <otaylor@redhat.com> - 27-2
See https://bugzilla.redhat.com/show_bug.cgi?id=1460076
- Wrap description lines
- Own /etc/rpm, to avoid requiring rpm package
- Preserve timestamp on installation

* Wed May 31 2017 Owen Taylor <otaylor@redhat.com> - 27-1
- Initial version, based on work by Alex Larsson <alexl@redhat.com>
