# Tests fail in mock, not in local build.
%bcond_with        tests

Name:              redict
Version:           7.3.2
Release:           1%{?dist}
Summary:           A persistent key-value database
# redict: LGPL-3.0-only
# hiredict: BSD-3-Clause
# hdrhistogram, jemalloc, lzf, linenoise: BSD-2-Clause
# lua: MIT
# fpconv: BSL-1.0
License:           BSD-3-Clause AND BSD-2-Clause AND MIT AND BSL-1.0 AND LGPL-3.0-only AND LGPL-3.0-or-later
URL:               https://redict.io
Source0:           https://codeberg.org/redict/redict/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:           %{name}.logrotate
Source2:           %{name}-sentinel.service
Source3:           %{name}.service
Source4:           %{name}.sysusers
# could have pulled this out of unpacked sources but
# our copy has additional options pre-programmed in
Source5:           %{name}-limit-systemd
Source6:           %{name}.sysconfig
Source7:           %{name}-sentinel.sysconfig
Source8:           macros.%{name}

BuildRequires:     make
BuildRequires:     gcc
%if %{with tests}
BuildRequires:     procps-ng
BuildRequires:     tcl
%endif
BuildRequires:     pkgconfig(libsystemd)
BuildRequires:     systemd-devel
BuildRequires:     systemd-rpm-macros
BuildRequires:     openssl-devel
Requires:          logrotate
Requires(pre):     shadow-utils
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
# from deps/hiredict/hiredict.h
Provides:          bundled(hiredict) = 1.0.3
# from deps/jemalloc/VERSION
Provides:          bundled(jemalloc) = 5.3.0
# from deps/lua/src/lua.h
Provides:          bundled(lua-libs) = 5.1.5
# from deps/linenoise/linenoise.h
Provides:          bundled(linenoise) = 1.0
Provides:          bundled(lzf)
# from deps/hdr_histogram/README.md
Provides:          bundled(hdr_histogram) = 0.11.0
# no version
Provides:          bundled(fpconv)

%global redict_modules_abi 1
%global redict_modules_dir %{_libdir}/%{name}/modules
Provides:          redict(modules_abi)%{?_isa} = %{redict_modules_abi}

ExcludeArch:       %{ix86}

%description
Redict is an advanced key-value store. It is often referred to as a data
structure server since keys can contain strings, hashes, lists, sets and
sorted sets.

You can run atomic operations on these types, like appending to a string;
incrementing the value in a hash; pushing to a list; computing set
intersection, union and difference; or getting the member with highest
ranking in a sorted set.

In order to achieve its outstanding performance, Redict works with an
in-memory dataset. Depending on your use case, you can persist it either
by dumping the dataset to disk every once in a while, or by appending
each command to a log.

Redict also supports trivial-to-setup master-slave replication, with very
fast non-blocking first synchronization, auto-reconnection on net split
and so forth.

Other features include Transactions, Pub/Sub, Lua scripting, Keys with a
limited time-to-live, and configuration settings to make Redict behave like
a cache.

You can use Redict from most programming languages also.

%package           devel
Summary:           Development header for Redict module development
# Header-Only Library (https://fedoraproject.org/wiki/Packaging:Guidelines)
Provides:          %{name}-static = %{version}-%{release}

%description       devel
Header file required for building loadable Redict modules.

%prep
%autosetup -n %{name} -p1

mv deps/lua/COPYRIGHT             COPYRIGHT-lua
mv deps/jemalloc/COPYING          COPYING-jemalloc
mv deps/hiredict/LICENSES/BSD-3-Clause.txt COPYING-hiredict-BSD-3-Clause
mv deps/hdr_histogram/LICENSE.txt LICENSE-hdrhistogram
mv deps/hdr_histogram/COPYING.txt COPYING-hdrhistogram
mv deps/fpconv/LICENSE.txt        LICENSE-fpconv

# See https://bugzilla.redhat.com/2240293
# See https://src.fedoraproject.org/rpms/jemalloc/blob/rawhide/f/jemalloc.spec#_34
%ifarch %ix86 %arm x86_64 s390x
sed -e 's/--with-lg-quantum/--with-lg-page=12 --with-lg-quantum/' -i deps/Makefile
%endif
%ifarch ppc64 ppc64le aarch64
sed -e 's/--with-lg-quantum/--with-lg-page=16 --with-lg-quantum/' -i deps/Makefile
%endif

# Module API version safety check
api=`sed -n -e 's/#define REDICTMODULE_APIVER_[0-9][0-9]* //p' src/redictmodule.h`
if test "$api" != "%{redict_modules_abi}"; then
   : Error: Upstream API version is now ${api}, expecting %%{redict_modules_abi}.
   : Update the redict_modules_abi macro, the rpmmacros file, and rebuild.
   exit 1
fi

%global make_flags DEBUG="" V="echo" PREFIX=%{_prefix} BUILD_WITH_SYSTEMD=yes BUILD_TLS=yes

%build
%make_build %{make_flags}

%install
%make_install %{make_flags}

# remove sample confs
rm -rf %{buildroot}%{_datadir}/%{name}

# System user
install -p -D -m 0644 %{S:4} %{buildroot}%{_sysusersdir}/%{name}.conf

# Filesystem.
install -d %{buildroot}%{_sharedstatedir}/%{name}
install -d %{buildroot}%{_localstatedir}/log/%{name}
install -d %{buildroot}%{_localstatedir}/run/%{name}
install -d %{buildroot}%{redict_modules_dir}

# Install logrotate file.
install -pDm644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install configuration files.
install -pDm640 %{name}.conf  %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -pDm640 sentinel.conf %{buildroot}%{_sysconfdir}/%{name}/sentinel.conf

# Install systemd unit files.
mkdir -p %{buildroot}%{_unitdir}
install -pm644 %{S:3} %{buildroot}%{_unitdir}
install -pm644 %{S:2} %{buildroot}%{_unitdir}

# Install systemd limit files
install -p -D -m 644 %{S:5} %{buildroot}%{_unitdir}/%{name}.service.d/limit.conf
install -p -D -m 644 %{S:5} %{buildroot}%{_unitdir}/%{name}-sentinel.service.d/limit.conf

# Fix non-standard-executable-perm error.
chmod 755 %{buildroot}%{_bindir}/%{name}-*

# Install redict module header
install -pDm644 src/%{name}module.h %{buildroot}%{_includedir}/%{name}module.h

# Install rpm macros for redict modules
#mkdir -p %{buildroot}%{_rpmmacrodir}
install -pDm644 %{S:8} %{buildroot}%{_rpmmacrodir}/macros.%{name}

# Install sysconfig files
install -Dpm 644 %{S:6} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dpm 644 %{S:7} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-sentinel

%check
%if %{with tests}
# https://github.com/redis/redis/issues/1417 (for "taskset -c 1")
taskset -c 1 make %{make_flags} test
make %{make_flags} test-sentinel
%endif

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

%files
%license LICENSES/LGPL-3.0-only.txt
%license COPYRIGHT-lua
%license COPYING-jemalloc
%license LICENSE-hdrhistogram
%license COPYING-hdrhistogram
%license LICENSE-fpconv
%license COPYING-hiredict-BSD-3-Clause
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0750, redict, root) %dir %{_sysconfdir}/%{name}
%attr(0640, redict, root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0640, redict, root) %config(noreplace) %{_sysconfdir}/%{name}/sentinel.conf
%dir %{_libdir}/%{name}
%dir %{redict_modules_dir}
%dir %attr(0750, redict, redict) %{_sharedstatedir}/%{name}
%dir %attr(0750, redict, redict) %{_localstatedir}/log/%{name}
%{_bindir}/%{name}-*
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-sentinel.service
%dir %{_unitdir}/%{name}.service.d
%{_unitdir}/%{name}.service.d/limit.conf
%dir %{_unitdir}/%{name}-sentinel.service.d
%{_unitdir}/%{name}-sentinel.service.d/limit.conf
%dir %attr(0755, redict, redict) %ghost %{_localstatedir}/run/%{name}
%{_sysusersdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-sentinel


%files devel
# main package is not required
%license LICENSES/BSD-3-Clause.txt
%{_includedir}/%{name}module.h
%{_rpmmacrodir}/macros.%{name}


%changelog
* Wed Jan 08 2025 Jonathan Wright <jonathan@almalinux.org> - 7.3.2-1
- update to 7.3.2 rhbz#2315906
  fixes CVE-2024-46981
  fixes CVE-2024-51741
  fixes CVE-2024-31449
  fixes CVE-2024-31227
  fixes CVE-2024-31228


* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 03 2024 Jonathan Wright <jonathan@almalinux.org> - 7.3.0-1
- Update to 7.3.0 stable

* Thu Mar 28 2024 Jonathan Wright <jonathan@almalinux.org> - 7.3.0~rc2-1
- update to 7.3.0-rc2
- remove sample confs from /usr/share

* Sun Mar 24 2024 Jonathan Wright <jonathan@almalinux.org> - 7.3.0~rc1-1
- Initial package build, release candidate
