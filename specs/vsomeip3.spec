%global _lto_cflags %{nil}

Name:    vsomeip3
Version: 3.5.11
Release: 7%{?dist}
Summary: COVESA implementation of SOME/IP protocol
# remove from i686 as not needed.
ExcludeArch: %{ix86}

License: MPL-2.0
URL:     https://github.com/COVESA/vsomeip
Source0: %{URL}/archive/%{VERSION}/vsomeip-%{VERSION}.tar.gz
Source1: routingmanagerd.service
Source3: tmpfiles-vsomeip.conf
Source4: etc-vsomeip.json
Source5: vsomeip.fc
Source6: vsomeip.if
Source7: vsomeip.te
Source8: vsomeip3.sysusers.conf

# Build/Install tools and examples
Patch1: 01-vsomeip-build-extra.patch
# Do various conversions of /usr/lib -> /usr/lib64
Patch2: 02-vsomeip-fix-cmake_libdir.patch

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: dlt-libs-devel
BuildRequires: systemd-devel
BuildRequires: gcc-c++
BuildRequires: google-benchmark-devel

# Fedora has extra tools for secondary items
%if 0%{?fedora}
BuildRequires: doxygen
BuildRequires: gtest-devel
BuildRequires: asciidoc
%endif

%description

The vsomeip stack implements the http://some-ip.com/ (Scalable
service-Oriented MiddlewarE over IP (SOME/IP)) protocol. The stack
consists out of:
* a shared library for SOME/IP (libvsomeip3.so)
* a second shared library for SOME/IP's service discovery
  (libvsomeip3-sd.so) which is loaded during runtime if the service
  discovery is enabled.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package selinux
Summary:        SELinux policy module for %{name}
BuildArch:      noarch

BuildRequires:  selinux-policy-devel
BuildRequires:  make
BuildRequires:  checkpolicy
%if "%{_selinux_policy_version}" != ""
Requires:	selinux-policy >= %{_selinux_policy_version}
%endif

Requires(post):	policycoreutils
%if "%{_selinux_policy_version}" != ""
Requires(post): selinux-policy-base >= %_selinux_policy_version
Requires(post): selinux-policy-any >= %_selinux_policy_version
%endif

%description selinux
This package contains the SELinux policy module for %{name}.


## routing manager
%package routingmanager
Summary: Routingmanager daemon %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: systemd
Requires: dlt-daemon
Recommends: vsomeip3-selinux

%description routingmanager
%{summary}. Also requires dlt-daemon running.


%package examples
Summary: Examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%package tools
Summary: Tools for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
%{summary}.

%package compat
Summary: Compat libraries for vsomeip2
Requires: %{name}%{?_isa} = %{version}-%{release}
%description compat
%{summary}.

%package compat-devel
Summary: Development files for %{name}-compat
Requires: %{name}-compat%{?_isa} = %{version}-%{release}
%description compat-devel
%{summary}.

%prep
%autosetup -n vsomeip-%{version} -p1
mkdir vsomeip-selinux
cp %{SOURCE5} %{SOURCE6} %{SOURCE7} vsomeip-selinux/

# For some reasons, some source files are executable, which messes
# with debuginfo
find -name "*.[ch]pp" | xargs chmod a-x

%ldconfig_scriptlets

%ldconfig_scriptlets compat

%build
%cmake \
    -DENABLE_SIGNAL_HANDLING=OFF  \
    -DENABLE_CONFIGURATION_OVERLAYS=ON \
    -DENABLE_COMPAT=ON \
    -DVSOMEIP_INSTALL_ROUTINGMANAGERD=ON \
    -DBASE_PATH=/run/vsomeip \
    -Wno-dev
#    -Wno-dev \
#    --trace-expand --log-level=TRACE
%cmake_build --target all --target vsomeip_ctrl --target examples --target hello_world_client --target hello_world_service

(cd vsomeip-selinux &&
  make -f  /usr/share/selinux/devel/Makefile vsomeip.pp &&
  bzip2 -9 vsomeip.pp
  )

%install
%cmake_install
# Install samples
DESTDIR="%{buildroot}" %__cmake --install "%{__cmake_builddir}/tools/vsomeip_ctrl"
DESTDIR="%{buildroot}" %__cmake --install "%{__cmake_builddir}/examples"
DESTDIR="%{buildroot}" %__cmake --install "%{__cmake_builddir}/examples/hello_world"

mkdir -p %{buildroot}%{_datadir}/vsomeip
# Move sample config
mv %{buildroot}%{_prefix}%{_sysconfdir}/vsomeip %{buildroot}%{_datadir}/vsomeip/examples

for b in %{buildroot}%{_bindir}/*-sample %{buildroot}%{_bindir}/*hello_world*; do \
    mv $b $(dirname $b)/vsomeip-$(basename $b); \
done

# Home directory for the 'routingmanagerd' user
mkdir -p $RPM_BUILD_ROOT/var/lib/routingmanagerd

mkdir -p %{buildroot}%{_unitdir}
install %{SOURCE1} %{buildroot}%{_unitdir}/ # service

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf

mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/vsomeip.json

mkdir -p %{buildroot}%{_datadir}/selinux/packages/ %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -m 0644 vsomeip-selinux/vsomeip.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/
install -m 0644 vsomeip-selinux/vsomeip.if %{buildroot}%{_datadir}/selinux/devel/include/contrib/

install -m0644 -D %{SOURCE8} %{buildroot}%{_sysusersdir}/vsomeip3.conf

%post selinux
. %{_sysconfdir}/selinux/config
%selinux_modules_install -s ${SELINUXTYPE} %{_datadir}/selinux/packages/vsomeip.pp.bz2
restorecon -R %{_bindir}/routingmanagerd &> /dev/null || :
restorecon -R %{_rundir}/vsomeip/ &> /dev/null || :
restorecon -R %{_localstatedir}/%{_rundir}/vsomeip/ &> /dev/null || :
restorecon -R /var/lib/routingmanagerd/ &> /dev/null || :

%postun selinux
if [ $1 -eq 0 ]; then
   . %{_sysconfdir}/selinux/config
   %selinux_modules_uninstall -s ${SELINUXTYPE} vsomeip
   restorecon -R %{_bindir}/routingmanagerd &> /dev/null || :
   restorecon -R %{_rundir}/vsomeip/ &> /dev/null || :
   restorecon -R %{_localstatedir}/%{_rundir}/vsomeip/ &> /dev/null || :
   restorecon -R /var/lib/routingmanagerd/ &> /dev/null || :
fi

%pre routingmanager
%sysusers_create_compat vsomeip3.conf

%post routingmanager
%systemd_post routingmanagerd.service

%preun routingmanager
%systemd_preun routingmanagerd.service

%postun routingmanager
%systemd_postun_with_restart routingmanagerd.service

%files
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_libdir}/libvsomeip3.so.*
%{_libdir}/libvsomeip3-*.so.*
%{_tmpfilesdir}/%{name}.conf
%{_sysconfdir}/vsomeip.json

%files selinux
%{_datadir}/selinux/packages/vsomeip.pp.bz2
%{_datadir}/selinux/devel/include/contrib/vsomeip.if

%files compat
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_libdir}/libvsomeip.so.*

%files routingmanager
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_sysusersdir}/vsomeip3.conf
%attr(755,routingmanagerd,routingmanagerd) %dir /var/lib/routingmanagerd
%{_bindir}/routingmanagerd
%{_unitdir}/routingmanagerd.service

%files tools
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_bindir}/vsomeip_ctrl

%files examples
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_bindir}/vsomeip-*-sample
%{_bindir}/vsomeip-hello_world*
# Example configurations:
%{_datadir}/vsomeip

%files compat-devel
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_includedir}/compat
%{_libdir}/libvsomeip.so
%{_libdir}/cmake/vsomeip
%{_libdir}/pkgconfig/vsomeip.pc

%files devel
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_includedir}/vsomeip
%{_libdir}/libvsomeip3.so
%{_libdir}/libvsomeip3-*.so
%{_libdir}/cmake/vsomeip3
%{_libdir}/pkgconfig/vsomeip3.pc

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Dec 08 2025 Stephen Smoogen  <smooge@fedoraproject.org> - 3.5.11-6
- Find a couple of small changes needed to allow for selinux to be applied to non-standard policies

* Sun Dec 07 2025 Stephen Smoogen  <smooge@fedoraproject.org> - 3.5.11-4
- Use bluechi selinux to fix problem with non-default targets

* Wed Dec  3 2025 Stephen Smoogen <smooge@fedoraproject.org> - 3.5.11-3
- Rewrite the selinux policy from scratch with sepolgen
- Remove the socket creation as systemd as vsomeip will not work with it.

* Mon Dec  1 2025 Stephen Smoogen <smooge@fedoraproject.org> - 3.5.11-2
- Try to fix the selinux problem seen with CS10
- Try to fix problem with socket creation and systemd

* Mon Dec  1 2025 Stephen Smoogen <smooge@fedoraproject.org> - 3.5.11-1
- Update to newest version of vsomeip3.

* Wed Aug 27 2025 Stephen Smoogen <smooge@fedoraproject.org> - 3.5.7-2
- Remove i686 as it no longer builds and is not needed.

* Tue Aug 26 2025 Stephen Smoogen <smooge@fedoraproject.org> - 3.5.7-1
- Update to 3.5.7
- Clean up patches to just two as others are now upstream

* Mon Mar 31 2025 Stephen Smoogen <smooge@fedoraproject.org> - 3.5.5-2
- Updated 3.5.4 to 3.5.5.
- Try to make the Cmake pic vs pie patch upstreamable

* Mon Mar 17 2025 Stephen Smoogen <smooge@fedoraproject.org> - 3.5.4-1
- Moved from 3.3.x to 3.5.x
- License has changed from MPLv2 AND Boost to MPLv2
- No longer need to carry the big-endian patch
- Needed to fix some entries which did not include cstdint

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.8-6
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 3.3.8-2
- Rebuilt for Boost 1.83

* Mon Oct 16 2023 Stephen Smoogen <smooge@fedoraproject.org> - 3.3.8-1
- Updated to 3.3.8
- Fixed vsomeip3.if selinux to allow interpod communication

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 18 2023 Stephen Smoogen <smooge@fedoraproject.org> - 3.3.0-2
- Readded endian patch for s390x build

* Thu May 18 2023 Stephen Smoogen <smooge@fedoraproject.org> - 3.3.0-1
- Updated to 3.3.0
- Removed un-needed patches to code to fix C20 problems
- Removed endian patches
- Changed CMakefileLists.txt patch to remove -Werror for gcc-13
- Opened upstream on that.

* Tue Mar  7 2023 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.20.3-11
- migrated to SPDX license

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 3.1.20.3-11
- Rebuilt for Boost 1.81

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.20.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug  3 2022 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.20.3-9
- Add patch to bring up to 2022-03-15 git 17cc55f24d1c56f6a5dcca6065a227ca91d01c90
- Remove patch for bigendian and boost-1.76 due to inclusion to git
- Add in boost-1.78 for rawhide fix BZ#2084320 BZ#2113757
- Add in minor fixes to clean up C20 warnings

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.20.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 3.1.20.3-7
- Rebuilt for Boost 1.78

* Thu Mar 10 2022 Alexander Larsson <alexl@redhat.com> - 3.1.20.3-6
- Make routingmanager socket activated
- Drop systemd buildrequires
- Add selinux policy

* Wed Mar  9 2022 Alexander Larsson <alexl@redhat.com> - 3.1.20.3-5
- Fix build on big-endian

* Wed Mar  9 2022 Alexander Larsson <alexl@redhat.com> - 3.1.20.3-4
- Change basedir to /run/vsomeip

* Wed Mar  9 2022 Alexander Larsson <alexl@redhat.com> - 3.1.20.3-3
- Fix build on boost 1.75

* Tue Mar  1 2022 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.20.3-2
- Add systemd to BuildRequires
- Update description to upstream text
- add %license line

* Thu Feb 24 2022 Stephen Smoogen <smooge@fedoraproject.org> - 3.1.20.3-1
- Begin work to make it 'valid' Fedora spec
- Add gcc-c++ because it is needed post Fedora 3x
- Update License to MPLv2.0 for rpmlint

* Tue Feb 22 2022 Alexander Larsson <alexl@redhat.com> - 3.1.20.3-1
- Initial version
