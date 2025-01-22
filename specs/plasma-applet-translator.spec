%global orig_name org.kde.plasma.translator

Name:           plasma-applet-translator
Version:        0.8
Release:        11%{?dist}
Summary:        Plasma 5 applet for translate-shell

License:        MIT
URL:            https://store.kde.org/p/1395666
Source0:        http://qml.i-glu4it.ru/%{orig_name}_%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils

Requires:       translate-shell
Requires:       plasma-workspace
Requires:       qt5-qtxmlpatterns

%description
Easy to use translation plasmoid (GUI for translate-shell package).

%prep
%autosetup -n %{orig_name}


%build


%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}
cp -r contents %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/
install -pm 644 metadata.desktop %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%files
%license LICENSE
# %doc add-docs-here
%{_datadir}/plasma/plasmoids/%{orig_name}

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Vasiliy Glazov <vascom2@gmail.com> - 0.8-1
- Update to 0.8

* Mon Aug 31 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.7-1
- Update to 0.7

* Mon Aug 10 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.5-1
- Update to 0.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.4-1
- Update to 0.4

* Fri Jul 10 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.3-1
- Update to 0.3

* Sun Jun 28 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.2-1
- Update to 0.2

* Wed Jun 24 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.1-1
- Initial packaging
