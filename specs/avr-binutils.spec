%define target avr

Name:           %{target}-binutils
Version:        2.44
Release:        1%{?dist}
Epoch:          1
Summary:        Cross Compiling GNU binutils targeted at %{target}
License:        GPL-2.0-or-later
URL:            http://www.gnu.org/software/binutils/
Source0:        https://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.xz
Source1:        README.fedora
#add widespread options to avr-size: --format=avr -mcu=XX
Patch1: http://distribute.atmel.no/tools/opensource/avr-gcc/binutils-2.20.1/30-binutils-2.20.1-avr-size.patch
Patch2: avr-binutils-config.patch

BuildRequires:  gawk texinfo gcc
#for autoreconf:
BuildRequires:  gettext-devel automake
BuildRequires:  autoconf
BuildRequires: make zlib-devel
Provides: bundled(libiberty)

%description
This is a Cross Compiling version of GNU binutils, which can be used to
assemble and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.


%prep
%setup -q -c
pushd binutils-%{version}
%patch -P1 -p2 -b .avr-size
%patch -P2 -p1 -b .config

# We call configure directly rather than via macros, thus if
# we are using LTO, we have to manually fix the broken configure
# scripts
pushd libiberty
#autoconf -f
popd
#pushd intl
#autoconf -f
#popd

popd 
cp %{SOURCE1} .


%build

mkdir -p build
pushd build
CFLAGS="$RPM_OPT_FLAGS" ../binutils-%{version}/configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
  --with-system-zlib \
  --target=%{target} --disable-werror --disable-nls
make %{?_smp_mflags}
popd

%check
cd build
%ifnarch s390x
make check
%endif
echo "completed"

%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd
# these are for win targets only
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,windres}.1
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm    $RPM_BUILD_ROOT%{_libdir}/lib*.a $RPM_BUILD_ROOT%{_libdir}/bfd-plugins/libdep* ||:

%files
%license binutils-%{version}/COPYING binutils-%{version}/COPYING.LIB
%doc binutils-%{version}/README README.fedora
%{_prefix}/%{target}
%{_bindir}/%{target}-*
%{_mandir}/man1/%{target}-*.1.gz


%changelog
* Tue Feb 04 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.44-1
- updated to 2.44

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 29 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:2.43-1
- updated to 2.43

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:2.42-1
- updated to 2.42

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.41-1
- updated to 2.41

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 14 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.40-2
- update license tag format (SPDX migration) for https://fedoraproject.org/wiki/Changes/SPDX_Licenses_Phase_1

* Wed Feb 01 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.40-1
- updated to 2.40

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Florian Weimer <fweimer@redhat.com> - 1:2.39-2
- Apply patch from binutils-2.39-6.fc38 to avoid C89 constructs

* Wed Aug 31 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.39-1
- updated to 2.39

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 09 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.38-1
- updated to 2.38

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 06 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.37-2
- temp. disable autoconf as 2.71 is not compatible

* Wed Aug 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.37-1
- updated to 2.37

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.36.1-1
- updated to 2.36.1

* Tue May 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.36-1
- updated to 2.36

* Tue May 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.35-5
- bump release for rebuild

* Sun Apr 11 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.35-4
- add explicit requirement for autoconf 2.69

* Tue Feb 02 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.35-3
- fix --format=avr option (#1907907)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Michal Hlavinka <mhlavink@redhat.com> - 1:2.35-1
- updated to 2.35

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 1:2.32-4
- Fix broken configure tests compromised by LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Michal Hlavinka <mhlavink@redhat.com> - 1:2.32-1
- updated to 2.32

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Michal Hlavinka <mhlavink@redhat.com> - 1:2.30-2
- add gcc buildrequire

* Tue Feb 06 2018 Michal Hlavinka <mhlavink@redhat.com> - 1:2.30-1
- updated to 2.30

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 02 2017 Michal Hlavinka <mhlavink@redhat.com> - 1:2.28-1
- updated to 2.28

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 12 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:2.27-1
- updated to 2.27

* Tue Jun 28 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:2.26-1
- updated to 2.26

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:2.25-1
- updated to 2.25

* Thu Nov 13 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:2.24-4
- fix CVE-2014-8738: out of bounds memory write

* Wed Nov 12 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:2.24-3
- fix directory traversal vulnerability (#1162657)
- fix CVE-2014-8501: out-of-bounds write when parsing specially crafted PE executable
- fix CVE-2014-8502: heap overflow in objdump
- fix CVE-2014-8503: stack overflow in objdump when parsing specially crafted ihex file
- fix CVE-2014-8504: stack overflow in the SREC parser

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:2.24-1
- updated to 2.24

* Mon Jun 09 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:2.23.2-6
- fix FTBFS caused by popd usage (#1105986)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.23.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Michal Hlavinka <mhlavink@redhat.com> - 1:2.23.2-4
- avr-binutils may be affected by libiberty CVE (#1059362)

* Tue Aug 13 2013 Michal Hlavinka <mhlavink@redhat.com> - 1:2.23.2-3
- fix tex again

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Michal Hlavinka <mhlavink@redhat.com> - 1:2.23.2-1
- updated to 2.23.2

* Tue Jun 18 2013 Jaromir Capik <jcapik@redhat.com> - 1:2.23.1-4
- autoreconf -vif doesn't work -> patching for aarch64 support (#925061)

* Fri Apr 19 2013 Michal Hlavinka <mhlavink@redhat.com> - 1:2.23.1-3
- fix aarch64 support (#925061)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Michal Hlavinka <mhlavink@redhat.com> - 1:2.23.1-1
- updated to 2.23.1
- added new option --format=avr to avr-size for compatibility reasons 
  with other avr toolchains

* Mon Oct 15 2012 Jon Ciesla <limburgher@gmail.com> - 1:2.20-5
- Provides: bundled(libiberty)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Thibault North <tnorth@fedoraproject.org> - 1:2.20-2
- Downgrade to 2.20 because of BZ#688645

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 19 2010 Thibault North <tnorth@fedoraproject.org> - 2.21-1
- New upstream release 2.21

* Fri Nov 20 2009 Thibault North <tnorth AT fedoraproject DOT org> - 2.20-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.18-4
- Rebase patch-coff-avr.patch (Fix F11 rebuild breakdown).

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.18-2
- Autorebuild for GCC 4.3

* Thu Jan 24 2008 John Voltz <ninevoltz@metalink.net> 2.18-1
- Bump to binutils 2.18 and add coff-avr patch for VMLAB (on Wine)

* Sun Dec  2 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.17-5
- Fix building with texinfo version > 4.9 (4.11 for example)

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.17-4
- Update License tag for new Licensing Guidelines compliance
- Fix building with new glibc open checking

* Sat Apr  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.17-3
- Use mkdir -p instead of mkdir, to fix rpmbuild --short-circuit (bz 234750)

* Fri Apr  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.17-2
- Several specfile improvements / fixes (bz 234750)

* Sun Apr  1 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.17-1
- Revert to GNU 2.17 release as using GNU releases are better for non linux
  targets
- Add --disable-nls, to disable translations, so that we don't use the native
  PO files, as using the PO files of the (different version) native binutils,
  can lead to all kinda problems when translating formatstrings.
- Don't use %%configure but DIY, to avoid unwanted side effects of %%configure

* Sun Apr  1 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.17.50.0.12-1
- Bump to 2.17.50.0.12, to sync with rawhide / Fedora 7
- "Dynamicly Generate" README.fedora so that macros can be used

* Thu Mar 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.17.50.0.9-1
- Bump to 2.17.50.0.9
- Use %%configure instead of ./configure
- Various fixups

* Wed Mar 28 2007 Koos Termeulen koostermeulen@gmail.com 2.17-1
- New version and some changes after unofficial review by Hans de Goede

* Wed Mar 21 2007 Koos Termeulen koostermeulen@gmail.com 2.16.1-1
- Initial release
