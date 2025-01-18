Name:           btrfs-heatmap
Version:        9
Release:        11%{?dist}
Summary:        Visualize the layout of data on your btrfs filesystem over time

License:        MIT
URL:            https://github.com/knorrie/btrfs-heatmap
Source0:        https://github.com/knorrie/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       python3-btrfs >= 10
Suggests:       %{name}-doc = %{version}-%{release}

%description
The btrfs heatmap script creates a visualization of how a btrfs filesystem is
utilizing the underlying disk space of the block devices that are added to it.

%package doc
Summary:        Documentation for %{name}

%description doc
The btrfs heatmap script creates a visualization of how a btrfs filesystem is
utilizing the underlying disk space of the block devices that are added to it.

This package contains the documentation.

%prep
%autosetup
# Remove execution bit from doc
find doc -type f -print0 | xargs -0 chmod 0644

%build

%install
install -D -p -m 0755 btrfs-heatmap %{buildroot}%{_bindir}/btrfs-heatmap
install -D -p -m 0644 man/btrfs-heatmap.1 %{buildroot}%{_mandir}/man1/btrfs-heatmap.1

%files
%license COPYING
%{_bindir}/btrfs-heatmap
%{_mandir}/man1/btrfs-heatmap.1*

%files doc
%doc README.md CHANGES doc
%license COPYING

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Juan Orti Alcaine <jortialc@redhat.com> - 9-1
- Version 9 (#1888432)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 8-1
- Version 8
- License changed to MIT

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 7-1
- Version 7

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 6-1
- Version 6

* Mon Feb 20 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 5-2.20170222git8c9b111
- Split doc in its own subpackage
- Preserve timestamp when installing

* Mon Feb 20 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 5-1.20170222git8c9b111
- Initial package
