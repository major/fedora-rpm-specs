%global         srcname  zeep
%global         desc     Zeep inspects the WSDL document and generates the corresponding\
code to use the services and types in the document. This\
provides an easy to use programmatic interface to a SOAP server.

Name:           python-%{srcname}
Version:        4.3.2
Release:        %autorelease
Summary:        A fast and modern Python SOAP client

# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            https://github.com/mvantellingen/python-zeep
Source0:        %pypi_source

BuildArch:      noarch
# Since python-aiohttp excludes s390x we have to exclude it, as well
# (because python-aioresponses requires python aiohttp)
# See also:
# https://src.fedoraproject.org/rpms/python-aiohttp/blob/67855c61bee706fcd99305d1715aad02d898cbfc/f/python-aiohttp.spec#_22
# https://fedoraproject.org/wiki/EPEL/FAQ#RHEL_8.2B_has_binaries_in_the_release.2C_but_is_missing_some_corresponding_-devel_package._How_do_I_build_a_package_that_needs_that_missing_-devel_package.3F
%if %{defined el8}
ExcludeArch:    s390x
%endif

# required for py3_build macro
BuildRequires:  python3-devel

# NB: the python dependency auto-generator is enabled by default,
#     we opt-in the build-time dependency generator, cf. below


%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

# disable linting dependencies and exact test dependencies
sed -i -e '/isort\|flake\|coverage\[toml\]\|pytest-cov/d' -e 's/\([a-z]\)[>=]\{2\}[0-9.]\+/\1/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l %{srcname}


%check
# skip tests that involve SHA1 since Fedora nowadays disables it, systemwide
PYTHONPATH=src %{__python3} -m pytest tests -v -k 'not (SHA1 or test_sign_pw or test_verify_error or (test_signature and not test_signature_binary))'


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md examples


%changelog
%autochangelog
