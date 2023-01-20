Name:           deepin-sound-theme
Version:        15.10.6
Release:        6%{?dist}
Summary:        Deepin sound theme
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-sound-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make

%description
Sound files for the Deeping Desktop Environment.

%prep
%setup -q

%build

%install
%make_install

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/sounds/deepin/
%dir %{_datadir}/sounds/deepin/stereo/
%{_datadir}/sounds/deepin/index.theme
%{_datadir}/sounds/deepin/stereo/*.wav

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Robin Lee <cheeselee@fedoraproject.org> - 15.10.6-1
- Update to 15.10.6

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 15.10.3-1
- Update to 15.10.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 15.10.2-1
- Update to 15.10.2

* Sun Aug  6 2017 mosquito <sensor.wen@gmail.com> - 15.10.1-1
- Rebuild

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 15.10.1-1.git0045de4
- Update to 15.10.1

* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build
