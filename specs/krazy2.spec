%global __cmake_in_source_build 1

%global snapdate 20140114
%global snaphash 35d9080f1870d44c384da8f17a46388ba97b9647

Name:           krazy2
Version:        2.97
Release:        0.35.%{snapdate}git%(echo %{snaphash} | cut -c -13)%{?dist}
Summary:        Krazy is a tool for checking code against the KDE coding guidelines

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://techbase.kde.org/Development/Tutorials/Code_Checking
Source0:        https://gitorious.org/krazy/krazy/archive/%{snaphash}.tar.gz
Source1:        krazy-licensecheck
# install the shared libraries (that are explicitly built as SHARED, not STATIC)
Patch0:         krazy2-install-shlibs.patch

# krazy-licensecheck moved from kdesdk to here in 4.2.0
Conflicts:      kdesdk < 4.2.0

BuildRequires:  groff
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(YAML)
# perldoc is now in separate package
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  qt4-devel
BuildRequires:  cmake
BuildRequires: make
# Krazy2 uses desktop-file-validate, so this is an actual Requires
Requires:       desktop-file-utils

%description
Krazy scans KDE source code looking for issues that should be fixed
for reasons of policy, good coding practice, optimization, or any other
good reason.


%prep
%setup -q -n krazy-krazy
%patch -P0 -p1 -b .install-shlibs
# delete (two!) bundled copies of desktop-file-utils
rm -rf src/desktop-file-utils-*


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
pushd src/passbyvalue
%{qmake_qt4}
make %{?_smp_mflags}
popd
pushd cppchecks
%{cmake} .
make %{?_smp_mflags} VERBOSE=1
popd


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install
chmod 0755 %{buildroot}%{_bindir}/krazy2{,all,xml}
pushd helpers
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd plugins
make PREFIX=%{buildroot}%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd extras
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd sets
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd src/passbyvalue
make INSTALL_ROOT=%{buildroot}%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd share
mkdir -p %{buildroot}%{_datadir}/dtd
install -m 644 -p kpartgui.dtd %{buildroot}%{_datadir}/dtd/kpartgui.dtd
install -m 644 -p kcfg.dtd %{buildroot}%{_datadir}/dtd/kcfg.dtd
popd
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/krazy-licensecheck
pushd cppchecks
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install/fast
popd
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'



%ldconfig_scriptlets


%files
%doc COPYING README
%{_mandir}/man1/krazy2.1.gz
%{_mandir}/man1/krazy2all.1.gz
%{_mandir}/man1/krazy2xml.1.gz
%{_mandir}/man3/krazyrc.3.gz
%{_bindir}/krazy-licensecheck
%{_bindir}/krazy2
%{_bindir}/krazy2all
%{_bindir}/krazy2xml
%{_libdir}/libcpp_parser.so
%{_libdir}/libcppmodel.so
%{_libdir}/libpreprocessor.so
%{_libdir}/libcheckutil.so
%{_libdir}/libcheckutil.so.1
%{_libdir}/libcheckutil.so.1.0
%{_libdir}/krazy2/
%{_datadir}/dtd/
%{perl_vendorlib}/Krazy/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.35.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.97-0.34.20140114git35d9080f1870d
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.33.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.32.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.31.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.30.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.29.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.28.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.97-0.27.20140114git35d9080f1870d
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.26.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.25.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.97-0.24.20140114git35d9080f1870d
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.23.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.22.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.97-0.21.20140114git35d9080f1870d
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.20.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.19.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.97-0.18.20140114git35d9080f1870d
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.17.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.16.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.97-0.15.20140114git35d9080f1870d
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.14.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.13.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.12.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.97-0.11.20140114git35d9080f1870d
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.97-0.10.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.97-0.9.20140114git35d9080f1870d
- Perl 5.24 rebuild

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.97-0.8.20140114git35d9080f1870d
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.97-0.7.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.97-0.6.20140114git35d9080f1870d
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.97-0.5.20140114git35d9080f1870d
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.97-0.4.20140114git35d9080f1870d
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.97-0.3.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.97-0.2.20140114git35d9080f1870d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 18 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.97-0.1.20140114git35d9080f1870d
- Update to latest master (35d9080f1870d44c384da8f17a46388ba97b9647, 2014-01-14)

* Sun Nov 17 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.94-0.2.20130817git8a0c3deb81ce2
- Don't install redundant krazyrc.5.gz, krazyrc.3.gz is the replacement

* Sun Nov 17 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.94-0.1.20130817git8a0c3deb81ce2
- Update to latest master (8a0c3deb81ce219ebfa073480036d1a2e8237964, 2013-08-17)
- Drop upstreamed part of prefix patch, rename rest to krazy2-install-shlibs
- BuildRequires: perl(YAML)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90-20.20100926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 2.90-19.20100926svn
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90-18.20100926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90-17.20100926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 2.90-16.20100926svn
- Perl 5.16 rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90-15.20100926svn
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Radek Novacek <rnovacek@redhat.com> 2.90-14.20100926svn
- Change BR: perl-Pod-Perldoc to perl(Pod::Perldoc)

* Mon Jan 16 2012 Radek Novacek <rnovacek@redhat.com> 2.90-13.20100926svn
- Add BR: perl-Pod-Perldoc (perldoc is now in separate package)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90-12.20100926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.90-11.20100926svn
- Perl mass rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90-10.20100926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 01 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.90-9.20100926svn
- Install sets (required for operation)
- Use install/fast instead of install for the cppchecks CMake makefile

* Fri Oct 01 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.90-8.20100926svn
- Remove unused (since Jan 2009!) kdelibs4-devel and kdevplatform-devel BRs

* Fri Oct 01 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.90-7.20100926svn
- Update to current SVN (revision 1179948 committed 20100926, version 2.90)
- Drop upstreamed qt47 and rpath patches

* Mon Jun 28 2010 Rex Dieter <rdieter@fedoraproject.org> 2.9-6.20100628svn
- Update snapshot
- FTBFS krazy2-2.9-4.20090928svn.fc13 (#599851)
- squash /lib rpaths

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.9-5.20090928svn
- Mass rebuild with perl-5.12.0

* Tue Sep 29 2009 Ben Boeckel <MathStuf@gmail.com> 2.9-4.20090928svn
- Update snapshot
- krazy2ebn is gone
- Use kdevplatform by default now

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-3.20090719svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Ben Boeckel <MathStuf@gmail.com> 2.9-2.20090719svn
- Fix %%changelog
- Fix CVS mistakes (update tarball)

* Mon Jul 20 2009 Ben Boeckel <MathStuf@gmail.com> 2.9-1.20090719svn
- Updated SVN
- Conditionalize patch
- Fix DESTDIR/PREFIX for doc
- Remove %%check section

* Mon Mar 16 2009 Ben Boeckel <MathStuf@gmail.com> 2.8-9.20090314svn
- Updated SVN

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-8.20090127svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Ben Boeckel <MathStuf@gmail.com> 2.8-7.20090127svn
- Updated SVN

* Sat Jan 24 2009 Ben Boeckel <MathStuf@gmail.com> 2.8-6.20090113svn916151
- Added flag for building with kdevplatform
- Removed patches applied upstream

* Tue Jan 13 2009 Ben Boeckel <MathStuf@gmail.com> 2.8-5.20090111svn909634
- Typo with sources

* Tue Jan 13 2009 Ben Boeckel <MathStuf@gmail.com> 2.8-4.20090111svn909634
- Forgot to commit krazy-licensecheck

* Tue Jan 13 2009 Ben Boeckel <MathStuf@gmail.com> 2.8-3.20090111svn909634
- Missed the patch

* Tue Jan 13 2009 Ben Boeckel <MathStuf@gmail.com> 2.8-2.20090111svn909634
- Moved krazy-licensecheck from kdesdk to here

* Tue Jan 6 2009 Ben Boeckel <MathStuf@gmail.com> 2.8-1.20090105svn906738
- New plugins and extra checks
- Updated plugins

* Wed Oct 8 2008 Ben Boeckel <MathStuf@gmail.com> 2.6-6.20081008svn869261
- Updated SVN
- Patch applied upstream

* Tue Sep 23 2008 Ben Boeckel <MathStuf@gmail.com> 2.6-5.20080923svn862962
- Updated SVN

* Thu Sep 18 2008 Ben Boeckel <MathStuf@gmail.com> 2.6-4.20080918svn862357
- Updated SVN
- Spec file cleaned up

* Thu Sep 18 2008 Ben Boeckel <MathStuf@gmail.com> 2.6-3
- Fixed where the plugins get installed to

* Wed Sep 17 2008 Ben Boeckel <MathStuf@gmail.com> 2.6-2
- Fixed the rpmlint errors

* Wed Sep 17 2008 Ben Boeckel <MathStuf@gmail.com> 2.6-1
- Fixed the spec file up

* Wed May 21 2008 Ben Boeckel <MathStuf@gmail.com> 1.11-1
- Created
