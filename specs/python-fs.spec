%global srcname fs

# RHEL does not include the test dependencies
%bcond tests %{undefined rhel}

Name:           python-%{srcname}
Version:        2.4.16
Release:        16%{?dist}
Summary:        Python's Filesystem abstraction layer

# https://spdx.org/licenses/MIT.html
License:        MIT
URL:            https://pypi.org/project/fs/
Source0:        https://github.com/PyFilesystem/pyfilesystem2/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Replace TestCase method aliases removed in Python 3.12
# https://github.com/PyFilesystem/pyfilesystem2/pull/570
# changelog fragment removed to avoid conflict
Patch:          570.patch

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(six)
%if %{with tests}
# Required for running tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)
BuildRequires:  python3dist(parameterized)
%endif

%global _description %{expand:
Think of PyFilesystem's FS objects as the next logical step to Python's file
objects. In the same way that file objects abstract a single file, FS objects
abstract an entire filesystem.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n pyfilesystem2-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%if %{with tests}
%check
%pyproject_check_import

# Almost all tests in tests/test_ftpfs.py need python3dist(pyftpdlib), which is
# packaged, but this imports from pyftpdlib.tests, which is not packaged.
ignore="${ignore-} --ignore=tests/test_ftpfs.py"

# Regressions related to URL formation in Python 3.14
# https://github.com/PyFilesystem/pyfilesystem2/issues/596
k="${k-}${k+ and }not test_complex_geturl"
# Matches test_geturl_for_fs but not test_geturl_for_fs_but_file_is_binaryio
k="${k-}${k+ and }not (test_geturl_for_fs and not binary)"

%pytest -k "${k-}" ${ignore-}
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md examples

%changelog
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 2.4.16-16
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 2.4.16-15
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 10 2025 Parag Nemade <pnemade AT redhat DOT com> - 2.4.16-13
- Convert a spec to use pyproject macros (rh#2377730)

* Sat Jun 14 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.16-12
- Remove obsolete test skip (regression was fixed in Python 3.12.1)
- Report and skip regressions related to URL formation in Python 3.14;
  fixes RHBZ#2336951

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 2.4.16-11
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.4.16-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Parag Nemade <pnemade AT redhat DOT com> - 2.4.16-4
- Help msuchy to count this package as already using SPDX license expression

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 2.4.16-3
- Rebuilt for Python 3.12

* Thu May 25 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 2.4.16-2
- Disable tests in RHEL builds

* Thu Mar 16 2023 Parag Nemade <pnemade AT redhat DOT com> - 2.4.16-1
- Update to 2.4.16 version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.4.11-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.11-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-5
- Add missing BR: python3-setuptools

* Mon Jun 01 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-4
- Disable few tests temporary for now (rhbz#1820916, rhbz#1841708)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.11-3
- Rebuilt for Python 3.9

* Mon Mar 30 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-2
- enable tests and use upstream source tarball

* Mon Mar 30 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-1
- Initial packaging

