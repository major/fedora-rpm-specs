# oslo.config and this are in circular build dependency, switch
# to without to get past this then build again 
%bcond_with bootstrap

%global sources_gpg 1
%global sources_gpg_sign 0x30566c450e41d7c91e442dfb231f942f608ddeff
%global pypi_name oslotest


%if %{without bootstrap}
%global with_doc 1
%else
%global with_doc 0
%endif

%global common_desc OpenStack test framework and test fixtures.

Name:           python-%{pypi_name}
Version:        6.1.1
Release:        %autorelease
Summary:        OpenStack test framework

License:        Apache-2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  python3-devel

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        OpenStack test framework


BuildRequires:  pyproject-rpm-macros


%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for the OpenStack test framework

%description -n python-%{pypi_name}-doc
%{common_desc} Documentation
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{version} -S git


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
#sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i '/sphinx-build/ s/-W//' tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt


%generate_buildrequires
%if %{without bootstrap}
%pyproject_buildrequires -t -e %{default_toxenv},docs
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel

%if 0%{?with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l oslotest


%check
%if %{without bootstrap}
%tox -e %{default_toxenv}
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_bindir}/oslo_debug_helper
%doc ChangeLog

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html
%doc README.rst
%endif


%changelog
%autochangelog
