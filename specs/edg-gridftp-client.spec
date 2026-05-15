Name:           edg-gridftp-client
Version:        1.2.9.2
Release:        %autorelease
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
%autochangelog
