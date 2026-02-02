%global modname piexif

Name:           python-%{modname}
Version:        1.1.3
Release:        %autorelease
Summary:        Pure Python library to simplify exif manipulations with python

# spdx
License:        MIT
URL:            https://github.com/hMatoba/Piexif
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

# Taken from https://github.com/hMatoba/Piexif/issues/108
Patch0:         python-piexif-fix-tests-pillow.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Very simple Python library to simplify exif manipulations that does
not depend on other libraries.

There are only just five functions:
    load(filename)                 - Get exif data as dict.
    dump(exif_dict)                - Get exif as bytes to save with JPEG.
    insert(exif_bytes, filename)   - Insert exif into JPEG.
    remove(filename)               - Remove exif from JPEG.
    transplant(filename, filename) - Transplant exif from JPEG to JPEG.}

%description %{_description}

%package -n     python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
Suggests:       python%{python3_version}dist(pillow)

%description -n python3-%{modname} %{_description}

%prep
%autosetup -p1 -n Piexif-%{version}

sed -i 's|==.*$||' requirements.txt
sed -i 's|unittest.makeSuite|unittest.defaultTestLoader.loadTestsFromTestCase|' tests/s_test.py

%generate_buildrequires
%pyproject_buildrequires requirements.txt -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
