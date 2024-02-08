%global srcname pycountry

Name:           python-%{srcname}
Version:        23.12.7
Release:        %autorelease
Summary:        ISO country, subdivision, language, currency and script definitions and their translations

License:        LGPL-2.1-only
URL:            https://github.com/pycountry/pycountry
Source:         %{pypi_source %{srcname}}
# Rebased from Debian by Elliott Sales de Andrade, then rebased again on
# 23.12.7 by Benjamin A. Beasley.
Patch:          0001-Use-system-iso-codes.patch
# With iso-codes 4.10+, the number of subdivisions and currencies changed
# the tests have asserts for exact values. Debian removed the asserts.
# Instead, we change the asserts to be approximates.
# If this proves to be too problematic in the future, we can go the Debian way.
#
# Rebased on 23.12.7 by Benjamin A. Beasley. While the same assertions are
# made approximate as before, as of this writing only
# test_subdivisions_directly_accessible would actually fail without this patch.
Patch:          0002-Replace-exact-value-asserts-of-the-lengths-of-some-d.patch
# Fix compatibility with iso-codes 4.16.0 by backporting commit
# 933164633e53b325905e71d9a4e365fe1ada8162,
# "Fix subdivision parent issue in #17 and #186 (#187)"
# Rebased on 23.12.7 and on the preceding two patches, without changes to
# HISTORY.txt since that file is no longer included in the PyPI sdist.
Patch:          0003-Fix-subdivision-parent-issue-in-17-and-186-187.patch

BuildArch:      noarch

BuildRequires:  iso-codes >= 4.15
BuildRequires:  python3-devel
# See [tool.poetry.dev-dependencies] in pyproject.toml.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(importlib-metadata)

%global _description %{expand:
pycountry provides the ISO databases for the standards:
* 639-3 Languages
* 3166 Countries
* 3166-3 Deleted countries
* 3166-2 Subdivisions of countries
* 4217 Currencies
* 15924 Scripts}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       iso-codes >= 4.15

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled iso-codes data
rm -rf src/%{srcname}/{databases,locales}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} --pyargs pycountry

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
