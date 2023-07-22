%global srcname conda-package-streaming
%global pkgname conda_package_streaming

# We have a circular dep on conda for tests
%bcond_with bootstrap

Name:           python-%{srcname}
Version:        0.7.0
Release:        6%{?dist}
Summary:        Extract metadata from remote conda packages without downloading whole file

License:        BSD-3-Clause
URL:            https://github.com/conda/conda-package-streaming
Source0:        https://github.com/conda/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global common_description %{expand:Download conda metadata from packages without transferring entire file. Get
metadata from local .tar.bz2 packages without reading entire files.

Uses enhanced pip lazy_wheel to fetch a file out of .conda with no more than
3 range requests, but usually 2.

Uses tar = tarfile.open(fileobj=...) to stream remote .tar.bz2. Closes the
HTTP request once desired files have been seen.}

%description
%{common_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
%if %{without bootstrap}
# Filed https://github.com/conda/conda-package-streaming/pull/52 to add conda dep upstream
BuildRequires:  conda
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{common_description}


%prep
%autosetup -n %{srcname}-%{version}
# do not run coverage in pytest, drop unneeded and unpackaged boto3-stubs dev dep
sed -i -e '/cov/d' -e '/boto3-stubs/d' pyproject.toml requirements.txt

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pkgname}

%check
%if %{without bootstrap}
# To set CONDA_EXE
. /etc/profile.d/conda.sh
export CONDA_EXE
# The deselected tests require a populated conda package cache which we can't really provide
%pytest -v tests \
  --deselect=tests/test_transmute.py::test_transmute \
  --deselect=tests/test_transmute.py::test_transmute_backwards \
  --deselect=tests/test_url.py::test_lazy_wheel
%else
# Minimal non-conda required test
%pytest -v tests/test_degraded.py
%endif

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md
%license %{python3_sitelib}/conda_package_streaming-%{version}.dist-info/LICENSE


%changelog
* Thu Jul 20 2023 Python Maint <python-maint@redhat.com> - 0.7.0-6
- Rebuilt for Python 3.12

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 0.7.0-5
- Bootstrap for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Orion Poplawski <orion@nwra.com> - 0.7.0-3
- Use test extras for build requires
- Add bootstrap conditional

* Wed Dec 07 2022 Orion Poplawski <orion@nwra.com> - 0.7.0-2
- Use macro for description
- Use %%pytest macro
- Fix license
- Add comments about deselected tests

* Sat Dec 03 2022 Orion Poplawski <orion@nwra.com> - 0.7.0-1
- Initial Fedora package
