%undefine __cmake_in_source_build
%global debian_release 1

Name:             apt-cacher-ng
Version:          3.7.4
Release:          10%{?dist}
Summary:          Caching proxy for package files from Debian

License:          BSD-4-Clause
URL:              http://www.unix-ag.uni-kl.de/~bloch/acng/
Source0:          http://ftp.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%{version}.orig.tar.xz
Source1:          http://ftp.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%{version}-%{debian_release}.debian.tar.xz
Source2:          %{name}.conf
Source3:          %{name}.rpmlintrc
# Purpose: versioning the private shared library to comply with Fedora Policy
Patch0:           supacng.patch
Patch1:           missing-algorithm-header.patch

BuildRequires:    gcc-c++
BuildRequires:    zlib-devel
BuildRequires:    bzip2-devel
BuildRequires:    xz-devel
BuildRequires:    fuse-devel
BuildRequires:    cmake
BuildRequires:    openssl-devel
BuildRequires:    boost-devel
BuildRequires:    systemd
BuildRequires:    systemd-devel
BuildRequires:    libevent-devel
BuildRequires:    c-ares-devel
BuildRequires:    perl-generators

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

Requires:         crontabs
Requires:         logrotate
Requires:         xz

%description
A caching proxy. Specialized for package files from Linux distributors,
primarily for Debian (and Debian based) distributions.

%prep
%autosetup -p1

tar xfvJ %{SOURCE1}

# Replace all instances of /usr/lib/apt-cacher-ng/ with /usr/libexec/apt-cacher-ng/
find debian -type f -exec sed -i "s#/usr/lib/apt-cacher-ng#/usr/libexec/apt-cacher-ng#g" '{}' \;

# Fix this here until UsrMerge is done in Debian too (which will take forever)
sed -i "s#/lib/systemd/system#/usr/lib/systemd/system#" systemd/CMakeLists.txt

%build
%cmake -DLIBDIR=%{_libexecdir}/%{name} -DSDINSTALL=on -DACNG_CACHE_DIR=%{_var}/cache/%{name} -DACNG_LOG_DIR=%{_var}/log/%{name}
sed -i 's/HAVE_STRLCPY/HAVE_STRLCPY 1/' */acsyscap.h
%cmake_build

%install
%cmake_install
# we do not want an unversioned .so or a -devel package
rm -vf %{buildroot}%{_libdir}/libsupacng.so

## install extra scripts
mkdir -p %{buildroot}%{_libexecdir}/%{name}/
install -pm 0755 scripts/*.pl %{buildroot}%{_libexecdir}/%{name}/

## add useful content from Debian packaging
mkdir -p %{buildroot}%{_sysconfdir}/cron.daily
install -D -pm 0755 debian/apt-cacher-ng.cron.daily %{buildroot}%{_sysconfdir}/cron.daily/%{name}

install -D -pm 0644 debian/apt-cacher-ng.default    %{buildroot}%{_sysconfdir}/default/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -D -pm 0644 debian/apt-cacher-ng.logrotate  %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}/%{_sysusersdir}/
install -pm 644 %{SOURCE2} %{buildroot}/%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_var}/cache/%{name}
mkdir -p %{buildroot}%{_var}/lib/%{name}
mkdir -p %{buildroot}%{_var}/log/%{name}

# without this I would only get 404 for every single request
sed -i '/^Remap-debrep/s/;/# ;/' %{buildroot}%{_sysconfdir}/apt-cacher-ng/acng.conf
sed -i '/^Remap-uburep/s/;/# ;/' %{buildroot}%{_sysconfdir}/apt-cacher-ng/acng.conf
sed -i '/^Remap-kxlrep/s/;/# ;/' %{buildroot}%{_sysconfdir}/apt-cacher-ng/acng.conf

# https://fedoraproject.org/wiki/Changes/Deprecate_TCP_wrappers
# Warning: configured to use libwrap filters but feature is not built-in.
# --> this is lekely a bug upstream
sed -i 's/^# UseWrap: 0/UseWrap: 0/' %{buildroot}%{_sysconfdir}/apt-cacher-ng/acng.conf

%pre

%post
%sysusers_create %{name}.conf
%tmpfiles_create %{name}.conf
chown -R %{name}:%{name} /var/log/%{name}/
chown -R %{name}:%{name} /var/cache/%{name}/
chown -R %{name}:%{name} /run/%{name}/
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%{_docdir}/%{name}/
%dir %{_var}/lib/%{name}/
%attr(755,%{name},%{name}) %dir %{_var}/log/%{name}/
%attr(755,%{name},%{name}) %dir %{_var}/cache/%{name}/

%exclude %{_sysconfdir}/avahi/services/%{name}.service
%config(noreplace) %{_sysconfdir}/apt-cacher-ng/
%config(noreplace) %{_sysconfdir}/cron.daily/%{name}
%config(noreplace) %{_sysconfdir}/default/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%ghost %attr(755,%{name},%{name}) %dir %{_rundir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_libexecdir}/%{name}/
%{_libdir}/libsupacng.so*
%{_sbindir}/apt-cacher-ng
%{_mandir}/man8/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 28 2023 Alexandre Detiste <alexandre.detiste@gmail.com> - 3.7.4-6
- Fix failure to build to a change in CMake (rhbz 2225704)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Alexandre Detiste <alexandre.detiste@gmail.com> - 3.7.4-5
- Fix clean install without needing a reboot (upgrade was already OK)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.7.4-3
- Add BR perl-generators

* Sun Jan 15 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.7.4-2
- Drop perl(:MODULE_COMPAT_XXX) dependency
  (https://fedoraproject.org/wiki/Changes/Perl_replace_MODULE_COMPAT_by_generator)

* Fri Dec 23 2022 Alexandre Detiste <alexandre.detiste@gmail.com> - 3.7.4-1
- New upstream release
- Workaround some remapping bug
  https://salsa.debian.org/blade/apt-cacher-ng/-/issues/13
- Re-create /run/apt-cacher-ng on boot. (Bugs #1734712, #1738884, #1500085)
- Depends on "xz" for cron job
- Fix 404 error on http://localhost:3142/acng-doc/html/index.html
  [Jonathan Wright]
- use a versionned libsupacng.so

* Thu Jan 14 2021 Frédéric Pierret <frederic.pierret@qubes-os.org> - 3.5-2
- Refactor installation stage to use cmake_install macro.
- Temporarly workaround libsupacng missing buildid

* Wed Jan 13 2021 Frédéric Pierret <frederic.pierret@qubes-os.org> - 3.5-1
- update to 3.5-3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 29 2018 Kenjiro Nakayama <knakayam@redhat.com> - 3.1-4
- Fix 1609197 - apt-cacher-ng service is running in wrong permissions

* Mon Dec 04 2017 Kenjiro Nakayama <knakayam@redhat.com> - 3.1-1
- update to 3.1

* Thu Jul 06 2017 Kenjiro Nakayama <knakayam@redhat.com> - 3-1
- update to 3

* Sat Jan 30 2016 Kenjiro Nakayama <knakayam@redhat.com> - 0.8.9-1
- update to 0.8.9

* Tue Dec 29 2015 Kenjiro Nakayama <knakayam@redhat.com> - 0.8.8-1
- update to 0.8.8

* Thu May 07 2015 Kenjiro Nakayama <knakayam@redhat.com> - 0.8.3-1
- update to 0.8.3

* Tue Jan 27 2015 Kenjiro Nakayama <knakayam@redhat.com> - 0.8.0-1
- update to 0.8.0

* Wed Jun 25 2014 Kenjiro Nakayama <knakayam@redhat.com> - 0.7.26-2
- update to 0.7.26 fixed XSS vulnerability (rhbz 1111808)

* Fri Mar 14 2014 Kenjiro Nakayama <knakayam@redhat.com> - 0.7.25-3
- update to 0.7.25
- fix spec file.

* Fri May 17 2013 Warren Togami <wtogami@gmail.com> - 0.7.11-3
- systemd service script
- license
