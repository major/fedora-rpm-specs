%global pypi_name secure_cookie
%global src_name secure-cookie

Name:		python-%{pypi_name}
Version:	0.2.0
Release:	6%{?dist}
Summary:	Provides interfaces for secure cookies and sessions in WSGI applications
License:	BSD
URL:		https://pypi.org/project/%{src_name}
Source0:	%{pypi_source %{src_name}}

BuildArch:	noarch

%global common_desc\
Provides interfaces for secure cookies and sessions in WSGI applications.\
Secure cookies are cryptographically signed (but not encrypted) to prevent\
tampering. Sessions are data associated with a given user across requests\
and responses.

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:		Provides interfaces for secure cookies and sessions in WSGI applications
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}

%prep
%setup -q -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst CHANGES.rst
%license LICENSE.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Rajeesh K V <rajeeshknambiar@gmail.com> - 0.2.0-1
- New release 0.2.0 compatible with werkzeug 2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Rajeesh K V <rajeeshknambiar@gmail.com> - 0.1.0-1
- Initial packaging
