%global pypi_name pylacrosse
%global pkg_name lacrosse

Name:           python-%{pkg_name}
Version:        0.4
Release:        10%{?dist}
Summary:        LaCrosse Python sensor library

License:        LGPLv2+
URL:            http://github.com/hthiery/python-lacrosse
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python libray to work with the Jeelink USB RF adapter.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python libray to work with the Jeelink USB RF adapter.

%prep
%autosetup -n %{name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pkg_name}
%doc AUTHORS README.rst
%license COPYING
%{_bindir}/pylacrosse
%{python3_sitelib}/%{pypi_name}/
# Unversioned egg-info: https://github.com/hthiery/python-lacrosse/issues/11
%{python3_sitelib}/%{pypi_name}*py%{python3_version}.egg-info/
%exclude %{python3_sitelib}/tests

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-2
- Add missing BR (#1879768)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-1
- Initial package for Fedora