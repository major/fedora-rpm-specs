%bcond tests 1

# Dependencies for some extras are not (yet?) in EPEL10
%bcond pendulum %{undefined el10}
%bcond phonenumbers %{undefined el10}
%bcond pycountry %{undefined el10}

%bcond cron 1
%bcond pymongo 1

%global forgeurl https://github.com/pydantic/pydantic-extra-types

Name:           python-pydantic-extra-types
Version:        2.11.0
%forgemeta
Release:        %autorelease
Summary:        Extra types for Pydantic

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli
%if %{with tests}
BuildRequires:  %{py3_dist dirty-equals}
BuildRequires:  %{py3_dist pytest}
# We patched this out of the “all” extra, but it is still a test dependency.
BuildRequires:  %{py3_dist pytz}
%endif

%if %{with cron} && %{with pendulum} && %{with phonenumbers} && %{with pycountry} && %{with pymongo}
%global all_extra 1
%else
%if %{with pymongo}
# This doesn’t have its own extra – it is only brought in through the “all”
# extra – but it is still required for import-checking
# pydantic_extra_types.mongo_object_id and for the test
# tests/test_mongo_object_id.py, so we depend on it manually.
BuildRequires:  %{py3_dist pymongo}
%endif
%endif

%global _description %{expand:
A place for pydantic types that probably shouldn't exist in the main pydantic
library.}
# this is here to fix vim's syntax highlighting

%description %_description


%package -n python3-pydantic-extra-types
Summary:        %{summary}

%description -n python3-pydantic-extra-types %_description


%prep
%autosetup %{forgesetupargs} -p1
# Since they will not be used, and https://pypi.org/project/tzdata/ is not
# packaged, because it "is intended to be a fallback for systems that do not
# have system time zone data installed (or don’t have it installed in a
# standard location)", we patch out the tzdata and pytz dependencies:
tomcli set pyproject.toml lists delitem --type regex --no-first \
    project.optional-dependencies.all '(tzdata|pytz)\b.*'


%generate_buildrequires
%{pyproject_buildrequires \
    %{?all_extra:-x all} \
    %{?with_phonenumbers:-x phonenumbers} \
    %{?with_pycountry:-x pycountry} \
    -x semver \
    -x python_ulid \
    %{?with_pendulum:-x pendulum} \
    %{?with_cron:-x cron} \
    }


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pydantic_extra_types


%check
%{pyproject_check_import \
    %{?!with_cron:-e pydantic_extra_types.cron} \
    %{?!with_pendulum:-e pydantic_extra_types.pendulum_dt} \
    %{?!with_phonenumbers:-e pydantic_extra_types.phone_numbers} \
    %{?!with_pycountry:-e pydantic_extra_types.country} \
    %{?!with_pycountry:-e pydantic_extra_types.currency_code} \
    %{?!with_pycountry:-e pydantic_extra_types.language_code} \
    %{?!with_pycountry:-e pydantic_extra_types.script_code} \
    %{?!with_pymongo:-e pydantic_extra_types.mongo_object_id} \
    %{nil}}

%if %{with tests}
%if %{without cron}
ignore="${ignore-} --ignore=tests/test_cron.py"
%endif
%if %{without pendulum}
ignore="${ignore-} --ignore=tests/test_pendulum_dt.py"
%endif
%if %{without phonenumbers}
ignore="${ignore-} --ignore=tests/test_phone_numbers.py"
ignore="${ignore-} --ignore=tests/test_phone_numbers_validator.py"
%endif
%if %{without pycountry}
ignore="${ignore-} --ignore=tests/test_country_code.py"
ignore="${ignore-} --ignore=tests/test_currency_code.py"
ignore="${ignore-} --ignore=tests/test_language_codes.py"
ignore="${ignore-} --ignore=tests/test_scripts.py"
%endif
%if %{without pymongo}
ignore="${ignore-} --ignore=tests/test_mongo_object_id.py"
%endif
%if %{without cron} || %{without pendulum} || %{without phonenumbers} || %{without pycountry} || %{without pymongo}
ignore="${ignore-} --ignore=tests/test_json_schema.py"
%endif

%pytest -Wdefault ${ignore-} -k "${k-}" -v
%endif


%files -n python3-pydantic-extra-types -f %{pyproject_files}
%doc README.md

%pyproject_extras_subpkg -n python3-pydantic-extra-types semver python_ulid
%if 0%{?all_extra}
%pyproject_extras_subpkg -n python3-pydantic-extra-types all
%endif
%if %{with pendulum}
%pyproject_extras_subpkg -n python3-pydantic-extra-types pendulum
%endif
%if %{with phonenumbers}
%pyproject_extras_subpkg -n python3-pydantic-extra-types phonenumbers
%endif
%if %{with pycountry}
%pyproject_extras_subpkg -n python3-pydantic-extra-types pycountry
%endif
%if %{with cron}
%pyproject_extras_subpkg -n python3-pydantic-extra-types cron
%endif


%changelog
%autochangelog
