%global gitowner gosquared
%global gitproject flags
%global commit 1d382a9ea87667ac59c493b8fd771f49ce837e6a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		iso-country-flags
Version:	0
Release:	0.9.20170202git%{shortcommit}%{?dist}
License:	MIT
Summary:	Country flags
URL:		https://github.com/%{gitowner}/%{gitproject}
Source0:	https://github.com/%{gitowner}/%{gitproject}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:	noarch

%description
ISO 3166-1 alpha-2 defines two-letter country codes which are used most
prominently for the Internet's country code top-level domains.
This package contains 244 country flag PNG icons.


%prep
%autosetup -n %{gitproject}-%{commit}
BASE="flags/flags-iso/flat"
# 1. rm extra dirs
rm -rf ${BASE}/{icns,ico}
# 2. rm extra flags
rm -rf ${BASE}/*/_*.png
# 3. filenames to lowercase
for i in `ls ${BASE}/*/*.png`; do mv $i `echo $i | tr [:upper:] [:lower:]`; done


%build
# nothing to do


%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r flags/flags-iso/flat/* %{buildroot}%{_datadir}/%{name}/


%files
%license LICENSE.txt
%doc README.md
%{_datadir}/%{name}/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20170202git1d382a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20170202git1d382a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20170202git1d382a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20170202git1d382a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20170202git1d382a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170202git1d382a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170202git1d382a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170202git1d382a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 TI_Eugene <ti.eugene@gmail.com> 0-0.1.20170202git1d382a9
- Spec fixes

* Sat Jan 30 2021 TI_Eugene <ti.eugene@gmail.com> 0-1.20170202
- Initial packaging
