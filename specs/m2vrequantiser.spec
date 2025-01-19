%global srcname M2VRequantiser

Name:           m2vrequantiser
Epoch:          1
Version:        1.1
Release:        11%{?dist}
Summary:        MPEG-2 stream requantizer

License:        GPL-2.0-or-later
URL:            https://launchpad.net/m2vrequantiser
Source:         %{url}/trunk/%{version}/+download/%{srcname}-v%{version}.tar.gz
Patch:          make_dest_strip.patch

BuildRequires:  gcc
BuildRequires:  make

%description
M2VRequantiser is a tool to requantize MPEG-2 streams without
recompressing.

%prep
%autosetup -n %{srcname}-v%{version}

%build
%make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%doc README.txt
%license LICENSE.txt
%{_bindir}/%{srcname}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 24 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 1:1.1-10
- Convert license tag to SPDX
- Rework specfile to follow the Fedora packaging guidelines
- Preserve timestamps when installing

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 05 2020 leigh123linux <leigh123linux@googlemail.com> - 1:1.1-1
- Update to 1.1 release

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20030929-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20030929-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20030929-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20030929-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 20030929-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 20030929-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 20030929-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 20030929-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 20030929-6
- Mass rebuilt for Fedora 19 Features

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 20030929-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 20030929-4
- rebuild for new F11 features

* Sat Sep 20 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 20030929-3
- rebuild for rpmfusion

* Wed Aug 22 2007 Ville Skyttä <ville.skytta at iki.fi> - 20030929-2
- License: GPL+

* Mon Dec 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 20030929-1
- First RLO build.

* Thu Aug 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 20030929-0.1
- First build.
