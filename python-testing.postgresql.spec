Name:           python-testing.postgresql
Version:        1.3.0
Release:        %autorelease
Summary:        Automatically sets up a PostgreSQL testing instance

License:        Apache-2.0
URL:            https://github.com/tk0miya/testing.postgresql
Source:         %{pypi_source testing.postgresql}
BuildArch:      noarch

# Backport unreleased commit 738c8eb19a4b064dd74ff851c379dd1cbf11bc65
# “Use utility methods of testing.common.database >= 1.1.0”, required
# for compatibility with testing.common.database >= 2.0.0.
Patch:          %{url}/commit/738c8eb19a4b064dd74ff851c379dd1cbf11bc65.patch

# Backport unreleased commit 577445d8ff5e0ea89ccaf09fd5b82165a0875afe
# “Add CentOS/RHEL postgesql home directory blob to search patterns.”
Patch:          %{url}/commit/577445d8ff5e0ea89ccaf09fd5b82165a0875afe.patch

# Replace assertRegexpMatches() with assertRegex()
# https://github.com/tk0miya/testing.postgresql/pull/44
Patch:          %{url}/pull/44.patch

BuildRequires:  python3-devel
BuildRequires:  postgresql-server

%global common_description %{expand:
Automatically sets up a PostgreSQL instance in a temporary directory, and
destroys it after testing.}

%description %{common_description}


%package -n     python3-testing.postgresql
Summary:        %{summary}

Requires:       postgresql-server

%description -n python3-testing.postgresql %{common_description}


%prep
%autosetup -n testing.postgresql-%{version} -p1
# Do not generate a BR on deprecated python3dist(nose); use pytest instead
sed -r -i "s/'nose'/'pytest'/" setup.py


%generate_buildrequires
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l testing


%check
%pytest


%files -n python3-testing.postgresql -f %{pyproject_files}
%doc README.rst

# The directory %%{python3_sitelib}/testing is a namespace package directory;
# we do not need to (co-)own it because it is owned by dependency
# python3dist(testing.common.database). (Co-owning it would not be harmful.)
%exclude %dir %{python3_sitelib}/testing
%{python3_sitelib}/testing.postgresql-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
