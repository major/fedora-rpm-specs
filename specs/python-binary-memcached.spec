%global module python-binary-memcached
%global srcname %{module}


Name:           %{module}
Version:        0.31.2
Release:        7%{?dist}
Summary:        Python module python-binary-memcached

License:        MIT
URL:            https://github.com/jaysonsantos/%{module}
Source:         https://github.com/jaysonsantos/%{module}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-flake8
BuildRequires:  python3-pytest
BuildRequires:  python3-trustme
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-uhashring
BuildRequires:  memcached

%global _description %{expand:
A pure python module (thread safe) to access memcached via it’s binary with SASL auth support.}

%description %_description

%package -n python3-binary-memcached
Summary:        %{summary}
Requires:  memcached

%description -n python3-binary-memcached
%_description

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files bmemcached

%check
%pytest


%files -n python3-binary-memcached -f %{pyproject_files}
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.31.2-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Joel Capitao <jcapitao@redhat.com> - 0.31.2-1
- Update to 0.31.2

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 0.31.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Alfredo Moralejo <amoralej@redhat.com> - 0.31.1-1
- Initial build with version 0.31.1

