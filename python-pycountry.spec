%global srcname pycountry

Name:           python-%{srcname}
Version:        22.3.5
Release:        %autorelease
Summary:        ISO country, subdivision, language, currency and script definitions and their translations

License:        LGPLv2
URL:            https://github.com/flyingcircusio/pycountry
Source0:        %pypi_source
# Rebased from Debian:
Patch0001:      0001-Use-system-iso-codes.patch
# With iso-codes 4.10+, the number of subdivisions and currencies changed
# the tests have asserts for exact values. Debian removed the asserts.
# Instead, we change the asserts to be approximates.
# If this proves to be too problematic in the future, we can go the Debian way.
Patch0002:      0002-Replace-exact-value-asserts-of-the-lengths-with-approximates.patch

BuildArch:      noarch

BuildRequires:  iso-codes >= 4.9
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
pycountry provides the ISO databases for the standards:
* 639-3 Languages
* 3166 Countries
* 3166-3 Deleted countries
* 3166-2 Subdivisions of countries
* 4217 Currencies
* 15924 Scripts


%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       iso-codes >= 4.9

%description -n python3-%{srcname}
pycountry provides the ISO databases for the standards:
* 639-3 Languages
* 3166 Countries
* 3166-3 Deleted countries
* 3166-2 Subdivisions of countries
* 4217 Currencies
* 15924 Scripts


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled iso-codes data
rm -rf src/%{srcname}/{databases,locales}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} --pyargs pycountry

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst HISTORY.txt
%license LICENSE.txt

%changelog
%autochangelog
