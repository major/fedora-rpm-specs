Name:           python-asyncmy
Summary:        A fast asyncio MySQL/MariaDB driver
Version:        0.2.9
Release:        %autorelease

License:        Apache-2.0
URL:            https://github.com/long2ice/asyncmy
# The GitHub source includes tests and examples; the PyPI source lacks them.
Source:         %{url}/archive/v%{version}/asyncmy-%{version}.tar.gz

# Doc/license files installed directly in site-packages
# https://github.com/long2ice/asyncmy/issues/33
Patch:          0001-Do-not-install-text-files-in-site-packages.patch

# Test failures and errors on 32-bit platforms
# https://github.com/long2ice/asyncmy/issues/34
# https://bugzilla.redhat.com/show_bug.cgi?id=2060899
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  python3-devel

%global common_description %{expand:
asyncmy is a fast asyncio MySQL/MariaDB driver, which reuses most of pymysql
and aiomysql but rewrites the core protocol with Cython to speed it up.}

%description %{common_description}


%package -n     python3-asyncmy
Summary:        %{summary}

%description -n python3-asyncmy %{common_description}


%prep
%autosetup -n asyncmy-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files asyncmy

# Do not distribute Cython-generated C source files; these are not useful
find '%{buildroot}%{python3_sitearch}/asyncmy' \
    -type f -name '*.c' -print -delete
sed -r -i '/\.c$/d' '%{pyproject_files}'


%check
# Tests require interacting with a temporary MySQL/mariadb database. Setting
# this up has become impractical.
%pyproject_check_import


%files -n python3-asyncmy -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
