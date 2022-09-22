%global srcname re_assert
%global pkgname re-assert

Name:    python-%{pkgname}
Version: 1.1.0
Release: 6%{?dist}
Summary: Show where your regex match assertion failed!
License: MIT

URL:     https://github.com/asottile/re-assert
Source0: %{pypi_source}

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest

%global _description %{expand:
Show where your regex match assertion failed!
}

%description %{_description}

%package -n python3-%{pkgname}
Summary: %summary

%py_provides python3-%{pkgname}
%description -n python3-%{pkgname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install


%files -n python3-%{pkgname}
%license LICENSE
%{python3_sitelib}/re_assert.py
%{python3_sitelib}/__pycache__/re_assert.*.pyc
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.10

* Sun Mar 21 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.1.0-1
- Initial commit
