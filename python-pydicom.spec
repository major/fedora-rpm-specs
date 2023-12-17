# Enable test with --with=pytest --enable-network, because they download data
# from the net and they don't work in koji
%bcond_with alltests

%global _description %{expand:
pydicom is a pure python package for working with DICOM files. It was made for
inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file.

pydicom is not a DICOM server, and is not primarily about viewing images. It is
designed to let you manipulate data elements in DICOM files with python code.

Limitations -- the main limitation of the current version is that compressed
pixel data (e.g. JPEG) cannot be altered in an intelligent way as it can for
uncompressed pixels. Files can always be read and saved, but compressed pixel
data cannot easily be modified.

Documentation is available at https://pydicom.github.io/pydicom}

Name:           python-pydicom
Version:        2.4.4
Release:        %autorelease
Summary:        Read, modify and write DICOM files with python code

# There are generated data (private dict) in special format from GDCM (see License file)
License:        MIT and BSD-3-Clause
URL:            https://github.com/darcymason/pydicom
Source0:        %{url}/archive/v%{version}/pydicom-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-pydicom
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-numpy

%if %{with alltests}
BuildRequires:  python3-pytest
BuildRequires:  python3-dateutil
%endif

Requires:       python3-dateutil
Recommends:     python3-numpy
Recommends:     python3-matplotlib
Recommends:     python3-tkinter
Recommends:     python3-pillow

%description -n python3-pydicom %_description

%prep
%autosetup -n pydicom-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pydicom

%check
%if %{with alltests}
%pyproject_check_import
# Disable TestPillowHandler_JPEG.test_color_3d because koji is unable to
# allocate enough RAM during build. Works ok building locally
# Disable test_handler_util, it fails to build with numpy 1.19
# reported upstream https://github.com/pydicom/pydicom/issues/1119
%{pytest} -k "not test_color_3d"
%else
# exclude ones that download
%pyproject_check_import -e *benchmark* -e *tests*
%endif

%files -n python3-pydicom -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/pydicom

%changelog
%autochangelog
