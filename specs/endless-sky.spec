Name:		endless-sky
Version:	0.10.10
Release:	2%{?dist}
Summary:	Space exploration, trading, and combat game

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://%{name}.github.io
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	endless-sky-wrapper
# Replace /usr/games with /usr/bin and /usr/share/games with /usr/share per
# https://fedoraproject.org/wiki/SIGs/Games/Packaging.
# Patch not submitted upstream. Upstream conforms to Debian packaging
# standards where the use of /usr/games is acceptable.
Patch0:		endless-sky-0.10.0-remove-games-path.patch

Requires:	%{name}-data = %{version}-%{release}
BuildRequires:	cmake
BuildRequires:  ninja-build
BuildRequires:	gcc-c++
BuildRequires:	SDL2-devel
BuildRequires:	openal-soft-devel
BuildRequires:	glew-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
BuildRequires:	libmad-devel
BuildRequires:	libuuid-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  catch-devel
BuildRequires:  libasan
BuildRequires:  libubsan

%description
Explore other star systems. Earn money by trading, carrying passengers, or
completing missions. Use your earnings to buy a better ship or to upgrade the
weapons and engines on your current one. Blow up pirates. Take sides in a civil
war. Or leave human space behind and hope to find some friendly aliens whose
culture is more civilized than your own...


%package data
Summary:	Game data for %{name}
# Sound and images appear to be a mix of Public Domain and CC-BY-SA licensing
# See copyright for details.
License:	Public Domain and CC-BY-SA
BuildArch:	noarch


%description data
Images, sound, and game data for %{name}.


%prep
%autosetup -p0


%build
%cmake -DES_USE_VCPKG=OFF
%cmake_build

%check
appstream-util validate-relax --nonet io.github.endless_sky.endless_sky.appdata.xml
desktop-file-validate io.github.endless_sky.endless_sky.desktop


%install
%cmake_install
mkdir -p %{buildroot}%{_bindir}
install redhat-linux-build/%{name}  %{buildroot}%{_bindir}/%{name}.bin
install -m755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
sed -i 's|/app|%{_prefix}|g' %{buildroot}%{_bindir}/%{name}
rm -f %{buildroot}%{_datadir}/doc/endless-sky/license.txt

%files
%doc README.md changelog copyright
%license license.txt
%{_bindir}/%{name}*
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/applications/io.github.endless_sky.endless_sky.desktop
%{_datadir}/metainfo/io.github.endless_sky.endless_sky.appdata.xml
%{_mandir}/man6/%{name}.6.gz


%files data
%license copyright
%{_datadir}/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 28 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.10.10-1
- 0.10.10

* Mon Sep 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.10.9-1
- 0.10.9

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.10.8-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.10.8-1
- 0.10.8

* Tue May 28 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.10.7-1
- 0.10.7

* Mon Feb 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.10.6-1
- 0.10.6

* Mon Jan 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.10.5-1
- 0.10.5

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.10.4-1
- 0.10.4

* Mon Oct 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.10.3-1
- 0.10.3

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 20 2023 Kalev Lember <klember@redhat.com> - 0.10.2-2
- Don't install duplicate appdata file

* Tue Jun 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.10.2-1
- 0.10.2

* Tue Feb 21 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.10.0-1
- 0.10.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.9.16.1-1
- 0.9.16.1

* Mon Oct 17 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.9.16-1
- 0.9.16

* Tue Oct 04 2022 Link Dupont <linkdupont@fedoraproject.org> - 0.9.15-1
- 0.9.15

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.9.14-4
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.9.14-1
- 0.9.14

* Mon Apr 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.9.13-1
- 0.9.13

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 0.9.12-3
- Add missing #includes for gcc-11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.9.12-1
- 0.9.12

* Tue Feb 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.9.11-1
- 0.9.11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.9.10-2
- Fix missing #include for gcc-10

* Mon Sep 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.9.10-1
- 0.9.10
- Environment patch upstreamed.

* Wed Aug 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.9.8-12
- Add flatpak wrapper.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 fedora-toolbox <otaylor@redhat.com> - 0.9.8-9
- Pass the entire environment to build commands; fixes CPLUS_INCLUDE_PATH for
  flatpaks.

* Fri Sep  7 2018 Owen Taylor <otaylor@redhat.com> - 0.9.8-8
- scons is in /usr/bin, even if we're compiling with a different %%{_prefix}

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.9.8-7
- Rebuilt for glew 2.1.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.9.8-5
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.8-3
- Remove obsolete scriptlets

* Wed Sep 13 2017 Link Dupont <linkdupont@fedoraproject.org> - 0.9.8-2
- Remove GNU C++ extensions patch
- Only use GNU C++ extensions when building on ppc64le

* Mon Aug 21 2017 Link Dupont <linkdupont@fedoraproject.org> - 0.9.8-1
- New upstream release (RH#1473666)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Feb 26 2017 Link Dupont <linkdupont@fedoraproject.org> - 0.9.6-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-5
- Rebuild for glew 2.0.0

* Sun Jan 1 2017 Link Dupont <linkdupont@fedoraproject.org> - 0.9.4-4
- Remove CCFLAGS override inside SConstruct

* Sat Dec 31 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.9.4-3
- Build and install with identical CXXFLAGS (RH#1402807)

* Thu Dec 8 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.9.4-2
- Build with $RPM_OPT_FLAGS (#1402807)

* Sat Oct 15 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.9.4-1
- New upstream release
- Remove local appdata.xml file deferring to upstream

* Sat Aug 20 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.9.2-1
- New upstream release
- Remove installation of 'extra' directory

* Sat Jan 16 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-5
- Add strict version requirement to data package
- Document dual licensing characteristics of game data
- Add appdata validation
- Update icon cache on installation

* Mon Jan 11 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-4
- Combine patches into single file

* Sun Jan 10 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-3
- Patch game to load resources from /usr/share/endless-sky

* Sun Jan 10 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-2
- Split data into separate package
- Patch game to avoid deprecated path /usr/games

* Sat Jan 9 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.10-1
- New upstream release
- Added appdata.xml

* Sun Jan 3 2016 Link Dupont <linkdupont@fedoraproject.org> - 0.8.9-1
- Initial package
