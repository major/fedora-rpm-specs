%global commit 60105d1b0755e48b37d779d8a2b9c4b458b5a2fd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# We don't build any binaries.
%undefine _debugsource_packages

Name:           libetnaviv
Version:        1.0.0
Release:        14.20141102git%{shortcommit}%{?dist}
Summary:        Vivante GPU user-space driver

License:        MIT
URL:            https://github.com/etnaviv/libetnaviv.git
Source0:        https://github.com/etnaviv/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/etnaviv/libetnaviv/pull/2
Patch0:         https://github.com/lkundrak/libetnaviv/commit/e61d9e169.patch#/0001-etna.h-include-other-headers-from-the-same-directory.patch

%description
Project Etnaviv is an open source user-space driver for the Vivante GCxxx
series of embedded GPUs.


%package -n etnaviv-headers
Summary:        Header files for etnaviv.
BuildArch:      noarch


%description -n etnaviv-headers
Header files for etnaviv.


%prep
%setup -q -n %{name}-%{commit}
%patch -P0 -p1


%build
# We don't actually build libetnaviv. It would only work with the out-of-tree
# galcore kernel module and needs its headers to build anyway.
# We just need the headers.


%install
mkdir -p %{buildroot}%{_includedir}/etnaviv/
install -pm644 src/*.h %{buildroot}%{_includedir}/etnaviv/


%files -n etnaviv-headers
%{_includedir}/etnaviv
%doc README.md


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.20141102git60105d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-1.20141101gitb8fb7b53
- Initial packaging
