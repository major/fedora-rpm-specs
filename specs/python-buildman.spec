Name:           python-buildman
Version:        0.0.6
Release:        %autorelease
Summary:        Buildman build tool for U-Boot

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/build/buildman.html
Source:         %{pypi_source buildman}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
This tool handles building U-Boot to check that you have not broken it with
your patch series. It can build each individual commit and report which boards
fail on which commits, and which errors come up. It aims to make full use of
multi-processor machines.}

%description %_description

%package -n     python3-buildman
Summary:        %{summary}

%description -n python3-buildman %_description

%prep
%autosetup -p1 -n buildman-%{version}

# Remove unnecessary shebangs
sed -i "\|#!/usr/bin/env python3|d" src/buildman/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files buildman

%check
%pyproject_check_import

%files -n python3-buildman -f %{pyproject_files}
%doc README.rst
%{_bindir}/buildman

%changelog
%autochangelog
