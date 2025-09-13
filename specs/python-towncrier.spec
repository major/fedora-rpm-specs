%global srcname towncrier

%global common_description %{expand:
Towncrier is a utility to produce useful, summarized news files (also known as
changelogs) for your project.

Rather than reading the Git history, or having one single file which developers
all write to and produce merge conflicts, towncrier reads “news fragments” which
contain information useful to end users.}

Name:           python-%{srcname}
Version:        25.8.0
%global plain_version %{lua:
    local plain_version = (string.gsub(macros.version, '^([^%^~]+)[%^~]+.*$', '%1'))
    if plain_version ~= macros.version then
        macros.prepostver = (string.gsub(macros.version, '^[^%^~]+[%^~]+([^%^~]+).*$', '%1'))
    end
    print(plain_version)
}
%global archive_version %{plain_version}%{?prepostver}

Release:        %autorelease
Summary:        Produce useful, summarized news files for your project

License:        MIT
URL:            https://github.com/twisted/towncrier
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-twisted
BuildRequires:  git-core
BuildRequires:  mercurial

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Provides:       %{srcname} = %{version}-%{release}

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{archive_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
test_targets=towncrier
if [ "$(%python3 -c 'import click; print(click.__version__)')" == "8.2.2" ]; then
# Version 8.2.2 of click breaks some tests, skip them.
test_targets="$(cd src && find towncrier/test -name test\*.py | grep -Fv test_create | sed 's|\.py$||g; s|/|.|g')"
fi
%{py3_test_envvars} %{_bindir}/trial $test_targets

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/towncrier

%changelog
%autochangelog
