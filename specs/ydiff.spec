Name:       ydiff
Version:    1.5
Release:    %autorelease
Summary:    View colored, incremental diff
URL:        https://github.com/ymattw/ydiff
License:    BSD-3-Clause
Source0:    https://github.com/ymattw/ydiff/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
BuildRequires: less
BuildArch: noarch

Requires: less
Requires: python%{python3_pkgversion}-%{name}
%description
Ydiff is a terminal-based tool to view colored, incremental diffs in
a version-controlled workspace or from stdin, in side-by-side (similar to
``diff -y``) or unified mode, and auto-paged.

%package -n     python3-%{name}
Summary:        %{summary}
%description -n python3-%{name}
Python library that implements API used by ydiff tool.

%prep
%autosetup -n %{name}-%{version}
/usr/bin/sed -i '/#!\/usr\/bin\/env python/d' ydiff.py
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
tests/regression.sh
%pyproject_check_import

# upstream pipeline uses `make test` which also has coverage
# and linters but we don't do those here

%install
%pyproject_install
%pyproject_save_files %{name}

%files
%doc README.rst
%license LICENSE
%{_bindir}/ydiff

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
