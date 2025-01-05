Name:           python-patch-manager
Version:        0.0.6
Release:        %autorelease
Summary:        Patman patch manager

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/develop/patman.html
Source:         %{pypi_source patch-manager}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

BuildRequires:  python3dist(pygit2)
BuildRequires:  python3dist(requests)

%global _description %{expand:
This package provides a tool intended to automate patch creation and make it a
less error-prone process. It is useful for U-Boot and Linux work so far, since
they use the checkpatch.pl script.}

%description %_description

%package -n     python3-patch-manager
Summary:        %{summary}

Requires:       python3dist(pygit2)
Requires:       python3dist(requests)

%description -n python3-patch-manager %_description

%prep
%autosetup -p1 -n patch-manager-%{version}

# Remove unnecessary shebangs
sed -i "\|#!/usr/bin/env python3|d" src/patman/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files patman

%check
%pyproject_check_import -e patman.setup

%files -n python3-patch-manager -f %{pyproject_files}
%doc README.rst
%{_bindir}/patman

%changelog
%autochangelog
