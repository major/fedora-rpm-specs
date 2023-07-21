Name:           buttermanager
Version:        2.4.2
Release:        8%{?dist}
Summary:        Tool for managing Btrfs snapshots, balancing filesystems and more

License:        GPLv3
URL:            https://github.com/egara/buttermanager
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
Requires:       btrfs-progs
Requires:       python3-tkinter
# Recommends:     grub2-btrfs

%description
ButterManager is a BTRFS tool for managing snapshots, balancing filesystems
and upgrading the system safely.

%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install

install -Dpm644 packaging/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Fix the desktop file
sed \
  -e "s/Icon=.*/Icon=%{name}/" \
  -i packaging/%{name}.desktop

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  packaging/%{name}.desktop


%files
%license LICENSE
%doc README.md doc
%{_bindir}/buttermanager
%{python3_sitelib}/buttermanager*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.4.2-7
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4.2-4
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2 (patches upstreamed)
- Add missing dependency on python3-tkinter
- Fix desktop icon location

* Tue Jun 22 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.4.1-1
- Initial package
