%global pypi_name josepy

%global py3_prefix python%{python3_pkgversion}

%bcond_without docs

Name:           python-%{pypi_name}
Version:        1.14.0
Release:        2%{?dist}
Summary:        JOSE protocol implementation in Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/josepy
Source0:        %{pypi_source}
Source2:        https://dl.eff.org/certbot.pub
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Used to verify OpenPGP signature
#BuildRequires:  gnupg2
%if 0%{?rhel} && 0%{?rhel} == 8
# "gpgverify" macro, not in COPR buildroot by default
BuildRequires:  epel-rpm-macros >= 8-5
%endif

%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif

%description
JOSE protocol implementation in Python using cryptography.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}


%if %{with docs}
Recommends:     python-%{pypi_name}-doc
%endif

%description -n python3-%{pypi_name}
JOSE protocol implementation in Python using cryptography.

This is the Python 3 version of the package.

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
Conflicts:      python2-%{pypi_name} < 1.1.0-9
Conflicts:      python3-%{pypi_name} < 1.1.0-9
%description -n python-%{pypi_name}-doc
Documentation for python-%{pypi_name}
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Build documentation
%if %{with docs}
make -C docs man PATH=${HOME}/.local/bin:$PATH SPHINXBUILD=sphinx-build-3
%endif

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with docs}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/_build/man/*.1*
%endif

%check
%pytest -Wdefault

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/jws

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc README.rst
%doc %{python3_sitelib}/CHANGELOG.rst
%doc %{python3_sitelib}/CONTRIBUTING.md
%{_mandir}/man1/*
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 23 2024 Nick Bebout <nb@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.13.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.13.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.13.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.13.0-2
- Rebuilt for Python 3.11

* Thu Mar 10 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.13.0-1
- update to 1.13.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.12.0-1
- update to 1.12.0

* Fri Jan 07 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.11.0-2
- Fix FTBFS with pytest 7.0.0rc1

https://github.com/pytest-dev/pytest/discussions/9415#discussioncomment-1926262

* Wed Nov 17 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.11.0-1
- update to 1.11.0

* Thu Sep 30 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.0-1
- update to 1.10.0

* Mon Sep 13 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.9.0-1
- update to 1.9.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.8.0-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.8.0-1
- update to 1.8.0

* Tue Feb 23 2021 Nick Bebout <nb@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Tue Feb 02 2021 Nick Bebout <nb@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Tue Aug 18 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.9

* Tue Mar 24 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-2
- build Python 3 subpackage also in EPEL7

* Wed Jan 29 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.3.0-1
- Update to 1.3.0 (#1795747)

* Wed Jan 29 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.2.0-6
- enable GPG source file verification

* Mon Oct 07 2019 Eli Young <elyscape@gmail.com> - 1.2.0-5
- Support EPEL8 builds

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Eli Young <elyscape@gmail.com> - 1.2.0-1
- Update to 1.2.0 (#1725899)

* Thu Jun 27 2019 Eli Young <elyscape@gmail.com> - 1.1.0-9
- Split docs to separate package (#1700273)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Eli Young <elyscape@gmail.com> - 1.1.0-7
- Remove Python 2 package in Fedora 30+ (#1658534)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Eli Young <elyscape@gmail.com> - 1.1.0-5
- Enable tests

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Eli Young <elyscape@gmail.com> - 1.1.0-3
- Use available python2 metapackages for EPEL7
- Specify binary name for sphinx-build
- Fix permissions on man files

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.7

* Tue Apr 17 2018 Eli Young <elyscape@gmail.com> - 1.1.0-1
- Update to 1.1.0 (#1567455)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Eli Young <elyscape@gmail.com> - 1.0.1-1
- Initial package.
