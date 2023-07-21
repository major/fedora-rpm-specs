# Upstream has lots of tests that work only in their CI.
# This will require more investigation to fix.
%bcond_with     tests

# telemetry and testsdk don't follow azure-cli's versioning scheme.
# They have their own versions in the main repository.
%global         telemetry_version   1.0.8
# testsdk follows its own versioning scheme.
%global         testsdk_version     0.3.0

%global         srcname     azure-cli
%global         forgeurl    https://github.com/Azure/azure-cli
Version:        2.50.0
%global         tag         %{srcname}-%{version}
%global         distprefix  %{nil}
%forgemeta

Name:           %{srcname}
Release:        %autorelease
Summary:        Microsoft Azure Command-Line Tools
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

# Offer azure-cli updates via dnf/rpm only.
# Avoid importing files from the local directory when running az.
# Source: https://github.com/Azure/azure-cli/pull/21261
Patch1:         az-fixes.patch

BuildArch:      noarch

%if 0%{?fedora}
# Only Fedora has antlr4 packages.
#
# Because antlr4 requires the JDK, it is not available on i686 in F37+. See:
#
# https://fedoraproject.org/wiki/Releases/37/ChangeSet#Drop_i686_builds_of_jdk8,11,17_and_latest_(18)_rpms_from_f37_onwards
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_arch_specific_runtime_and_build_time_dependencies
#
# Note that dropping i686 does not require a tracking bug due to:
#
# https://fedoraproject.org/wiki/Releases/37/ChangeSet#Encourage_Dropping_Unused_/_Leaf_Packages_on_i686
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  antlr4
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-managedservices)
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(pkginfo)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(vcrpy)
%endif

%description
Microsoft Azure Command-Line Tools

# python-azure-cli-core
%package -n python3-%{srcname}-core
Summary:        Microsoft Azure Command-Line Tools Core Module
Requires:       %{name} = %{version}-%{release}

%description -n python3-%{srcname}-core
Microsoft Azure Command-Line Tools Core Module

# python-azure-cli-telemetry
%package -n python3-%{srcname}-telemetry
Summary:        Microsoft Azure CLI Telemetry Package
Requires:       %{name} = %{version}-%{release}

%description -n python3-%{srcname}-telemetry
Microsoft Azure CLI Telemetry Package

# python-azure-cli-testsdk
%package -n python3-%{srcname}-testsdk
Summary:        Microsoft Azure CLI SDK testing tools
Requires:       %{name} = %{version}-%{release}

%description -n python3-%{srcname}-testsdk
Microsoft Azure CLI SDK testing tools


%prep
%forgeautosetup -p1

# Remove upper version boundaries on anything that isn't azure-related.
# Upstream has strict requirements on azure SDK packages, but many of the
# other requirements are set to versions too old for Fedora.
sed -i '/azure/!s/==/>=/' src/azure-cli/requirements.py3.Linux.txt
sed -i '/azure/!s/~=/>=/' src/azure-cli/setup.py
sed -i '/azure/!s/==/>=/' src/azure-cli/setup.py
sed -i '/azure/!s/~=/>=/' src/azure-cli-core/setup.py
sed -i '/azure/!s/==/>=/' src/azure-cli-core/setup.py

# Namespace packages are no longer needed after Python 3.7, but upstream
# insists on carrying them.
sed -i '/nspkg/d' src/azure-cli/requirements.py3.Linux.txt

# The requirements file has requirements set for azure-cli-{core,telemetry,testsdk}
# but we can't install those until we actually build this package.
sed -i '/azure-cli.*/d' src/azure-cli/requirements.py3.Linux.txt

# certifi's version is irrelevant since the package is empty in Fedora.
sed -i 's/certifi.=.*$/certifi/' \
    src/azure-cli/requirements.py3.Linux.txt

# Remove the unnecessary secure extra from urllib3.
sed -i 's/urllib3\[secure\]/urllib3/' src/azure-cli/setup.py

# Temporarily allow newer -core and -common versions in rawhide.
sed -i 's/^azure-core==.*$/azure-core==1.28.0/' src/azure-cli/requirements.py3.Linux.txt
sed -i 's/^azure-common==.*$/azure-common==1.1.28/' src/azure-cli/requirements.py3.Linux.txt

# Allow slightly older versions.
sed -i 's/^cryptography>=.*$/oauthlib>=37.0.2/' src/azure-cli/requirements.py3.Linux.txt
sed -i 's/^oauthlib>=.*$/oauthlib>=3.2.1/' src/azure-cli/requirements.py3.Linux.txt
sed -i 's/^packaging>=.*$/packaging>=21.3/' src/azure-cli/requirements.py3.Linux.txt
sed -i 's/^paramiko>=.*$/paramiko>=2.12.0/' src/azure-cli/requirements.py3.Linux.txt
sed -i 's/^pyOpenSSL>=.*$/pyOpenSSL>=21.0.0/' src/azure-cli/requirements.py3.Linux.txt
sed -i 's/^PyNaCl>=.*$/PyNaCl>=1.4.0/' src/azure-cli/requirements.py3.Linux.txt

# Allow an older argcomplete until we can get it updated in Fedora.
sed -i 's/argcomplete>=3.1.1/argcomplete>=2.0.0/' src/azure-cli-core/setup.py
sed -i 's/^argcomplete>=.*$/argcomplete>=2.0.0/' src/azure-cli/requirements.py3.Linux.txt

# Allow older versions for EPEL 9.
sed -i \
    -e 's/^argcomplete>=.*$/argcomplete>=1.12.0/' \
    -e 's/^cffi>=.*$/cffi>=1.12.0/' \
    -e 's/^distro>=.*$/distro>=1.5.0/' \
    -e 's/^Jinja2>=.*$/Jinja2>=2.11.3/' \
    -e 's/^jmespath>=.*$/jmespath>=0.9.4/' \
    -e 's/^MarkupSafe>=.*$/MarkupSafe>=1.1.1/' \
    -e 's/^oauthlib>=.*$/oauthlib>=3.1.1/' \
    -e 's/^packaging>=.*$/packaging>=20.9/' \
    -e 's/^psutil>=.*$/psutil>=5.8.0/' \
    -e 's/^requests\[socks\]>=.*$/requests[socks]>=2.25.1/' \
    -e 's/^six>=.*$/six>=1.15.0/' \
    -e 's/^urllib3>=.*$/urllib3>=1.26.5/' \
    -e 's/^websocket-client>=.*$/websocket-client>=1.2.3/' \
    src/azure-cli/requirements.py3.Linux.txt


%generate_buildrequires
%pyproject_buildrequires -N src/azure-cli/requirements.py3.Linux.txt


%build
%if 0%{?fedora}
# Regenerate ANTLR files in Fedora only.
pushd src/azure-cli/azure/cli/command_modules/monitor/grammar/autoscale
antlr4 -Dlanguage=Python3 AutoscaleCondition.g4
cd ../metric_alert
antlr4 -Dlanguage=Python3 MetricAlertCondition.g4
popd
%endif

PROJECTS=("azure-cli azure-cli-core azure-cli-telemetry azure-cli-testsdk")
for PROJECT in ${PROJECTS[@]}; do
    pushd src/${PROJECT}
        %pyproject_wheel
    popd
done


%install
%pyproject_install

# Remove Windows/Powershell files.
rm -f %{buildroot}%{_bindir}/az.{bat,ps1}
rm -f %{buildroot}%{_bindir}/azps.ps1

# Install the az bash completion script properly.
install -Dp %{buildroot}%{_bindir}/az.completion.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}
rm -f %{buildroot}%{_bindir}/az.completion.sh


%if %{with tests}
%check
echo -e "[pytest]\naddopts = -p no:warnings --reruns 5" > pytest.ini

# Test azure-cli-core.
# Client tests skipped due to upstream bug: https://github.com/Azure/azure-cli/issues/23014
# Parser/command tests skipped due to upstream bug: https://github.com/Azure/azure-cli/issues/23015
%pytest -n auto src/azure-cli-core \
    --ignore=src/azure-cli-core/azure/cli/core/tests/test_help.py \
    -k "not test_help_loads \
        and not test_get_mgmt_service_client \
        and not test_ext_not_in_index \
        and not test_no_exts_in_index \
        and not test_update_extension_no_updates"

# Test azure-cli-telemetry.
%pytest -n auto src/azure-cli-telemetry

# Test azure-cli and command modules.
pushd src/azure-cli/azure/cli/command_modules/

# Upstream requires that some tests are run without concurrency.
%pytest appservice/tests/latest
%pytest botservice/tests/latest
%pytest cloud/tests/latest
%pytest network/tests/latest \
    -k "not test_network_app_gateway_with_identity \
        and not test_network_virtual_appliance \
        and not test_network_security_partner_provider \
        and not test_private_endpoint_connection_service_bus"

# Concurrency is okay for the other tests.
%pytest -n auto acr/tests/latest
%pytest -n auto acs/tests/latest
%pytest -n auto advisor/tests/latest
%pytest -n auto ams/tests/latest
%pytest -n auto apim/tests/latest
%pytest -n auto appconfig/tests/latest
%pytest -n auto aro/tests/latest
%pytest -n auto backup/tests/latest
%pytest -n auto batchai/tests/latest
%pytest -n auto batch/tests/latest
%pytest -n auto billing/tests/latest
# Botservice is still in preview.
# %%pytest -n auto botservice/tests/latest
%pytest -n auto cdn/tests/latest
%pytest -n auto cognitiveservices/tests/latest
%pytest -n auto config/tests/latest
%pytest -n auto configure/tests/latest
%pytest -n auto consumption/tests/latest
%pytest -n auto container/tests/latest
%pytest -n auto cosmosdb/tests/latest
%pytest -n auto databoxedge/tests/latest
%pytest -n auto deploymentmanager/tests/latest
%pytest -n auto dla/tests/latest
%pytest -n auto dls/tests/latest
%pytest -n auto dms/tests/latest
%pytest -n auto eventgrid/tests/latest
%pytest -n auto eventhubs/tests/latest
%pytest -n auto find/tests/latest
%pytest -n auto hdinsight/tests/latest
%pytest -n auto identity/tests/latest
# test_certificate_lifecycle requires the azure-iot extension, which is not
# currently packaged.
%pytest -n auto iot/tests/latest \
    -k "test_certificate_lifecycle"
%pytest -n auto keyvault/tests/latest \
    -k "test_keyvault_hsm_key_release_policy"
%pytest -n auto kusto/tests/latest
%pytest -n auto lab/tests/latest
%pytest -n auto managedservices/tests/latest
%pytest -n auto maps/tests/latest
%pytest -n auto marketplaceordering/tests/latest
%pytest -n auto monitor/tests/latest \
    -k "not test_monitor_private_link_scope_scenario"
%pytest -n auto natgateway/tests/latest
%pytest -n auto netappfiles/tests/latest
%pytest -n auto policyinsights/tests/latest
%pytest -n auto privatedns/tests/latest
%pytest -n auto profile/tests/latest \
    -k "not test_login_validate_tenant"
%pytest -n auto rdbms/tests/latest
%pytest -n auto redis/tests/latest
%pytest -n auto relay/tests/latest
%pytest -n auto reservations/tests/latest
%pytest -n auto resource/tests/latest
%pytest -n auto role/tests/latest \
    -k "not test_create_for_rbac_create_cert"
%pytest -n auto search/tests/latest
%pytest -n auto security/tests/latest

# EPEL9 omits servicebus because it requires uamqp, which currently lacks
# OpenSSL 3.x support. 😢
# See https://github.com/Azure/azure-uamqp-python/issues/276
# See https://github.com/Azure/azure-c-shared-utility/discussions/566
%if 0%{?fedora}
%pytest -n auto servicebus/tests/latest
%endif

%pytest -n auto serviceconnector/tests/latest \
    --ignore=serviceconnector/tests/latest/test_webpp_connection_scenario.py
%pytest -n auto servicefabric/tests/latest \
    --ignore=src/azure-cli/azure/cli/command_modules/servicefabric/tests/latest/test_sf_application.py \
    -k "not test_cert_and_ext \
        and not test_create_cluster_with_separate_kv \
        and not test_update_settings_and_reliability"
%pytest -n auto signalr/tests/latest
%pytest -n auto sql/tests/latest
%pytest -n auto sqlvm/tests/latest
%pytest -n auto storage/tests/latest \
    -k "not test_storage_blob_upload_small_file"
%pytest -n auto synapse/tests/latest
%pytest -n auto util/tests/latest


popd

# The VM tests import stuff from azure.cli.command_modules.vm.tests, so the
# paths need some adjustments here.
PYTHONPATH=%{buildroot}%{python3_sitelib}:src/azure-cli/ \
    %pytest -n auto src/azure-cli/azure/cli/command_modules/vm/tests/latest

%endif


%files
%doc README.md
%license LICENSE
# Executable-related files/directories.
%{_bindir}/az
# Bash completions.
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
# Python sitelib files and directories.
%dir %{python3_sitelib}/azure
%{python3_sitelib}/azure/cli
%{python3_sitelib}/azure_cli-%{version}.dist-info/
# Prevent azure-cli from grabbing all of the files underneath azure/cli.
%exclude %{python3_sitelib}/azure/cli/core
%exclude %{python3_sitelib}/azure/cli/telemetry
%exclude %{python3_sitelib}/azure/cli/testsdk


%files -n python3-%{srcname}-core
%doc README.md
%{python3_sitelib}/azure/cli/core
%{python3_sitelib}/azure_cli_core-%{version}.dist-info/


%files -n python3-%{srcname}-testsdk
%doc README.md
%{python3_sitelib}/azure/cli/testsdk
%{python3_sitelib}/azure_cli_testsdk-%{testsdk_version}.dist-info/


%files -n python3-%{srcname}-telemetry
%doc README.md
%{python3_sitelib}/azure/cli/telemetry
%{python3_sitelib}/azure_cli_telemetry-%{telemetry_version}.dist-info/


%changelog
%autochangelog
