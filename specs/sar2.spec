Name:		sar2
Version:	2.5.0
Release:	12%{?dist}
Summary:	An open source helicopter simulator
# Code is GPLv2+
# Content is either GPLv2+ or Public Domain
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/SearchAndRescue2/sar2
Source0:	https://github.com/SearchAndRescue2/sar2/archive/v%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:	scons, desktop-file-utils
BuildRequires:	libX11-devel, libSM-devel, libXi-devel, libXmu-devel
BuildRequires:	SDL2-devel, SDL2_image-devel, openal-soft-devel, freealut-devel
BuildRequires:	mesa-libGLU-devel, mesa-libGL-devel, libICE-devel
BuildRequires:	libXpm-devel, libvorbis-devel, libXext-devel
BuildRequires:	libXxf86vm-devel

%description
Search and Rescue II is a rescue helicopter simulator for Linux. It features 
several missions in which the player pilots a helicopter in order to rescue 
people in distress. There are several scenarios and helicopter models.

Search and Rescue II has a strong focus on realistic physics and low graphics 
requirements. It is a fork of the game "Search and Rescue" 
(http://searchandrescue.sf.net), originally developed by Wolfpack 
Entertainment.

%prep
%setup -q

%build
scons --optflags="%{optflags}"

%install
# install.sh is pretty dumb.
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man6
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/
mkdir -p %{buildroot}%{_datadir}/pixmaps/

cp -ar data/* %{buildroot}%{_datadir}/%{name}/
cp -a man/* %{buildroot}%{_mandir}/man6
cp -a bin/%{name} %{buildroot}%{_bindir}
cp -a extra/%{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/
cp -a src/icons/SearchAndRescue.xpm %{buildroot}%{_datadir}/pixmaps/
pushd %{buildroot}%{_datadir}/pixmaps/
ln -s ../icons/hicolor/48x48/sar2.xpm sar2.xpm
popd
desktop-file-install --dir=%{buildroot}%{_datadir}/applications extra/%{name}.desktop

%files
%doc AUTHORS CHANGELOG.md HACKING LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/

%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/%{name}.xpm
%{_datadir}/pixmaps/*.xpm
%{_mandir}/man6/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.0-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Tom Callaway <spot@fedoraproject.org> - 2.5.0-1
- update to 2.5.0

* Wed May 27 2020 Tom Callaway <spot@fedoraproject.org> - 2.4.3-1
- update to 2.4.3

* Fri May  8 2020 Tom Callaway <spot@fedoraproject.org> - 2.4.2-1
- update to 2.4.2

* Mon May  4 2020 Tom Callaway <spot@fedoraproject.org> - 2.4.1-1
- update to 2.4.1

* Mon Apr 27 2020 Tom Callaway <spot@fedoraproject.org> - 2.4.0-1
- update to 2.4.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.3-4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Tom Callaway <spot@fedoraproject.org> - 2.3.3-1
- update to 2.3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Tom Callaway <spot@fedoraproject.org> - 2.3.2-1
- update to 2.3.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug  8 2011 Tom Callaway <spot@fedoraproject.org> - 2.3.0-2
- update icon cache

* Tue Jun 14 2011 Tom Callaway <spot@fedoraproject.org> - 2.3.0-1
- initial package
