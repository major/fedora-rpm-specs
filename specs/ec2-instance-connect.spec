%global project aws-ec2-instance-connect-config
%global modulename ec2-instance-connect
%global selinuxtype targeted

Name:           ec2-instance-connect
Summary:        EC2 Instance Connect scripts
Version:        1.1.17
Release:        3%{?dist}

License:        Apache-2.0
URL:            https://github.com/aws/%{project}
Source0:        https://github.com/aws/%{project}/archive/%{version}/%{project}-%{version}.tar.gz
# SELinux Policy
Source1:        %{modulename}.te
Source2:        %{modulename}.if
Source3:        %{modulename}.fc
# User definition
Source4:        %{modulename}.sysusers
# Systemd drop-in file
Source5:        %{modulename}.conf

# Mentioned as v1.1.18 fix in upstream .spec but never released. Backport till upstream releases >1.1.17
Patch1:         0001-Update-curl-command-to-not-fail-silently-on-HTTP-ser.patch

BuildArch:      noarch

BuildRequires:  systemd-rpm-macros
%{?sysusers_requires_compat}

Requires:       openssh >= 6.9.0
Requires:       coreutils
Requires:       openssh-server >= 6.9.0
Requires:       openssl
Requires:       curl
Requires:       systemd

Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
Recommends:     %{name}-config

%description
This package contains the EC2 instance configuration and 
scripts necessary to enable AWS EC2 Instance Connect.


# SELinux subpackage
%package selinux
Summary:        ec2-instance-connect SELinux policy
BuildArch:      noarch
Requires:       selinux-policy-%{selinuxtype}
Requires:       ec2-instance-connect
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description selinux
Custom SELinux policy module for ec2-instance-connect


# Configuration subpackage
%package config
Summary:        ec2-instance-connect configuration
BuildArch:      noarch
Requires:       ec2-instance-connect
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description config
Systemd drop-in for sshd.service to set ec2-instance-connect 
specific AuthorizedKeysCommand and AuthorizedKeysCommandUser


%prep
%autosetup -p1 -n %{project}-%{version}


%build
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module
mkdir selinux
cp -p %{SOURCE1} selinux/
cp -p %{SOURCE2} selinux/
cp -p %{SOURCE3} selinux/

make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp


%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 "%{_builddir}/%{project}-%{version}/src/bin/eic_run_authorized_keys" %{buildroot}/%{_bindir}
install -p -m 755 "%{_builddir}/%{project}-%{version}/src/bin/eic_curl_authorized_keys" %{buildroot}/%{_bindir}
install -p -m 755 "%{_builddir}/%{project}-%{version}/src/bin/eic_parse_authorized_keys" %{buildroot}/%{_bindir}

install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{modulename}.if

install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{modulename}.conf

install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/sshd.service.d/%{modulename}.conf


# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}


%post config
%systemd_post sshd.service

%preun config
%systemd_preun sshd.service

%postun config
%systemd_postun_with_restart sshd.service


%files config
%{_unitdir}/sshd.service.d/%{modulename}.conf


%files
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%license LICENSE NOTICE

%attr(0755,root,root) %{_bindir}/eic_run_authorized_keys
%attr(0755,root,root) %{_bindir}/eic_curl_authorized_keys
%attr(0755,root,root) %{_bindir}/eic_parse_authorized_keys

%{_sysusersdir}/%{modulename}.conf


%pre
%sysusers_create_compat %{SOURCE4}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 03 2024 Dominik Wombacher <dominik@wombacher.cc> 1.1.17-1
- Initial package
- Fix: Update curl command to not fail silently on HTTP server error.
