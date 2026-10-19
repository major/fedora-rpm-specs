Name:           python-u-boot-pylib
Version:        0.1.0
%global forgeurl https://github.com/nxtboot/u-boot-pylib
%global forgename github
%forgemeta
Release:        %autorelease
Summary:        U-Boot Python library

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org
Source:         %{pypi_source u_boot_pylib}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a Python library used by various U-Boot tools, including patman,
buildman and binman.}

%description %_description

%package -n     python3-u-boot-pylib
Summary:        %{summary}

%description -n python3-u-boot-pylib %_description

%prep
%autosetup -p1 -n u_boot_pylib-%{version}
# Remove shebang from non-executable script
sed -i -e '1{\@^#!/usr/bin/env python@d}' u_boot_pylib/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files u_boot_pylib

%check
%pyproject_check_import

%files -n python3-u-boot-pylib -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
