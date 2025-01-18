# private libraries that do not have an soname should not be in provides
%global _privatelibs ^(%{_libdir}/%{name}/plugins.*/.*\\.so.*)$
%global _priv_debuginfo ^(.*lib.*[.]so-.*)$
%global __provides_exclude_from ^(%{_privatelibs}|%{_priv_debuginfo})$
%global __requires_exclude_from ^(%{_privatelibs}|%{_priv_debuginfo})$

%global latestversion 1.6.1
%global commit r12890
%global commitdate 20250110
%global postrelease .p5
%global namesuffix src

Name:           aubit4gl
Version:        %{latestversion}%{postrelease} 
Release:        2%{?dist}
Summary:        IBM Informix 4GL compatible compiler

# The entire source code is GPL-2.0-or-later except
# tools/cgi_4gl which is MIT
# lib/bin/svn2cl.xsl which is BSD-3-Clause
# lib/libaubit4gl/curl.c which is BSD-3-Clause
# lib/extra_libs/mantisconnect/pregen which is GPL-1.0-or-later
# tools/adbload2/adbload2_parse_pregen.tab.c which is GPL-3.0-or-later
# tools/no_yacc/cygwin/compilers which is GPL-3.0-or-later
# lib/libui/ui_json/libjson.c which is LGPL-2.0-or-later
# lib/libui/ui_xml which is LGPL-2.0-or-later
# incl/json.h which is MIT
# lib/libaubit4gl/json.c which is MIT
# lib/extra_libs/memcached/memcache.h which is MIT
# lib/libaubit4gl/mapm which is NTP
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND GPL-1.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-3-Clause
URL:            https://www.aubit.com
Source0:        https://downloads.sourceforge.net/aubit4gl/%{latestversion}/%{name}%{namesuffix}.%{latestversion}.tar.gz
Source1:        https://downloads.sourceforge.net/aubit4gl/Aubit4gl-manual/aubitmanpages.tar.bz2
#Source2:        https://aubit.com/aubit4gl/manuals/aubman.pdf
#Source3:        https://aubit.com/aubit4gl/manuals/aubitqref.pdf
# Patch the latest release to the post release
# Changes made by the patch are listed in the commit log
# https://sourceforge.net/p/aubit4gl/aubit4gl_code/12890/log/?path=
# https://sourceforge.net/p/aubit4gl/aubit4gl_code/commit_browser
Patch0:         https://downloads.sourceforge.net/aubit4gl/SRPM/%{name}-%{version}.patch

BuildRequires: gcc
BuildRequires: ncurses-devel
BuildRequires: libpq-devel
BuildRequires: bison flex procps-ng
# https://fedoraproject.org/wiki/Changes/SunRPCRemoval
BuildRequires: rpcgen libtirpc-devel
Requires: gcc
# These are not primary architectures, so not required to build on them.
# https://fedoraproject.org/wiki/Architectures#Structure 
ExcludeArch: i686 s390x ppc64le


%description
Aubit 4GL compiler is software that translates IBM Informix 4GL source code
into C code, and compiles into executable programs.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -n %{name}%{namesuffix}
%patch 0 -p1


%build
# setting LDFLAGS=-pie prevents rpmlint warning
# position-independent-executable-suggested on the binaries.
%configure LDFLAGS=-pie \
           --disable-prefix-check \
           --with-smtp=no \
           %if "%{getenv:INFORMIXDIR}" != ""
           --with-informix=%{getenv:INFORMIXDIR} \
           %endif
           --without-zlib \
           --enable-minimal=yes
# It does not compile with multiple threads
%make_build -j1


%install
rm -rf %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
tar xvf %{SOURCE1} -C %{buildroot}%{_mandir}/man1
#cp %%{SOURCE2} %%{SOURCE3} %%{_builddir}/%%{name}-%%{version}
# Remove the execute bit on the example files so rpmlint does not complain
chmod -x %{_builddir}/%{name}%{namesuffix}/tools/examples/*/*.4gl

%make_install PREFIX=%{buildroot}%{_libdir}/%{name} \
              LIB_INSTALL_LINK=%{_builddir}/%{name}%{namesuffix} \
              BIN_INSTALL_LINK=%{_builddir}/%{name}%{namesuffix} \
              aubitrc=new

# Remove files which will not be packaged, to cleanup licensing.
# compilers/ace/dump_4gl.c contains: "This code is not covered by the GPL"
# Not compiling...
#rm -f %%{buildroot}%%{_libdir}/%%{name}/bin/aace_4gl

# Install header files
cp -p %{buildroot}%{_libdir}/%{name}/incl/*.h %{buildroot}%{_includedir}/%{name}
rm -rf %{buildroot}%{_libdir}/%{name}/incl

# Install the Aubit4GL library into the system library directory
cp -d %{buildroot}%{_libdir}/%{name}/lib/lib%{name}.so* %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_libdir}/%{name}/lib

# Put the Aubit4GL aubitrc config file into place.
mkdir -p %{buildroot}%{_sysconfdir}
install %{_builddir}/%{name}%{namesuffix}/etc/aubitrc %{buildroot}%{_sysconfdir}
# Fixup paths in aubitrc
sed -i -e "s|%{buildroot}||g" \
       -e "s|%{_builddir}/%{name}%{namesuffix}|%{_libdir}/%{name}|g" \
       -e "s|^\(AUBITETC=\).*|\1%{_sysconfdir}|g" \
       %{buildroot}%{_sysconfdir}/aubitrc

# Fix shebang on scripts
sed -i -e '1d' %{buildroot}%{_libdir}/%{name}/bin/report.pm 
sed -i -e '1d' %{buildroot}%{_libdir}/%{name}/bin/using.pm 
sed -i -e '1d;2i#!/usr/bin/bash' %{buildroot}%{_libdir}/%{name}/bin/aubit 

# Remove zero-length files shown as error by rpmlint
rm -f %{buildroot}%{_libdir}/%{name}/etc/import/default
rm -f %{buildroot}%{_libdir}/%{name}/tools/4glpc/settings/C
rm -f %{buildroot}%{_libdir}/%{name}/tools/4glpc/settings/C_INFORMIX
rm -f %{buildroot}%{_libdir}/%{name}/tools/4glpc/settings/EC

# Install the binaries
mkdir -p %{buildroot}%{_bindir}
install %{buildroot}%{_libdir}/%{name}/bin/4glpc %{buildroot}%{_bindir}
install %{buildroot}%{_libdir}/%{name}/bin/4glc %{buildroot}%{_bindir}
install %{buildroot}%{_libdir}/%{name}/bin/fcompile %{buildroot}%{_bindir}
install %{buildroot}%{_libdir}/%{name}/bin/amkmessage %{buildroot}%{_bindir}
# The above binaries are required, a ticket can be filed if others are needed
rm -rf %{buildroot}%{_libdir}/%{name}/bin

# To avoid duplicate build-ids with libLEX_C and libLEX_CS, create a link
ln -sf libLEX_C.so %{buildroot}%{_libdir}/%{name}/plugins-%{latestversion}/libLEX_CS.so

# docs are installed in the system location
rm -rf %{buildroot}%{_libdir}/%{name}/docs
rm -f %{buildroot}%{_libdir}/%{name}/README.txt


%check
make test
make -C tools/test


%files
%license docs/COPYING
%doc docs/CREDITS
%doc README.txt
%doc tools/examples
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins-%{latestversion}
%dir %{_libdir}/%{name}/etc
%dir %{_libdir}/%{name}/tools
%{_libdir}/%{name}/etc/*
%{_libdir}/%{name}/tools/*
%{_libdir}/%{name}/plugins-%{latestversion}/*.so
%{_libdir}/lib%{name}.so.*
%config(noreplace) %{_sysconfdir}/aubitrc
%{_bindir}/4glc
%{_bindir}/4glpc
%{_bindir}/amkmessage
%{_bindir}/fcompile
%{_mandir}/man1/*


%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1.p5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Chad Lemmen <rpm@stansoft.org> - 1.6.1.p5-1
- updated to 1.6.1.p5

* Wed Jan 31 2024 Chad Lemmen <rpm@stansoft.org> - 1.6.1.p4-1 
- added BuildRequires: rpcgen libtirpc-devel
- added configure option --enable-minimal=yes to not build aace or glade
- updated to 1.6.1.p4

* Mon Oct 02 2023 Chad Lemmen <rpm@stansoft.org> - 1.6.1.p3-1
- added configure option --with-informix
- cleaned up include directory to match upstream
- updated to 1.6.1.p3

* Thu Sep 14 2023 Chad Lemmen <rpm@stansoft.org> - 1.6.1.p2-1
- updated to 1.6.1.p2
- applied patch to latest aubit4gl version for this post release

* Fri Jul 28 2023 Chad Lemmen <rpm@stansoft.org> - 1.6.1.p1-1
- updated to 1.6.1.p1
- applied patch to latest aubit4gl version for this post release

* Wed Feb 22 2023 Chad Lemmen <rpm@stansoft.org> - 1.6.1-1
- updated to 1.6.1

* Thu Dec 29 2022 Chad Lemmen <rpm@stansoft.org> - 1.5.3-1
- initial Fedora RPM packaging

