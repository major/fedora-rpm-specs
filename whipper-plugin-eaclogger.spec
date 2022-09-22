%global srcname whipper-plugin-eaclogger
%global sum Whipper plugin to provide EAC style log reports
%global desc Whipper plugin to provide EAC style log reports.

Name:    %{srcname}
Version: 0.5.0
Release: 10%{?dist}
Summary: %{sum}
URL:     https://github.com/whipper-team/whipper-plugin-eaclogger
License: ISC

Source0: https://github.com/whipper-team/%{srcname}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: whipper >= 0.9.0

%description
%{desc}

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%{python3_sitelib}/whipper_plugin_eaclogger-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/eaclogger/
%license LICENSE
%doc README.md

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.0-9
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 5 2019 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.0-1
- Initial RPM release