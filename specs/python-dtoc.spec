Name:           python-dtoc
Version:        0.5.4
Release:        %autorelease
Summary:        Devicetree-to-C generator

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/develop/driver-model/of-plat.html
Source:         %{pypi_source dtoc}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
This is a Python program and associated utilities, which supports converting
devicetree files into C code. It generates header files containing struct
definitions, as well as C files containing the data. It does not require any
modification of the devicetree files.}

%description %_description

%package -n     python3-dtoc
Summary:        %{summary}

%description -n python3-dtoc %_description

%prep
%autosetup -p1 -n dtoc-%{version}

# Rename PEP 508 dep name to match the Fedora-provided virtual name
sed -i 's/"pylibfdt >= 1.7"/"libfdt >= 1.7"/' pyproject.toml

# Drop test assets not needed at runtime
rm -rf dtoc/test

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
