# Requires python-pymongo 4.4.0 or later.
%bcond bson %[ %{undefined fc42} && %{undefined fc41} ]
%bcond cbor2 1
%bcond msgpack 1
%bcond msgspec 1
%bcond orjson 1

#global commit xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#global snapdate YYYYMMDD

Name:           python-cattrs
Version:        25.1.0%{?commit:^%{snapdate}git%{sub %{commit} 1 7}}
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

Obsoletes:      python3-cattrs+bson < 23.2.3-1
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
# These unconditionally import msgspec, so they error during test collection
ignore="${ignore-} --ignore=tests/preconf/test_msgspec_cpython.py"
%endif

%if v"0%{?python3_version}" >= v"3.14"
# https://github.com/python-attrs/cattrs/issues/626
#
# With 3.14.0b2:
#
# FAILED tests/strategies/test_include_subclasses.py::test_structure_as_union
# FAILED tests/strategies/test_include_subclasses.py::test_structuring_unstructuring_unknown_subclass
# FAILED tests/strategies/test_include_subclasses.py::test_overrides[wo-union-strategy-grandchild-only]
# FAILED tests/strategies/test_include_subclasses.py::test_overrides[wo-union-strategy-parent-only]
# FAILED tests/strategies/test_include_subclasses.py::test_parents_with_generics[True]
# FAILED tests/strategies/test_include_subclasses.py::test_overrides[wo-union-strategy-child1-only]
# FAILED tests/strategies/test_include_subclasses.py::test_parents_with_generics[False]
# FAILED tests/strategies/test_include_subclasses.py::test_overrides[wo-union-strategy-child2-only]
# FAILED tests/test_generics.py::test_deep_copy - assert list[~T | None] == lis...
# FAILED tests/test_generics.py::test_structure_nested_generics_with_cols[True-int-result0]
# FAILED tests/test_generics.py::test_structure_nested_generics_with_cols[False-int-result0]
# FAILED tests/test_preconf.py::test_bson
# FAILED tests/test_gen_dict.py::test_type_names_with_quotes - cattrs.errors.St...
# FAILED tests/test_self.py::test_self_roundtrip[True] - AssertionError: assert...
# FAILED tests/test_self.py::test_self_roundtrip[False] - AssertionError: asser...
# FAILED tests/test_self.py::test_self_roundtrip_dataclass[True] - AssertionErr...
# FAILED tests/test_self.py::test_self_roundtrip_dataclass[False] - AssertionEr...
# FAILED tests/test_self.py::test_self_roundtrip_typeddict[True] - cattrs.error...
# FAILED tests/test_self.py::test_self_roundtrip_typeddict[False] - cattrs.erro...
# FAILED tests/test_self.py::test_self_roundtrip_namedtuple[True] - AssertionEr...
# FAILED tests/test_self.py::test_self_roundtrip_namedtuple[False] - AssertionE...
# FAILED tests/test_self.py::test_subclass_roundtrip[True] - AssertionError: as...
# FAILED tests/test_self.py::test_subclass_roundtrip[False] - AssertionError: a...
# FAILED tests/test_self.py::test_subclass_roundtrip_dataclass[True] - Assertio...
# FAILED tests/test_self.py::test_subclass_roundtrip_dataclass[False] - Asserti...
# FAILED tests/test_self.py::test_nested_roundtrip[True] - AssertionError: asse...
# FAILED tests/test_self.py::test_nested_roundtrip[False] - AssertionError: ass...
# FAILED tests/test_structure.py::test_structuring_unsupported - AssertionError...
# FAILED tests/test_preconf.py::test_bson_converter
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-grandchild-only]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-union-container]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-union-compose-child]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-parent-only]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-union-compose-parent]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-non-union-container]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-union-compose-grandchild]
# ERROR tests/strategies/test_include_subclasses.py::test_circular_reference[with-subclasses]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-parent-only]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-child1-only]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-union-compose-child]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-non-union-compose-parent]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-child1-only]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-union-compose-grandchild]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-child2-only]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-non-union-compose-child]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-non-union-compose-parent]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-child2-only]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-non-union-compose-grandchild]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-non-union-compose-child]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-grandchild-only]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-union-container]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-union-compose-parent]
# ERROR tests/strategies/test_include_subclasses.py::test_structuring_with_inheritance[with-subclasses-non-union-compose-grandchild]
# ERROR tests/strategies/test_include_subclasses.py::test_unstructuring_with_inheritance[with-subclasses-non-union-container]
k="${k-}${k+ and }not test_bson"
k="${k-}${k+ and }not test_bson_converter"
k="${k-}${k+ and }not test_circular_reference"
k="${k-}${k+ and }not test_deep_copy"
k="${k-}${k+ and }not test_include_subclasses"
k="${k-}${k+ and }not test_nested_roundtrip"
k="${k-}${k+ and }not test_self_roundtrip"
k="${k-}${k+ and }not test_self_roundtrip_dataclass"
k="${k-}${k+ and }not test_self_roundtrip_namedtuple"
k="${k-}${k+ and }not test_self_roundtrip_typeddict"
k="${k-}${k+ and }not test_structure_nested_generics_with_cols"
k="${k-}${k+ and }not test_structuring_unsupported"
k="${k-}${k+ and }not test_structuring_with_inheritance"
k="${k-}${k+ and }not test_subclass_roundtrip"
k="${k-}${k+ and }not test_subclass_roundtrip_dataclass"
k="${k-}${k+ and }not test_type_names_with_quotes"
k="${k-}${k+ and }not test_unstructuring_with_inheritance"
%endif

%pytest --ignore-glob='bench/*' ${ignore-} -k "${k-}" -n auto


%files -n python3-cattrs -f %{pyproject_files}
%doc HISTORY.md
%doc README.md


%changelog
%autochangelog
