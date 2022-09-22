%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name:       hunspell-tr
Summary:    Turkish hunspell dictionaries
Version:    1.1.0
License:    MIT
Release:    2%{?dist}

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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 14 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.1.0-1
- Initial Package fixes (rhbz#2075521 , rhbz#1830582)
