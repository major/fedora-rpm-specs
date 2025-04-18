%bcond tests 1
%global forgeurl https://github.com/pydantic/pydantic-extra-types

Name:           python-pydantic-extra-types
Version:        2.10.3
%forgemeta
Release:        %autorelease
Summary:        Extra types for Pydantic

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

# Assume zoneinfo has system tzdata
#
# Downstream patch: in the system Python installation, zoneinfo is
# guaranteed to be importable and have system time zone data available, so
# we always use it, and do not check for the tzdata PyPI package.
#
# Since they will not be used (and https://pypi.org/project/tzdata/ is not
# packaged, because it "is intended to be a fallback for systems that do not
# have system time zone data installed (or don’t have it installed in a
# standard location"), we patch out the tzdata and pytz dependencies from the
# "all" extra in %%prep.
#
# All of this works because python3-libs depends on the system tzdata package.
Patch0:         0001-Assume-zoneinfo-has-system-tzdata.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli
%if %{with tests}
BuildRequires:  %{py3_dist dirty-equals}
BuildRequires:  %{py3_dist pytest}
# We patched this out of the “all” extra, but it is still a test dependency.
BuildRequires:  %{py3_dist pytz}
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
# See notes above 0001-Assume-zoneinfo-has-system-tzdata.patch.
tomcli set pyproject.toml lists delitem --type regex --no-first \
    project.optional-dependencies.all '(tzdata|pytz)\b.*'


%generate_buildrequires
%pyproject_buildrequires -x all


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pydantic_extra_types


%check
%if %{with tests}
%pytest -Wdefault -v
%endif


%files -n python3-pydantic-extra-types -f %{pyproject_files}
%doc README.md
%license LICENSE

%pyproject_extras_subpkg -n python3-pydantic-extra-types all phonenumbers pycountry semver python_ulid pendulum


%changelog
%autochangelog
