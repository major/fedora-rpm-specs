%global srcname xd
%global pypi_name xdfile
%global date 20240101
%global commit 3349ddcf5f4503b243ab9629d8cdbed756cbff56
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        1.9.0~%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Python parser for .xd crossword format

License:        MIT
URL:            https://github.com/century-arcade/xd
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  sed

%global _description %{expand:
This package provides a simple parser for .xd -- a corpus-oriented format,
modeled after the simplicity and intuitiveness of the markdown format. It
supports 99.99% of published crosswords, and is intended to be convenient for
bulk analysis of crosswords by both humans and machines, from the present and
into the future.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{srcname}-%{commit}

# remove bundled library
rm -r crossword

# remove unnecessary shebangs
sed -i 's:^#!/usr/bin/env python.*$::' xdfile/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# remove sample script
rm %{buildroot}%{_bindir}/sample

%check
# remove broken test
# https://github.com/century-arcade/xd/issues/72
rm xdfile/tests/test_xdfile.py
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md doc/xd-format.md

%changelog
%autochangelog
