%global srcname Mathics3

Name:           python-mathics3
Version:        5.0.2
Release:        %autorelease
Summary:        General-purpose computer algebra system

# mathics3 itself is GPLv3, the other licenses are for the data files (see below)
License:        GPL-3.0-only AND Public Domain AND CC-BY-SA-3.0 AND W3C
URL:            https://mathics.org
# Fetched from PyPI and repackaged with mathics-repackage-source.sh due to
# https://github.com/Mathics3/mathics-core/issues/728
Source:         %{srcname}-%{version}.tar.gz
Source:         mathics-repackage-source.sh
# ExampleData: update copyright byline for Namespaces.xml
Patch:          https://github.com/Mathics3/mathics-core/pull/733.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest

%global _description %{expand:
Mathics is a general-purpose computer algebra system (CAS) providing a free,
open-source alternative to Mathematica.}

%description %_description

%package -n     mathics
Summary:        %{summary}
License:        GPL-3.0-only
Recommends:     mathics-data = %{version}-%{release}
Provides:       python-mathics3 = %{version}-%{release}
Provides:       mathics3 = %{version}-%{release}

# Needed for pkg_resources which is used in mathics/settings.py
Requires:       python3dist(setuptools)

%description -n mathics %_description

%package -n     mathics-data
Summary:        Example data files for Mathics
# From mathics/data/ExampleData/copyright.csv
License:        Public Domain AND CC-BY-SA-3.0 AND W3C

%description -n mathics-data
This package provides example data files for Mathics.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Relax sympy version requirement
# https://github.com/Mathics3/mathics-core/commit/c031eb7e487f789dddccb8c41ae45a2805d6f525
sed -i 's:"sympy.*":"sympy":' setup.py

# Fix permissions
# https://github.com/Mathics3/mathics-core/pull/729
chmod -x mathics/data/ExampleData/{InventionNo1.xml,numberdata.csv}

export USE_CYTHON=1
%generate_buildrequires
%pyproject_buildrequires

%build
export USE_CYTHON=1
%pyproject_wheel

%install
export USE_CYTHON=1
%pyproject_install
%pyproject_save_files mathics

%check
# test_string_split: https://github.com/Mathics3/mathics-core/issues/743
# test_system_specific_long_integer:
# https://github.com/Mathics3/mathics-core/issues/760
%pytest \
%ifarch s390x
  --deselect=test/test_evaluation.py::test_system_specific_long_integer \
%endif
  --deselect=test/test_strings.py::test_string_split

%files -n mathics -f %{pyproject_files}
%license COPYING.txt
%doc README.rst FUTURE.rst AUTHORS.txt CHANGES.rst ChangeLog
%{_bindir}/mathics
%exclude %{python3_sitearch}/mathics/data

%files -n mathics-data
%license mathics/data/ExampleData/copyright.csv
%{python3_sitearch}/mathics/data

%changelog
%autochangelog
