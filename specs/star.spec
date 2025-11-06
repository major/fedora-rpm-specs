%global ALTERNATIVES %{_bindir}/alternatives
%global version_schily 2024-03-21

# Use a specific order for building as libraries are linked to each other:
%global components libschily libdeflt libmdigest libfind librmt rmt star
Name:           star
Version:        %(echo %version_schily | tr '-' '.')
Release:        %autorelease 
Summary:        An archiving tool with ACL support

# libschily: CDDL-1.0 AND BSD-3-Clause AND BSD-4-Clause
# libdeflt: CDDL-1.0
# libmdigest: BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
# libfind: CDDL-1.0
# librmt: CDDL-1.0
# rmt: CDDL-1.0
# star: CDDL-1.0 AND BSD-3-Clause

License:        CDDL-1.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://codeberg.org/schilytools/schilytools

Source0:        %{url}/archive/%{version_schily}.tar.gz#/schily-%{version_schily}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libattr-devel libacl-devel libselinux-devel libcap-devel
BuildRequires:  make e2fsprogs-devel
BuildRequires:  sed

# drop i686 support (https://fedoraproject.org/wiki/Changes/Noi686Repositories)
ExcludeArch:    %{ix86}

Provides:       star = %{version}-%{release}
Obsoletes:      star <= 1.6
Provides:       spax = %{version}-%{release}
Obsoletes:      spax <= 1.6
Provides:       scpio = %{version}-%{release}
Obsoletes:      scpio <= 1.6

Requires(post):  %{ALTERNATIVES}
Requires(preun): %{ALTERNATIVES}

%description
Star saves many files together into a single tape or disk archive,
and can restore individual files from the archive. Star supports ACL.

%package -n     rmt
Summary:        Provides certain programs with access to remote tape devices
Provides:       rmt = %{version}-%{release}
Epoch:          2
Obsoletes:      rmt <= 1.6

%description -n rmt
The rmt utility provides remote access to tape devices for programs
like dump (a filesystem backup program), restore (a program for
restoring files from a backup), and tar (an archiving program)

%package libs
Summary:        Libraries for %{name}
Provides:       star-libs = %{version}-%{release}
Obsoletes:      star-libs <= 2023.09.28-1

%description libs
This package provides the shared libraries for star.

%prep
%autosetup -p1 -n schilytools

# Convert files to utf8 for german letters:
for i in \
    $(find . -name "*.1") \
    $(find . -name "*.5") \
    $(find . -name "*.8") \
    $(find . -name "README*") \
    $(find . -name "THANKS*"); do
    iconv -f iso-8859-1 $i -t utf-8 -o $i.new && mv -f $i.new $i
done

# Move rmt to bin instead of sbin
sed -i 's/sbin/bin/' rmt/Makefile
# Run star tests with LD_PRELOAD_PATH flag, specified in the check section
sed -i 's/$(SHELL)/$(SHELL) -c $(TEST_FLAGS)/' star/tests/Makefile

%build
make_command() {
  cd $i
  make %{_make_output_sync} -f Makefile \
      CPPOPTX="%{build_cxxflags} -Wno-incompatible-pointer-types -Wno-old-style-definition" \
      COPTX="%{build_cflags} -Wno-incompatible-pointer-types -Wno-old-style-definition" \
      GMAKE_NOWARN=true \
      LINKMODE="dynamic" \
      NOECHO= \
      RUNPATH= \
      LDOPTX="%build_ldflags" \
      $*
   cd -
}

for i in %{components}; do
  make_command config
  make_command %{?_smp_mflags} all
done

%install
for i in %{components}; do
  cd $i
  make -f Makefile \
      DESTDIR=%{buildroot} \
      GMAKE_NOWARN=true \
      INS_BASE=%{_prefix} \
      INS_RBASE=/ \
      LINKMODE="dynamic" \
      NOECHO= \
      RUNPATH= \
      install
  cd -
done

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}
ln -s %{_bindir}/rmt ${RPM_BUILD_ROOT}%{_sysconfdir}/rmt

# Move libraries to the appropriate place on 64 bit arches
if [ %{_libdir} != %{_prefix}/lib ]; then
    mkdir -p %{buildroot}%{_libdir}
    mv %{buildroot}%{_prefix}/lib/lib*.so.* %{buildroot}%{_libdir}
fi

# Make binaries executable
chmod 755 %{buildroot}%{_libdir}/lib*.so* %{buildroot}%{_bindir}/*

# XXX Nuke unpackaged files.
( cd ${RPM_BUILD_ROOT}
  rm -fv .%{_bindir}/mt
  rm -fv .%{_bindir}/smt
  rm -fv .%{_bindir}/tartest
  rm -fv .%{_bindir}/tar
  rm -fv .%{_bindir}/gnutar
  rm -fv .%{_bindir}/star_fat
  rm -fv .%{_bindir}/star_sym
  rm -fv .%{_bindir}/suntar
  rm -fv .%{_sysconfdir}/default/star
  rm -rfv .%{_prefix}%{_sysconfdir}
  rm -rfv .%{_prefix}/include
  rm -rfv .%{_prefix}/lib # hard-wired intently
  rm -rfv .%{_mandir}/man3
  rm -rfv .%{_mandir}/man5/{makefiles,makerules}.5*
  rm -rfv .%{_mandir}/man1/{tartest,gnutar,smt,mt,suntar,match}.1*
  rm -rfv .%{_docdir}/star/testscripts
  rm -rfv .%{_docdir}/star/TODO
  rm -rfv .%{_libdir}/*.so
  rm -rfv .%{_docdir} #install documents directly in the files section
)

%global general_docs \
%dir %{_pkgdocdir} \

%check
for i in %{components}; do
  cd $i
  make -f Makefile \
      GMAKE_NOWARN=true \
      LINKMODE="dynamic" \
      NOECHO= \
      RUNPATH= \
      TEST_FLAGS='LD_LIBRARY_PATH=%{buildroot}%{_libdir}' \
      tests
  cd -
done

# "desired" alternative constants
%global ALT_NAME                pax
%global ALT_LINK                %{_bindir}/pax
%global ALT_SL1_NAME            pax-man
%global ALT_SL1_LINK            %{_mandir}/man1/pax.1.gz

# "local" alternative constants
%global ALT_PATH                %{_bindir}/spax
%global ALT_SL1_PATH            %{_mandir}/man1/spax.1.gz

%post
%{ALTERNATIVES} \
    --install   %{ALT_LINK}     %{ALT_NAME}     %{ALT_PATH}     66 \
    --slave     %{ALT_SL1_LINK} %{ALT_SL1_NAME} %{ALT_SL1_PATH}

%preun
if [ $1 -eq 0 ]; then
    # only on pure uninstall (not upgrade)
    %{ALTERNATIVES} --remove %{ALT_NAME} %{ALT_PATH}
fi

%files -n star
%doc star/STARvsGNUTAR
%doc star/README.*
%doc star/README
%{_bindir}/star
%{_bindir}/ustar
%{_bindir}/spax
%{_bindir}/scpio
%{_mandir}/man1/star.1*
%{_mandir}/man1/ustar.1*
%{_mandir}/man5/star.5*
%doc %{_mandir}/man1/spax.1*
%doc %{_mandir}/man1/scpio.1*
%ghost %attr(0755,root,root) %verify(not md5 size mode mtime) %{ALT_LINK}
%ghost %attr(0644,root,root) %verify(not md5 size mode mtime) %{ALT_SL1_LINK}

%files -n rmt
%general_docs
%{_bindir}/rmt
%{_mandir}/man1/rmt.1*
%config(noreplace) %{_sysconfdir}/default/rmt
# This symlink is used by cpio, star, spax, scpio,... thus it is needed. Even
# if the cpio may be configured to use /bin/rmt rather than /etc/rmt, star (and
# thus spax, ..) has the lookup path hardcoded to '/etc/rmt' (it means that even
# non rpm based systems will try to look for /etc/rmt). And - the conclusion is
# it does not make sense to fight against /etc/rmt symlink ATM (year 2013).
%{_sysconfdir}/rmt

%files libs
%license COPYING GPL-2.0.txt LGPL-2.1.txt CDDL.Schily.txt AN-2024-03-21 CONTRIBUTORS
%doc README
%{_libdir}/libdeflt.so.1.0
%{_libdir}/libfind.so.4.0
%{_libdir}/libmdigest.so.1.0
%{_libdir}/libschily.so.2.0
%{_libdir}/librmt.so.1.0

%changelog
* Tue Nov 04 2025 Petr Khartskhaev <pkhartsk@redhat.com> - 2024.03.21-4
- Update license info
- Replace spax and scpio subpackages with Provides due to them being compiled as symlinks
- Re-add rmt's epoch
- Re-add linker flags and add default rpm flags to make
- Make tests functional by adding LD_LIBRARY_PATH and enable them
- Re-add post and preun scriptlets for alternatives
- Change rmt's location to bin instead of sbin in a cleaner way
- Exclude 32bit architectures since the build was failing on them
- Convert star 5 manfile to UTF-8

* Fri Sep 12 2025 David Wang <cryptic.triangles@gmail.com> - 2024.03.21-3
- Fix bogus date warning in spec
- Added missing generaldocs macro for rmt
- Unsuccessfully tried fixing check. Leaving it disabled as Fedora Sources 
  variant presently does not have this

* Tue Sep 09 2025 David Wang <cryptic.triangles@gmail.com> - 2024.03.21-2
- Bump release to include rmt package as requested
- Added provides/obsoletes
- Fixed up package versioning to avoid the use of epoch
- Switch to autorelease

* Fri Aug 08 2025 David Wang <cryptic.triangles@gmail.com> - 2024.03.21-1
- Draft release
- Update to new maintained fork at Codeberg:
  https://codeberg.org/schilytools/schilytools

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 30 2025 Lukas Javorsky <ljavorsk@redhat.com> - 1.6-17
- Fix the install dir of `rmt` to /usr/bin due to Fedora Change

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 David Abdurachmanov <david.abdurachmanov@gmail.com> - 1.6-14
- Enable riscv64

* Mon Jan 29 2024 Florian Weimer <fweimer@redhat.com> - 1.6-13
- Link in build configuration for i686 to use Fedora build flags

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 1.6-11
- Set build_type_safety_c to 0 (#2187168)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 17 2023 Florian Weimer <fweimer@redhat.com> - 1.6-9
- Build in C89 mode (#2187168)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Pavel Raiskup <praiskup@redhat.com> - 1.6-1
- new upstream release
- drop WITH_SELINUX knob and selinux patches, there's built-in support now
- drop several patches which were incorporated upstream, except for
  changewarnSegv patch (did not apply, and not needed nowadays)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Pavel Raiskup <praiskup@redhat.com> - 1.5.3-15
- fix covscan issues which have upstream fix (rhbz#1602700)
- reorder patches so we can easily apply %%_rawbuild macro

* Wed Aug 01 2018 Vaclav Danek <vdanek@redhat.com> - 1.5.3-14
- Fix segfault on restore default acl (rhbz#1567836)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Rafael Santos <rdossant@redhat.com> - 1.5.3-12
- Use standard Fedora linker flags (bug #1548670)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Michal Toman <mtoman@fedoraproject.org> - 1.5.3-7
- Build properly on MIPS

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 17 2014 Pavel Raiskup <praiskup@redhat.com> - 1.5.3-4
- fix segfault for pax -X (#1175009)

* Tue Sep 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.3-3
- Re-enable profiling on aarch64

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Pavel Raiskup <praiskup@redhat.com> - 1.5.3-1
- rebase to 1.5.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Pavel Raiskup <praiskup@redhat.com> - 1.5.2-10
- enable build for ppc64le (#1054401)

* Mon Jan 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.2-9
- Temporarily disable profiling on aarch64

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Pavel Raiskup <praiskup@redhat.com> - 1.5.2-7
- we should provide /etc/rmt symlink for a while (related to #968980)
- use the ssh as the default remote access method

* Thu May 30 2013 Pavel Raiskup <praiskup@redhat.com> - 1.5.2-6
- subpackage also 'rmt' (#968980)

* Fri May 24 2013 Pavel Raiskup <praiskup@redhat.com> - 1.5.2-5
- add missing ghost files (#960007)
- fix the upgrade path, sorry for the noise (#959917, #960007)

* Mon May 06 2013 Pavel Raiskup <praiskup@redhat.com> - 1.5.2-2
- package spax and scpio separately (#959917)
- fedora-review fixes, unapplied patch
- make the spax to be pax alternative (#960007)

* Wed Apr 10 2013 Pavel Raiskup <praiskup@redhat.com> - 1.5.2-1
- rebase to most up2date upstream tarball, remove patches already upstream, fix
  code movements in patches (#928758)
- fix man-page-day objections (private #948866)
- fix the build for aarch64 (#926571)

* Thu Mar 21 2013 Pavel Raiskup <praiskup@redhat.com> - 1.5.1-12
- package also the 'scpio' utility (#771926)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 18 2012 Pavel Raiskup <praiskup@redhat.com> - 1.5.1-10
- do not crash during extracting if extended attributes are not set on all
  archived files (#861848)
- note in man page that H=crc format uses Sum32 algorithm (FIPS refuses CRC)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 04 2011 Ondrej Vasik <ovasik@redhat.com> 1.5.1-6
- fix segfault with multivol option due to signedness(#666015)

* Wed Sep 29 2010 jkeating - 1.5.1-5
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Ondrej Vasik <ovasik@redhat.com> 1.5.1-4
- fix another instance of buffer overflow for files with
  long names(#632384)

* Tue Aug 17 2010 Ondrej Vasik <ovasik@redhat.com> 1.5.1-3
- Fix some invalid manpage references (#624612)
- ship star.4 manpage with star format description

* Wed Feb 03 2010 Ondrej Vasik <ovasik@redhat.com> 1.5.1-2
- fix buffer overflow for files with names of length
  100 chars(#556664)

* Wed Jan 13 2010 Ondrej Vasik <ovasik@redhat.com> 1.5.1-1
- new upstream release 1.5.1

* Thu Aug 27 2009 Ondrej Vasik <ovasik@redhat.com> 1.5-8
- provide symlinked manpage for ustar

* Thu Aug 27 2009 Ondrej Vasik <ovasik@redhat.com> 1.5-7
- Merge review (#226434) changes: convert AN-1.5 to utf-8,
  spec file cosmetic/policy changes, ship README.linux in doc

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.5-5
- Build with $RPM_OPT_FLAGS.
- Convert specfile to UTF-8.

* Wed Apr 08 2009 Ondrej Vasik <ovasik@redhat.com> 1.5-4
- fix build failure due to symbols conflicting
  with stdio(#494213)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Ondrej Vasik <ovasik@redhat.com> 1.5-2
- remove names.c requirements from non-fat Makefiles,
  do not ship names.c (#255261 for details)

* Tue Jan 27 2009 Ondrej Vasik <ovasik@redhat.com> 1.5-1
- use final instead of beta
- ship missing names.c separately
- enable optimalization again

* Wed Dec 03 2008 Ondrej Vasik <ovasik@redhat.com> 1.5a89-1
- update to latest upstream release

* Fri Jun 06 2008 Dennis Gilmore <dennis@ausil.us> 1.5a84-6
- add sparcv9 support

* Mon May 12 2008 Peter Vrabec <pvrabec@redhat.com> 1.5a84-5
- add super-H(sh3,4) architecture support (#442883)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5a84-4
- Autorebuild for GCC 4.3

* Fri Aug 31 2007 Dan Kopecek <dkopecek@redhat.com> 1.5a84-3
- added -O0 to COPTX (CFLAGS) (see #255261)

* Mon Aug 27 2007 Peter Vrabec <pvrabec@redhat.com> 1.5a84-2
- fix segfault of data-change-warn option (#255261),
  patch from dkopecek@redhat.com

* Fri Aug 24 2007 Peter Vrabec <pvrabec@redhat.com> 1.5a84-1
- new upstream release with CVE-2007-4134 fix

* Sun Jun 24 2007 Peter Vrabec <pvrabec@redhat.com> 1.5a76-3
- build star on ARM platforms (#245465)

* Mon Jan 29 2007 Peter Vrabec <pvrabec@redhat.com> 1.5a76-2
- fix buildreq. and rebuild

* Thu Jan 18 2007 Jan Cholasta <grubber.x@gmail.com> 1.5a76-1
- upgrade

* Tue Aug 08 2006 Peter Vrabec <pvrabec@redhat.com> 1.5a75-1
- upgrade

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.5a74-3.1
- rebuild

* Tue Jun 13 2006 Peter Vrabec <pvrabec@redhat.com> 1.5a74-3
- use autoconf provided by star

* Fri Jun 02 2006 Peter Vrabec <pvrabec@redhat.com> 1.5a74-2
- update tarball

* Mon Apr 24 2006 Peter Vrabec <pvrabec@redhat.com> 1.5a74-1
- upgrade

* Wed Mar 22 2006 Peter Vrabec <pvrabec@redhat.com> 1.5a73-1
- upgrade

* Wed Mar 01 2006 Peter Vrabec <pvrabec@redhat.com> 1.5a72-1
- upgrade

* Wed Feb 22 2006 Peter Vrabec <pvrabec@redhat.com> 1.5a71-1
- upgrade

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 08 2005 Peter Vrabec <pvrabec@redhat.com> 1.5a69-1
- upgrade

* Mon Oct 10 2005 Peter Vrabec <pvrabec@redhat.com> 1.5a68-1
- upgrade

* Thu Sep 22 2005 Peter Vrabec <pvrabec@redhat.com> 1.5a67-1
- upgrade

* Fri Aug 26 2005 Peter Vrabec <pvrabec@redhat.com> 1.5a65-1
- upgrade 1.5a65-1 made by Horst H. von Brand <vonbrand@inf.utfsm.cl>
- Source URL changed, no homepage now
- License changed from GPL to CDDL 1.0
- Define MAKEPROG=gmake like the Gmake.linux script does
- Disable fat binary as per star/Makefile, update star-1.5-selinux.patch for
  the various *.mk files used in that case
- Axe /usr/share/man/man1/match.1*, /usr/etc/default/rmt too
- Explicit listing in %%files, allow for compressed or plain manpages

* Fri Aug 26 2005 Peter Vrabec <pvrabec@redhat.com>
- do not remove star_fat

* Fri Aug 12 2005 Peter Vrabec <pvrabec@redhat.com>
- upgrade  1.5a64-1

* Thu Aug 04 2005 Karsten Hopp <karsten@redhat.de> 1.5a54-3
- remove /usr/bin/tar symlink

* Fri Mar 18 2005 Peter Vrabec <pvrabec@redhat.com>
- rebuilt

* Mon Nov 22 2004 Peter Vrabec <pvrabec@redhat.com>
- upgrade 1.5a54-1 & rebuild

* Mon Oct 25 2004 Peter Vrabec <pvrabec@redhat.com>
- fix dependencie (#123770)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 26 2004 Dan Walsh <dwalsh@redhat.com> 1.5a25-4
- Fix call to is_selinux_enabled

* Mon Jan 19 2004 Jeff Johnson <jbj@jbj.org> 1.5.a25-3
- fix: (!(x & 1)) rather than (!x & 1) patch.

* Wed Sep 24 2003 Dan Walsh <dwalsh@redhat.com> 1.5a25-2
- turn selinux off

* Tue Sep 16 2003 Dan Walsh <dwalsh@redhat.com> 1.5a25-1.sel
- turn selinux on

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> 1.5a18-5
- turn selinux off

* Mon Aug 25 2003 Dan Walsh <dwalsh@redhat.com> 1.5a18-3
- Add SELinux modification to handle setting security context before creation.

* Thu Aug 21 2003 Dan Walsh <dwalsh@redhat.com> 1.5a18-2
- Fix free_xattr bug

* Wed Jul 16 2003 Dan Walsh <dwalsh@redhat.com> 1.5a18-1
- Add SELinux support

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 12 2002 Elliot Lee <sopwith@redhat.com> 1.5a08-3
- Build when uname -m != _target_platform
- Use _smp_mflags
- Build on x86_64

* Mon Nov 11 2002 Jeff Johnson <jbj@redhat.com> 1.5a08-2
- update to 1.5a08.
- build from cvs.

* Wed Jun 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.5a04
- Initial build. Alpha version - it's needed for ACLs.
