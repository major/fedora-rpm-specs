%global pypi_name clikit

%global common_description %{expand:
CliKit is a group of utilities to build beautiful and testable command
line interfaces. This is at the core of Cleo.}

Name:           python-%{pypi_name}
Summary:        Utilities to build beautiful and testable CLIs
Version:        0.6.2
Release:        7%{?dist}
License:        MIT

URL:            https://github.com/sdispater/clikit
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.2-1
- Update to version 0.6.2.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.4.2-1
- Update to version 0.4.2.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Fabio Valentini <decathorpe@gmail.com> - 0.4.1-1
- Update to version 0.4.1.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 0.4.0-1
- Update to version 0.4.0.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-2
- Rebuilt for Python 3.8

* Sun May 12 2019 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-1
- Update to version 0.2.4.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-1
- Initial package.

