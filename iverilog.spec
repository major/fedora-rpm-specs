Name:        iverilog
Version:     11.0
%define uver 11_0
Release:     6%{?dist}
Summary:     Icarus Verilog is a verilog compiler and simulator
License:     GPLv2
URL:         http://iverilog.icarus.com
Source0:     https://github.com/steveicarus/iverilog/archive/%{name}-%{uver}.tar.gz
# added upstream patch to fix FTBFS due autoconf-2.71 update
# https://github.com/steveicarus/iverilog/commit/4b3e1099e5517333dd690ba948bce1236466a395?raw
Patch0:      4b3e1099e5517333dd690ba948bce1236466a395.patch

BuildRequires: autoconf
BuildRequires: bzip2-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: gperf
BuildRequires: gcc-c++
BuildRequires: readline-devel
BuildRequires: zlib-devel
BuildRequires: make

 
%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including simulation. It strives to be true
to the IEEE-1364 standard.
 
%prep
%autosetup -n %{name}-%{uver}
# Clean junks from tarball
find . -type f -name ".git" -exec rm '{}' \;
rm -rf `find . -type d -name "autom4te.cache" -exec echo '{}' \;`

%build
chmod +x autoconf.sh
sh autoconf.sh
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure

# use make, avoid use V=1 due https://github.com/steveicarus/iverilog/issues/262
make %{?_smp_mflags}

 
%install
%{__make}    prefix=%{buildroot}%{_prefix} \
             bindir=%{buildroot}%{_bindir} \
             libdir=%{buildroot}%{_libdir} \
             libdir64=%{buildroot}%{_libdir} \
             includedir=%{buildroot}%{_includedir} \
             mandir=%{buildroot}%{_mandir}  \
             vpidir=%{buildroot}%{_libdir}/ivl/ \
             INSTALL="install -p" \
install
 
%check
make check
 
 
%files
%doc BUGS.txt README.txt QUICK_START.txt
%doc ieee1364-notes.txt mingw.txt swift.txt netlist.txt
%doc t-dll.txt vpi.txt cadpli/cadpli.txt
%doc xilinx-hint.txt examples/
%doc va_math.txt tgt-fpga/fpga.txt extensions.txt glossary.txt attributes.txt
%license COPYING
%{_bindir}/*
%{_libdir}/ivl
%{_mandir}/man1/*
# headers for PLI: This is intended to be used by the user.
%{_includedir}/*.h
# RHBZ 480531
%{_libdir}/*.a
 
 
%changelog
* Fri Aug 26 2022 Filipe Rosset <rosset.filipe@gmail.com> - 11.0-6
- Fix FTBFS rhbz#1999455

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Filipe Rosset <rosset.filipe@gmail.com> - 11.0-1
- Update to 11.0 fixes rhbz#1882986

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Filipe Rosset <rosset.filipe@gmail.com> - 10.3-3
- Fix FTBFS rhbz#1799526

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Filipe Rosset <rosset.filipe@gmail.com> - 10.3-1
- Update to 10.3 fixes rhbz#1742864

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10_2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10_2-5
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10_2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10_2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 10_2-2
- spec cleanup (thanks to Vasiliy N. Glazov <vascom2@gmail.com)

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 10_2-1
- update to latest 10_2 upstream version + spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Filipe Rosset <rosset.filipe@gmail.com> - 10-7
- rebuilt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 10-3
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Kiara Navarro <sophiekovalevsky@fedoraproject.org> - 10-1
- Bump to upstream version.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.20120609-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20120609-1
- new stable upstream release 0.9.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20111101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20111101-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20111101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20111101-1
- new stable upstream release 0.9.5

* Sat May 28 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20110317-1
- new stable upstream release 0.9.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20100928-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20100928-1
- new stable upstream release

* Sat Sep 11 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20100911-1
- New sources for upcoming  - 0.9.3 - for testing repos only
- removing useless -devel subpackage

* Wed Dec 30 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091230-1
- New stable snapshot - 0.9.2

* Sat Dec 12 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091212-1
- New development snapshot - 0.9.2 final prerelease snapshot

* Sat Dec 05 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091205-1
- New development snapshot - 0.9.2 prerelease snapshot

* Fri Dec 04 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091204-1
- New development snapshot - 0.9.2 prerelease snapshot

* Sat Nov 28 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091130-1
- New development snapshot

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20090423-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20090423-5
- Improved VPI support

* Mon Mar 23 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20081118-4
- new development release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20081118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 07 2008 Balint Cristian <rezso@rdsor.ro> 0.9.20081118-1
- new snapshot release upstream.

* Fri Sep 12 2008 Balint Cristian <rezso@rdsor.ro> 0.9.20080905-1
- new snapshot release upstream.

* Mon May 26 2008 Balint Cristian <rezso@rdsor.ro> 0.9.20080429-1
- new snapshot release upstream.

* Fri Mar 28 2008 Balint Cristian <rezso@rdsor.ro> 0.9.20080314-1
- new snapshot release upstream.
- add check section for some tests

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.20070608-2
- Autorebuild for GCC 4.3

* Sun Jun 10 2007 Balint Cristian <cbalint@redhat.com> 0.9.20070608-1
- new snapshot release upstream.

* Mon Apr 23 2007 Balint Cristian <cbalint@redhat.com> 0.9.20070421-1
- new snapshot release upstream.

* Tue Feb 27 2007 Balint Cristian <cbalint@redhat.com> 0.9.20070227-1
- new snapshot release.

* Tue Feb 27 2007 Balint Cristian <cbalint@redhat.com> 0.9.20070123-5
- clean junks from tarball
- exlude static library
- smp build seems fine
- use snapshot instead of cvsver macro
- follow package n-v-r from fedora standard

* Fri Feb 23 2007 Balint Cristian <cbalint@redhat.com> 20070123-4
- use cvsver macro
- move examples in main.
- more spec cleanup

* Fri Feb 23 2007 Balint Cristian <cbalint@redhat.com> 20070123-3
- buildroot coherency in spec

* Thu Feb 22 2007 Balint Cristian <cbalint@redhat.com> 20070123-2
- first build for fedora-extras
- request gnu/stubs-32.h to force working gcc in 32 bit enviroment
- fix PAGE_SIZE wich is missing on some arch
- dont use libdir macro, all library always will be 32 bit

* Thu Feb 22 2007 Balint Cristian <cbalint@redhat.com> 20070123-1
- initial release
