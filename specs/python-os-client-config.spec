%global pypi_name os-client-config
%global with_doc 1

%global common_desc %{expand:
The os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you do not
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named "envvars"
* If you have neither, you will get a cloud named `defaults` with base defaults}

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        %autorelease
Summary:        OpenStack Client Configuration Library
License:        Apache-2.0
URL:            https://github.com/openstack/%{pypi_name}
Source0:        %{pypi_source os_client_config}

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel


%description
%{common_desc}


%package -n python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
%package  -n python-%{pypi_name}-doc
Summary:        Documentation for OpenStack os-client-config library


%description -n python-%{pypi_name}-doc
Documentation for the os-client-config library.
%endif


%prep
%autosetup -n os_client_config-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^reno[[:space:]]*[><=]/d" \
    -e "/^coverage[[:space:]]*[><=]/d" \
     test-requirements.txt doc/requirements.txt

sed -i -e "s/'reno.sphinxext',//" doc/source/conf.py

%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e docs
%else
%pyproject_buildrequires -t
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%if 0%{?with_doc}
rm -rf doc/build/html/.{doctrees,buildinfo} doc/build/html/objects.inv
%endif

%pyproject_save_files -l os_client_config


%check
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc ChangeLog README.rst


%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html
%endif


%changelog
%autochangelog
