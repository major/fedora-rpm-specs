%global srcname imageio

Name: python-%{srcname}
Version: 2.22.4
Release: 2%{?dist}
Summary: Python IO of image, video, scientific, and volumetric data formats.
License: BSD
URL: https://imageio.github.io
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires: python3-devel

%global _description %{expand:
Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-setuptools

%description -n python3-%{srcname}
%_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files imageio

%check
# Testing requires image sample, either local or from the internet
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md 
# Exclude files that download binary freeimage library
%exclude %{_bindir}/imageio*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 2.22.4-1
- New upstream source (2.22.4)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.9.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.9.0-2
- Rebuilt for Python 3.10

* Wed Feb 03 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 2.9.0-1
- Initial package

