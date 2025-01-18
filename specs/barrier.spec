%undefine __cmake_in_source_build
%global icon_path %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
Summary: Use a single keyboard and mouse to control multiple computers
Name: barrier
Version: 2.4.0
Release: 10%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/debauchee/barrier/wiki
Source0: https://github.com/debauchee/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/debauchee/barrier/issues/1366
Patch0: fix-includes.patch
# Add missing #include directives needed for GCC 13
# https://github.com/debauchee/barrier/pull/1886
Patch1: https://github.com/debauchee/barrier/pull/1886.patch

BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: cmake3
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gmock-devel
BuildRequires: gtest-devel
BuildRequires: gulrak-filesystem-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: make

Requires: hicolor-icon-theme

%description
Barrier is software that mimics the functionality of a KVM switch, which
historically would allow you to use a single keyboard and mouse to control
multiple computers. Barrier does this in software, allowing you to tell it
which machine to control by moving your mouse to the edge of the screen,
or by using a key press to switch focus to a different system.

%prep
%autosetup -p1
## thus remove test

## thus ignore the tests
sed -i.remove-test -e 's/.*gtest.cmake/#&/' src/CMakeLists.txt
## Category DesktopUtility is NOT registered
sed -i.remove-invalid -e 's/DesktopUtility;//' res/%{name}.desktop

sed -i.use-gcc-ar -e '/include (CheckIncludeFiles)/ i set(CMAKE_AR "/usr/bin/gcc-ar")' CMakeLists.txt
sed -i.use-gcc-ranlib -e '/include (CheckIncludeFiles)/ i set(CMAKE_RANLIB "/usr/bin/gcc-ranlib")' CMakeLists.txt

%build
%cmake . \
    -DBARRIER_BUILD_INSTALLER=OFF \
    -DBARRIER_BUILD_TESTS=no
%cmake_build

%install
cd %{_vpath_builddir}
install -D -p -m 0755 bin/barrier      %{buildroot}%{_bindir}/barrier
install -D -p -m 0755 bin/barrierc     %{buildroot}%{_bindir}/barrierc
install -D -p -m 0755 bin/barriers     %{buildroot}%{_bindir}/barriers
cd -
install -D -p -m 0644 res/barrier.desktop %{buildroot}%{_datadir}/applications/barrier.desktop
install -D -p -m 0644 doc/barrierc.1 %{buildroot}%{_mandir}/man1/barrierc.1
install -D -p -m 0644 doc/barriers.1 %{buildroot}%{_mandir}/man1/barriers.1
install -D -p -m 0644 res/barrier.ico  %{buildroot}%{_datadir}/pixmaps/barrier.ico
install -D -p -m 0644 res/barrier.svg %{buildroot}%{icon_path}

cd %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/metainfo
## Write AppStream
cat <<END> %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2020 Ding-Yi Chen <dchen@redhat.com> -->
<component type="desktop-application">
  <id>%{name}</id>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPLv2</project_license>
  <name>%{name}</name>
  <summary>%{summary}</summary>

  <description>
    <p>%{description}</p>
  </description>

  <launchable type="desktop-id">%{name}.desktop</launchable>

  <url type="homepage">%{url}</url>

  <provides>
    <binary>barrier</binary>
    <binary>barrierc</binary>
    <binary>barriers</binary>
  </provides>

  <releases>
    <release version="%{version}" date="2021-11-02" />
  </releases>
</component>
END

desktop-file-install --delete-original  \
  --dir %{buildroot}%{_datadir}/applications            \
  --set-icon=%{icon_path}           \
  %{buildroot}%{_datadir}/applications/barrier.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/barrier.desktop

%files
# None of the documentation files are actually useful here, they all point to
# the online website, so include just one, the README
%license LICENSE
%doc ChangeLog res/Readme.txt doc/barrier.conf.example*
%{_bindir}/barrierc
%{_bindir}/barriers
%{_bindir}/barrier
%{_datadir}/pixmaps/barrier.ico
%{icon_path}
%{_datadir}/applications/barrier.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/barrierc.1*
%{_mandir}/man1/barriers.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.0-4
- Add missing #include directives needed for GCC 13 (fix RHBZ#2113118)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Ding-Yi Chen <dchen@redhat.com> - 2.4.0-1
- Upstream update to 2.4.0
  - Fixed CVE-2021-42072 (RHBZ 2022094)
- BuildDepends added: gmock-devel, gulrak-filesystem-devel
- Address the issue from pull request #1, thanks aekoroglu.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.3.3-5
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Ding-Yi Chen <dchen@redhat.com> - 2.3.3-2
- Fix build for Fedora 32

* Fri Oct 30 2020 Ding-Yi Chen <dchen@redhat.com> - 2.3.3-1
- Upstream update to 2.3.3
- Add BuildRequires: gtest-devel

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Ding-Yi Chen <dchen@redhat.com> -  2.3.2-2
- Address review comments:
  + Use better URL
  + BuildRequires added: gcc-c++
  + Requires add: hicolor-icon-theme
- BuildRequires remove: qt-devel


* Tue Jun 30 2020 Ding-Yi Chen <dchen@redhat.com> -  2.3.2-1
- Upstream update to 2.3.2
- Remove the link to synergy command to avoid package collision.

* Wed Jan 23 2019 Brian J. Murrell <brian@interlinx.bc.ca> - 2.1.2-1
- Initial RPM release, based on the spec from Fedora's synergy.
- Create convenience symlinks to old synergy* names for the benefit
  of tools that will have those names hard-coded, such as quicksynergy
