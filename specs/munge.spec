%bcond_without check

Name:           munge
Version:        0.5.18
Release:        %autorelease
Summary:        Enables uid & gid authentication across a host cluster

# The libs and devel package is GPLv3+ and LGPLv3+ where as the main package is GPLv3 only.
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://dun.github.io/munge/
Source0:        https://github.com/dun/munge/releases/download/munge-%{version}/munge-%{version}.tar.xz
Source1:        https://github.com/dun/munge/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://github.com/dun.gpg
Source3:        munge.sysusers
Source4:        README.md

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel bzip2-devel openssl-devel
Requires:       munge-libs = %{version}-%{release}
Requires:       logrotate

%if %{with check}
BuildRequires:  procps-ng
BuildRequires:  util-linux
%endif


%{?systemd_requires}

%description
MUNGE (MUNGE Uid 'N' Gid Emporium) is an authentication service for creating
and validating credentials. It is designed to be highly scalable for use
in an HPC cluster environment.
It allows a process to authenticate the UID and GID of another local or
remote process within a group of hosts having common users and groups.
These hosts form a security realm that is defined by a shared cryptographic
key. Clients within this security realm can create and validate credentials
without the use of root privileges, reserved ports, or platform-specific
methods.

%package devel
Summary:        Development files for uid * gid authentication across a host cluster
Requires:       munge-libs%{?_isa} = %{version}-%{release}

%description devel
Header files for developing using MUNGE.

%package libs
Summary:        Runtime libs for uid * gid authentication across a host cluster

%description libs
Runtime libraries for using MUNGE.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N -S git
cp "%{SOURCE4}"  README-Fedora.md

%autopatch

%build
%configure  --disable-static --with-crypto-lib=openssl --runstatedir="%{_rundir}" --with-systemdunitdir="%{_unitdir}"  --with-sysconfigdir="%{_sysconfdir}/sysconfig/" --with-logrotateddir="%{_sysconfdir}/logrotate.d/"
# Get rid of some rpaths for /usr/sbin
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install

# Install extra files.
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/munge.conf

# rm unneeded files.
# Exclude .la files
rm %{buildroot}/%{_libdir}/libmunge.la


# Fix a few permissions
chmod 700 %{buildroot}%{_var}/lib/munge %{buildroot}%{_var}/log/munge
chmod 700 %{buildroot}%{_sysconfdir}/munge

# Create and empty key file and pid file to be marked as a ghost file below.
# i.e it is not actually included in the rpm, only the record
# of it is.
mkdir -p %{buildroot}%{_rundir}/munge
touch %{buildroot}%{_rundir}/munge/munged.pid

%check
%if %{with check}
%make_build check \
    LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
    root=/tmp/munge-$$ VERBOSE=t verbose=t
%endif



%preun
%systemd_preun munge.service

%post
%systemd_post munge.service

%postun
%systemd_postun_with_restart munge.service

%ldconfig_scriptlets   libs

%files
%{_bindir}/munge
%{_bindir}/remunge
%{_bindir}/unmunge
%{_sbindir}/munged
%{_sbindir}/mungekey
%{_mandir}/man1/munge.1.gz
%{_mandir}/man1/remunge.1.gz
%{_mandir}/man1/unmunge.1.gz
%{_mandir}/man7/munge.7.gz
%{_mandir}/man8/munged.8.gz
%{_mandir}/man8/mungekey.8.gz
%{_unitdir}/munge.service

%attr(0700,munge,munge) %dir  %{_var}/log/munge
%attr(0700,munge,munge) %dir  %{_var}/lib/munge
%attr(0700,munge,munge) %dir %{_sysconfdir}/munge
%attr(0755,munge,munge) %ghost %dir  /run/munge/
%attr(0644,munge,munge) %ghost /run/munge/munged.pid

%{_sysusersdir}/munge.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/munge
%config(noreplace) %{_sysconfdir}/sysconfig/munge

%license COPYING COPYING.LESSER
%doc README-Fedora.md
%doc AUTHORS
%doc JARGON NEWS QUICKSTART README
%doc doc

%files libs
%{_libdir}/libmunge.so.2
%{_libdir}/libmunge.so.2.*

%files devel
%{_includedir}/munge.h
%{_libdir}/libmunge.so
%{_libdir}/pkgconfig/munge.pc
%{_mandir}/man3/munge.3.gz
%{_mandir}/man3/munge_ctx.3.gz
%{_mandir}/man3/munge_ctx_copy.3.gz
%{_mandir}/man3/munge_ctx_create.3.gz
%{_mandir}/man3/munge_ctx_destroy.3.gz
%{_mandir}/man3/munge_ctx_get.3.gz
%{_mandir}/man3/munge_ctx_set.3.gz
%{_mandir}/man3/munge_ctx_strerror.3.gz
%{_mandir}/man3/munge_decode.3.gz
%{_mandir}/man3/munge_encode.3.gz
%{_mandir}/man3/munge_enum.3.gz
%{_mandir}/man3/munge_enum_int_to_str.3.gz
%{_mandir}/man3/munge_enum_is_valid.3.gz
%{_mandir}/man3/munge_enum_str_to_int.3.gz
%{_mandir}/man3/munge_strerror.3.gz


%changelog
%autochangelog
