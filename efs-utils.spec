%bcond_without tests
%global with_selinux 1
%global selinuxtype targeted
%global modulename efsutils
%global watchdog_service_name amazon-efs-mount-watchdog

Name:           efs-utils
Version:        1.35.0
Release:        %autorelease
Summary:        Utilities for Amazon Elastic File System (EFS)

License:        MIT
URL:            https://github.com/aws/efs-utils
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Source1:        efsutils.te
Source2:        efsutils.if
Source3:        efsutils.fc
Source4:        efsutils_selinux.8

# Patch a deprecation warning to avoid having it fill the logs.
# https://github.com/aws/efs-utils/pull/189
Patch:          fix-deprecation-warning.patch

BuildArch:      noarch

Requires:       nfs-utils
Requires:       openssl
Requires:       stunnel
Requires:       util-linux
Requires:       which
Requires:       python3dist(botocore)

%if 0%{?with_selinux}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif

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

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:             %{name} SELinux policy
Requires:            %{name} = %{version}-%{release}
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}

%description selinux
Custom %{name} SELinux policy module
%endif

%prep
%autosetup -n %{name}-%{version} -p1

# Use unittest.mock for testing.
sed -i 's/from mock/from unittest.mock/' test/common.py

%build
echo "Nothing to build"

%if 0%{?with_selinux}
mkdir selinux
cp -p %{SOURCE1} selinux/
cp -p %{SOURCE2} selinux/
cp -p %{SOURCE3} selinux/
cp -p %{SOURCE4} selinux/

%make_build -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif


%install
# Watchdog service unit file.
install -m 0755 -vd %{buildroot}%{_unitdir}
install -vp -m 644 dist/%{watchdog_service_name}.service %{buildroot}%{_unitdir}/

# Watchdog service itself.
install -m 0755 -vd %{buildroot}%{_bindir}
install -vp -m 755 src/watchdog/__init__.py %{buildroot}%{_bindir}/amazon-efs-mount-watchdog

# Configuration files and Amazon root certificates.
install -m 0755 -vd %{buildroot}%{_sysconfdir}/amazon/efs/
install -vp -m 644 dist/%{name}.conf %{buildroot}%{_sysconfdir}/amazon/efs/
install -vp -m 444 dist/%{name}.crt %{buildroot}%{_sysconfdir}/amazon/efs/

# mount.efs script allows mounting EFS file systems by their short name.
install -m 0755 -vd %{buildroot}%{_sbindir}
install -vp -m 755 src/mount_efs/__init__.py %{buildroot}%{_sbindir}/mount.efs

# Man page.
install -m 0755 -vd %{buildroot}%{_mandir}/man8/
install -vp -m 644 man/mount.efs.8 %{buildroot}%{_mandir}/man8/

# Log directory.
install -m 0755 -vd %{buildroot}%{_localstatedir}/log/amazon/efs

%if 0%{?with_selinux}
install -D -m 0644 -t %{buildroot}%{_mandir}/man8 selinux/%{modulename}_selinux.8
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%endif


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


########################################################################################
#
# BEGIN SELINUX PRE/POST
#
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%if 0%{?with_selinux}
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
   %systemd_postun_with_restart %{watchdog_service_name}.service
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
    %systemd_postun_with_restart %{watchdog_service_name}.service
fi
%endif
########################################################################################


%files -n %{name}
%license LICENSE
%doc CONTRIBUTING.md README.md
%dir /var/log/amazon/efs
%dir %{_sysconfdir}/amazon
%dir %{_sysconfdir}/amazon/efs
%config(noreplace) %{_sysconfdir}/amazon/efs/efs-utils.conf
%{_unitdir}/%{watchdog_service_name}.service
%{_sysconfdir}/amazon/efs/efs-utils.crt
%{_sbindir}/mount.efs
%{_bindir}/amazon-efs-mount-watchdog
%{_mandir}/man8/mount.efs.8*


%if 0%{?with_selinux}
%files selinux
%{_mandir}/man8/%{modulename}_selinux.8.*
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif


%post
%systemd_post %{watchdog_service_name}.service

%preun
%systemd_preun %{watchdog_service_name}.service

%postun
%systemd_postun_with_restart %{watchdog_service_name}.service

%changelog
%autochangelog
