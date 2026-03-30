%global with_doc 0

%global sname rsdclient
%global pyname python_rsdclient

%global _description %{expand:
This is a client for the RSD Pod Manager API, which is based on OpenStack
client framework. It provides a Python API (rsdclient/v1 module) and a RSD
specific plugin for OpenStack client (rsdclient/osc).}


Name:           python-%{sname}
Version:        1.0.2
Release:        %autorelease
Summary:        OpenStack client plugin for Rack Scale Design

License:        Apache-2.0
URL:            http://git.openstack.org/cgit/openstack/%{name}
Source0:        http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
%_description


%package -n     python3-%{sname}
Summary:        %{summary}

BuildRequires:  git-core
BuildRequires:  python3-devel


%description -n python3-%{sname}
%_description


%package -n python3-%{sname}-tests
Summary: python-rsdclient tests
Requires: python3-%{sname} = %{version}-%{release}


%description -n python3-%{sname}-tests
Tests for python-rsdclient


%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: python-rsdclient documentation


%description -n python-%{sname}-doc
Documentation for python-rsdclient
%endif


%prep
%autosetup -n %{name}-%{version} -S git

sed -i /.*-c{env:UPPER_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    test-requirements.txt

%generate_buildrequires
%pyproject_buildrequires -t


%build
%{pyproject_wheel}

%if 0%{?with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyproject_install}

%pyproject_save_files -l rsdclient

# Setup directories , not sure why these are here
install -d -m 755 %{buildroot}%{_datadir}/%{pyname}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{pyname}
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{pyname}


%check 
%pyproject_check_import rsdclient -e rsdclient.tests.*


%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%doc README.rst doc/source/readme.rst
%exclude %{python3_sitelib}/%{sname}/tests


%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests


%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif


%changelog
%autochangelog
