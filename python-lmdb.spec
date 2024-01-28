%global srcname lmdb
%global sum Python binding for the LMDB 'Lightning' Database (CPython & CFFI included)

Name:           python-%{srcname}
Version:        1.4.0
Release:        5%{?dist}
Summary:        %{sum}

License:        OpenLDAP
URL:            https://github.com/dw/py-lmdb
Source0:        %{pypi_source lmdb}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  lmdb-devel
BuildRequires:  python3-pytest

%description
%{sum}

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{sum}


%prep
%autosetup -n lmdb-%{version}

%generate_buildrequires
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%pyproject_buildrequires


%build
# do not use bundled LMDB library
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%pyproject_wheel


%install
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%pyproject_install

%pyproject_save_files lmdb


%check
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc ChangeLog


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.12

* Fri Feb 03 2023 Jonathan Wright <jonathan@almalinux.org> - 1.4.0-1
- Update to 1.4.0
- modernize spec

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.10

* Wed May 12 2021 Petr Viktorin <pviktori@redhat.com> - 1.0.0-1
- Update to version 1.0.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.92-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.92-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.92-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.92-7
- Subpackage python2-lmdb has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.92-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Petr Špaček <petr.spacek@nic.cz> - 0.92-1
 Initial build using CPython extension and system LMDB library by default.

 The code was imported from PyPI package v0.92 MD5 00520384f53f0c9f6347e681d4bb8140
 + test from Git repo 4651bb3a865c77008ac261443899fe25f88173f2.

 Known problems:
 - crash on put if Environment(writemap=True) and data is too big for FS
   https://github.com/dw/py-lmdb/issues/161
 - crash on Environment(readonly=True).db_open(create=True)
   https://github.com/dw/py-lmdb/issues/160
