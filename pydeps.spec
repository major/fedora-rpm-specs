%global pypi_name pydeps

%global desc %{expand: \
Python module dependency visualization. This package installs the pydeps
command, and normal usage will be to use it from the command line.}

%bcond_without check

Name:		%{pypi_name}
Version:	1.10.18
Release:	3%{?dist}
Summary:	Display module dependencies
License:	BSD
URL:		https://github.com/thebjorn/pydeps
# Use the github source to build
Source0:	%{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

%{?python_enable_dependency_generator}

BuildRequires:	python3-devel
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(stdlib-list)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pyyaml)
BuildRequires:	python3dist(tox)
BuildRequires:	/usr/bin/dot

%description
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version} -N
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
# Exclude failing tests:
# https://github.com/thebjorn/pydeps/issues/71
# https://github.com/thebjorn/pydeps/issues/118
pytest-%{python3_version} -k "not test_file and not test_file_pylib and not test_file_pyliball and not test_relative_imports_same_name_with_std and not test_relative_imports_same_name_with_std_future and not test_pydeps_colors and not test_find_package_names"
%endif

%files -n %{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/pydeps
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.10.18-2
- Rebuilt for Python 3.11

* Sat May 07 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.10.18-1
- Release 1.10.18

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 09 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.10.12-1
- Release 1.10.12

* Thu Sep 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.10.5-4
- Remove patch
- Remove all Requires packages

* Thu Sep 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.10.5-3
- Drop enum34 dependency if use Python >= 3.4.0 (rhbz#2008666) /3

* Thu Sep 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.10.5-2
- Drop enum34 dependency if use Python >= 3.4.0 (rhbz#2008666) /2

* Thu Sep 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.10.5-1
- Release 1.10.5
- Drop enum34 dependency if use Python >= 3.4.0 (rhbz#2008666)

* Fri Sep 24 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.10.3-1
- Release 1.10.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.9.13-1
- Release 1.9.13
- Disable tests (upstream bug #95)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.10-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Luis Bazan <lbazan@fedoraproject.org> - 1.9.10-1
- New upstream version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9.9-1
- Update to new release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.3-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.9.3-1
- New upstream version

* Thu Apr 23 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.9.0-1
- New upstream version

* Wed Apr 22 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.8.8-1
- Initial package
