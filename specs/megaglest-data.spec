Name:		megaglest-data
Version:	3.13.0
Release:	16%{?dist}
Summary:	Mega Glest data files
# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:	LicenseRef-Callaway-CC-BY-SA
Url:		http://megaglest.org/
Source0:        https://github.com/MegaGlest/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
Obsoletes:	glest-data <= 3.2.2

%description
MegaGlest is an entertaining free (freeware and free software) and
open source cross-platform 3D real-time strategy (RTS) game, where
you control the armies of one of seven different factions: Tech,
Magic, Egypt, Indians, Norsemen, Persian or Romans. The game is
setup in one of 17 naturally looking settings, which -like the
unit models- are crafted with great appreciation for detail.
A lot of additional game data can be downloaded from within the
game at no cost.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p %{_vpath_builddir}
%cmake \
  -DMEGAGLEST_ICON_INSTALL_PATH=%{_datadir}/icons
%cmake_build

%install
%cmake_install
rm -fr %{buildroot}/%{_datadir}/megaglest/docs
for image in `ls %{buildroot}/%{_datadir}/megaglest/icons`
do
  [ -e %{buildroot}%{_datadir}/$image ] \
  || ln -sf %{_datadir}/icons/$image %{buildroot}/%{_datadir}/megaglest
done
for file in megaglest megaglest_editor megaglest_g3dviewer
do
  desktop-file-validate %{buildroot}/%{_datadir}/applications/$file.desktop
done

# remove Debian style menu file
rm %{buildroot}/%{_datadir}/menu/megaglest


%files
%doc docs/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/megaglest*.desktop
%{_datadir}/icons/megaglest.*
%dir %{_datadir}/megaglest
%{_datadir}/megaglest/data/
%{_datadir}/megaglest/maps/
%{_datadir}/megaglest/scenarios/
%{_datadir}/megaglest/techs/
%{_datadir}/megaglest/tilesets/
%{_datadir}/megaglest/tutorials/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.13.0-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Andy Mender <andymenderunix@fedoraproject.org> - 3.13.0-5
- Fix archive name in %%prep stage and Source0 field
- Fix out-of-source cmake build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.13.0-1
- Update to latest upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 24 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.12.0-1
- Update to latest upstream release
- Install desktop and icons as they are no longer in the main package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.11.1-1
- Update to latest upstream release.
- Update description from upstream webpage.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.9.1-1
- Update to latest upstream release.

* Tue Nov 19 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.9.0-1
- Update to latest upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-2
- Rebuild for proper glest-data upgrade (#891875).

* Fri Nov 23 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-1
- Update to latest upstream release.

* Fri Jul 13 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-3
- Make again package owner of base data directory.
- Install documentation as %%doc (#817315).

* Fri Jul 6 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-2
- Mark documentation files as %%doc (#828544).
- Use sourceforce link format as specified in the fedora wiki (#828544).

* Fri Jun  1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-1
- Initial megaglest-data spec.
