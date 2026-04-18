Name:           python-ujson
Version:        5.12.0
Release:        %autorelease
Summary:        Ultra fast JSON encoder and decoder written in pure C

# The entire source is BSD-3-Clause, except:
#
# ----
#
#   Portions of code from MODP_ASCII - Ascii transformations (upper/lower, etc)
#   https://github.com/client9/stringencoders
#
# BSD-3-Clause but with its own copyright statement
#
# ----
#
#   Numeric decoder derived from from TCL library
#   https://opensource.apple.com/source/tcl/tcl-14/tcl/license.terms
#
# TCL: possibly present in python/objToJSON.c, python/ujson.c, and/or
# python/JSONtoObj.c.
License:        BSD-3-Clause AND TCL
URL:            https://github.com/ultrajson/ultrajson
Source:         %{pypi_source ujson}

BuildSystem:    pyproject
BuildOption(install):   -l ujson

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(double-conversion)

BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
UltraJSON is an ultra fast JSON encoder and decoder written in pure C with
bindings for Python.}

%description %{_description}


%package -n python3-ujson
Summary:        %{summary}

%description -n python3-ujson %{_description}


%prep -a
# Remove bundled double-conversion
rm -rv src/ujson/deps


%build -p
export UJSON_BUILD_NO_STRIP=1
export UJSON_BUILD_DC_INCLUDES="$(
  pkg-config --variable=includedir double-conversion
)/double-conversion"
export UJSON_BUILD_DC_LIBS="$(pkg-config --libs double-conversion)"


%install -a
# For setuptools_scm 10+; see:
# https://bugzilla.redhat.com/show_bug.cgi?id=2453824
rm -rvf '%{buildroot}%{python3_sitearch}/src'


%check -a
%pytest -v


%files -n python3-ujson -f %{pyproject_files}
%doc README.md

%dir %{python3_sitearch}/ujson-stubs
%{python3_sitearch}/ujson-stubs/__init__.pyi


%changelog
%autochangelog
