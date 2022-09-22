%global module	gettext

Name:		python-%{module}
Version:	4.0
Release:	7%{?dist}
Summary:	Python Gettext po to mo file compiler
License:	BSD

URL:		https://pypi.org/project/python-gettext/
Source0:	%{pypi_source %{name}}
BuildArch:	noarch

%description
This implementation of Gettext for Python includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.

%package -n	python3-%{module}
Summary:	Python 3 Gettext po to mo file compiler
BuildRequires:	python3-devel
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
This implementation of Gettext for Python 3 includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.

%prep
%autosetup -p1

# Remove bundled egg-info
rm -rf python_gettext.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python3_sitelib}/pythongettext/
%{python3_sitelib}/python_gettext-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 04 2020 Neal Gompa <ngompa13@gmail.com> - 4.0-1
- Initial package


