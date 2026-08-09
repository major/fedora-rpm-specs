Name:           python-binary-manager
Version:        0.0.7
Release:        %autorelease
Summary:        Binman firmware-packaging tool

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/develop/package/index.html
Source:         %{pypi_source binary_manager}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-libfdt
BuildRequires:  python3-pkg-resources
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pycryptodomex)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(yamllint)
BuildRequires:  sed


%global _description %{expand:
Binman provides a mechanism for building images, from simple SPL + U-Boot
combinations, to more complex arrangements with many parts. It also allows
users to inspect images, extract and replace binaries within them, repacking if
needed.}

%description %_description

%package -n     python3-binary-manager
Summary:        %{summary}
Requires:       python3-libfdt
Requires:       python3dist(jsonschema)
Requires:       python3dist(pycryptodomex)
Requires:       python3dist(pyyaml)
Requires:       python3dist(yamllint)

%description -n python3-binary-manager %_description

%prep
%autosetup -p1 -n binary_manager-%{version}

# Fix dependency name
sed -i 's:"pylibfdt", ::' pyproject.toml

# Remove unnecessary shebangs
sed -i "\|#!/usr/bin/env python3|d" src/binman/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files binman

%check
%pyproject_check_import -e binman.setup

%files -n python3-binary-manager -f %{pyproject_files}
%doc README.rst
%{_bindir}/binman

%changelog
%autochangelog
