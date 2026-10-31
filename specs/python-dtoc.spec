Name:           python-dtoc
Version:        0.1.0
Release:        %autorelease
Summary:        Devicetree-to-C generator

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/develop/driver-model/of-plat.html
Source:         %{pypi_source dtoc}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-libfdt
BuildRequires:  python3-u-boot-pylib
BuildRequires:  sed

%global _description %{expand:
This is a Python program and associated utilities, which supports converting
devicetree files into C code. It generates header files containing struct
definitions, as well as C files containing the data. It does not require any
modification of the devicetree files.}

%description %_description

%package -n     python3-dtoc
Summary:        %{summary}
Requires:       python3-libfdt
Requires:       python3-u-boot-pylib

%description -n python3-dtoc %_description

%prep
%autosetup -p1 -n dtoc-%{version}

# Remove dependencies handled by BuildRequires/Requires
sed -i -e '/"pylibfdt/d' -e '/"u-boot-pylib/d' pyproject.toml

# Remove unnecessary shebangs
sed -i dtoc/*.py \
  -e "\|#!/usr/bin/env python3|d" \
  -e "\|#!/usr/bin/python|d"

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dtoc

%check
%pyproject_check_import -e dtoc.setup

%files -n python3-dtoc -f %{pyproject_files}
%doc README.rst
%{_bindir}/dtoc

%changelog
%autochangelog
