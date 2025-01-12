%bcond tests 1

Name:           python-pydantic
Version:        2.10.4
%global srcversion %{lua:return(rpm.expand("%{version}"):gsub("~",""))}
Release:        %autorelease
Summary:        Data validation using Python type hinting

# SPDX
License:        MIT
URL:            https://github.com/pydantic/pydantic
Source:         %{url}/archive/v%{srcversion}/pydantic-%{srcversion}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli
# For check phase
%if %{with tests}
BuildRequires:  %{py3_dist cloudpickle}
BuildRequires:  %{py3_dist dirty-equals}
BuildRequires:  %{py3_dist jsonschema}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
BuildRequires:  %{py3_dist pytz}
# Required for test_pretty_print
BuildRequires:  %{py3_dist rich}
%endif

%global _description %{expand:
Data validation and settings management using python type hinting.}

%description %{_description}


%package -n     python3-pydantic
Summary:        %{summary}
Recommends:     python3-pydantic+email
# The dotenv extra was removed in pydantic v2.
# Remove the Obsoletes in Fedora 43+
Obsoletes:      python3-pydantic+dotenv < 2~~

%description -n python3-pydantic %{_description}


%package        doc
Summary:        Documentaton for Pydantic

%description    doc
This package includes the documentation for Pydantic in Markdown format.


%prep
%autosetup -n pydantic-%{srcversion} -p1

# Delete pytest addopts. We don't care about benchmarking or coverage.
tomcli-set pyproject.toml del 'tool.pytest.ini_options.addopts'
# CPython 3.13 warns on FutureRef._evaluate/typing._eval_type not passing
# type_params
# https://github.com/pydantic/pydantic/issues/9613
#
#   DeprecationWarning: Failing to pass a value to the 'type_params' parameter
#   of 'typing._eval_type' is deprecated, as it leads to incorrect behaviour
#   when calling typing._eval_type on a stringified annotation that references
#   a PEP 695 type parameter. It will be disallowed in Python 3.15.
tomcli-set pyproject.toml append 'tool.pytest.ini_options.filterwarnings' \
    'ignore:Failing to pass a value.*PEP 695.*:DeprecationWarning:'


%generate_buildrequires
%pyproject_buildrequires -x email -x dotenv


%build
%pyproject_wheel


# Docs are in MarkDown, and should be added when mkdocs is packaged.

%install
%pyproject_install
%pyproject_save_files -l pydantic


%check
%pyproject_check_import -e pydantic.mypy -e pydantic.v1.mypy
%if %{with tests}
%if %{defined fc40} || %{defined el10}
# An error message has different text than the test expects, but the expected
# error occurs and the message is semantically equivalent, so we can safely
# skip this test.
# E       AssertionError: Regex pattern did not match.
# E        Regex: "Unable\\ to\\ evaluate\\ type\\ annotation\\ 'CustomType\\[int\\]'\\."
# E        Input: "type 'CustomType' is not subscriptable"
k="${k-}${k+ and }not test_invalid_forward_ref"
# This seems to be related to adaptations in the tests for pytest version 8;
# Fedora 40 still has pytest version 7. See
# https://github.com/pydantic/pydantic/issues/8674.
# E       Failed: DID NOT WARN. No warnings of type (<class
#         'pydantic.json_schema.PydanticJsonSchemaWarning'>,) were emitted.
# E       The list of emitted warnings is: [].
k="${k-}${k+ and }not test_callable_fallback_with_non_serializable_default"
%endif

# We don't build docs or care about benchmarking
ignore="${ignore-} --ignore=tests/test_docs.py"
ignore="${ignore-} --ignore=tests/benchmarks"

%pytest ${ignore-} -k "${k-}" -rs
%endif


%files -n python3-pydantic -f %{pyproject_files}
%doc CITATION.cff
%doc HISTORY.md
%doc README.md

# Note that the timezone extra has no dependencies on our platform.
%pyproject_extras_subpkg email timezone -n python3-pydantic

%files doc
%license LICENSE
%doc docs/*

%changelog
%autochangelog
