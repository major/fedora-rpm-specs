Name:           python-pytest-datadir
Version:        1.5.0
Release:        1%{?dist}
Summary:        Pytest plugin for test data directories and files
License:        MIT
URL:            https://github.com/gabrielcnr/pytest-datadir
Source0:        %{url}/archive/v%{version}/pytest-datadir-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist docutils}

%global _desc %{expand:
This package contains a pytest plugin for manipulating test data
directories and files.}

%description %_desc

%package     -n python3-pytest-datadir
Summary:        %{summary}

%description -n python3-pytest-datadir %_desc

%prep
%autosetup -n pytest-datadir-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -t

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel
rst2html --no-datestamp CHANGELOG.rst CHANGELOG.html

%install
%pyproject_install
%pyproject_save_files pytest_datadir

%check
%tox

%files -n python3-pytest-datadir -f %{pyproject_files}
%doc AUTHORS CHANGELOG.html README.md

%changelog
* Tue Oct  3 2023 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- Version 1.5.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 1.4.1-2
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Version 1.4.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Initial RPM
