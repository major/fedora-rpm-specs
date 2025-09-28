%global pypi_name aioresponses

Name:           python-%{pypi_name}
Version:        0.7.8
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
BuildRequires:  python3dist(ddt)

%global common_description %{expand:
Aioresponses is a helper to mock/fake web requests in the python aiohttp
package. The purpose of this package is to provide an easy way to test
asynchronous HTTP requests.}

%description %{common_description}


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}


%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        BSD-2-Clause AND MIT
BuildArch:      noarch
BuildRequires:  python3dist(sphinx)
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/ html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install

%pyproject_save_files %{pypi_name}


%check
# disable tests that connect to httpbin.org
%pytest -v -k 'not test_address_as_instance_of_url_combined_with_pass_through and not test_pass_through_with_origin_params and not test_pass_through_unmatched_requests'


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc ChangeLog README.rst


%files -n python-%{pypi_name}-doc
%doc html


%changelog
%autochangelog
