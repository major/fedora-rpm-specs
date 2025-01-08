Name:		lightdm-settings
Version:	2.0.7
Release:	1%{?dist}
Summary:	Configuration tool for the LightDM display manager

License:	GPL-3.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	make

Requires:	filesystem
Requires:	gtk3
Requires:	hicolor-icon-theme
Requires:	polkit
Requires:	python3-xapp
Requires:	python3-gobject
Requires:	python3-setproctitle
Requires:	slick-greeter

%description
This tool currently lets users configure slick-greeter.


%prep
%autosetup -p 1

%build
%make_build

%install
# No install-target in Makefile.
%{__cp} -pr .%{_prefix} %{buildroot}

# Set exec-permissions where needed.
%{__chmod} -c 0755 %{buildroot}%{_bindir}/%{name} \
	 %{buildroot}%{_prefix}/lib/%{name}/%{name}

# Find localizations and build manifest.
%find_lang %{name}

%check
%{_bindir}/desktop-file-validate \
	%{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license debian/copyright COPYING
%doc debian/changelog README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/polkit-1/actions/org.x.%{name}.policy


%changelog
* Mon Jan 06 2025 Leigh Scott <leigh123linux@gmail.com> - 2.0.7-1
- Update to 2.0.7

* Fri Dec 06 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Tue Aug 20 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.4-1
- Update to 2.0.4

* Wed Jun 05 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Leigh Scott <leigh123linux@gmail.com> - 2.0.2-1
- Update to 2.0.2 release

* Mon Dec 04 2023 Leigh Scott <leigh123linux@gmail.com> - 2.0.1-1
- Update to 2.0.1 release

* Thu Nov 30 2023 Leigh Scott <leigh123linux@gmail.com> - 2.0.0-1
- Update to 2.0.0 release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.8.2-1
- Update to 1.8.2 release

* Thu Jun 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.8.1-1
- Update to 1.8.1 release

* Fri Jun 02 2023 Leigh Scott <leigh123linux@gmail.com> - 1.8.0-1
- Update to 1.8.0 release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Leigh Scott <leigh123linux@gmail.com> - 1.6.1-1
- Update to 1.6.1 release

* Mon Dec 05 2022 Leigh Scott <leigh123linux@gmail.com> - 1.6.0-1
- Update to 1.6.0 release

* Sun Jul 24 2022 Jonathan Wright <jonathan@almalinux.org> - 1.5.10-2
- Update to 1.5.10 rhbz#2144745

* Sun Jul 24 2022 Leigh Scott <leigh123linux@gmail.com> - 1.5.9-1
- Update to 1.5.9 release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Leigh Scott <leigh123linux@gmail.com> - 1.5.8-1
- Update to 1.5.8 release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 01 2022 Leigh Scott <leigh123linux@gmail.com> - 1.5.7-1
- Update to 1.5.7 release

* Mon Dec 06 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.6-1
- Update to 1.5.6 release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.5-1
- Update to 1.5.5 release

* Thu Jun 10 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.4-1
- Update to 1.5.4 release

* Tue Jun 01 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.3-1
- Update to 1.5.3 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.2-1
- Update to 1.5.2 release

* Thu Dec 10 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.1-1
- Update to 1.5.1 release

* Mon Nov 30 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.0-1
- Update to 1.5.0 release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.2-1
- Update to 1.4.2 release

* Wed Jun 17 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.1-1
- Update to 1.4.1 release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.0-1
- Update to 1.4.0 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.3.3-1
- Update to 1.3.3 release

* Wed Dec 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-1
- Update to 1.3.2 release

* Tue Nov 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.1-1
- Update to 1.3.1 release

* Fri Nov 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.0-1
- Update to 1.3.0 release

* Wed Jul 31 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.8-1
- Update to 1.2.8 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.7-1
- Update to 1.2.7 release

* Sun Jun 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.6-1
- Update to 1.2.6 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.5-1
- Update to 1.2.5 release

* Tue Nov 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-1
- Update to 1.2.4 release

* Wed Aug 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.3-1
- Update to 1.2.3 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- Update to 1.2.1 release

* Thu May 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-1
- Update to 1.2.0 release

* Thu Feb 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-1
- Update to 1.1.4 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3 release (rhbz#1509947)

* Fri Oct 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.2-1
- Update to 1.1.2 release

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-6
- Preserve mode of files when changing hashbang

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-5
- Fix hashbangs for EPEL

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-4
- Another fix for EPEL

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-3
- Adjustments for EPEL

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 release (rhbz#1466545)

* Tue Jun 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 release (rhbz#1460470)

* Wed May 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9 release (rhbz#1455370)

* Thu May 18 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.7-2
- Activate support for pkexec

* Wed May 17 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7 release (rhbz#1451532)

* Mon May 15 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 release (rhbz#1450706)

* Sun May 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4 release (rhbz#1448705)
- Pick up installed locales

* Fri May 05 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.3-1
- Update to 1.0.3 release
- Add requires python3-xapp

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-4
- Add missing dependency on python3-setproctitle (rhbz#1444436)

* Sat Apr 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-3
- Add more patches from upstream

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-2
- Add patches from upstream

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-1
- Initial import (rhbz#1440240)

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.1
- Initial rpm-release (rhbz#1440240)
