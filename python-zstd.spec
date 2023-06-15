%global pypi_name zstd
%global zstd_version 1.4.5

Name:           python-%{pypi_name}
Version:        %{zstd_version}.1
Release:        11%{?dist}
Summary:        Zstd Bindings for Python

License:        BSD
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source0:        %{pypi_source}

# Patches to fix test execution
Patch0:         python-zstd-1.4.5.1-test-external.patch
Patch1:         python-zstd-1.4.5.1-test-once.patch

# Python 3.10 compatibility, merged upstream
# From https://github.com/sergey-dryabzhinsky/python-zstd/commit/428a31edcd
Patch2:         python-zstd-1.4.5.1-py_ssize_t_clean.patch

# Python 3.11 compatibility, merged upstream 
# From https://github.com/sergey-dryabzhinsky/python-zstd/commit/4e9b8b0cbf
Patch3:         0003-Port-to-Python-3.11-use-Py_SET_SIZE.patch

# Part of https://github.com/sergey-dryabzhinsky/python-zstd/commit/b823bc087b2
Patch4:         python-zstd-1.4.5.1-c99.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(libzstd) >= %{zstd_version}

%description
Simple Python bindings for the Zstd compression library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
# The library does not do symbol versioning to fully match automatically on
Requires:       libzstd%{?_isa} >= %{zstd_version}

%description -n python3-%{pypi_name}
Simple Python bindings for the Zstd compression library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove bundled zstd library
rm -rf zstd/
# do not test the version matching, we don't really need exact version of
# zstd here
rm tests/test_version.py
sed -i -e '/test_version/d' tests/__init__.py

%build
%py3_build -- --legacy --pyzstd-legacy --external

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pypi_name}*.so

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.5.1-11
- Rebuilt for Python 3.12

* Wed Feb 01 2023 Nikita Popov <npopov@redhat.com> - 1.4.5.1-10
- Port to C99

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.5.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.5.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Joel Capitao <jcapitao@redhat.com> - 1.4.5.1-2
- Edit macro for CentOS interoperability

* Sun Aug 23 2020 Neal Gompa <ngompa13@gmail.com> - 1.4.5.1-1
- Initial package (#1870571)
