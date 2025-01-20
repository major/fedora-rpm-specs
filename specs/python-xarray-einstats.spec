%bcond_without check

%global srcname xarray-einstats

Name: python-%{srcname}
Version: 0.5.1
Release: 6%{?dist}
Summary: Stats, linear algebra and einops for xarray 
License: Apache-2.0

URL: https://github.com/arviz-devs/xarray-einstats
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires:  python3-devel

%global _description %{expand:
xarray-einstats is an open source Python library part of the ArviZ project. 
It acts as a bridge between the xarray library for labelled arrays and 
libraries for raw arrays such as NumPy or SciPy.}     

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname}
%_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files xarray_einstats

%check
# Tests are not included in the tarball
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md 

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Python Maint <python-maint@redhat.com> - 0.5.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jun 03 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.1-1
- Initial package

