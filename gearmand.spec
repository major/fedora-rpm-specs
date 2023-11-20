Name:           gearmand
Version:        1.1.21
Release:        %autorelease
Summary:        A distributed job system
# migrated to SPDX
License:        BSD-3-Clause
URL:            http://www.gearman.org
Source0:        https://github.com/gearman/%{name}/releases/download/%{version}/gearmand-%{version}.tar.gz
Source1:        gearmand.init
Source2:        gearmand.sysconfig
Source3:        gearmand.service
Patch0:         gearmand-1.1.21-ppc64le.patch
# Fails to build on PPC.
# See https://bugzilla.redhat.com/987104 and https://bugzilla.redhat.com/987109
ExcludeArch:    ppc

BuildRequires:  gcc-c++
BuildRequires:  chrpath
BuildRequires:  libuuid-devel
BuildRequires:  boost-devel >= 1.37.0, boost-thread
BuildRequires:  sqlite-devel
BuildRequires:  tokyocabinet-devel
BuildRequires:  libevent-devel
BuildRequires:  libmemcached-devel, memcached
BuildRequires:  hiredis-devel
BuildRequires:  gperf
BuildRequires:  mariadb-connector-c-devel openssl-devel
BuildRequires:  libpq-devel
BuildRequires:  zlib-devel
BuildRequires:  systemd

# For %%check
# https://github.com/gearman/gearmand/issues/277
#BuildRequires:  curl-devel

# google perftools available only on these
%ifarch %{ix86} x86_64 ppc64 ppc64le aarch64 %{arm}
BuildRequires:  gperftools-devel
%endif
BuildRequires: make
Requires(pre):  shadow-utils
Requires:       procps
%{?systemd_requires}

%description
Gearman provides a generic framework to farm out work to other machines
or dispatch function calls to machines that are better suited to do the work.
It allows you to do work in parallel, to load balance processing, and to
call functions between languages. It can be used in a variety of applications,
from high-availability web sites to the transport for database replication.
In other words, it is the nervous system for how distributed processing
communicates.


%package -n libgearman
Summary:        Development libraries for gearman
Provides:       libgearman-1.0 = %{version}-%{release}
Obsoletes:      libgearman-1.0 < %{version}-%{release}

%description -n libgearman
Development libraries for %{name}.

%package -n libgearman-devel
Summary:        Development headers for libgearman
Requires:       pkgconfig, libgearman = %{version}-%{release}
Requires:       libevent-devel
Provides:       libgearman-1.0-devel = %{version}-%{release}
Obsoletes:      libgearman-1.0-devel < %{version}-%{release}

%description -n libgearman-devel
Development headers for %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static --disable-silent-rules --enable-ssl
sed -i 's/ DRIZZLED_BINARY .*/ DRIZZLED_BINARY ""/' gear_config.h
make %{_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -v %{buildroot}%{_libdir}/libgearman*.la
chrpath --delete %{buildroot}%{_bindir}/gearman
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/gearmand

# install systemd unit file
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service


%check
# https://github.com/gearman/gearmand/issues/277
#make test


%pre
getent group gearmand >/dev/null || groupadd -r gearmand
getent passwd gearmand >/dev/null || \
        useradd -r -g gearmand -d / -s /sbin/nologin \
        -c "Gearmand job server" gearmand
exit 0

%post
%systemd_post gearmand.service


%preun
%systemd_preun gearmand.service

%postun
%systemd_postun_with_restart gearmand.service

%ldconfig_scriptlets -n libgearman

%files
%license COPYING
%doc AUTHORS ChangeLog CONTRIBUTING.md README.md THANKS
%config(noreplace) %{_sysconfdir}/sysconfig/gearmand
%{_sbindir}/gearmand
%{_bindir}/gearman
%{_bindir}/gearadmin
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_unitdir}/%{name}.service

%files -n libgearman
%license COPYING
%{_libdir}/libgearman.so.8
%{_libdir}/libgearman.so.8.0.0

%files -n libgearman-devel
%license COPYING
%doc AUTHORS ChangeLog CONTRIBUTING.md README.md THANKS
%{_includedir}/libgearman/
%{_libdir}/pkgconfig/gearmand.pc
%{_libdir}/libgearman.so
%{_includedir}/libgearman-1.0/
%{_mandir}/man3/*


%changelog
%autochangelog
