%global pypi_name aioresponses

Name:           python-%{pypi_name}
Version:        0.7.9
Release:        %autorelease
Summary:        Mock out requests made by ClientSession from aiohttp package

License:        MIT
URL:            https://github.com/pnuckowski/aioresponses
Source:         %{pypi_source}

BuildArch:      noarch
# Since python-aiohttp excludes s390x we have to exclude it, as well
# See also:
# https://src.fedoraproject.org/rpms/python-aiohttp/blob/67855c61bee706fcd99305d1715aad02d898cbfc/f/python-aiohttp.spec#_22
# https://fedoraproject.org/wiki/EPEL/FAQ#RHEL_8.2B_has_binaries_in_the_release.2C_but_is_missing_some_corresponding_-devel_package._How_do_I_build_a_package_that_needs_that_missing_-devel_package.3F
%if %{defined el8}
ExcludeArch:    s390x
%endif

BuildRequires:  python3-devel
# for tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(ddt)

%global common_description %{expand:
Aioresponses is a helper to mock/fake web requests in the python aiohttp
package. The purpose of this package is to provide an easy way to test
asynchronous HTTP requests.}

%description %{common_description}


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}



%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# remove linting and other superfluous build dependencies
sed -e '/flake\|tox\|coverage\|pytest-cov\|pytest-html\|Sphinx/d' requirements-dev.txt -i


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{pypi_name}


%check
# disable tests that connect to httpbin.org
%pytest -v -k 'not test_address_as_instance_of_url_combined_with_pass_through and not test_pass_through_with_origin_params and not test_pass_through_unmatched_requests'


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc ChangeLog README.rst


%changelog
%autochangelog
