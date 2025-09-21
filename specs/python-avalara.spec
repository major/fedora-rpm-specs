%global srcname AvaTax-REST-V2-Python-SDK
%global pkgname avalara

Name:           python-avalara
Version:        25.1.0
Release:        6%{?dist}
Summary:        AvaTax Python SDK


License:        Apache-2.0
URL:            https://github.com/avadev/%{srcname}
Source0:        https://github.com/avadev/%{srcname}/archive/refs/tags/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel



%global _description %{expand:
Sales Tax API SDK for Python and AvaTax REST.}

%description %_description

%package -n python3-%{pkgname}
Summary: %{summary}

%description -n python3-%{pkgname} %_description



%prep
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pkgname}


%check
%pyproject_check_import
# Not running tests here as they require you to have an account and an internet connection.

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt


%changelog
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 25.1.0-6
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 25.1.0-5
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 25.1.0-3
- Rebuilt for Python 3.14

%autochangelog
