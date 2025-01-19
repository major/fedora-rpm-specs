%bcond_with     tests

Name:           keydb
Version:        6.3.4
Release:        5%{?dist}
Summary:        Multithreaded Fork of Redis

ExcludeArch:    %{ix86}

License:        BSD-3-Clause AND BSD-2-Clause AND MIT
# hiredis: BSD-3-Clause
# hdrhistogram, jemalloc, linenoise: BSD-2-Clause
# lua: MIT
URL:            https://keydb.dev/
Source0:        https://github.com/snapchat/keydb/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.logrotate
Source2:        %{name}-sentinel.service
Source3:        %{name}.service
Source4:        %{name}.sysusers
# could have pulled this out of unpacked sources but
# our copy has additional options pre-programmed in
Source5:        %{name}-limit-systemd
Source6:        %{name}.sysconfig
Source7:        %{name}-sentinel.sysconfig

BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
BuildRequires:  libatomic
BuildRequires:  zlib-devel
BuildRequires:  lz4-devel
BuildRequires:  libzstd-devel
BuildRequires:  snappy-devel
BuildRequires:  bzip2-devel
BuildRequires:  systemd-rpm-macros
# for tests
%if %{with tests}
BuildRequires:  tcl
BuildRequires:  procps-ng
%endif

Requires:       logrotate

Patch:          use_destdir_var.patch

# from deps/hiredis/hiredis.h
Provides:          bundled(hiredis) = 1.0.0
# from deps/jemalloc/VERSION
Provides:          bundled(jemalloc) = 5.2.1
# from deps/lua/src/lua.h
Provides:          bundled(lua-libs) = 5.1.5
# from deps/linenoise/linenoise.h
Provides:          bundled(linenoise) = 1.0
# from deps/hdr_histogram/README.md
Provides:          bundled(hdr_histogram) = 0.11.0
# from deps/memkind/src/src/memkind.c
Provides:          bundled(memkind) = 1.8.0
# from deps/rocksdb/include/rocksdb/version.h
Provides:          bundled(rocksdb) = 7.9.2
# no version listed
Provides:          bundled(concurrentqueue)

%description
KeyDB is a multi-threaded fork of Redis, an advanced key-value store.
It is often referred to as a data structure server since keys can contain
strings, hashes, lists, sets and sorted sets.

You can run atomic operations on these types, like appending to a string;
incrementing the value in a hash; pushing to a list; computing set
intersection, union and difference; or getting the member with highest
ranking in a sorted set.

In order to achieve its outstanding performance, Redis works with an
in-memory dataset. Depending on your use case, you can persist it either
by dumping the dataset to disk every once in a while, or by appending
each command to a log.

KeyDB also supports trivial-to-setup master-slave replication, with very
fast non-blocking first synchronization, auto-reconnection on net split
and so forth.

Other features include Transactions, Pub/Sub, Lua scripting, Keys with a
limited time-to-live, and configuration settings to make Redis behave like
a cache.

You can use Redis from most programming languages also.


%package           devel
Summary:           Development header for Redis module development
# Header-Only Library (https://fedoraproject.org/wiki/Packaging:Guidelines)
Provides:          %{name}-static = %{version}-%{release}
Conflicts:         redis-devel

%description       devel
Header file required for building loadable KeyDB modules.


%prep
%autosetup -n KeyDB-%{version} -p1
# these deps don't see to be used
rm -rf deps/cpp-statsd-client

mv deps/lua/COPYRIGHT             COPYRIGHT-lua
mv deps/jemalloc/COPYING          COPYING-jemalloc
mv deps/hiredis/COPYING           COPYING-hiredis
mv deps/hdr_histogram/LICENSE.txt LICENSE-hdrhistogram
mv deps/hdr_histogram/COPYING.txt COPYING-hdrhistogram


# See https://bugzilla.redhat.com/2240293
# See https://src.fedoraproject.org/rpms/jemalloc/blob/rawhide/f/jemalloc.spec#_34
%ifarch ppc64le aarch64
sed -e 's/--with-lg-quantum/--with-lg-page=16 --with-lg-quantum/' -i deps/Makefile
%endif


%build
# due to makefile weirdness these flags need to be on build and install
%make_build USE_SYSTEMD=yes PREFIX=%{_prefix} NO_MOTD=yes


%install
# due to makefile weirdness these flags need to be on build and install
%make_install USE_SYSTEMD=yes PREFIX=%{_prefix} NO_MOTD=yes

install -p -D -m 0644 %{S:4} %{buildroot}%{_sysusersdir}/%{name}.conf

install -d %{buildroot}%{_sharedstatedir}/%{name}
install -d %{buildroot}%{_localstatedir}/log/%{name}
install -d %{buildroot}%{_localstatedir}/run/%{name}

# Install logrotate file.
install -pDm644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install configuration files.
install -pDm640 %{name}.conf  %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -pDm640 sentinel.conf %{buildroot}%{_sysconfdir}/%{name}/sentinel.conf

# Install systemd unit files.
mkdir -p %{buildroot}%{_unitdir}
install -pm644 %{S:3} %{buildroot}%{_unitdir}
install -pm644 %{S:2} %{buildroot}%{_unitdir}

# Install man pages
built_man_dir="pkg/rpm/%{name}_build/%{name}_rpm%{_mandir}"
for page in ${built_man_dir}/*/*; do
    manx=$(basename $(dirname "$page"))
    target_dir="%{buildroot}%{_mandir}/$manx"
    mkdir -p "$target_dir"
    install -Dpm 644 "$page" "$target_dir/"
done

# Install keydb module header
install -Dpm 644 src/redismodule.h %{buildroot}%{_includedir}/redismodule.h

# Install systemd limit files (requires systemd >= 204)
install -Dpm 644 %{S:5} %{buildroot}%{_unitdir}/%{name}.service.d/limit.conf
install -Dpm 644 %{S:5} %{buildroot}%{_unitdir}/%{name}-sentinel.service.d/limit.conf

# Install sysconfig files
install -Dpm 644 %{S:6} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dpm 644 %{S:7} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-sentinel

%pre
%sysusers_create_compat %{S:4}


%post
%systemd_post %{name}.service
%systemd_post %{name}-sentinel.service


%preun
%systemd_preun %{name}.service
%systemd_preun %{name}-sentinel.service


%postun
%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}-sentinel.service


%check
%if %{with tests}
make test
%endif


%files
%license COPYING
%license COPYRIGHT-lua
%license COPYING-jemalloc
%license COPYING-hiredis
%license LICENSE-hdrhistogram
%license COPYING-hdrhistogram
%doc README.md BUGS 00-RELEASENOTES
%{_bindir}/%{name}-*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0750, keydb, root) %dir %{_sysconfdir}/%{name}
%attr(0640, keydb, root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0640, keydb, root) %config(noreplace) %{_sysconfdir}/%{name}/sentinel.conf
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-sentinel.service
%dir %attr(0750, keydb, keydb) %{_sharedstatedir}/%{name}
%dir %attr(0750, keydb, keydb) %{_localstatedir}/log/%{name}
%{_sysusersdir}/%{name}.conf
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*
%dir %attr(0755, keydb, keydb) %ghost %{_localstatedir}/run/%{name}
%{_unitdir}/%{name}.service.d/limit.conf
%{_unitdir}/%{name}-sentinel.service.d/limit.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-sentinel


%files devel
%license COPYING
%{_includedir}/redismodule.h


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 Jonathan Wright <jonathan@almalinux.org> - 6.3.4-3
- Spec file fixes

* Sat Mar 23 2024 Jonathan Wright <jonathan@almalinux.org> - 6.3.4-2
- Fix sentinal environment file path

* Wed Mar 20 2024 Jonathan Wright <jonathan@almalinux.org> - 6.3.4-1
- Initial package build
