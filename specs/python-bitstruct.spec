%global pypi_name bitstruct
%global global_desc \
This module performs conversions between Python values and C bit \
field structs represented as Python byte strings.  It is intended to \
have a similar interface as the python struct module, but working on \
bits instead of primitive data types (char, int, …).

Name:           python-%{pypi_name}
Version:        8.22.0
Release:        %autorelease
Summary:        Interpret strings as packed binary data
License:        MIT
URL:            https://github.com/eerimoq/bitstruct
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/bitstruct-%{version}.tar.gz
Patch:          python-bitstruct-0001-PATCH-Fix-float16-pack-unpack-on-big-endian-systems.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildSystem:    pyproject
BuildOption(install): -l %{pypi_name}

%description
%{global_desc}

%package        -n python3-%{pypi_name}
Summary:        %{summary}

%description    -n python3-%{pypi_name}
%{global_desc}

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
