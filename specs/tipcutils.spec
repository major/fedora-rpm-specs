Name:       tipcutils
Version:    3.0.6
Release:    2%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://tipc.sourceforge.net/
Summary:    TIPC utilities package for Linux
Source0:    http://downloads.sourceforge.net/project/tipc/%{name}-%{version}.tgz


BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libdaemon-devel
BuildRequires: libmnl-devel

%description
Tipcutils contains a variety of utility programs for use with Linux TIPC,
including:

1) TIPC pipe: A netcat like program for tipc.

2) tipclog: A simple userspace network event logger running as daemon that
logs link and node availability status.

3) tipc-link-watcher: A daemon keeping track of the status of TIPC nodes and
links in a cluster by using the topology service

4) net_topology_tracker: A daemon using the toplogy service to keep track of
the status of the overall cluster connectivity.  It connects to the topolgy
servers of all detected peer nodes, ans subscribes for their network view.


%prep
%setup -q
head -n34 include/tipcc.h | tail -n25 | sed -e 's/ \* //g' -e 's/\*//g' > LICENSE

# undefined UIO_MAXIOV in iovec_client.c => skip it
sed -ie 's/ iovec / /g' test/Makefile.am

# tipc-trace needs Python2 => skip it
sed -ie 's/ tipc-trace//g' utils/Makefile.am

%build
./bootstrap
LDFLAGS="-fPIE" \
	%configure
make

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/tipclog
%{_sbindir}/tipc-link-watcher
%{_bindir}/tipc-pipe
%{_mandir}/man1/tipc-pipe.1.gz
%doc LICENSE README

%check
make check

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 15 2024 Peter Hanecak <hany@hany.sk> - 3.0.6-1
- Newer stable version
- Dropped patches since no longer needed

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.4-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 25 2020 Peter Hanecak <hany@hany.sk> - 3.0.4-2
- droppped tipc-trace since it requires Python 2
  (see https://bugzilla.redhat.com/show_bug.cgi?id=1817029)

* Mon Mar 16 2020 Peter Hanecak <hany@hany.sk> - 3.0.4-1
- Newer stable version
- GPLv2 licensing dropped, BSD license remains
- patched few GCC warnings

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul  9 2018 Peter Hanecak <hany@hany.sk> - 2.2.0-2
- Newer stable version
- Switched back to source tarball on Sourceforge since it is newer
- Added BuildRequires: gcc (by Igor Gnatenko's), libtool and libdaemon-devel
- Updated description
- Updated license: some of the code is also under GPLv2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct  2 2014 Peter Hanecak <hany@hany.sk> - 2.0.6-1
- new stable version
- source tarball is now on GitHub, with slightly different structure
  (build requires autoconf and automake)
- fixed license: only BSD (no piece of code in current version states GPL)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2.0.5-6
- correct license information

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Lokesh Mandvekar <lsm5@buffalo.edu> - 2.0.5-4
- LICENSE file generated

* Fri Apr 19 2013 Lokesh Mandvekar <lsm5@buffalo.edu> - 2.0.5-3
- prefix removed, not needed

* Fri Apr 19 2013 Lokesh Mandvekar <lsm5@buffalo.edu> - 2.0.5-2
- macro used for prefix, defattr removed
- check section added
- description updated

* Thu Apr 18 2013 Lokesh Mandvekar <lsm5@buffalo.edu> - 2.0.5-1
- New stable version - initial package

* Tue Apr 16 2013 Lokesh Mandvekar <lsm5@buffalo.edu> - 2.0.4-1
- Version upgrade

* Fri Sep 07 2012 Erik Hugne <erik.hugne@ericsson.com> - 2.0.3-1
- Initial Fedora package
