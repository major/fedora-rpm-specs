%global srcname pingfs
%global commit f2f2b5ff1893d0531d0a0d1ea2ae96b52dcf780e
%global snapinfo 20200820git%{shortcommit}
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    fuse-pingfs
Version: 0
Release: 0.12.%{snapinfo}%{?dist}
Summary:  Stores your data in ICMP ping packets

License: ISC
URL:     https://github.com/yarrick/pingfs
Source0: https://github.com/yarrick/pingfs/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires: gcc
BuildRequires: pkgconfig(fuse)
BuildRequires: make

%description
pingfs is a filesystem where the data is stored only in the Internet itself, as
ICMP Echo packets (pings) travelling from you to remote servers and back again.

%prep
%autosetup -n pingfs-%{commit}

%build
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a pingfs %{buildroot}%{_bindir}/pingfs

%files
%{_bindir}/pingfs

%doc README
%license LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20200820gitf2f2b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 3 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0-0.2.20200820gitf2f2b5f
- Spec changes based on review

* Thu Aug 20 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0-0.1.20200820gitf2f2b5f
- Initial version of the package
