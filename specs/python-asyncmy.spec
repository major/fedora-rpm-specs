%if !0%{?fedora}%{?rhel} || 0%{?fedora} >= 43 || 0%{?rhel} >= 11
%bcond old_poetry 0
%else
%bcond old_poetry 1
%endif

Name:           python-asyncmy
Summary:        A fast asyncio MySQL/MariaDB driver
Version:        0.2.11
Release:        %autorelease

License:        Apache-2.0
URL:            https://github.com/long2ice/asyncmy
# The GitHub source includes tests and examples; the PyPI source lacks them.
Source:         %{url}/archive/v%{version}/asyncmy-%{version}.tar.gz

# Doc/license files installed directly in site-packages
# https://github.com/long2ice/asyncmy/issues/33
Patch0:         python-asyncmy-0.2.11-text-files-in-sdist.patch

# Old poetry needs the basic entries replicated in tools.poetry
Patch1:         python-asyncmy-0.2.11-old-poetry.patch

BuildSystem:            pyproject
BuildOption(install):   -L asyncmy

# Test failures and errors on 32-bit platforms
# https://github.com/long2ice/asyncmy/issues/34
# https://bugzilla.redhat.com/show_bug.cgi?id=2060899
ExcludeArch:    %{ix86}

BuildRequires:  gcc

%global common_description %{expand:
asyncmy is a fast asyncio MySQL/MariaDB driver, which reuses most of pymysql
and aiomysql but rewrites the core protocol with Cython to speed it up.}

%description %{common_description}


%package -n     python3-asyncmy
Summary:        %{summary}

%description -n python3-asyncmy %{common_description}


%prep
%autosetup -C -N
%patch 0 -p1 -b .text-files-in-sdist
%if %{with old_poetry}
%patch 1 -p1 -b .old-poetry
%endif


%install -a
# Do not distribute Cython-generated C source files; these are not useful
find '%{buildroot}%{python3_sitearch}/asyncmy' \
    -type f -name '*.c' -print -delete
sed -r -i '/\.c$/d' '%{pyproject_files}'


# Tests require interacting with a temporary MySQL/mariadb database. Setting
# this up has become impractical.


%files -n python3-asyncmy -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
