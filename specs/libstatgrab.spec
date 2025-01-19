%bcond_without  log4cplus
%bcond_without  examples

Name:           libstatgrab
Epoch:          1
Version:        0.92.1
Release:        12%{?dist}
Summary:        A library that provides cross platform access to statistics of the system
License:        LGPL-2.1-or-later
URL:            http://www.i-scream.org/libstatgrab
Source0:        http://ftp.i-scream.org/pub/i-scream/%{name}/%{name}-%{version}.tar.gz
# REJECTED due to Solaris or whatever linking issue,
# thus we cope with pkgconfig manually.
# See: https://github.com/i-scream/libstatgrab/pull/70
Source1:        libstatgrab.pc.in
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%if %{with log4cplus}
BuildRequires:  log4cplus-devel
%endif
BuildRequires:  ncurses-devel
# Tests.
BuildRequires:  perl-generators
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires: make

%description
Libstatgrab is a library that provides cross platform access to statistics
about the system on which it's running. It's written in C and presents a
selection of useful interfaces which can be used to access key system
statistics. The current list of statistics includes CPU usage, memory
utilisation, disk usage, process counts, network traffic, disk I/O, and more.

The current list of supported and tested platforms includes FreeBSD, Linux,
NetBSD, OpenBSD, Solaris, DragonFly BSD, HP-UX and AIX.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
This package contains libraries, header files and manpages for
developing applications that use libstatgrab.

%if %{with examples}
%package        examples
Summary:        The example files from %{name}
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    examples
This package contains various examples used to show how
to develop libstatgrab based applications.
%endif

%package -n     saidar
Summary:        System information real-time monitor
License:        GPL-2.0-or-later

%description -n saidar
Saidar is a curses-based interface to viewing the current state of the
system.

%package -n     statgrab
Summary:        Sysctl-style interface to the statistics from libstatgrab
License:        GPL-2.0-or-later

%description -n statgrab
Statgrab gives a sysctl-style interface to the statistics gathered by
libstatgrab. This extends the use of libstatgrab to people writing scripts or
anything else that can't easily make C function calls. Included with statgrab
is a script to generate an MRTG configuration file to use statgrab.

# TODO: F23+2 must drop -tools-compat?
%package        tools-compat
Summary:        Transition package for statgrab-tools
Obsoletes:      statgrab-tools < 1:0.91-0
Requires:       statgrab%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       saidar%{?_isa} = %{epoch}:%{version}-%{release}

%description    tools-compat
This package only exists to help transition statgrab-tools users to the new
package split. It will be removed after 2 distribution release cycles, please
do not reference it or depend on it in any way.

%prep
%setup -q
# Instead of wasting several lines to install these programs, makefile hack
# will save the time.
sed -i 's|noinst_PROGRAMS|bin_PROGRAMS|g' examples/Makefile*
# Place log files underneath /var/log.
sed -i 's|@localstatedir@|@localstatedir@/log|g;s|.log4cplus|.log|g' *.properties.in

%build
cp -pf %{S:1} .
autoreconf -fiv
# Changing to asciidoc            --enable-man-build
%configure --with-ncurses      \
%if %{with log4cplus}
           --with-log4cplus    \
%endif
%if %{with examples}
           --enable-examples   \
%endif
           --disable-static

%make_build

%install
%make_install
%if %{with examples}
%make_install -C examples/
%endif
# Use %%doc instead.
rm -frv %{buildroot}%{_docdir}
# Drop libtool archive.
find %{buildroot} -name '*.la' -delete -print

mkdir -p %{buildroot}%{_docdir}/%{name}-tools-compat/
cat <<'EOF' >> %{buildroot}%{_docdir}/%{name}-tools-compat/README.Fedora
This package only exists to help transition statgrab-tools users to the new
package split. the structure of the transition is:

└── statgrab-tools --> └── %{name}-tools-compat
                           ├── saidar
                           └── statgrab

In the past prior to Fedora 24, libstatgrab had only 1 package for 2 programs
with different usage, while putting them inside one package seems reasonable,
however in order to reduce the size of the package, we decided to halve the
original package, now users can choose which to install, saidar or statgrab.

Note this compat package will be removed after 2 distribution release cycles,
please do not reference it or depend on it in any way.

Yours,
libstatgrab maintainers
EOF

%check
make check

%ldconfig_scriptlets

%files
%license COPYING.LGPL
%{_libdir}/*.so.*

%files devel
%doc AUTHORS NEWS PLATFORMS README
%doc examples/*.c
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/*/sg_*

%if %{with examples}
%files examples
%license COPYING
%{_bindir}/cpu_usage
%{_bindir}/disk_traffic
%{_bindir}/filesys_snapshot
%{_bindir}/load_stats
%{_bindir}/network_iface_stats
%{_bindir}/network_traffic
%{_bindir}/os_info
%{_bindir}/page_stats
%{_bindir}/process_snapshot
%{_bindir}/process_stats
%{_bindir}/user_list
%{_bindir}/valid_filesystems
%{_bindir}/vm_stats
%endif

%files tools-compat
%{_docdir}/%{name}-tools-compat/README.Fedora

%files -n saidar
%license COPYING
%{_bindir}/saidar
%if %{with log4cplus}
%config(noreplace) %{_sysconfdir}/saidar.properties
%endif
%{_mandir}/*/saidar*

%files -n statgrab
%license COPYING
%{_bindir}/statgrab*
%if %{with log4cplus}
%config(noreplace) %{_sysconfdir}/statgrab.properties
%endif
%{_mandir}/*/*statgrab*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 10 2023 Martin Osvald <mosvald@redhat.com> - 1:0.92.1-8
- Rebuilt for log4cplus 2.1.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 27 2023 Tim Orling <ticotimo@gmail.com> - 1:0.92.1-5
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Tim Orling <ticotimo@gmail.com> - 1:0.92.1-1
- Update to 0.92.1 (Fix rhbz 1943112)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 29 18:49:18 JST 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.92-6
- Rebuild for new log4cplus

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 01 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.92-3
- Add perl(lib) for tests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Tim Orling <ticotimo@gmail.com> - 1:0.92-1
- Update to 0.92 (rhbz 1742062)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.91-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.91-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.91-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.91-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.91-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.91-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:0.91-6
- Add BR: perl(App::Prove) (Fix F26FTBFS).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 18 2016 Tomas Hozza <thozza@redhat.com> - 1:0.91-4
- Rebuild against log4cplus 1.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 Christopher Meng <rpm@cicku.me> - 1:0.91-2
- Fix upgrade path of statgrab-tools

* Sun Jul 26 2015 Christopher Meng <rpm@cicku.me> - 1:0.91-1
- Update to 0.91

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.17-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.17-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.17-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 17 2013 Oliver Falk <oliver@linux-kernel.at> - 1:0.17-5.2
- Fix requires (epoch)

* Tue Sep 17 2013 Oliver Falk <oliver@linux-kernel.at> - 1:0.17-5.1
- Fix BZ#1008491 - too many broken deps

* Fri Aug 16 2013 Christopher Meng <rpm@cicku.me> - 0.90-2
- SPEC Cleanup.
- Remove unneeded Requires.

* Tue Aug 13 2013 Oliver Falk <oliver@linux-kernel.at> - 0.90-1
- Update
- Should fix BZ#925891

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.17-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Apr 10 2011 Sven Lankes <sven@lank.es> - 0.17-1
- new upstream release 

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Oliver Falk <oliver@linux-kernel.at> 0.16-5
- Rebuild for new perl-5.12.3

* Fri Feb 12 2010 Oliver Falk <oliver@linux-kernel.at> 0.16-4
- Disable building of static libs #556075

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 20 2008 Oliver Falk <oliver@linux-kernel.at> 0.16-1
- Update

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 0.15-2
- Bump-n-build for GCC 4.3

* Mon Aug 20 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 0.15-1
- New upstream version
- License clarification
- Fixed License tags for statgrab-tools and libstatgrab-examples
- Fix for rpath (problem found in previous versions, as well)

* Wed Jan 24 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 0.14-1
- New upstream version
- Minor cleanup for rpmlint warning

* Wed Oct 04 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 0.13-3
- Bump-n-build

* Tue Sep 19 2006 Patrick "Jima" Laughton <jima@beer.tclug.org>	- 0.13-2
- Bump for FC6 rebuild

* Thu Apr 20 2006 Oliver Falk <oliver@linux-kernel.at> - 0.13-1
- Update

* Wed Aug 10 2005 Oliver Falk <oliver@linux-kernel.at> - 0.12-1
- Update
- Added saidar manpage

* Fri Jul 08 2005 Oliver Falk <oliver@linux-kernel.at> - 0.11.1-3
- Included examples/*.c in doc

* Wed Jul  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.11.1-2
- a lot of fixes for Fedora Extras

* Thu May 19 2005 Oliver Falk <oliver@linux-kernel.at> - 0.11.1-1.1
- Specfile cleanup

* Sun Apr 03 2005 Oliver Falk <oliver@linux-kernel.at> - 0.11.1-1
- Update

* Fri Mar 25 2005 Oliver Falk <oliver@linux-kernel.at> - 0.11-2.1
- Fix rpmlint warnings

* Tue Feb 15 2005 Oliver Falk <oliver@linux-kernel.at> - 0.11-2
- Don't require coreutils. They are normally installed on Fedora, but
  not available on RH 8, where the tools are usually also installed.
  Yes, rebuilding with nodeps would also do it, but it's not fine...

* Tue Feb 15 2005 Oliver Falk <oliver@linux-kernel.at> - 0.11-1
- Initial build for Fedora Core
