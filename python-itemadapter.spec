%global pkg_name itemadapter
%global desc %{expand:
The ItemAdapter class is a wrapper for data container objects,
providing a common interface to handle objects of different
types in an uniform manner, regardless of their underlying implementation.}
Name:		python-itemadapter
Version:	0.4.0
Release:	6%{?dist}
Summary:	The ItemAdapter class is a wrapper for data container object

License:	BSD
URL:		https://github.com/scrapy/itemadapter
Source0:	%{pypi_source %pkg_name}

BuildArch:	noarch


%description
%{desc}

%package -n python3-%{pkg_name}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Requires:	python3-attrs

%py_provides  python3-%{pkg_name}


%description -n python3-%{pkg_name}
%{desc}

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%py3_build


%install
%py3_install

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/itemadapter
%{python3_sitelib}/itemadapter-*.egg-info

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.11

* Sun Feb 20 2022 Eduardo Echeverria <echevemaster@gmail.com> - 0.4.0-1
- Bumped to the latest upstream version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.10

* Sat Apr 3 2021 Eduardo Echeverria <echevemaster@gmail.com> - 0.2.0-1
- Initial packaging

