Name:           python-hiredis
Version:        2.3.2
Release:        %autorelease
Summary:        Python wrapper for hiredis

License:        BSD-2-Clause
URL:            https://github.com/redis/hiredis-py
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
# Drop vendor sources for hiredis and use the system one.
# Upstream issues (reported by OpenSUSE package mainteners):
# - https://github.com/redis/hiredis-py/issues/158
# - https://github.com/redis/hiredis-py/pull/159
# - https://github.com/redis/hiredis-py/pull/161
Patch0:         use-system-hiredis.patch

BuildRequires: python3-devel
BuildRequires: hiredis-devel
BuildRequires: gcc
BuildRequires: python3dist(pytest)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Python extension that wraps protocol parsing code in hiredis.
It primarily speeds up parsing of multi bulk replies.}

%description %_description

%package -n     python3-hiredis
Summary:        %{summary}

%description -n python3-hiredis %_description


%prep
%autosetup -p1 -n hiredis-py-%{version}
# Use system hiredis
rm -r vendor/hiredis

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files hiredis


%check
%pyproject_check_import
%pytest --import-mode append


%files -n python3-hiredis -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
