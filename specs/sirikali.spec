%global srcname SiriKali
%global srcurl  https://github.com/mhogomchungu/%{name}

Name:           sirikali
Version:        1.8.0
Release:        2%{?dist}
Summary:        GUI front end to encfs,cryfs,gocryptfs and securefs
# generally GPLv2+, BSD for tasks and NetworkAccessManager folders
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            http://mhogomchungu.github.io/%{name}

Source0:        %{srcurl}/releases/download/%{version}/%{srcname}-%{version}.tar.xz

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: json-devel
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(lxqt-wallet)

BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Network)

BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
Requires:      hicolor-icon-theme

Recommends:    fuse-encfs

%description
%{srcname} is a Qt/C++ GUI front end to encfs,cryfs,gocryptfs and securefs.


%prep
%autosetup -p0 -n%{srcname}-%{version}
# collect licenses
cp -p src/3rdParty/tasks/LICENSE LICENSE-tasks
# unbundle
pushd src/3rdParty
rm -rv lxqt_wallet
popd
sed -i -r 's:".*(json.hpp)":"\1":' CMakeLists.txt
sed -i 's:3rdParty/json:json:' src/%{name}.cpp

%build
%cmake -DQT5=true -DNOKDESUPPORT=true -DNOSECRETSUPPORT=false \
 -DINTERNAL_LXQT_WALLET=false -DBUILD_WITH_QT6=true \
 -DJSON_HEADER_PATH=/usr/include/nlohmann/json.hpp ..
pushd %{_vpath_builddir}
%make_build

%install
pushd %{_vpath_builddir}
%make_install
%find_lang %{name} --with-qt --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.mhogomchungu.sirikali.desktop


%files -f %{_vpath_builddir}/%{name}.lang
%license COPY* LICENSE* GPLv*
%doc README.md ABOUT* changelog
%{_bindir}/%{name}*
%{_datadir}/applications/io.github.mhogomchungu.sirikali.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/%{name}*.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.8.0-1
- 1.8.0

* Mon Dec 02 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.7.2-2
- lxqt-wallet rebuild

* Tue Nov 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.7.2-1
- 1.7.2

* Thu Nov 14 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.7.1-1
- 1.7.1

* Mon Nov 11 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.7.0-1
- 1.7.0

* Mon Oct 28 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-1
- 1.6.0, qt6

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5.1-1
- 1.5.1

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5.0-4
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.5.0-1
- 1.5.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.4.8-6
- liblxqt-wallet rebuild.

* Thu Feb 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.4.8-5
- 1.4.8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-1
- 1.4.4

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4.3-1
- 1.4.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.2-1
- 1.4.2

* Mon Nov 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- 1.4.1

* Sun Sep 08 2019 Raphael Groner <projects.rg@smart.ms> - 1.3.9-1
- new version

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 1.3.8-1
- new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.6-1
- new version

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.3.4-3
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.4-2
- Rebuild for new binutils

* Thu Jul 26 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.4-1
- bump to 1.3.4, fix FTBFS
- try harder to add all license texts

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.3-1
- new version
- drop upstream patches, due to incl.
- add license breakdown for 3rdParty folders

* Wed Feb 07 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.2-2
- drop obsolete scriptlets
- drop explicit file permission
- include upstreamed patches

* Sat Jan 13 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.2-1
- new version
- drop BSD because unbundled json
- unbundle lxqt_wallet

* Tue Jul 11 2017 Raphael Groner <projects.rg@smart.ms> - 1.2.9-1
- new version
- unbundle json

* Mon Jun 12 2017 Raphael Groner <projects.rg@smart.ms> - 1.2.7.1.20170611git
- new version
- use git snapshot to include latest upstream patches
- include upstream patch to get full path of su binary
- distribute additonal files
- drop workaround for duplicated readme files
- fix length of line in description

* Sun Jun 04 2017 Raphael Groner <projects.rg@smart.ms> - 1.2.5-2
- fix duplication of license documentation files
- reorder explicit ownership of folders
- fix file attributes of desktop file
- add weak dependency to fuse-encfs

* Wed Mar 01 2017 Raphael Groner <projects.rg@smart.ms> - 1.2.5-1
- adopt for Fedora
