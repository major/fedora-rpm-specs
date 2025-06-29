# Created by pyp2rpm-3.3.5
%if 0%{?rhel}
%bcond_with docs
%else
%bcond_without docs
%endif
%bcond_without tests

%global pypi_name drgn

%global _description %{expand:
drgn (pronounced "dragon") is a debugger with an emphasis on programmability.
drgn exposes the types and variables in a program for easy, expressive
scripting in Python.}

Name:           python-%{pypi_name}
Version:        0.0.32
Release:        %autorelease
Summary:        Programmable debugger

License:        LGPL-2.1-or-later
URL:            https://github.com/osandov/drgn
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%if %{with docs}
BuildRequires:  sed
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-docs
BuildRequires:  graphviz
%endif
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  bzip2-devel
BuildRequires:  elfutils-devel
BuildRequires:  elfutils-debuginfod-client-devel
BuildRequires:  libkdumpfile-devel
BuildRequires:  zlib-devel
BuildRequires:  xz-devel
# These are needed when building from git snapshots
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description %{_description}

%package -n     %{pypi_name}
Summary:        %{summary}
Recommends:     elfutils-debuginfod-client

%description -n %{pypi_name} %{_description}

%if %{with docs}
%package -n %{pypi_name}-doc
Summary:        %{pypi_name} documentation
BuildArch:      noarch
Requires:       python3-docs

%description -n %{pypi_name}-doc %{_description}

This package contains additional documentation for %{pypi_name}.
%endif

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py
%endif
# Ensure version is always set, even when building from git snapshots
if [ ! -f drgn/internal/version.py ]; then
  echo '__version__ = "%{version}"' > drgn/internal/version.py
fi

%build
# verbose build
V=1 %py3_build

%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install
mkdir -p %{buildroot}%{_datadir}/drgn
cp -PR contrib tools %{buildroot}%{_datadir}/drgn

%if %{with tests}
%check
%pytest
%endif

%files -n %{pypi_name}
%license COPYING
%license LICENSES
%doc README.rst
%{_bindir}/drgn
%{_datadir}/drgn
%{python3_sitearch}/_%{pypi_name}.pyi
%{python3_sitearch}/_%{pypi_name}.cpython*.so
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/_%{pypi_name}_util
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n %{pypi_name}-doc
%license COPYING
%license LICENSES
%doc html
%endif

%changelog
%autochangelog
