Name:           wayfire-config-manager
Version:        0.7.0
Release:        5%{?dist}
Summary:        Wayfire Config Manager

License:        MIT
URL:            https://github.com/WayfireWM/wcm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  meson

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wf-config) >= 0.7.0
BuildRequires:  pkgconfig(wf-shell) >= 0.7.0

Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -n wcm-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%{_bindir}/wcm
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/wayfire/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 10 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-3
- fix: FTBFS 35

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jan 29 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-1
- build(update): 0.7.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.0-1
- build(update): 0.6.0

* Tue Aug 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-2
- Enable LTO

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20190920git2f3e075
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-3.20190920git2f3e075
- Tiny fixes

* Thu Sep 26 2019 gasinvein <gasinvein@gmail.com>
- Initial package
