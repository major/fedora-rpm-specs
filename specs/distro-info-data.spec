Name:    distro-info-data
Version: 0.42
Release: 13%{?dist}

Summary: Information about releases of Debian and Ubuntu (data files)
License: ISC
URL:     https://tracker.debian.org/pkg/distro-info-data
Source0: http://deb.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz

BuildArch: noarch

BuildRequires: /usr/bin/python3
BuildRequires: python3
BuildRequires: make

%description
Information about all releases of Debian and Ubuntu. The distro-info script
will give you the codename for e.g. the latest stable release of your
distribution. To get information about a specific distribution there are the
debian-distro-info and the ubuntu-distro-info scripts.

This package contains the data files.

%prep
%autosetup -n %{name}

%build

%install
%make_install

%check
make test

%files
%license debian/copyright
%{_datadir}/distro-info

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Michael Kuhn <suraia@fedoraproject.org> - 0.42-1
- Update to 0.42

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Michael Kuhn <suraia@fedoraproject.org> - 0.38-1
- Update to 0.38
- Explicitly depend on /usr/bin/python

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Michael Kuhn <suraia@fedoraproject.org> - 0.37-1
- Update to 0.37

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Michael Kuhn <suraia@fedoraproject.org> - 0.32-1
- Update to 0.32.

* Thu May 12 2016 Michael Kuhn <suraia@fedoraproject.org> - 0.29-1
- Update to 0.29.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Michael Kuhn <suraia@fedoraproject.org> - 0.28-3
- Explicitly require python2.

* Tue Dec 29 2015 Michael Kuhn <suraia@fedoraproject.org> - 0.28-2
- Add license text.
- Own distro-info directory.

* Fri Nov 06 2015 Michael Kuhn <suraia@fedoraproject.org> - 0.28-1
- Initial package.
