#% define pre_release rc1
%define pre_release %nil

%global bash_completion_dir %(pkg-config --variable=completionsdir bash-completion || echo /etc/bash_completion.d)

Name:            cifs-utils
Version:         7.5
Release:         %autorelease
Summary:         Utilities for mounting and managing CIFS mounts

License:         GPL-3.0-only
URL:             http://linux-cifs.samba.org/cifs-utils/

BuildRequires:  gcc
BuildRequires:  libcap-ng-devel libtalloc-devel krb5-devel keyutils-libs-devel autoconf automake libwbclient-devel pam-devel
BuildRequires:  python3-docutils
BuildRequires: make

Requires:        keyutils
Requires(post):  /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives

Recommends: %{name}-info%{?_isa} = %{version}-%{release}

Source0:         https://download.samba.org/pub/linux-cifs/cifs-utils/%{name}-%{version}.tar.bz2

%description
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains tools for mounting
shares on Linux using the SMB/CIFS protocol. The tools in this package
work in conjunction with support in the kernel to allow one to mount a
SMB/CIFS share onto a client and use it as if it were a standard Linux
file system.

%package devel
Summary:        Files needed for building plugins for cifs-utils

%description devel
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains the header file
necessary for building ID mapping plugins for cifs-utils.

%package -n pam_cifscreds
Summary:        PAM module to manage NTLM credentials in kernel keyring

%description -n pam_cifscreds
The pam_cifscreds PAM module is a tool for automatically adding
credentials (username and password) for the purpose of establishing
sessions in multiuser mounts.

When a cifs filesystem is mounted with the "multiuser" option, and does
not use krb5 authentication, it needs to be able to get the credentials
for each user from somewhere. The pam_cifscreds module can be used to
provide these credentials to the kernel automatically at login.

%prep
%autosetup -n %{name}-%{version}%{pre_release} -p1

%build
grep -F -r -l '/usr/bin/env python' | xargs --no-run-if-empty -n1 sed -i 's@/usr/bin/env python.*@%python3@g'
autoreconf -i
%configure --prefix=/usr ROOTSBINDIR=%{_sbindir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/request-key.d
install -m 644 contrib/request-key.d/cifs.idmap.conf %{buildroot}%{_sysconfdir}/request-key.d
install -m 644 contrib/request-key.d/cifs.spnego.conf %{buildroot}%{_sysconfdir}/request-key.d
install -Dpm 644 bash-completion/smbinfo %{buildroot}%{_datadir}%{bash_completion_dir}/smbinfo

%files
%doc
%license COPYING
%{_bindir}/getcifsacl
%{_bindir}/setcifsacl
%{_bindir}/cifscreds
%{_sbindir}/mount.cifs
%{_sbindir}/mount.smb3
%{_sbindir}/cifs.upcall
%{_sbindir}/cifs.idmap
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/idmapwb.so
%{_mandir}/man1/getcifsacl.*
%{_mandir}/man1/setcifsacl.*
%{_mandir}/man1/cifscreds.*
%{_mandir}/man8/cifs.upcall.*
%{_mandir}/man8/cifs.idmap.*
%{_mandir}/man8/mount.cifs.*
%{_mandir}/man8/mount.smb3.*
%{_mandir}/man8/idmapwb.*
%{_datadir}%{bash_completion_dir}/smbinfo
%dir %{_sysconfdir}/cifs-utils
%ghost %{_sysconfdir}/cifs-utils/idmap-plugin
%config(noreplace) %{_sysconfdir}/request-key.d/cifs.idmap.conf
%config(noreplace) %{_sysconfdir}/request-key.d/cifs.spnego.conf

%post
alternatives --install /etc/cifs-utils/idmap-plugin cifs-idmap-plugin %{_libdir}/%{name}/idmapwb.so 10

%preun
if [ $1 = 0 ]; then
	alternatives --remove cifs-idmap-plugin %{_libdir}/%{name}/idmapwb.so
fi

%files devel
%{_includedir}/cifsidmap.h

%files -n pam_cifscreds
%{_libdir}/security/pam_cifscreds.so
%{_mandir}/man8/pam_cifscreds.8.gz

# This subpackage also serves the purpose of avoiding a Python dependency on
# the main package: https://bugzilla.redhat.com/show_bug.cgi?id=1909288.
%package info
Summary: Additional tools for querying information about CIFS mount
Requires: %{name}%{?_isa} = %{version}-%{release}

%description info
This subpackage includes additional tools for querying information
about CIFS mount.

%files info
%{_bindir}/smb2-quota
%{_bindir}/smbinfo
%{_mandir}/man1/smb2-quota.*
%{_mandir}/man1/smbinfo.*

%changelog
%autochangelog
