Name:           linode-cli
Version:        5.23.0
Release:        %autorelease
Summary:        Official command-line interface to the Linode platform

License:        BSD
URL:            https://github.com/linode/linode-cli/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Downloaded from https://www.linode.com/docs/api/openapi.yaml
Source1:        openapi.yaml
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Linode CLI is a simple command-line interface to the Linode platform.

%prep
%autosetup
cp -p %SOURCE1 .
# harcode version as script requires connection
sed -i setup.py -e "s/version=get_version()/version='%{version}'/"

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files linodecli
# generate bash-completion
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{buildroot}%{_bindir}/linode-cli bake openapi.yaml --skip-config

# Bash completion
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv linode-cli.sh %{buildroot}%{_datadir}/bash-completion/completions/linode-cli
# baked data
mv data-3 %{buildroot}/%{python3_sitelib}/linodecli/

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/linode-cli
%{_datadir}/bash-completion/
%{python3_sitelib}/linodecli/data-3

%changelog
%autochangelog
