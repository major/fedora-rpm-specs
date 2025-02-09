%global srcname imageio

Name: python-%{srcname}
Version: 2.37.0
Release: %autorelease
Summary: Python IO of image, video, scientific, and volumetric data formats.
License: BSD-2-Clause
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
%autochangelog
