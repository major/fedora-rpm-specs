%global srcname matrix-common
%global releasename matrix-python-common
%global pymodulename matrix_common

Name:           python-%{srcname}
Version:        1.3.0
Release:        2%{?dist}
Summary:        Common utilities for Synapse, Sydent and Sygnal

License:        ASL 2.0
URL:            https://github.com/matrix-org/%{releasename}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Common utilities for Synapse, Sydent and Sygnal.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{releasename}-%{version}


%generate_buildrequires
%pyproject_buildrequires -e py


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pymodulename}


%check
%tox


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 10 2022 Kai A. Hiller <V02460@gmail.com> - 1.3.0-1
- Update to v1.3.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Kai A. Hiller <V02460@gmail.com> - 1.2.1-1
- Update to v1.2.1

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.11

* Fri Feb 11 2022 Kai A. Hiller <V02460@gmail.com> - 1.1.0-1
- Update to v1.1.0

* Sat Jan 08 2022 Kai A. Hiller <V02460@gmail.com> - 1.0.0-1
- Initial package
- Fixes rhbz#2038993
