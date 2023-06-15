%global pkg_name protego
%global pypi_name Protego
%global desc %{expand:
Protego is a pure-Python `robots.txt` parser with support for modern
conventions.}

Name:		python-protego
Version:	0.2.1
Release:	5%{?dist}
Summary:	Pure-Python robots.txt parser with support for modern conventions

License:	BSD
URL:		https://github.com/scrapy/protego
Source0:	%{pypi_source}

BuildArch:	noarch


%description
%{desc}

%package -n python3-%{pkg_name}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pytest
BuildRequires:	python3-six


%description -n python3-%{pkg_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build


%install
%py3_install

%check
%pytest

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%pycached %{python3_sitelib}/protego.py
%{python3_sitelib}/Protego-*.egg-info

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.11

* Sun Feb 20 2022 Eduardo Echeverria <echevemaster@gmail.com> - 0.2.1-1
- Bumped to the latest upstream version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.16-2
- Rebuilt for Python 3.10

* Sat Apr 3 2021 Eduardo Echeverria <echevemaster@gmail.com> - 0.1.16-1
- Initial packaging
