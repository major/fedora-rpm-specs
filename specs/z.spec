%global projname z

%global desc \
Tracks your most used directories, based on 'frecency'.\
\
After a short learning phase, z will take you to the most 'frecent'\
directory that matches ALL of the regexps given on the command line, in\
order.

Name:		%{projname}
Version:	1.12
Release:	4%{?dist}
Summary:	Maintains a jump-list of the directories you actually use
License:	WTFPL
Source0:	https://github.com/rupa/%{projname}/archive/v%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gzip

%description %{desc}


%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libexecdir}
install -pm 644 z.sh %{buildroot}%{_libexecdir}/z.sh
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 z.1 %{buildroot}%{_mandir}/man1/z.1

%check

%files
%{_libexecdir}/z.sh
%{_mandir}/man1/z.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Ben Cotton <bcotton@fedoraproject.org> - 1.12-1
- Upstream release 1.12

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Ben Cotton <bcotton@fedoraproject.org> - 1.11-0
- Update to latest upstream release

* Fri Oct 18 2019 Ben Cotton <bcotton@fedoraproject.org> - 1.9-0
- Initial packaging
