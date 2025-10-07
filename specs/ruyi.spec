Name:           ruyi
Version:        0.41.0
Release:        %autorelease
Summary:        RuyiSDK Package Manager

License:        Apache-2.0
URL:            https://github.com/ruyisdk/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Configuration file to disable telemetry by default
# https://github.com/ruyisdk/ruyi/blob/main/README.md
Source1:        config.toml

BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  libgit2-devel
BuildRequires:  python3-devel
BuildRequires:  pytest

%description
The package manager for RuyiSDK.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

# Generate documentation by help2man
export RUYI_TELEMETRY_OPTOUT=1
export RUYI_FORCE_ALLOW_ROOT=1
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}/%{python3_sitelib} help2man --version-string=%{version} \
  -o %{buildroot}%{_mandir}/man1/ruyi.1 %{buildroot}%{_bindir}/ruyi

# Install config file with telemetry disabled
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/config.toml

%check
%pytest

%files -f %{pyproject_files}
%doc README.md
%license LICENSE-Apache.txt
%{_bindir}/ruyi
%{_mandir}/man1/ruyi.1*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/config.toml

%changelog
%autochangelog
