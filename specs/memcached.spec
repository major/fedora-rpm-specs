%define username   memcached
%define groupname  memcached
%bcond_without sasl
%bcond_with seccomp
%bcond_without tls
%bcond_with tests
%global selinuxtype	targeted
%global selinuxmoduletype	contrib
%global selinuxmodulename	memcached
%global selinuxmodulever	1.0.3
%global selinuxmoduledir	%{selinuxmodulename}-selinux-%{selinuxmodulever}

Name:           memcached
Version:        1.6.39
Release:        %autorelease
Epoch:          0
Summary:        High Performance, Distributed Memory Object Cache

License:        BSD-3-clause AND Zlib AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://www.memcached.org/
Source0:        https://www.memcached.org/files/%{name}-%{version}.tar.gz
Source1:        memcached.sysconfig
# SELinux policy sources: https://pagure.io/memcached-selinux/tree/master
Source2:        https://pagure.io/memcached-selinux/blob/master/f/memcached-selinux-1.0.3.tar.gz
Source3:	memcached.conf

Patch1:         memcached-unit.patch

BuildRequires:  make
BuildRequires:  gcc libevent-devel systemd
BuildRequires:  perl-generators
BuildRequires:  perl(Test::More), perl(Test::Harness)
%{?with_sasl:BuildRequires: cyrus-sasl-devel}
%{?with_seccomp:BuildRequires: libseccomp-devel}
%{?with_tls:BuildRequires: openssl-devel}
BuildRequires:  systemd-rpm-macros

Requires(pre):  shadow-utils
# Rich dependency syntax - require selinux policy subpackage
# when selinux-policy-targeted is installed
# This ensures that the selinux subpackage is not installed when not needed
# (e.g. inside a container)
Requires: (%{name}-selinux if selinux-policy-targeted)
%{?systemd_requires}

%description
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%package devel
Summary: Files needed for development using memcached protocol
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
Install memcached-devel if you are developing C/C++ applications that require
access to the memcached binary include files.

%package selinux
Summary:             Selinux policy module
License:             GPL-2.0-only
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel

%description selinux
Install memcached-selinux to ensure your system contains the latest SELinux policy
optimised for use with this version of memcached.

%prep
# Unpack memcached sources into memcached-X.X.X directory
# and SELinux policy sources into memcached-selinux-X.X
%setup -q -b 2
%autopatch -p1

%build
%configure \
  %{?with_sasl: --enable-sasl --enable-sasl-pwdb} \
  %{?with_seccomp: --enable-seccomp} \
  %{?with_tls: --enable-tls}

make %{?_smp_mflags}

pushd ../%{selinuxmoduledir}
make
popd

%check
# tests are disabled by default as they are unreliable on build systems
%{!?with_tests: exit 0}

# whitespace tests fail locally on fedpkg systems now that they use git
rm -f t/whitespace.t

# Parts of the test suite only succeed as non-root.
if [ `id -u` -ne 0 ]; then
  # remove failing test that doesn't work in
  # build systems
  rm -f t/daemonize.t t/watcher.t t/expirations.t
fi
make test

%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
# remove memcached-debug
rm -f %{buildroot}/%{_bindir}/memcached-debug

# Perl script for monitoring memcached
install -Dp -m0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool
install -Dp -m0644 scripts/memcached-tool.1 \
        %{buildroot}%{_mandir}/man1/memcached-tool.1

# Unit file
install -Dp -m0644 scripts/memcached.service \
        %{buildroot}%{_unitdir}/memcached.service

# Default configs
install -Dp -m0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

# install SELinux policy module
pushd ../%{selinuxmoduledir}
install -d %{buildroot}%{_datadir}/selinux/packages
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/%{selinuxmoduletype}
# Not installing memcached.if - interface file from selinux-policy-devel will be used
# see. "Independant product policy" documentation for more details
install -m 0644 %{selinuxmodulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
popd

install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/memcached.conf

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post
%systemd_post memcached.service

%post selinux
# install selinux policy module with priority 200 to override the default policy
%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/%{selinuxmodulename}.pp.bz2 &> /dev/null

%preun
%systemd_preun memcached.service

%postun
%systemd_postun_with_restart memcached.service

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{selinuxmodulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype} &> /dev/null

%files
%doc AUTHORS ChangeLog COPYING NEWS README.md doc/CONTRIBUTORS doc/*.txt
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/memcached-tool
%{_bindir}/memcached
%{_mandir}/man1/memcached-tool.1*
%{_mandir}/man1/memcached.1*
%{_unitdir}/memcached.service
%{_sysusersdir}/memcached.conf

%files devel
%{_includedir}/memcached/*

%files selinux
%attr(0644,root,root) %{_datadir}/selinux/packages/%{selinuxmodulename}.pp.bz2
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{selinuxmodulename}
%license ../%{selinuxmoduledir}/COPYING

%changelog
%autochangelog
