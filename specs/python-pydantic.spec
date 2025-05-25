%bcond tests 1

Name:           python-pydantic
Version:        2.11.5
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
# We could generate test dependencies using dependency groups, but there are so
# many unwanted dependencies that it is easier to list them manually.

# From the dev dependency group:
# coverage[toml] is for coverage analysis, therefore unwanted downstream
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist dirty-equals}
# eval-type-backport is only needed for older Pythons
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
# pytest-pretty is purely cosmetic
# pytest-examples is not packaged (and not mandatory)
# faker is only used in a benchmark, which we do not run
# pytest-benchmark is only for benchmarking
# pytest-codspeed is only for benchmarking
# pytest-run-parallel might be useful, but is not packaged
BuildRequires:  %{py3_dist packaging}
BuildRequires:  %{py3_dist jsonschema}

# From the testing-extra dependency group:
BuildRequires:  %{py3_dist cloudpickle}
# devtools is not packaged; ansi2html is used only with devtools
# sqlalchemy is "used in docs tests" that we do not run
# pytest-memray is a profiler, therefore unwanted downstream
%endif

%global _description %{expand:
Data validation and settings management using python type hinting.}

%description %{_description}


%package -n     python3-pydantic
Summary:        %{summary}
Recommends:     python3-pydantic+email

%description -n python3-pydantic %{_description}


%package        doc
Summary:        Documentation for Pydantic

%description    doc
This package includes the documentation for Pydantic in Markdown format.


%prep
%autosetup -n pydantic-%{srcversion} -p1

# Delete pytest addopts. We don't care about benchmarking or coverage.
tomcli-set pyproject.toml del 'tool.pytest.ini_options.addopts'
# Work around patched-out pytest-run-parallel plugin dependency (avoid
# "pytest.PytestUnknownMarkWarning: Unknown pytest.mark.thread_unsafe" error)
tomcli-set pyproject.toml append 'tool.pytest.ini_options.markers' \
    'thread_unsafe: mark as incompatible with patched-out pytest-run-parallel'


%generate_buildrequires
%pyproject_buildrequires -x email -x timezone


%build
%pyproject_wheel


# Docs are in MarkDown, and should be added when mkdocs is packaged.

%install
%pyproject_install
%pyproject_save_files -l pydantic


%check
%pyproject_check_import -e pydantic.mypy -e pydantic.v1.mypy
%if %{with tests}
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
