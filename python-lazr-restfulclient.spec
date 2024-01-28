%global pypi_name lazr.restfulclient
Name:           python-lazr-restfulclient
Version:        0.14.6
Release:        3%{?dist}
Summary:        Programmable client library for lazr.restful web services

License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.restfulclient
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
A programmable client library that takes advantage of the commonalities among
lazr.restful web services to provide added functionality on top of wadllib.}

%description %_description


%package -n     python3-lazr-restfulclient
Summary:        %{summary}
%{?python_provide:%python_provide python3-lazr-restfulclient}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# check is disabled, but we BR runtime dpes to make sure they exists:
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(httplib2) >= 0.7.7
BuildRequires:  python3dist(oauthlib)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(wadllib) >= 1.1.4

%description -n python3-lazr-restfulclient %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

#check
#lazr.restful test dependency not packaged
#{__python3} setup.py test

%files -n python3-lazr-restfulclient
%license COPYING.txt
%doc README.rst
%{python3_sitelib}/lazr
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Ondřej Pohořelský <opohorel@redhat.com> - 0.14.6-1
- Update to 0.14.6
- Resolves: rhbz#2257346

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.14.5-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Ondřej Pohořelský <opohorel@redhat.com> - 0.14.5-1
- Update to 0.14.5
- Resolves: rhbz#2135052

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.14.4-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Ondřej Pohořelský <opohorel@redhat.com> - 0.14.4-1
- Update to 0.14.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.14.3-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-2
- Rebuilt for Python 3.9

* Wed Feb 5 2020 Ondřej Pohořelský <opohorel@redhat.com> - 0.14.3-1
- Update to 0.14.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-1
- Initial package
