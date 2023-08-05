%bcond_without     tests

Name:           efs-utils
Version:        1.35.0
Release:        %autorelease
Summary:        Utilities for Amazon Elastic File System (EFS)

License:        MIT
URL:            https://github.com/aws/efs-utils
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       nfs-utils
Requires:       openssl
Requires:       stunnel
Requires:       util-linux
Requires:       which
Requires:       python3dist(botocore)

BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

%if %{with tests}
BuildRequires:  python3dist(botocore)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
%endif

%global _description %{expand:
Utilities for Amazon Elastic File System (EFS).}

%description %{_description}


%prep
%autosetup -n %{name}-%{version}

# Use unittest.mock for testing.
sed -i 's/from mock/from unittest.mock/' test/common.py


%build
echo "Nothing to build"


%install
# Watchdog service unit file.
install -m 0755 -vd %{buildroot}%{_unitdir}
install -vp -m 644 dist/amazon-efs-mount-watchdog.service %{buildroot}%{_unitdir}/

# Watchdog service itself.
install -m 0755 -vd %{buildroot}%{_bindir}
install -vp -m 755 src/watchdog/__init__.py %{buildroot}%{_bindir}/amazon-efs-mount-watchdog

# Configuration files and Amazon root certificates.
install -m 0755 -vd %{buildroot}%{_sysconfdir}/amazon/efs/
install -vp -m 644 dist/efs-utils.conf %{buildroot}%{_sysconfdir}/amazon/efs/
install -vp -m 444 dist/efs-utils.crt %{buildroot}%{_sysconfdir}/amazon/efs/

# mount.efs script allows mounting EFS file systems by their short name.
install -m 0755 -vd %{buildroot}%{_sbindir}
install -vp -m 755 src/mount_efs/__init__.py %{buildroot}%{_sbindir}/mount.efs

# Man page.
install -m 0755 -vd %{buildroot}%{_mandir}/man8/
install -vp -m 644 man/mount.efs.8 %{buildroot}%{_mandir}/man8/

# Log directory.
install -m 0755 -vd %{buildroot}%{_localstatedir}/log/amazon/efs


%if %{with tests}
%check
# Avoid running tests with coverage enabled.
touch pytest.ini

# Ignore some tests that require networking and get stuck forever.
PYTHONPATH=$(pwd)/src %pytest \
    --ignore test/mount_efs_test/test_main.py \
    --ignore test/mount_efs_test/test_bootstrap_tls.py \
    --ignore test/mount_efs_test/test_create_self_signed_cert.py \
    --ignore test/watchdog_test/test_refresh_self_signed_certificate.py
%endif


%files -n %{name}
%license LICENSE
%doc CONTRIBUTING.md README.md
%dir /var/log/amazon
%dir %{_sysconfdir}/amazon
%dir %{_sysconfdir}/amazon/efs
%config(noreplace) %{_sysconfdir}/amazon/efs/efs-utils.conf
%{_unitdir}/amazon-efs-mount-watchdog.service
%{_sysconfdir}/amazon/efs/efs-utils.crt
%{_sbindir}/mount.efs
%{_bindir}/amazon-efs-mount-watchdog
%{_mandir}/man8/mount.efs.8*

%post
%systemd_post amazon-efs-mount-watchdog.service

%preun
%systemd_preun amazon-efs-mount-watchdog.service

%postun
%systemd_postun_with_restart amazon-efs-mount-watchdog.service


%changelog
%autochangelog
