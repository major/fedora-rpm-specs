%global pypi_name rtslib_fb
%global upstream_name rtslib-fb

# epydoc is gone, so disable for now
%bcond_with apidocs

Name:             python-rtslib
License:          Apache-2.0
Summary:          API for Linux kernel LIO SCSI target
Version:          2.2.3
Release:          %autorelease
URL:              https://github.com/open-iscsi/%{upstream_name}
Source:           %{pypi_source %{pypi_name}}
Patch0:           0001-disable-xen_pvscsi.patch
BuildArch:        noarch
%if %{with apidocs}
BuildRequires:    epydoc
%endif
BuildRequires:    systemd


%global _description\
API for generic Linux SCSI kernel target. Includes the 'target'\
service and targetctl tool for restoring configuration.

%description %_description


%if %{with apidocs}
%package doc
Summary:        Documentation for python-rtslib
Requires:       python3-rtslib = %{version}-%{release}

%description doc
API documentation for rtslib, to configure the generic Linux SCSI
multiprotocol kernel target.
%endif

%package -n python3-rtslib
Summary:        API for Linux kernel LIO SCSI target

BuildRequires:  python3-devel
# Optional dependency, not declared in pyproject.toml
BuildRequires:  python3-kmod

Requires:       python3-kmod
%if ! %{with apidocs}
Obsoletes:      %{name}-doc < %{version}-%{release}
%endif

%description -n python3-rtslib
API for generic Linux SCSI kernel target.


%package -n target-restore
Summary:          Systemd service for targetcli/rtslib
Requires:         python3-rtslib = %{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description -n target-restore
Systemd service to restore the LIO kernel target settings
on system restart.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with apidocs}
mkdir -p doc/html
epydoc --no-sourcecode --html -n rtslib -o doc/html rtslib/*.py
%endif

%install
%pyproject_install
%pyproject_save_files -l 'rtslib*'

mkdir -p %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/target/backup
mkdir -p %{buildroot}%{_localstatedir}/target/pr
mkdir -p %{buildroot}%{_localstatedir}/target/alua
install -m 644 systemd/target.service %{buildroot}%{_unitdir}/target.service
install -m 644 doc/targetctl.8 %{buildroot}%{_mandir}/man8/
install -m 644 doc/saveconfig.json.5 %{buildroot}%{_mandir}/man5/

%check
%pyproject_check_import

%post -n target-restore
%systemd_post target.service

%preun -n target-restore
%systemd_preun target.service

%postun -n target-restore
%systemd_postun_with_restart target.service


%files -n python3-rtslib -f %{pyproject_files}
%doc README.md doc/getting_started.md

%files -n target-restore
%{_bindir}/targetctl
%{_unitdir}/target.service
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup
%dir %{_localstatedir}/target
%dir %{_localstatedir}/target/pr
%dir %{_localstatedir}/target/alua
%{_mandir}/man8/targetctl.8*
%{_mandir}/man5/saveconfig.json.5*

%if %{with apidocs}
%files doc
%doc doc/html
%endif

%changelog
%autochangelog
