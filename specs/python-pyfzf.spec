%global srcname pyfzf

Summary:        Python wrapper for junegunn's fuzzyfinder (fzf)
Name:           python-%{srcname}
Version:        0.3.1
Release:        %autorelease
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %{pypi_source %{srcname}}
Patch:          pyfzf-0.3.1-test.patch
BuildArch:      noarch
BuildRequires:  fzf
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%global _description \
Python wrapper for junegunn's awesome fuzzyfinder (fzf), \
a general-purpose command-line fuzzy finder.
%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
Requires:       fzf
%description -n python3-%{srcname} %{_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i '1{\@^#!/usr/bin/env python@d}' pyfzf/pyfzf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
