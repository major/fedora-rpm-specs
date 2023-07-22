%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name:       hunspell-tr
Summary:    Turkish hunspell dictionaries
Version:    1.1.0
License:    MIT
Release:    5%{?dist}

URL:        https://github.com/tdd-ai/hunspell-tr
Source:     https://github.com/tdd-ai/hunspell-tr/archive/v%{version}/%{name}-v%{version}.tar.gz


BuildArch:  noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-tr)

%description
Turkish hunspell dictionaries.

%prep
%autosetup -p1
rm trspell10.csv

%build
# nothing to see here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README.md
%license LICENSE
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 24 2023 Caolán McNamara <caolanm@redhat.com> - 1.1.0-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 14 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.1.0-1
- Initial Package fixes (rhbz#2075521 , rhbz#1830582)
