%global gitcommit_full f47ec3d7e72ad4b8bc163a515b6e66bd94a6b02e
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20221013

Name:           co2mon
Version:        2.1.1
Release:        17.%{date}git%{gitcommit}%{?dist}
Summary:        CO2 monitor software

License:        GPL-3.0-or-later
URL:            https://github.com/dmage/co2mon
Source0:        %{url}/tarball/%{gitcommit_full}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)

Requires:       udev

%description
Software for USB CO2 Monitor devices.

%package        devel
Summary:        Include files for CO2 monitor software
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for USB CO2 Monitor devices.

%prep
%autosetup -n dmage-%{name}-%{gitcommit}


%build
%cmake
%cmake_build


%install
%cmake_install

mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 644 udevrules/99-%{name}.rules %{buildroot}%{_udevrulesdir}

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r graph %{buildroot}%{_datadir}/%{name}/


%files
%doc README.md
%license LICENSE
%{_bindir}/co2mond
%{_datadir}/%{name}
%{_libdir}/*.so.1*
%{_udevrulesdir}/99-%{name}.rules

%files devel
%{_libdir}/*.so
%{_includedir}/%{name}.h

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-17.20221013gitf47ec3d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-16.20221013gitf47ec3d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-15.20221013gitf47ec3d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-14.20221013gitf47ec3d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-13.20221013gitf47ec3d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-12.20221013gitf47ec3d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 2.1.1-9.20221013gitf47ec3d
- Update to latest git

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10.20201127gitfcb1277
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 12 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 2.1.1-9.20201127gitfcb12779
- Update to latest git

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4.20190313git6a53ffa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3.20190313git6a53ffa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2.20190313git6a53ffa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.1.1-1.20190313git6a53ffa
- Clean spec

* Tue Jun 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 0-0.20190313git6a53ffa.1
- Update to latest git

* Fri Jul 20 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-0.20180527git664378b
- Update to latest git

* Wed Apr 13 2016 vascom <vascom2@gmail.com> 2.1.0-2
- Add udev post script

* Wed Nov 11 2015 vascom <vascom2@gmail.com> 2.1.0-1
- Update to 2.1.0
- Added udev rule

* Sun Nov 08 2015 vascom <vascom2@gmail.com> 2.0.2-1
- First package release
