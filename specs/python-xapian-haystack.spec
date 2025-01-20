# Created by pyp2rpm-3.3.10

Name:           python-xapian-haystack
Version:        3.1.0
Release:        5%{?dist}
Summary:        A Xapian backend for Haystack

License:        GPL-2.0-only
URL:            https://github.com/notanumber/xapian-haystack
Source0:        %{url}/archive/%{version}/xapian-haystack-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Xapian backend for Django-Haystack}

%description %_description

%package -n     python3-xapian-haystack
Summary:        %{summary}

Requires:       python3-xapian >= 1.4
%description -n python3-xapian-haystack %_description

%prep
%autosetup -n xapian-haystack-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-xapian-haystack
%license LICENSE
%doc README.rst
%pycached %{python3_sitelib}/xapian_backend.py
%{python3_sitelib}/xapian_haystack-%{version}.dist-info/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 8 2024 Michal Konecny <mkonecny@redhat.com> - 3.1.0-4
- Update spec file based on python packaging guidelines for Fedora

* Thu Oct 3 2024 Michal Konecny <mkonecny@redhat.com> - 3.1.0-3
- Change requires for xapian-bindings

* Thu Sep 19 2024 Michal Konecny <mkonecny@redhat.com> - 3.1.0-2
- Add missing dependencies

* Wed Sep 18 2024 mockbuilder - 3.1.0-1
- Initial package.
