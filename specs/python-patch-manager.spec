%global forgeurl https://github.com/nxtboot/patman
Version:        0.2.0
%forgemeta

Name:           python-patch-manager
Release:        %autorelease
Summary:        Patman patch manager

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

# Fix asyncio event loop issues on Python 3.10+
Patch:          0001-Fix-asyncio-event-loop-retrieval-on-Python-3.10.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
This package provides a tool intended to automate patch creation and make it a
less error-prone process. It is useful for U-Boot and Linux work so far, since
they use the checkpatch.pl script.}

%description %_description

%package -n     python3-patch-manager
Summary:        %{summary}

%description -n python3-patch-manager %_description

%prep
%forgeautosetup -p1

# Remove unnecessary shebangs
sed -i "\|#!/usr/bin/env python3|d" patman/*.py u_boot_pylib/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files patman u_boot_pylib

%check
%pyproject_check_import -e patman.setup

%files -n python3-patch-manager -f %{pyproject_files}
%doc README.rst
%{_bindir}/patman

%changelog
%autochangelog
