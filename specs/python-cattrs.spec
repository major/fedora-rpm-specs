%bcond bson 1
%bcond cbor2 1
%bcond msgpack 1
%bcond msgspec 1
%bcond orjson 1

#global commit xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#global snapdate YYYYMMDD

Name:           python-cattrs
Version:        26.1.0%{?commit:^%{snapdate}git%{sub %{commit} 1 7}}
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
%global srcversion %(echo %{version} | cut --delimiter='^' --fields=1)
%endif

# Downstream: temporarily loosen version bounds on some test dependencies
Patch:          0001-Downstream-temporarily-loosen-version-bounds-on-some.patch

# Because an extras metapackage is conditionalized on architecture, the base
# package cannot be noarch – but the rest of the binary packages *are* noarch,
# with no compiled code.
%global debug_package %{nil}

%dnl msgspec_enabled should be defined to 1 or undefined, never defined to 0
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

# Removed for Fedora 42; we can drop the Obsoletes after Fedora 44.
Obsoletes:      python-cattrs-doc < 24.1.2^20241004gitae80674-6

%description -n python3-cattrs %_description


# Most extras metapackages are noarch:
%pyproject_extras_subpkg -n python3-cattrs -a ujson pyyaml tomlkit tomllib
%if %{with bson}
%pyproject_extras_subpkg -n python3-cattrs -a bson
%endif
%if %{with cbor2}
%pyproject_extras_subpkg -n python3-cattrs -a cbor2
%endif
%if %{defined msgspec_enabled}
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
%autosetup -C

# Don’t run benchmarks when testing
%pyproject_patch_dependency pytest-benchmark:ignore
sed --regexp-extended --in-place \
    's/ --benchmark[^[:blank:]"]*//g' pyproject.toml
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency coverage:ignore

# Remove bundled fonts to show they are not packaged:
rm --recursive --verbose docs/_static/fonts/


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{srcversion}'
%{pyproject_buildrequires %{shrink:
    --extras ujson
    %{?with_orjson:--extras orjson}
    %{?with_msgpack:--extras msgpack}
    --extras pyyaml
    --extras tomlkit
    %{?with_cbor2:--extras cbor2}
    %{?with_bson:--extras bson}
    %{?msgspec_enabled:--extras msgspec}
    --extras tomllib
    --dependency-groups test
    }}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{srcversion}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files --assert-license cattrs cattr


%check
%if %{without bson} || %{without cbor2} || %{without msgpack}
# These unconditionally import bson, cbor2, and msgpack, so they error during
# test collection
ignore="${ignore-} --ignore=tests/test_preconf.py"
ignore="${ignore-} --ignore=tests/preconf/test_pyyaml.py"
%endif

%if %{undefined msgspec_enabled}
k="${k-}${k+ and }not test_literal_dicts_msgspec"
k="${k-}${k+ and }not test_msgspec_efficient_enum"
k="${k-}${k+ and }not test_msgspec_json_converter"
k="${k-}${k+ and }not test_msgspec_json_unions"
k="${k-}${k+ and }not test_msgspec_json_unstruct_collection_overrides"
k="${k-}${k+ and }not test_msgspec_native_enums"
# These unconditionally import msgspec, so they error during test collection
ignore="${ignore-} --ignore=tests/preconf/test_msgspec_cpython.py"
%endif

%if %{without orjson}
k="${k-}${k+ and }not test_literal_dicts_orjson"
k="${k-}${k+ and }not test_orjson"
k="${k-}${k+ and }not test_orjson_converter"
k="${k-}${k+ and }not test_orjson_converter_unstruct_collection_overrides"
k="${k-}${k+ and }not test_orjson_efficient_enum"
k="${k-}${k+ and }not test_orjson_native_enums"
k="${k-}${k+ and }not test_orjson_unions"
%endif

%pytest --ignore-glob='bench/*' ${ignore-} -k "${k-}" --numprocesses=auto


%files -n python3-cattrs -f %{pyproject_files}
%doc HISTORY.md
%doc README.md


%changelog
%autochangelog
