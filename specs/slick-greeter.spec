%global build_type_safety_c 0

Summary:	A slick-looking LightDM greeter
Name:		slick-greeter
Version:	2.0.9
Release:	2%{?dist}
License:	GPL-3.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	10_%{name}-cinnamon.gschema.override.in
Source2:	10_%{name}-mate.gschema.override
Source3:	%{name}.conf

ExcludeArch:    %{ix86}

BuildRequires:	make
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	pkgconfig(liblightdm-gobject-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:  pkgconfig(xapp)
BuildRequires:	vala

Provides:	lightdm-greeter = 1.2
Provides:	lightdm-%{name} = %{version}

Requires:	lightdm%{?_isa}

# Themeing require
Requires:	google-noto-sans-fonts
Requires:	system-logos
Requires:	desktop-backgrounds-compat

Recommends:	lightdm-settings
Recommends:	onboard

# Make sure cinnamon override is installed
Requires:	(%{name}-cinnamon = %{version}-%{release} if cinnamon)

%description
A cross-distro LightDM greeter based on unity-greeter.

%package -n %{name}-cinnamon
Summary: Slick-greeter customisation for the CINNAMON desktop
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
# Themeing require
Requires:	desktop-backgrounds-basic
Requires:	mint-y-icons
Requires:	mint-y-theme
Recommends: paper-icon-theme

%description -n %{name}-cinnamon
Slick-greeter customisation for the CINNAMON desktop.

%package -n %{name}-mate
Summary: Slick-greeter customisation for the MATE desktop
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description -n %{name}-mate
Slick-greeter customisation for the MATE desktop.


%prep
%autosetup -p1

%{__install} -pm 0644 %{SOURCE2} %{name}.conf.example
%{__mkdir} -p m4

NOCONFIGURE=1 ./autogen.sh


%build
%configure	\
	--disable-silent-rules
%make_build


%install
%make_install

%{__mkdir} -p %{buildroot}%{_datadir}/lightdm/lightdm.conf.d	\
	%{buildroot}%{_datadir}/glib-2.0/schemas	\
	%{buildroot}%{_sysconfdir}/lightdm

%{__install} --target-directory=%{buildroot}%{_datadir}/lightdm/lightdm.conf.d	\
	-Dpm 0644 debian/90-%{name}.conf

%{__sed} -e 's!@color@!#202020!g'	\
	-e 's!@wallpaper@!%{_datadir}/backgrounds/tiles/default_blue.jpg!'	\
	< %{SOURCE1}								\
	> %{buildroot}%{_datadir}/glib-2.0/schemas/10_%{name}-cinnamon.gschema.override

%{__install} --target-directory=%{buildroot}%{_datadir}/glib-2.0/schemas	\
	-Dpm 0644 %{SOURCE2}

%{__install} --target-directory=%{buildroot}%{_sysconfdir}/lightdm	\
	-Dpm 0644 %{SOURCE3}

%{__chmod} -c a+x %{buildroot}%{_bindir}/*

%find_lang %{name}


%check
%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/xgreeters/*.desktop


%pre
%{_sbindir}/update-alternatives --remove lightdm-greeter	\
	%{_datadir}/xgreeters/%{name}.desktop 2> /dev/null ||:


%files -f %{name}.lang
%doc debian/changelog README.md %{name}.conf.example
%license debian/copyright COPYING
%{_bindir}/%{name}-check-hidpi
%{_bindir}/%{name}-set-keyboard-layout
%{_bindir}/%{name}-enable-tap-to-click
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/lightdm/%{name}.conf
%{_datadir}/%{name}/
%{_datadir}/xgreeters/
%{_datadir}/glib-2.0/schemas/x.dm.%{name}.gschema.xml
%{_datadir}/lightdm/lightdm.conf.d/90-%{name}.conf
%{_mandir}/man?/%{name}*

%files -n %{name}-cinnamon
%{_datadir}/glib-2.0/schemas/10_%{name}-cinnamon.gschema.override

%files -n %{name}-mate
%{_datadir}/glib-2.0/schemas/10_%{name}-mate.gschema.override


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Leigh Scott <leigh123linux@gmail.com> - 2.0.9-1
- Update to 2.0.9

* Fri Dec 06 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.8-1
- Update to 2.0.8

* Mon Nov 25 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.7-1
- Update to 2.0.7

* Tue Aug 20 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Wed Jun 05 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.4-1
- Update to 2.0.4

* Mon Feb 19 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.3-4
- Use paper cursor theme as adwaita is broken

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.3-2
- Disable modern c build flags due to vala issue

* Thu Jan 04 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.3-1
- Update to 2.0.3 release

* Thu Dec 21 2023 Leigh Scott <leigh123linux@gmail.com> - 2.0.2-1
- Update to 2.0.2 release

* Tue Dec 05 2023 Leigh Scott <leigh123linux@gmail.com> - 2.0.1-1
- Update to 2.0.1 release

* Thu Nov 30 2023 Leigh Scott <leigh123linux@gmail.com> - 2.0.0-1
- Update to 2.0.0 release

* Fri Nov 10 2023 Leigh Scott <leigh123linux@gmail.com> - 1.8.2-3
- Add icon for cinnamon wayland

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.8.2-1
- Update to 1.8.2 release

* Thu Jun 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.8.1-1
- Update to 1.8.1 release

* Fri Jun 02 2023 Leigh Scott <leigh123linux@gmail.com> - 1.8.0-1
- Update to 1.8.0 release

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.6.1-1
- Update to 1.6.1 release

* Mon Dec 05 2022 Leigh Scott <leigh123linux@gmail.com> - 1.6.0-1
- Update to 1.6.0 release

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Leigh Scott <leigh123linux@gmail.com> - 1.5.9-1
- Update to 1.5.9 release

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 01 2022 Leigh Scott <leigh123linux@gmail.com> - 1.5.6-1
- Update to 1.5.6 release

* Mon Dec 06 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.5-1
- Update to 1.5.5 release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.4-1
- Update to 1.5.4 release

* Thu Jun 10 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.3-1
- Update to 1.5.3 release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.2-1
- Update to 1.5.2 release

* Thu Dec 10 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.1-1
- Update to 1.5.1 release

* Mon Nov 30 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.0-1
- Update to 1.5.0 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.1-1
- Update to 1.4.1 release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.0-1
- Update to 1.4.0 release

* Mon Apr 20 2020 Leigh Scott <leigh123linux@gmail.com> - 1.3.2-4
- Use desktop-backgrounds-basic for background instead of fedora default

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-2
- Remove at-spi load/kill code

* Thu Jan 09 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-1
- Update to 1.3.2 release

* Wed Dec 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.1-1
- Update to 1.3.1 release

* Sat Dec 07 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.0-1
- Update to 1.3.0 release

* Tue Nov 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.9-1
- Update to 1.2.9 release

* Fri Nov 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.8-1
- Update to 1.2.8 release

* Tue Jul 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.7-1
- Update to 1.2.7 release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.6-1
- Update to 1.2.6 release

* Mon Jul 01 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.5-1
- Update to 1.2.5 release

* Sun Feb 17 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-5
- Remove mlockall call

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-3
- Fix f30 compile issue (thanks to mtwebster)

* Mon Dec 31 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-2
- rebuilt

* Sun Dec 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-1
- New upstream release

* Tue Nov 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.3-1
- New upstream release

* Thu Nov 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-4
- Switch theme and add version to mint-y-theme requires

* Thu Nov 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-3
- Add Recommends onboard for fedora (rhbz#1644816)

* Wed Aug 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-2
- Fix vala compile issue

* Wed Aug 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- New upstream release

* Thu May 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-1
- New upstream release

* Sat Apr 14 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.5-0.4.20180309gitfc13bd0
- adjust dependencies and override for MATE

* Fri Apr 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.5-0.3.20180309gitfc13bd0
- Ensure override transition for cinnamon is correct

* Fri Apr 13 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.5-0.2.20180309gitfc13bd0
- add subpackages for cinnamon and MATE

* Sat Mar 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.5-0.1.20180309gitfc13bd0
- Update to git snapshot

* Thu Feb 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-3
- Use upstream fix for session cleanup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.4-1
- New upstream release (rhbz#1529690)

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-5
- Use upstreamed fix for vala >= 0.39

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-4
- Temporary fix for vala >= 0.39

* Thu Dec 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-3
- Re-add missed dependency on mint-y-icons

* Thu Dec 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-2
- Replace Arc-Dark theme with Mint-Y-Dark theme

* Wed Nov 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-1
- New upstream release
- Match initial background color with default plymouth theme
- Revert: Show Fedora / Shadow Man logo on non-primary monitors

* Wed Nov 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-3
- Show Fedora / Shadow Man logo on non-primary monitors

* Tue Nov 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-2
- Revert: Match initial background color with default plymouth theme
- Simplify handling of gschema overrides

* Tue Nov 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-1
- New upstream release
- Add patch to screen size in some cases
- Match initial background color with default plymouth theme
- General cleanup

* Fri Nov 17 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-1
- New upstream release (rhbz#1514464)

* Fri Nov 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-4
- Add patch from upstream to use gsettings default if there is no
  different preset in the config file

* Fri Nov 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-3
- Show system-logo in lower left corner by default

* Mon Nov 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-2
- Realigned patches

* Mon Nov 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-1
- New upstream release (rhbz#1509759)

* Fri Oct 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.9-1
- Update to 1.0.9 release

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-13
- Use Patch1 on newer distros only

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-12
- Preserve mode of files when changing hashbang

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-11
- Fix regex for EPEL

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-10
- Use Python2 on EPEL <= 7

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-9
- Make sure `m4`-dir exists

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-8
- Properly compile gschemas on epel <= 7

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-7
- Use different gschema overrides for Fedora and EPEL

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-6
- Require google-noto-sans-fonts on epel7 too

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.8-3
- remove tooltip override

* Thu Jul 06 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.8-2
- Add patch to remove at-spi kill code, fixes log warnings

* Tue Jun 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.8-1
- Update to 1.0.8 release

* Wed Jun 14 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.7-2
- Add patch to kill onboard and orca on session start

* Tue Jun 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.7-1
- Update to 1.0.7 release

* Tue May 30 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.6-1
- Update to 1.0.6 release

* Fri May 26 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.5-2
- Add upstream patch to improve gtk3 compatibility

* Thu May 25 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.5-1
- Update to 1.0.5 release

* Wed May 24 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-2
- Add upstream patch to fix background

* Tue May 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-1
- Update to 1.0.4 release

* Sat May 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 release (rhbz#1450544)

* Fri May 05 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.1-1
- Update to 1.0.1 release

* Sat Apr 15 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-15
- Remove unused file
- Fix override schema
- Add virtual provides

* Wed Apr 12 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-14
- Revert previous change, lightdm-settings is noarch

* Tue Apr 11 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-13
- Enforce arch on Recommends: lightdm-settings

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-12
- Add some patches for enhancements from upstream

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-11
- Set `org.gnome.desktop.interface toolkit-accessibility true`
  in gschema.override

* Sat Apr 08 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-10
- Add hidpi on or off support

* Sat Apr 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-9
- Set system-defaults in gschema-override

* Sat Apr 08 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-8
- Fix permissions for slick-greeter-check-hidpi

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-7
- Fix font used in default config

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-6
- Add several fixes from upstream
- Add new binary slick-greeter-check-hidpi
- Add changelog and copyright from debian-directory

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-5
- Fix conditional

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-4
- Add Recommends: lightdm-settings

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-3
- Use Noto Sans Regular font on Fedora

* Fri Apr 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-2
- Do review changes

* Fri Apr 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-1
- First build
