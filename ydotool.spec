# -*-Mode: rpm-spec-mode; -*-

%undefine __cmake_in_source_build

%global github_url https://github.com
%global iodash_name IODash
%global iodash_version 0.1.0
%global libevdevplus_name libevdevPlus
%global libevdevplus_version 0.2.1
%global libuinputplus_name libuInputPlus
%global libuinputplus_version 0.2.1
%global cxxopts_name cxxopts
%global cxxopts_version 3.0.0
%global cxxopts_commit 2d8e17c4f88efce80e274cb03eeb902e055a91d3
%global cpm_cmake_name cpm.cmake
%global cpm_cmake_version 0.27.5
%global debug_package %{nil}

Name:     ydotool
Version:  1.0.1
Release:  3%{?dist}
Summary:  Generic command-line automation tool (no X!)
License:  AGPLv3, Public Domain
URL:      %github_url/ReimuNotMoe/%{name}

Source0:  %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:  %{github_url}/YukiWorkshop/%{iodash_name}/archive/v%{iodash_version}/%(c=%{iodash_name}; echo ${c,,})-%{iodash_version}.tar.gz
Source2:  %{github_url}/YukiWorkshop/%{libevdevplus_name}/archive/v%{libevdevplus_version}/%{libevdevplus_name}-%{libevdevplus_version}.tar.gz
Source3:  %{github_url}/YukiWorkshop/%{libuinputplus_name}/archive/v%{libuinputplus_version}/%{libuinputplus_name}-%{libuinputplus_version}.tar.gz
Source4:  %{github_url}/jarro2783/%{cxxopts_name}/archive/%{cxxopts_commit}/%{cxxopts_name}-%{cxxopts_commit}.tar.gz
Source5:  %{github_url}/TheLartians/%{cpm_cmake_name}/archive/v%{cpm_cmake_version}/%{cpm_cmake_name}-%{cpm_cmake_version}.tar.gz
Source6:  https://gist.githubusercontent.com/panzi/6856583/raw/1eca2ab34f2301b9641aa73d1016b951fff3fc39/portable_endian.h

Patch1:   ydotool-man-page.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: scdoc
BuildRequires: systemd-rpm-macros

%description

Performs some of the functions of xdotool(1) without requiring X11 -
however, it generally requires root permission (to open /dev/uinput)

NOTE: changes in this release:
NOTE: --delay option is now --next-delay
NOTE: mousemove is now relative unless --absolute is given
NOTE: mouseup, mousedown, mousemove_relative is removed
NOTE: click accepts left, right, middle instead of 1, 2, 3
NOTE: sleep is a new command

SEE: ydotool <cmd> --help for latest info

Currently implemented command(s):

- type - Type a string
- key - Press keys
- mousemove - Move mouse pointer to absolute position
- click - Click on mouse buttons
- recorder - Record/replay input events
- sleep - sleep ms

N.B. it is strongly recommended to start the ydotoold daemon with:

- systemctl enable ydotool
- systemctl start ydotool

%prep
%setup -q
gzip -dc %{S:1} | tar xf -
gzip -dc %{S:2} | tar xf -
gzip -dc %{S:3} | tar xf -
gzip -dc %{S:4} | tar xf -
gzip -dc %{S:5} | tar xf -

%patch1 -p1

# this is missing from IODash - I have logged a bug report upstream
# https://github.com/YukiWorkshop/IODash/issues/1
# it is licenced 'public domain':
cp %{S:6} %{iodash_name}-%{iodash_version}/portable-endian.h

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF \
-DCPM_%{iodash_name}_SOURCE=$PWD/%{iodash_name}-%{iodash_version} \
-DCPM_%{libevdevplus_name}_SOURCE=$PWD/%{libevdevplus_name}-%{libevdevplus_version} \
-DCPM_%{libuinputplus_name}_SOURCE=$PWD/%{libuinputplus_name}-%{libuinputplus_version} \
-DCPM_%{cxxopts_name}_SOURCE=$PWD/%{cxxopts_name}-%{cxxopts_commit}

make -C %{_vpath_builddir} -j `nproc`

%install
mkdir -p %{buildroot}/%{_bindir}
strip */%{name}
strip */%{name}d
install -p -m 0755 */%{name} %{buildroot}/%{_bindir}
install -p -m 0755 */%{name}d %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 0644 */%{name}.service %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man8
scdoc < manpage/%{name}.1.scd > %{buildroot}/%{_mandir}/man1/%{name}.1
scdoc < manpage/%{name}d.8.scd > %{buildroot}/%{_mandir}/man8/%{name}d.8

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_unitdir}/%{name}.service
%{_bindir}/%{name}*
%license LICENSE
%doc README.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man8/%{name}d.8.*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-2
- added new manual (also pushed upstream)

* Thu Feb 17 2022 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-1
- new version

* Sun Feb 06 2022 Bob Hepple <bob.hepple@gmail.com> - 1.0.0-2
- now builds on all architectures without patches

* Sun Feb 06 2022 Bob Hepple <bob.hepple@gmail.com> - 1.0.0-1
- new version

* Sun Jan 30 2022 Bob Hepple <bob.hepple@gmail.com> - 0.2.0-8
- add -Wno-error= flags for FTBFS #2047136 in f36
- exclude armv7hl as it fails to compile

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.2.0-3
- Rebuilt for Boost 1.75

* Wed Jan 20 2021 Bob Hepple <bob.hepple@gmail.com> - 0.2.0-2
- rebuilt excluding s390x and ppc64le

* Mon Jan 11 2021 Bob Hepple <bob.hepple@gmail.com> - 0.2.0-1
- new version
- upstream has dropped the idea of -devel libraries so we are only
  distributing the regular package now; also libevdevPlus-devel and
  libuInputPlus-devel are no longer needed as they are now compiled
  in.

* Sat Aug 15 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.4.20200815.git.787fd25
- most recent version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-0.3.20200405.git.9c3a4e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.1.9-0.2.20200405.git.9c3a4e7
- Rebuilt for Boost 1.73

* Sun Apr 05 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200405.git.9c3a4e7
- Changes per RHBZ#1807753 - %{?systemd_requires} and ldconfig are no longer required

* Fri Apr 03 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200403.git.9c3a4e7
- Changes per RHBZ#1807753

* Wed Apr 01 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200401.git.9c3a4e7
- Changes per RHBZ#1807753

* Mon Mar 30 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200330.git.9c3a4e7
- Changes per RHBZ#1807753

* Sun Mar 22 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200322.git.9c3a4e7
- fix Source to get git tag directly

* Sat Feb 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200229.git.9c3a4e7
- Add a note on how to get source from upstream
- use lib*-devel packages in BuildRequires

* Tue Feb 18 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200218.git.9c3a4e7
- rebuild from head to pick up manuals & service file
- remove static build
- strip binaries (rpmlint complained about them)

* Mon Feb 17 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.8.20200211.3
- add BuildRequires: systemd-rpm-macros; add dist to release

* Sun Feb 16 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.8.20200211.2
- use %%_unitdir

* Sun Feb 16 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.8.20200211.1
- Initial version of the package
