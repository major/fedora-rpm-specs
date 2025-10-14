# Requires python-pymongo 4.4.0 or later, so disable for F41/F42.
# F43: disable until RHBZ#2356166 is fixed in python-pymongo.
%bcond bson %[ %{undefined fc42} && %{undefined fc41} ]
%bcond cbor2 1
%bcond msgpack 1
%bcond msgspec 1
%bcond orjson 1

#global commit xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#global snapdate YYYYMMDD

Name:           python-cattrs
Version:        25.3.0%{?commit:^%{snapdate}git%{sub %{commit} 1 7}}
Release:        %autorelease
Summary:        Python library for structuring and unstructuring data

# SPDX
License:        MIT
URL:            https://github.com/python-attrs/cattrs
# The GitHub archive contains tests and docs, which the PyPI sdist lacks
%if %{undefined commit}
Source:         %{url}/archive/v%{version}/cattrs-%{version}.tar.gz
%global srcversion %{version}
%else
Source:         %{url}/archive/%{commit}/cattrs-%{commit}.tar.gz
%global srcversion %(echo %{version} | cut -d '^' -f 1)
%endif

# Downstream: temporarily loosen version bounds on some test dependencies
Patch:          0001-Downstream-temporarily-loosen-version-bounds-on-some.patch

# Because an extras metapackage is conditionalized on architecture, the base
# package cannot be noarch – but the rest of the binary packages *are* noarch,
# with no compiled code.
%global debug_package %{nil}

BuildRequires:  python3-devel
BuildRequires:  tomcli

%global msgspec_enabled 0
%if %{with msgspec}
%ifnarch s390x %{ix86}
%global msgspec_enabled 1
%endif
%endif

%global _description %{expand:
cattrs is an open source Python library for structuring and
unstructuring data. cattrs works best with attrs classes and the usual
Python collections, but other kinds of classes are supported by
manually registering converters.}

%description %_description


%package -n python3-cattrs
Summary:        %{summary}

BuildArch:      noarch

%if %{without bson}
Obsoletes:      python3-cattrs+bson < 25.1.1-2
%endif
# Removed for Fedora 42; we can drop the Obsoletes after Fedora 44.
Obsoletes:      python-cattrs-doc < 24.1.2^20241004gitae80674-6

%description -n python3-cattrs %_description


# Most extras metapackages are noarch:
%pyproject_extras_subpkg -n python3-cattrs -a ujson pyyaml tomlkit
%if %{with bson}
%pyproject_extras_subpkg -n python3-cattrs -a bson
%endif
%if %{with cbor2}
%pyproject_extras_subpkg -n python3-cattrs -a cbor2
%endif
%if %{msgspec_enabled}
# python-msgspec is ExcludeArch: s390x i686; the extras metapackage is arched
# because it is not present on every architecture
%pyproject_extras_subpkg -n python3-cattrs msgspec
%endif
%if %{with msgpack}
%pyproject_extras_subpkg -n python3-cattrs -a msgpack
%endif
%if %{with orjson}
%pyproject_extras_subpkg -n python3-cattrs -a orjson
%endif


%prep
%autosetup -n cattrs-%{?!commit:%{version}}%{?commit:%{commit}}

# Don’t run benchmarks when testing
tomcli set pyproject.toml lists delitem 'dependency-groups.test' \
    'pytest-benchmark\b.*'
sed -r -i 's/ --benchmark[^[:blank:]"]*//g' pyproject.toml
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem 'dependency-groups.test' \
    'coverage\b.*'

# Remove bundled fonts to show they are not packaged:
rm -rv docs/_static/fonts/


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{srcversion}'
%{pyproject_buildrequires \
    -x ujson \
%if %{with orjson}
    -x orjson \
%endif
%if %{with msgpack}
    -x msgpack \
%endif
    -x pyyaml \
    -x tomlkit \
%if %{with cbor2}
    -x cbor2 \
%endif
%if %{with bson}
    -x bson \
%endif
%if %{msgspec_enabled}
    -x msgspec \
%endif
    -g test}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{srcversion}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l cattrs cattr


%check
%if %{without bson} || %{without cbor2}
# These unconditionally import bson and cbor2, so they error during test
# collection
ignore="${ignore-} --ignore=tests/test_preconf.py"
ignore="${ignore-} --ignore=tests/preconf/test_pyyaml.py"
%endif

%if !%{msgspec_enabled}
k="${k-}${k+ and }not test_literal_dicts_msgspec"
k="${k-}${k+ and }not test_msgspec_efficient_enum"
k="${k-}${k+ and }not test_msgspec_json_converter"
k="${k-}${k+ and }not test_msgspec_json_unions"
k="${k-}${k+ and }not test_msgspec_json_unstruct_collection_overrides"
k="${k-}${k+ and }not test_msgspec_native_enums"
# These unconditionally import msgspec, so they error during test collection
ignore="${ignore-} --ignore=tests/preconf/test_msgspec_cpython.py"
%endif

%pytest --ignore-glob='bench/*' ${ignore-} -k "${k-}" -n auto


%files -n python3-cattrs -f %{pyproject_files}
%doc HISTORY.md
%doc README.md


%changelog
%autochangelog
