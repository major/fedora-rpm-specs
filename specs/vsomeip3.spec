Name:    vsomeip3
Version: 3.3.8
Release: 5%{?dist}
Summary: COVESA implementation of SOME/IP protocol

License: MPL-2.0 AND BSL-1.0
URL:     https://github.com/COVESA/vsomeip
Source0: %{URL}/archive/%{VERSION}/vsomeip-%{VERSION}.tar.gz
Source1: routingmanagerd.service
Source2: routingmanagerd.socket
Source3: tmpfiles-vsomeip.conf
Source4: etc-vsomeip.json
Source5: vsomeip.fc
Source6: vsomeip.if
Source7: vsomeip.te

# Install libs, etc into /usr
Patch0: vsomeip-install-dirs.patch
# Use -fPIC, not -fPIE
Patch1: vsomeip-compiler-flags.patch
# Build/Install tools and examples
Patch2: vsomeip-build-extra.patch

Patch3: vsomeip-big-endian.patch

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: dlt-libs-devel
BuildRequires: systemd-devel
BuildRequires: gcc-c++
BuildRequires: gtest-devel

# Fedora has extra tools for secondary items
%if 0%{?fedora}
BuildRequires: doxygen
BuildRequires: asciidoc
%endif

# https://fedoraproject.org/wiki/SELinux/IndependentPolicy
Requires:       (vsomeip3-selinux = %{?epoch:%{epoch}:}%{version}-%{release} if selinux-policy-targeted)

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
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  make
BuildArch:      noarch
%{?selinux_requires}

%description selinux
This package contains the SELinux policy module for %{name}.

%package routingmanager
Summary: Routingmanager daemon %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires(pre): shadow-utils
Requires: systemd

%description routingmanager
%{summary}.

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
       --trace-expand --log-level=TRACE
%cmake_build --target all --target vsomeip_ctrl --target examples --target hello_world_client --target hello_world_service

(cd vsomeip-selinux &&
  make -f  /usr/share/selinux/devel/Makefile vsomeip.pp &&
  bzip2 -9 vsomeip.pp
  )

%install
%cmake_install
# Install samples
DESTDIR="%{buildroot}" %__cmake --install "%{__cmake_builddir}/tools"
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
install %{SOURCE2} %{buildroot}%{_unitdir}/ # socket

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf

mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/vsomeip.json

mkdir -p %{buildroot}%{_datadir}/selinux/packages/ %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -m 0644 vsomeip-selinux/vsomeip.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/
install -m 0644 vsomeip-selinux/vsomeip.if %{buildroot}%{_datadir}/selinux/devel/include/contrib/

%post selinux
%selinux_modules_install %{_datadir}/selinux/packages/vsomeip.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall %{_datadir}/selinux/packages/vsomeip.pp.bz2
fi

%pre routingmanager
## This creates the users that are needed for routingmanagerd
getent group routingmanagerd >/dev/null || groupadd -r routingmanagerd
getent passwd routingmanagerd >/dev/null || \
    useradd -r -g routingmanagerd -d /var/lib/routingmanagerd -s /sbin/nologin \
    -c "User for routingmanagerd" routingmanagerd
exit 0

%post routingmanager
%systemd_post routingmanagerd.socket routingmanagerd.service

%preun routingmanager
%systemd_preun routingmanagerd.socket routingmanagerd.service

%postun routingmanager
%systemd_postun_with_restart routingmanagerd.socket routingmanagerd.service

%files
%doc AUTHORS CHANGES README.md
%license LICENSE LICENSE_boost
%{_libdir}/libvsomeip3.so.*
%{_libdir}/libvsomeip3-*.so.*
%{_tmpfilesdir}/%{name}.conf
%{_sysconfdir}/vsomeip.json

%files selinux
%{_datadir}/selinux/packages/vsomeip.pp.bz2
%{_datadir}/selinux/devel/include/contrib/vsomeip.if

%files compat
%doc AUTHORS CHANGES README.md
%license LICENSE LICENSE_boost
%{_libdir}/libvsomeip.so.*

%files routingmanager
%doc AUTHORS CHANGES README.md
%license LICENSE LICENSE_boost
%attr(755,routingmanagerd,routingmanagerd) %dir /var/lib/routingmanagerd
%{_bindir}/routingmanagerd
%{_unitdir}/routingmanagerd.service
%{_unitdir}/routingmanagerd.socket

%files tools
%doc AUTHORS CHANGES README.md
%license LICENSE LICENSE_boost
%{_bindir}/vsomeip_ctrl

%files examples
%doc AUTHORS CHANGES README.md
%license LICENSE LICENSE_boost
%{_bindir}/vsomeip-*-sample
%{_bindir}/vsomeip-hello_world*
# Example configurations:
%{_datadir}/vsomeip

%files compat-devel
%doc AUTHORS CHANGES README.md
%license LICENSE LICENSE_boost
%{_includedir}/compat
%{_libdir}/libvsomeip.so
%{_libdir}/cmake/vsomeip
%{_libdir}/pkgconfig/vsomeip.pc

%files devel
%doc AUTHORS CHANGES README.md
%license LICENSE LICENSE_boost
%{_includedir}/vsomeip
%{_libdir}/libvsomeip3.so
%{_libdir}/libvsomeip3-*.so
%{_libdir}/cmake/vsomeip3
%{_libdir}/pkgconfig/vsomeip3.pc

%changelog
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
