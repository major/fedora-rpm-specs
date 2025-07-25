Name:           python-untangle
Version:        1.2.1
Release:        8%{?dist}
Summary:        Converts XML to Python objects

License:        MIT
URL:            https://github.com/stchris/untangle
VCS:            https://github.com/stchris/untangle
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

# Remove unnecessary shebang
# https://github.com/stchris/untangle/pull/140
Patch0:         https://github.com/stchris/untangle/pull/140.patch#/python-untangle-1.2.1-shebang.patch

# macro pytest is not defined on rhel7
%{!?pytest: %global pytest PYTHONPATH="%{buildroot}%{python3_sitelib}:$PYTHONPATH" pytest-3}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-defusedxml
BuildRequires:  python%{python3_pkgversion}-pytest


%description
Converts XML to a Python object. * Siblings with similar names are grouped into
a list. * Children can be accessed with parent.child, attributes with
element['attribute'].

%package -n     python%{python3_pkgversion}-untangle
Summary:        %{summary}
%if 0%{?rhel}
%{?python_provide:%python_provide python%{python3_pkgversion}-untangle}
%else
%py_provides    python3-untangle
%endif

Requires:       python%{python3_pkgversion}-defusedxml

%description -n python%{python3_pkgversion}-untangle
Converts XML to a Python object. Siblings with similar names are grouped into
a list. Children can be accessed with parent.child, attributes with
element.


%prep
%autosetup -n untangle-%{version}

%build
# using old py3_build/py3_install to keep remain compatible with EPEL7/8 builds
%py3_build

%install
%py3_install


%check
%if 0%{?rhel} == 7
# avoid UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 6: ordinal not in range(128)
# in UnicodeTestCase.test_unicode_element
export LANG=en_US.UTF-8
%endif

%pytest -sv


%files -n python%{python3_pkgversion}-untangle
%license LICENSE
%doc README.md AUTHORS CHANGELOG.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/untangle.py
%{python3_sitelib}/untangle-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 1.2.1-7
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Michal Ambroz <rebus@seznam.cz> - 1.2.1-2
- #PR140 - remove unnecessary shebang

* Wed Dec 07 2022 Michal Ambroz <rebus@seznam.cz> - 1.2.1-1
- Initial package.
