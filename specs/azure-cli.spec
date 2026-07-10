# The vast majority of azure-cli's tests require docker, networking, or both. 😢
%bcond_with     tests

# telemetry and testsdk don't follow azure-cli's versioning scheme.
# They have their own versions in the main repository.
%global         telemetry_version   1.1.0
# testsdk follows its own versioning scheme.
%global         testsdk_version     0.3.0

%global         srcname     azure-cli
%global         forgeurl    https://github.com/Azure/azure-cli
Version:        2.88.0
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
BuildRequires:  python3-antlr4-runtime
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
%if 0%{?fedora}
Recommends:     python3-antlr4-runtime
%endif

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
# Azure CLI *loves* to pin alpha/beta/random versions
%pyproject_patch_dependency azure-common:set_upper:2.0
%pyproject_patch_dependency azure-data-tables:set_upper:13.0
%pyproject_patch_dependency azure-keyvault-administration:set_upper:5.0
%pyproject_patch_dependency azure-keyvault-keys:set_upper:5.0
%pyproject_patch_dependency azure-mgmt-advisor:set_upper:10.0
%pyproject_patch_dependency azure-mgmt-appconfiguration:set_upper:7.0
%pyproject_patch_dependency azure-mgmt-authorization:set_upper:6.0
%pyproject_patch_dependency azure-mgmt-batchai:set_upper:8.0
%pyproject_patch_dependency azure-mgmt-cdn:set_upper:14.0
%pyproject_patch_dependency azure-mgmt-cognitiveservices:set_upper:16.0
%pyproject_patch_dependency azure-mgmt-containerservice:set_upper:42.0
%pyproject_patch_dependency azure-mgmt-datamigration:set_upper:11.0
%pyproject_patch_dependency azure-mgmt-domainregistration:set_upper:2.0
%pyproject_patch_dependency azure-mgmt-eventgrid:set_upper:11.0
%pyproject_patch_dependency azure-mgmt-extendedlocation:set_upper:2.0
%pyproject_patch_dependency azure-mgmt-hdinsight:set_upper:10.0
%pyproject_patch_dependency azure-mgmt-loganalytics:set_upper:14.0
%pyproject_patch_dependency azure-mgmt-managementgroups:set_upper:2.0
%pyproject_patch_dependency azure-mgmt-maps:set_upper:3.0
%pyproject_patch_dependency azure-mgmt-marketplaceordering:set_upper:2.0
%pyproject_patch_dependency azure-mgmt-postgresqlflexibleservers:set_upper:4.0
%pyproject_patch_dependency azure-mgmt-privatedns:set_upper:2.0
%pyproject_patch_dependency azure-mgmt-search:set_upper:10.0
%pyproject_patch_dependency azure-mgmt-servicefabricmanagedclusters:set_upper:3.0
%pyproject_patch_dependency azure-mgmt-storage:set_upper:26.0
%pyproject_patch_dependency azure-mgmt-trafficmanager:set_upper:2.0
%pyproject_patch_dependency azure-mgmt-web:set_upper:12.0
%pyproject_patch_dependency azure-monitor-query:set_upper:2.0
%pyproject_patch_dependency azure-storage-blob:set_upper:13.0
%pyproject_patch_dependency azure-storage-file-datalake:set_upper:13.0
%pyproject_patch_dependency azure-storage-file-share:set_upper:13.0
%pyproject_patch_dependency azure-storage-queue:set_upper:13.0

# Unnecessary dependencies
%pyproject_patch_dependency certifi:ignore
%pyproject_patch_dependency py-deviceid:ignore

# Non-Azure dependencies that need tweaks
%pyproject_patch_dependency paramiko:set_upper:6.0
%pyproject_patch_dependency pyjwt:set_upper:3.0

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


# Remove the unnecessary secure extra from urllib3.
sed -i 's/urllib3\[secure\]/urllib3/' src/azure-cli/setup.py

# Remove the broker extra from msal because it would require the closed-source
# pymsalruntime.
sed -i 's/msal\[broker\]/msal/' src/azure-cli/setup.py
sed -i 's/msal\[broker\]/msal/' src/azure-cli/requirements.py3.Linux.txt
sed -i 's/msal\[broker\]/msal/' src/azure-cli-core/setup.py

# Bring in the antlr4 python runtime manually to avoid a requires/provides mismatch.
sed -i '/antlr4-python3-runtime/d' src/azure-cli/requirements.py3.Linux.txt src/azure-cli/setup.py

# Allow older versions for EPEL 9.
%if %{defined el9}
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
sed -i \
    -e 's/websocket-client>=1.3.1/websocket-client>=1.2.3/' \
    src/azure-cli/setup.py
sed -i \
    -e 's/argcomplete>=3.1.1/argcomplete/' \
    -e 's/psutil>=5.9/psutil/' \
    src/azure-cli-core/setup.py
%endif


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
%pytest -n auto src/azure-cli-core
%pytest -n auto src/azure-cli-telemetry
%pytest -n auto src/azure-cli
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
