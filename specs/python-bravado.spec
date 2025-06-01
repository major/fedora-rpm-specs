Name:           python-bravado
Version:        12.0.1
Release:        %autorelease
Summary:        Library for accessing Swagger-enabled API's

License:        BSD-3-Clause
URL:            https://github.com/Yelp/bravado
# PyPI tarball is missing tests
Source:         %{url}/archive/v%{version}/bravado-%{version}.tar.gz
# https://github.com/Yelp/bravado/pull/484
Patch:          0001-Use-standard-library-mock-when-possible.patch
# https://github.com/Yelp/bravado/pull/498
Patch:          0002-Drop-monotonic-dependency.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-httpretty

%global _description %{expand:
Bravado is a Yelp maintained fork of digium/swagger-py for use with OpenAPI
Specification version 2.0 (previously known as Swagger).}


%description %_description


%package -n     python3-bravado
Summary:        %{summary}


%description -n python3-bravado %_description


%prep
%autosetup -n bravado-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires -x integration-tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l bravado


%check
# Fido tests require fido, which is deprecated upstream and won't be packaged
%pytest -v \
    --ignore tests/fido_client \
    --ignore tests/integration/fido_client_test.py \
    tests


%files -n python3-bravado -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
