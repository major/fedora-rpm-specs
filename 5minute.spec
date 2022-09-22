Name:           5minute
Version:        0.2.32
Release:        13%{?dist}
Summary:        Give me an instance of mine image on OpenStack. Hurry!
License:        GPLv2
URL:            https://github.com/SatelliteQE/%{name}/
Source0:        https://github.com/SatelliteQE/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3
BuildRequires:  python3-cinderclient
BuildRequires:  python3-heatclient
BuildRequires:  python3-neutronclient
BuildRequires:  python3-xmltodict
BuildRequires:  python3-prettytable
BuildRequires:  python3-novaclient
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-glanceclient
BuildRequires:  python3-setuptools
Requires:       python3
Requires:       python3-cinderclient
Requires:       python3-heatclient
Requires:       python3-neutronclient
Requires:       python3-xmltodict
Requires:       python3-prettytable
Requires:       python3-novaclient
Requires:       python3-keystoneclient
Requires:       python3-glanceclient

%description
This is a command-line tool to provide and maintain virtual machine on
OpenStack instance or set of instances based on pre-prepared image and
scenario configuration file which defines network setup. This way if you
prepare OpenStack image(s), maybe with complex setup on them, you can
easily provide hosts for development, testing or to scale your production
environment from command-line.

%prep
%autosetup -n %{name}-%{name}-%{version}


%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/*

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.32-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.32-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.32-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.32-10
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.32-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.32-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.32-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.32-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Jan Hutar <jhutar@redhat.com> - 0.2.32-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Jan Hutar <jhutar@redhat.com> - 0.2.31-1
- Ondrej rebased to new upstream version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.26-2
- Rebuilt for Python 3.7

* Fri Jan 26 2018 Pavlina Moravcova Varekova <pmoravco@redhat.com> - 0.2.26-1
- Initial package
