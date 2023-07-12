%bcond_with check
%global srcname tifffile

Name: python-%{srcname}
Version: 2023.4.12
Release: 1%{?dist}
Summary: Read and write TIFF(r) files

License: BSD
URL: https://www.lfd.uci.edu/~gohlke/
Source0: %{pypi_source}

BuildArch: noarch

BuildRequires: python3-devel

%global _description %{expand:
Tifffile is a Python library to:
 * store numpy arrays in TIFF (Tagged Image File Format) files, and
 * read image and metadata from TIFF-like files used in bioimaging.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  %{py3_dist setuptools}
# Testing
%if %{with check}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist fsspec}
%endif

%description -n python3-%{srcname} %_description

%prep
# Remove shebang
%autosetup -n %{srcname}-%{version}
sed -i -e "1d" tifffile/lsm2bin.py 
sed -i 's/\r$//' README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files tifffile

%if %{with check}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
export PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}"
# 7 tests fail out of 1000 
# these tests require network or additional packages not in Fedora
pytest-%{python3_version} -v tests \
 --deselect=tests/test_tifffile.py::test_issue_infinite_loop \
 --deselect=tests/test_tifffile.py::test_issue_jpeg_ia \
 --deselect=tests/test_tifffile.py::test_func_pformat_xml \
 --deselect=tests/test_tifffile.py::test_filehandle_seekable \
 --deselect=tests/test_tifffile.py::test_read_cfa \
 --deselect=tests/test_tifffile.py::test_read_tiles \
 --deselect=tests/test_tifffile.py::test_write_cfa \
 --deselect=tests/test_tifffile.py::test_write_volume_png
%else
%pyproject_check_import -t
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/lsm2bin
%{_bindir}/tifffile
%{_bindir}/tiff2fsspec
%{_bindir}/tiffcomment

%changelog
* Mon Jul 10 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 2023.4.12-1
- New upstream source 2023.4.12
- New style macros
- Checking only package import, some deps are still broken

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2020.7.4-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2020.7.4-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2020.7.4-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2020.7.4-2
- Fix license

* Wed Jul 08 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2020.7.4-1
- Initial spec

