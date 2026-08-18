%global forgeurl        https://github.com/trbs/bucky
%global commit          cda507241c8898c3a1926cae18371bce84be6d2c
%global forgesetupargs  -n bucky-%{commit}

Name:           python-bucky
Version:        2.3.1
Release:        %autorelease -p
Summary:        CollectD and StatsD adapter for Graphite
%forgemeta

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{forgeurl}

Source0:        %{forgesource}
Source1:        python-bucky-example.conf
Source2:        python-bucky-supervisord-example.conf
Source3:        python-bucky.sysusers.conf
Source4:        python-bucky.tmpfiles.conf

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

%global _description\
Bucky is a small server for collecting and translating metrics for\
Graphite. It can current collect metric data from CollectD daemons\
and from StatsD clients.

%description %_description

%package -n python3-bucky
Summary: %summary
Requires:       collectd
Requires:       python3-pkg-resources
%py_provides python3-bucky

%description -n python3-bucky %_description

%prep
%forgeautosetup
install -p -m 0644 %{SOURCE2} .


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l bucky

mkdir -p %{buildroot}%{_localstatedir}/log/bucky
mkdir -p %{buildroot}%{_sysconfdir}/bucky
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bucky/bucky.conf

install -p -m 0644 -D %{SOURCE3} %{buildroot}%{_sysusersdir}/python-bucky.conf
install -p -m 0644 -D %{SOURCE4} %{buildroot}%{_tmpfilesdir}/python-bucky.conf


%check
# bucky.sentry requires raven, which is not packaged in Fedora
%pyproject_check_import -e bucky.sentry


%pre -n python3-bucky
%sysusers_create_package python-bucky %{SOURCE3}


%post -n python3-bucky
%tmpfiles_create_package python-bucky %{SOURCE4}


%files -n python3-bucky -f %{pyproject_files}
%doc THANKS README.rst python-bucky-supervisord-example.conf
%{_bindir}/bucky
%attr(-,bucky,bucky) %{_localstatedir}/log/bucky
%ghost %attr(0755,bucky,bucky) %dir %{_rundir}/bucky
%config(noreplace) %{_sysconfdir}/bucky/bucky.conf
%{_sysusersdir}/python-bucky.conf
%{_tmpfilesdir}/python-bucky.conf


%changelog
%autochangelog
