# systemd units for snapper
%global snapper_svcs snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer snapperd.service

Name:           snapper
Version:        0.11.0
Release:        3%{?dist}
Summary:        Tool for filesystem snapshot management

License:        GPL-2.0-only
URL:            http://snapper.io
Source0:        https://github.com/openSUSE/snapper/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-remove-ext4-info-xml.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  glibc-all-langpacks

BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  btrfs-progs-devel
BuildRequires:  libmount-devel
BuildRequires:  libselinux-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  libacl-devel
# No explicit configure checks
BuildRequires:  boost-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  dbus-devel
BuildRequires:  json-c-devel
BuildRequires:  ncurses-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       diffutils

%description
This package contains snapper, a tool for filesystem snapshot management.

%package libs
Summary:        Library for filesystem snapshot management
Requires:       util-linux%{?_isa}
Requires:       btrfs-progs%{?_isa}

%description libs
This package contains the snapper shared library
for filesystem snapshot management.

%package devel
Summary:        Header files and development libraries for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel%{?_isa}
Requires:       libacl-devel%{?_isa}
Requires:       boost-devel%{?_isa}
Requires:       btrfs-progs-devel
Requires:       libxml2-devel%{?_isa}
Requires:       libmount-devel%{?_isa}

%description devel
This package contains header files and documentation for developing with
snapper.

%package tests
Summary:        Integration tests for snapper
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description tests
%{summary}.

%package -n pam_snapper
Summary:        PAM module for calling snapper
BuildRequires:  pam-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n pam_snapper
A PAM module for calling snapper during user login and logout.

%files tests
%license COPYING
%dir %{_libdir}/snapper
%{_libdir}/snapper/testsuite/

%prep
%autosetup -p1
# use libexecdir
find -type f -exec sed -i -e "s|/usr/lib/snapper|%{_libexecdir}/%{name}|g" {} ';'

%build
autoreconf -vfi
# NOTE: --disable-ext4 option removes support for ext4 internal snapshots since the feature
# never made it into upstream kernel
%configure \
  --disable-ext4 \
  --disable-zypp \
  --enable-selinux \
  %{nil}
%make_build

%install
%make_install
install -Dpm0644 data/sysconfig.snapper %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%find_lang %{name}
find %{buildroot} -name '*.la' -print -delete
rm -rf %{buildroot}%{_sysconfdir}/cron.hourly
rm -rf %{buildroot}%{_sysconfdir}/cron.daily
rm -rf %{buildroot}%{_docdir}/%{name}/COPYING

%check
make %{?_smp_mflags} check

%post
%systemd_post %{snapper_svcs}

%preun
%systemd_preun %{snapper_svcs}

%postun
%systemd_postun_with_restart %{snapper_svcs}

%pre libs
# Migration from /etc/snapper to /usr/share/snapper
for i in config-templates/default filters/base.txt filters/lvm.txt filters/x11.txt ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i}.rpmsave.old ||:
done

%posttrans libs
# Migration from /etc/snapper to /usr/share/snapper
for i in config-templates/default filters/base.txt filters/lvm.txt filters/x11.txt ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i} ||:
done

%files -f snapper.lang
%license COPYING
%doc AUTHORS
%{_bindir}/snapper
%{_sbindir}/mksubvolume
%{_sbindir}/snapperd
%config(noreplace) %{_sysconfdir}/logrotate.d/snapper
%{_unitdir}/%{name}*
%{_datadir}/bash-completion/completions/snapper
%{_datadir}/zsh/site-functions/_snapper
%{_datadir}/dbus-1/system.d/org.opensuse.Snapper.conf
%{_datadir}/dbus-1/system-services/org.opensuse.Snapper.service
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/mksubvolume.8*
%{_mandir}/man8/snapperd.8*
%{_mandir}/man5/snapper-configs.5*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/installation-helper
%{_libexecdir}/%{name}/systemd-helper

%files libs
%license COPYING
%{_libdir}/libsnapper.so.*
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/configs
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/config-templates
%{_datadir}/%{name}/config-templates/default
%dir %{_datadir}/%{name}/filters
%{_datadir}/%{name}/filters/*.txt
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%files devel
%doc examples/c/*.c
%doc examples/c++-lib/*.cc
%{_libdir}/libsnapper.so
%{_includedir}/%{name}/

%files -n pam_snapper
%{_libdir}/security/pam_snapper.so
%{_prefix}/lib/pam_snapper/
%{_mandir}/man8/pam_snapper.8*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 23 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.10.4-3
- Rebuilt for Boost 1.83

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.10.4-1
- Update to 0.10.4

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.10.1-2
- Rebuilt for Boost 1.78

* Thu Apr 28 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.10.1-1
- Rebase to 0.10.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.8.16-4
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 0.8.16-2
- Rebuild for versioned symbols in json-c

* Sat Mar 20 2021 Neal Gompa <ngompa13@gmail.com> - 0.8.16-1
- Update to 0.8.16

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.8.9-3
- Rebuilt for Boost 1.75

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.9-1
- Update to 0.8.9

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.8.3-4
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3

* Mon Feb 18 2019 Neal Gompa <ngompa13@gmail.com> - 0.8.2-1
- Rebase to 0.8.2 (RH#1669128) to fix FTBFS (RH#1676010)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.6-1
- Update to 0.5.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-3
- Escape macros in %%changelog

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-2
- Switch to %%ldconfig_scriptlets

* Tue Jan 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-3
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-2
- Rebuilt for Boost 1.64

* Thu Jun 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.4.1-2
- Rebuilt for Boost 1.63

* Fri Jan 06 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.4.1-1
- Update to 0.4.1 (RHBZ #1405664)
- Use libexecdir for helpers
- Run tests
- Simplify spec

* Tue Aug 02 2016 Ondrej Kozina <okozina@redhat.com> - 0.3.3-1
- Update to snapper 0.3.3

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 0.2.8-4
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.2.8-2
- Rebuilt for Boost 1.60

* Mon Nov 02 2015 Ondrej Kozina <okozina@redhat.com> - 0.2.8-1
- Update to snapper 0.2.8

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.2.6-2
- Rebuilt for Boost 1.59

* Wed Aug 19 2015 Ondrej Kozina <okozina@redhat.com> - 0.2.6-1
- Update to snapper 0.2.6

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.2.5-5
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.5-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 07 2015 Ondrej Kozina <okozina@redhat.com> - 0.2.5-2
- Rebuild for boost 1.57.0

* Fri Jan 30 2015 Ondrej Kozina <okozina@redhat.com> - 0.2.5-1
- Update to snapper 0.2.5
- enable rollback support (btrfs, w/o grub2 plugin yet)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.2.3-3
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Ondrej Kozina <okozina@redhat.com> - 0.2.3-1
- Update to snapper 0.2.3
- patch: enable systemd timer files

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.1.8-2
- Rebuild for boost 1.55.0

* Wed Dec 04 2013 Ondrej Kozina <okozina@redhat.com> - 0.1.8-1
- Update to snapper 0.1.8

* Fri Nov 01 2013 Ondrej Kozina <okozina@redhat.com> - 0.1.7-1
- Update to snapper 0.1.7.
- removed --enable-xattrs (already enabled by default)
- patch: reflect recent change in libbtrfs API

* Wed Jul 31 2013 Ondrej Kozina <okozina@redhat.com> - 0.1.5-2
- Add a missing requirement on crontabs to spec file (#989115)

* Mon Jul 29 2013 Ondrej Kozina <okozina@redhat.com> - 0.1.5-1
- updated to latest upstream
- allow whitespace in ALLOW_USERS and ALLOW_GROUPS
- enable new pam module
- modified specfile to reflect recent change in %%doc macro (no more version suffix)
- patch: pam module installed in proper libdir

* Sat Jul 27 2013 Petr Machata <pmachata@redhat.com> - 0.1.3-2.20130426git35ff4ec
- rebuild for boost 1.54.0
- Boost.Thread DSO does not include -mt suffix anymore (snapper-boost-mt.patch)

* Fri Apr 26 2013 Ondrej Kozina <okozina@redhat.com> - 0.1.3-1.20130426git35ff4ec
- fixed possible security vulnerability in extended attributes handling

* Thu Apr 18 2013 Ondrej Kozina <okozina@redhat.com> - 0.1.3-1.20130418git7ca81a2
- updatet to latest upstream version
- add support to compare extended attributes ('xadiff' command)
- add support to revert modificiations in file's extended attributes
- patch: avoid useless build dependency on libattr-devel

* Mon Feb 11 2013 Ondrej Kozina <okozina@redhat.com> - 0.1.2-1.20130211git676556f
- updated to latest upstream version
- fixed wrong include: "auto_ptr.h" -> <memory>
- moved diffutils dependency to client

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.1.0-2.20121026git1aaa372
- Rebuild for Boost-1.53.0

* Fri Oct 26 2012 Ondrej Kozina <okozina@redhat.com> - 0.1.0-1.20121026git1aaa372
- removed python binding since python can use dbus interface instead
- removed btrfs-progs and LVM dependecies (#852174)
- patch: do not build zypp plugin
- patch: avoid abrt when 'diff' command is executed without arguments
- patch: do not check for btrfs-progs binary
- patch: do not allow 'create-config' command on non-thin LVM volumes (#852174)
- edit libtool script to link with: '-Wl, --as-needed'
- spec file polishing

* Wed Sep 26 2012 Ondrej Kozina <okozina@redhat.com> - 0.0.14-3.20120926git7918e5c
- add dbus interface
- patch man page to reflect unsupported ext4 snapshots

* Wed Sep 5 2012 Ondrej Kozina <okozina@redhat.com> - 0.0.14-2.20120905gitb0d0145
- Rename cron files
- Fix multiple review notes issued in (#852174)

* Mon Aug 27 2012 Ondrej Kozina <okozina@redhat.com> - 0.0.14-1
- Initial build
