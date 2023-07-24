%define __cmake_in_source_build 1

%global release_date 2022-07-19
%global icon_path %{_datadir}/icons/hicolor/scalable/apps/synergy.svg
Summary: Share mouse and keyboard between multiple computers over the network
Name: synergy
Epoch: 1
Version: 1.14.5.17
Release: 2%{?dist}
License: GPLv2
URL: https://symless.com/synergy
Source0: https://github.com/symless/synergy-core/archive/refs/tags/%{version}.tar.gz
Patch0: synergy-1.14_fix-includes.patch

# Last built version of synergy-plus was 1.3.4-12.fc20
Provides: synergy-plus = %{version}-%{release}
Obsoletes: synergy-plus < 1.3.4-13
BuildRequires: make
BuildRequires: cmake3
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libXtst-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libnotify-devel
BuildRequires: libxkbfile-devel
BuildRequires: openssl-devel
BuildRequires: pugixml-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: gtest-devel
BuildRequires: gmock-devel
Requires: qt5-qtbase


%description
Synergy lets you easily share your mouse and keyboard between multiple
computers, where each computer has its own display. No special hardware is
required, all you need is a local area network. Synergy is supported on
Windows, Mac OS X and Linux. Redirecting the mouse and keyboard is as simple
as moving the mouse off the edge of your screen.

%prep
%setup -q -n %{name}-core-%{version}
%patch0 -p1
#Remove the submodule pugixml
sed -i.remove-sub-pugixml -e '/pugixml/ s/^/#/' src/lib/synergy/CMakeLists.txt

#Add lib pugixml
sed -i.add-lib-pugixml -e '/target_link_libraries(synlib arch/ s/target_link_libraries(synlib arch \(.*\))/target_link_libraries(synlib arch \1 pugixml)/' src/lib/synergy/CMakeLists.txt

#insert include <array> to avoid has initializer but incomplete type
sed -i.include-array -e '/#include <sys\/utsname.h>/ i #include <array>' src/lib/arch/unix/ArchSystemUnix.cpp

%build
PATH="$PATH:/usr/lib64/qt4/bin:/usr/lib/qt4/bin"
#Disable tests for now (bundled gmock/gtest)
%{cmake3} -DSYNERGY_VERSION_STAGE:STRING=stable -DBUILD_TESTS=false -DSYNERGY_ENTERPRISE=true .
%make_build

%install
%make_install

## Making manpages
mkdir -p %{buildroot}%{_mandir}/man8
gzip -c doc/synergyc.man > %{buildroot}%{_mandir}/man8/synergyc.8.gz
gzip -c doc/synergys.man > %{buildroot}%{_mandir}/man8/synergys.8.gz

mkdir -p %{buildroot}%{_datadir}/metainfo
## Write AppStream
cat <<END> %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2018 Ding-Yi Chen <dchen@redhat.com> -->
<component type="desktop-application">
  <id>%{name}</id>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPLv2</project_license>
  <name>synergy</name>
  <summary>Share mouse and keyboard between multiple computers over the network</summary>

  <description>
    <p>
    Synergy lets you easily share your mouse and keyboard between multiple
    computers, where each computer has its own display. No special hardware is
    required, all you need is a local area network. Synergy is supported on
    Windows, Mac OS X and Linux. Redirecting the mouse and keyboard is as simple
    as moving the mouse off the edge of your screen.
    </p>
  </description>

  <launchable type="desktop-id">%{name}.desktop</launchable>

  <url type="homepage">https://symless.com/synergy</url>

  <provides>
    <binary>synergy</binary>
    <binary>synergyc</binary>
    <binary>synergys</binary>
    <binary>syntool</binary>
  </provides>

  <releases>
    <release version="%{epoch}:%{version}" date="%{release_date}" />
  </releases>
</component>
END

desktop-file-install --delete-original  \
  --dir %{buildroot}%{_datadir}/applications            \
  --set-icon=%{icon_path}            \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/synergy.desktop

%files
# None of the documentation files are actually useful here, they all point to
# the online website, so include just one, the README
%doc LICENSE ChangeLog README.md res/Readme.txt doc/synergy.conf.example*
%{_bindir}/synergyc
%{_bindir}/synergys
%{_bindir}/syntool
%{_bindir}/synergy
%{icon_path}
%{_datadir}/applications/synergy.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man8/synergyc.8.gz
%{_mandir}/man8/synergys.8.gz

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.14.5.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 21 2023 David Kaufmann <astra@ionic.at> - 1:1.14.5.17-1
- Update to v1.14.5.17

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.14.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.14.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 25 2022 Ding-Yi Chen <dchen@redhat.com> - 1:1.14.3.5-1
- Upstream update to v1.14.3.5-stable
- Add BuildRequires: libnotify-devel, libxkbfile-devel, pugixml-devel

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.14.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:1.14.0.4-2
- Rebuilt with OpenSSL 3.0.0

* Tue Sep 14 2021 David Kaufmann <astra@ionic.at> - 1:1.14.0.4-1
- Upstream update to v1.14.0.4-stable (from v1.13, changelog entry is missing)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.13.1.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 David Kaufmann <astra@ionic.at> - 1:1.12.0-1
- Upstream update to v1.12.0-stable

* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 1:1.11.1-4
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Ding-Yi Chen <dchen@redhat.com> - 1:1.11.1-1
- Upstream update to v1.11.1-stable

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Ding-Yi Chen <dchen@redhat.com> - 1:1.10.2-1
- Revert to v1 as Synergy 2 is back to beta
  https://symless.com/blog/synergy-2-back-beta
- Following files/programs are gone
  * /usr/bin/synergy-core
  * /usr/share/pixmaps/synergy.ico
- Following files/programs are back
  * /usr/bin/synergy
  * /usr/bin/syntool

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.0.0-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Tue Feb 06 2018 Ding-Yi Chen <dchen@redhat.com> - 2.0.0-2
- Restore Program /usr/bin/synergy
- Fixes Bug 1542286 synergy-2.0.0 should not have been pushed anywhere except rawhide
- Fixes Bug 1541640 - synergy.desktop file useless

* Wed Jan 17 2018 Ding-Yi Chen <dchen@redhat.com> - 2.0.0-1
- Update to 2.0.0
- Fixes Bug 1476515 - AppStream metadata for Synergy package are missing
- The real executable is now "synergy-core",
  "synergy" is now a symlink to synergy-core
- cmake3 is now BuildRequired
- syntool is removed by upstream

* Thu Oct 26 2017 Ding-Yi Chen <dchen@redhat.com> - 1.8.8-2
- Skip SSL patch if the system does not have SSL_get_client_ciphers

* Thu Oct 12 2017 Ding-Yi Chen <dchen@redhat.com> - 1.8.8-1
- Update to 1.8.8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 11 2016 Johan Swensson <kupo@kupo.se> - 1.7.6-1
- Update to 1.7.6
- Clean up BuildRequires
- Package syntool

* Sun Feb 21 2016 Johan Swensson <kupo@kupo.se> - 1.7.5-1
- Update to 1.7.5
- Add BuildRequires openssl-devel

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Dec 20 2014 Johan Swensson <kupo@kupo.se> - 1.6.2-1
- Update to 1.6.2

* Fri Nov 28 2014 Johan Swensson <kupo@kupo.se> - 1.6.1-1
- Update to 1.6.1
- BuildRequire avahi-compat-libdns_sd-devel

* Sat Aug 23 2014 Johan Swensson <kupo@kupo.se> - 1.5.1-1
- Update to 1.5.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Johan Swensson <kupo@kupo.se> - 1.5.0-1
- Update to 1.5.0
- Update source url
- libcurl-devel, qt-devel, cryptopp-devel and desktop-file-utils buildrequired
- unbundle cryptopp
- unbundle gmock and gtest
- include synergy gui
- fix icon path

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May  7 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4.10-4
- increase synergy-plus obs_ver once more to obsolete the F20 rebuild

* Mon Sep 16 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4.10-3
- correct synergy-plus obs_ver

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Christian Krause <chkr@fedoraproject.org> - 1.4.10-1
- Update to 1.4.10 (#843971).
- Cleanup spec file.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Matthias Saou <matthias@saou.eu> 1.3.7-3
- Add missing Provides for synergy-plus (#722843 re-review).

* Mon Jul 18 2011 Matthias Saou <matthias@saou.eu> 1.3.7-2
- Update summary.

* Tue Jul 12 2011 Matthias Saou <matthias@saou.eu> 1.3.7-1
- Update to 1.3.7.
- Drop patch disabling XInitThreads, see upstream #610.
- Update %%description and %%doc.
- Replace cmake patch with our own install lines : Less rebasing.

* Mon Jul 11 2011 Matthias Saou <matthias@saou.eu> 1.3.6-2
- Update Obsoletes for the latest version + fix (release + 1 because of dist).
- Add missing cmake BuildRequires.
- Update cmake patch to also install man pages.

* Fri Feb 18 2011 quiffman GMail 1.3.6-1
- Update to reflect the synergy/synergy+ merge to synergy-foss.org (#678427).
- Build 1.3.5 and newer use CMake.
- Patch CMakeLists.txt to install the binaries.

* Thu Jul  8 2010 Matthias Saou <matthias@saou.eu> 1.3.4-6
- Don't apply the RHEL patch on RHEL6, only 4 and 5.

* Mon Dec  7 2009 Matthias Saou <matthias@saou.eu> 1.3.4-5
- Obsolete synergy (last upstream released version is from 2006) since synergy+
  is a drop-in replacement (#538179).

* Tue Nov 24 2009 Matthias Saou <matthias@saou.eu> 1.3.4-4
- Disable XInitThreads() on RHEL to fix hang (upstream #194).

* Tue Aug 18 2009 Matthias Saou <matthias@saou.eu> 1.3.4-3
- Don't use the -executable find option, it doesn't work with older versions.

* Tue Aug 18 2009 Matthias Saou <matthias@saou.eu> 1.3.4-2
- Initial RPM release, based on the spec from the original synergy.
- Remove spurious executable bit from sources files.

