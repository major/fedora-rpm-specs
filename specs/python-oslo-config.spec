# There is a cirucular dependency on oslo.log at least for the tests
# Change to "without" for boot strap mode.
%bcond_with bootstrap

%global sources_gpg 1
%global sources_gpg_sign 0xb8e9315f48553ec5aff9ffe5e69d97da9efb5aff
%global sname oslo.config
%global pypi_name oslo-config
# doc and tests are enabled by default unless %%repo_bootstrap
%bcond doc %[!0%{?with_bootstrap}]
%bcond tests %[!0%{?with_bootstrap}]


Name:       python-oslo-config
Epoch:      2
Version:    10.3.0
Release:    %autorelease
Summary:    OpenStack common configuration library

Group:      Development/Languages
License:    Apache-2.0
URL:        https://launchpad.net/%{sname}
Source0:    https://tarballs.openstack.org/%{sname}/oslo_config-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{sname}/oslo_config-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%global _description %{expand:
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.}

%description
%_description

%package -n python3-%{pypi_name}
Summary:    OpenStack common configuration library

BuildRequires: python3-devel
BuildRequires: git-core

%description -n python3-%{pypi_name}
%_description


%if %{with doc}
%package -n python-%{pypi_name}-doc
Summary:    Documentation for OpenStack common configuration library


%description -n python-%{pypi_name}-doc
Documentation for the oslo-config library.
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n oslo_config-%{version} -S git
# Remove shebang from non executable file, it's used by the oslo-config-validator binary.
sed -i '/\/usr\/bin\/env/d' oslo_config/validator.py

# Remove tests requiring sphinx if sphinx is not available
%if %{with doc} == 0
rm oslo_config/tests/test_sphinxext.py
rm oslo_config/tests/test_sphinxconfiggen.py
%endif

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini


sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^doc8[[:space:]]*[!><=]/d" \
    test-requirements.txt doc/requirements.txt


%generate_buildrequires
%pyproject_buildrequires %{?with_doc:-e docs} %{?with_tests:-e %{default_toxenv}}


%build
%pyproject_wheel


%if %{with doc}
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l oslo_config

pushd %{buildroot}/%{_bindir}
for i in generator validator
do
ln -s oslo-config-$i oslo-config-$i-3
done
popd


%check
%if %{with tests}
# Re-enable when updated in a coordinated manner.
%tox -e %{default_toxenv}
%else
%pyproject_check_import oslo_config -e oslo_config.fixture -e oslo_config.sphinxconfiggen -e oslo_config.sphinxext -e oslo_config.tests.*
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/oslo-config-generator
%{_bindir}/oslo-config-generator-3
%{_bindir}/oslo-config-validator
%{_bindir}/oslo-config-validator-3


%if %{with doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
