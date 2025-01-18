Name:           edg-gridftp-client
Version:        1.2.9.2
Release:        32%{?dist}
Summary:        Command line clients to GridFTP libraries

License:        EUDatagrid
URL:            http://jra1mw.cvs.cern.ch:8180/cgi-bin/jra1mw.cgi/edg-gridftp-client/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#cvs -d :pserver:anonymous@glite.cvs.cern.ch:/local/reps/jra1mw \
#           checkout -r v1_2_9_2  -d edg-gridftp-client-1.2.9.2 edg-gridftp-client
#chmod 644 edg-gridftp-client-1.2.9.2/README
#chmod 644 edg-gridftp-client-1.2.9.2/INSTALL
#chmod 644 edg-gridftp-client-1.2.9.2/LICENSE
#chmod 644 edg-gridftp-client-1.2.9.2/src/*.c
#tar cfz edg-gridftp-client-1.2.9.2.tar.gz  edg-gridftp-client-1.2.9.2
#rm -rf edg-gridftp-client-1.2.9.2
Source0:        edg-gridftp-client-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  globus-ftp-client-devel
BuildRequires:  libtool
BuildRequires:  perl-generators
BuildRequires: make

%description
The edg-gridftp-client package is a thin command line interface on top
of the GridFTP libraries supplied by Globus.  They do, however,
represent a useful set of commands to do basic management of files on
a GridFTP server.

The commands provided are:

  edg-gridftp-exists   test if a file/directory exists on the server
  edg-gridftp-mkdir    create a directory on the server
  edg-gridftp-rmdir    remove a directory from a server
  edg-gridftp-rm       remove a file from a server
  edg-gridftp-ls       list files/directories on a server
  edg-gridftp-rename   rename a file/directory on a server

%prep
%setup -q
# Adapt for flavourless globus
sed -i 's/_$(FLAVOR)//g' src/Makefile.am
# A library changed name.
sed -i 's/-lgssapi_error/-lglobus_gssapi_error/' src/Makefile.am

%build
./autogen.sh
CFLAGS="${CFLAGS:-%optflags} -I%{_includedir}/globus -I%{_libdir}/globus/include" ; export CFLAGS
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
#Install docs from src tree instead.
rm -rf %{buildroot}%{_defaultdocdir}

%files
%{_bindir}/edg-gridftp-exists
%{_bindir}/edg-gridftp-ls
%{_bindir}/edg-gridftp-mkdir
%{_bindir}/edg-gridftp-rename
%{_bindir}/edg-gridftp-rm
%{_bindir}/edg-gridftp-rmdir
%{_bindir}/edg-gridftp-exists
%{_libexecdir}/edg-gridftp-base-ls
%{_libexecdir}/edg-gridftp-base-mkdir
%{_libexecdir}/edg-gridftp-base-rename
%{_libexecdir}/edg-gridftp-base-rm
%{_libexecdir}/edg-gridftp-base-rmdir
%{_libexecdir}/edg-gridftp-base-exists
%{_mandir}/man1/edg-gridftp-exists.1*
%{_mandir}/man1/edg-gridftp-ls.1*
%{_mandir}/man1/edg-gridftp-mkdir.1*
%{_mandir}/man1/edg-gridftp-rename.1*
%{_mandir}/man1/edg-gridftp-rm.1*
%{_mandir}/man1/edg-gridftp-rmdir.1*
%doc LICENSE README

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 15 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.9.2-30
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Steve Traylen <steve.traylen@cern.ch> - 1.2.9.2-17
- Remove _isa from BR rhbz#1545174

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2.9.2-6
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul  6 2011 Steve Traylen <steve.traylen@cern.ch> - 1.2.9.2-2
- Adapted to Fedora guidelines.

* Sun Jul  3 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 1.2.9.2-1
- Pull to latest upstream.
- Tweaked the RPM so it can be built from a CVS tarball.

* Fri May 27 2011 Derek Weitzel <dweitzel@cse.unl.edu> - 1.0-1
- Initial build of edg-gridftp-client

