%bcond tests 1
%global forgeurl https://github.com/Rogdham/pyzstd
%define tag %{version}

Name:           python-pyzstd
Version:        0.16.2
%forgemeta
Release:        %autorelease
Summary:        Python bindings to Zstandard (zstd) compression library

License:        BSD-3-Clause
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  python3-devel
BuildRequires:  tomcli
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%global _description %{expand:
Pyzstd module provides classes and functions for compressing and decompressing
data, using Facebook’s Zstandard (or zstd as short name) algorithm.}

%description %_description


%package -n python3-pyzstd
Summary:        %{summary}

%description -n python3-pyzstd %_description


%prep
%autosetup -p1 %{forgesetupargs}
# Ensure dynamic-link-zstd is always used
sed -i 's|DYNAMIC_LINK =.*|DYNAMIC_LINK = True|' setup.py
# Stop disabling debuginfo
sed -i "s|'-g0', ||" setup.py
# Fix non-executable-script rpmlint error
sed -i -e '1{\@^#!.*@d}' src/__main__.py
# Remove setuptools upperbound
tomcli set pyproject.toml arrays replace 'build-system.requires' '(setuptools.*),<.+' '\1'


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyzstd


%check
%pytest


%files -n python3-pyzstd -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%license LICENSE


%changelog
%autochangelog
