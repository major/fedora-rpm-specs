%global pypi_name build

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        4%{?dist}
Summary:        A simple, correct PEP517 package builder

License:        MIT
URL:            https://github.com/pypa/build
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros >= 0-41

%description
A simple, correct PEP517 package builder.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A simple, correct PEP517 package builder.


%pyproject_extras_subpkg -n python3-%{pypi_name} virtualenv


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test,virtualenv

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# The skipped tests require internet
%pytest -k "not (test_build_package or \
                 test_build_package_via_sdist or \
                 test_output[via-sdist-isolation] or \
                 test_output[wheel-direct-isolation] or \
                 test_wheel_metadata[True] or \
                 test_wheel_metadata_isolation or \
                 test_with_get_requires or \
                 test_build_sdist or \
                 test_build_wheel[from_sdist] or \
                 test_build_wheel[direct])"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/pyproject-build

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.11

* Tue May 24 2022 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Package the build[virtualenv] extra

* Mon May 23 2022 Lumír Balhar <lbalhar@redhat.com> - 0.8.0-1
- Update to 0.8.0
Resolves: rhbz#2089034

* Fri Mar 18 2022 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Fix virtualenv creation by using the "venv" sysconfig installation scheme
- Resolves: rhbz#2059268

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Lumír Balhar <lbalhar@redhat.com> - 0.7.0-1
- Update to 0.7.0
Resolves: rhbz#2005146

* Wed Aug 04 2021 Lumír Balhar <lbalhar@redhat.com> - 0.6.0-1
- Update to 0.6.0
Resolves: rhbz#1989297

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 Lumír Balhar <lbalhar@redhat.com> - 0.5.1-1
- Initial package.
