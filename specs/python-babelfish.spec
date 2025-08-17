%global srcname babelfish

Name: python-%{srcname}
Version: 0.6.1
Release: 7%{?dist}
Summary: Python library to work with countries and languages
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://babelfish.readthedocs.org/
Source: https://github.com/Diaoul/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

%global _description %{expand:
Babelfish makes it easy to work with countries, languages, scripts, ISO codes
and IETF codes from Python. It has converters between all different data
can be extended to use custom converters and data.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -L %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.6.1-7
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
