%global pypi_name os-service-types
%global module_name os_service_types

%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff
%global sources_gpg 1

%global excluded_brs hacking coverage reno

%global common_desc %{expand:
OsServiceTypes is a Python library for consuming OpenStack
service-types-authority data. The OpenStack Service Types
Authority contains information about official OpenStack services and
their historical service-type aliases.

The data is in JSON and the latest data should always be used. This simple
library exists to allow for easy consumption of the data, along with a built-in
version of the data to use in case network access is for some reason not
possible and local caching of the fetched data.}

%global with_doc 1

Name:           python-os-service-types
Version:        1.8.2
Release:        %autorelease
Summary:        Python library for consuming OpenStack service-types-authority data

License:        Apache-2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/os-service-types/%{module_name}-%{version}.tar.gz
Source1:        https://tarballs.openstack.org/os-service-types/%{module_name}-%{version}.tar.gz.asc
Source2:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt

BuildArch:      noarch
BuildRequires:  git-core
%if 0%{?sources_gpg} == 1
BuildRequires:    /usr/bin/gpgv2
%endif


%description
%{common_desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        %{pypi_name} documentation
Requires:       python-%{pypi_name} = %{version}-%{release}


%description -n python-%{pypi_name}-doc
%{common_desc}

Documentation for %{pypi_name}
%endif


%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%endif
%autosetup -n %{module_name}-%{version} -S git

# Ignore global openstack constraints
sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini

for br in %{excluded_brs}; do
  sed -i \
      -e "/^${br}[[:space:]]*[><=]/d" \
      test-requirements.txt requirements.txt doc/requirements.txt
done


%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e %{default_toxenv},docs
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%if 0%{?with_doc}
sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l %{module_name}


%check
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc ChangeLog README.rst doc/source/readme.rst


%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%endif


%changelog
%autochangelog
