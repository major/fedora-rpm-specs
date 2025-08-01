Name:           john
Summary:        John the Ripper password cracker
Version:        1.9.0
Release:        12%{?dist}

%bcond_without  check

URL:            https://www.openwall.com/john
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
Source0:        https://www.openwall.com/john/k/john-%{version}.tar.xz
Source1:        https://www.openwall.com/john/k/john-%{version}.tar.xz.sign

# The authenticator public key obtained from https://www.openwall.com/signatures/
# https://www.openwall.com/signatures/openwall-offline-signatures.asc
# gpg --keyid-format long --list-options show-keyring  openwall-offline-signatures.asc
# it's ID 05C027FD4BDC136E resp. 297AD21CF86C948081520C1805C027FD4BDC136E
# uid "Openwall offline signing key"
#
# Compared to public records of pgp.mit.edu
# gpg2 --keyserver pgp.mit.edu --search-key 297AD21CF86C948081520C1805C027FD4BDC136E
# gpg2 --list-public-keys 297AD21CF86C948081520C1805C027FD4BDC136E
#
# Verified manually signature on tarball
# gpg --verify john-1.9.0.tar.xz.sign john-1.9.0.tar.xz
# OK
#
# gpg2 -vv john-1.9.0.tar.xz.sign
# Signed by 05C027FD4BDC136E which belongs to "Openwall offline signing key"
# gpg2 --export --export-options export-minimal 297AD21CF86C948081520C1805C027FD4BDC136E > gpgkey-297AD21CF86C948081520C1805C027FD4BDC136E.gpg
Source2:        gpgkey-297AD21CF86C948081520C1805C027FD4BDC136E.gpg

# Align the naming of the fallback binaries with jumbo patch + kali
# https://github.com/openwall/john/issues/5233


BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  libxcrypt-devel

%description
John the Ripper is a fast password cracker (password security auditing
tool). Its primary purpose is to detect weak Unix passwords, but a number
of other hash types are supported as well.


%prep
#check signature
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 1

chmod 0644 doc/*
sed -i 's#\$JOHN/john.conf#%{_sysconfdir}/john.conf#' src/params.h

# Extra charsets - not needed anymore, part of 1.9.0 core release
# tar --strip-components 1 --directory run -xf "%%{SOURCE2}"

%build
%set_build_flags

# WARNING - john makefile is defining -c on the level of CFLAGS and not the compile lines
# when overriding the Makefile we need to keep this logic
ORIGCPU=$(echo "$CFLAGS" | grep -o -E -e '-m(sse2|avx|avx2|avx512|avx512f|xop)( |$)' | tr -d '\n' )
CFLAGS=$(echo "$CFLAGS" | sed -E 's/-m(sse2|avx|avx2|avx512|avx512f|xop)( |$)//;' )
export CFLAGS="$CFLAGS -c -DJOHN_SYSTEMWIDE=1"

# ASFLAGS needs info about libraries same as LDFLAGS, but needs -c for compilation only
export ASFLAGS="-c $LDFLAGS"

# By default build with "make generic"
ARCH_CHAIN="generic"
%global with_fallback 0

# By default quote fallback binary name with just "
Q='"'
%ifarch %{ix86} || x86_64
# on intel quote with '\"' ... do not ask me why
Q='\"'
%endif






# i686 settings
%ifarch %{ix86}
# Fedora current settings starts on sse2 so it is not necessary going bellow that
# ARCH_CHAIN="linux-x86-any linux-x86-mmx linux-x86-sse2 linux-x86-avx linux-x86-xop linux-x86-avx2"
ARCH_CHAIN="linux-x86-any linux-x86-sse2 linux-x86-avx linux-x86-xop linux-x86-avx2"
%if (0%{?fedora}) || ( 0%{?rhel} >= 8 )
ARCH_CHAIN="$ARCH_CHAIN linux-x86-avx512"
%endif
%global with_fallback 1
%endif

%ifarch x86_64
ARCH_CHAIN="linux-x86-64 linux-x86-64-avx linux-x86-64-xop linux-x86-64-avx2"
%if (0%{?fedora}) || ( 0%{?rhel} >= 8 )
ARCH_CHAIN="$ARCH_CHAIN linux-x86-64-avx512"
%endif
%global with_fallback 1
%endif

%ifarch ppc
ARCH_CHAIN="linux-ppc32 linux-ppc32-altivec"
%endif

%ifarch ppc64
ARCH_CHAIN="linux-ppc64 linux-ppc64-altivec"
%endif

# Compile the fallback binary
ARCH_FIRST=$( echo "${ARCH_CHAIN}" | cut -d ' ' -f 1 )

# WARNING: original LDFLAGS in Makefile contain -s to strip the binaries
# We need to override that
make -C src "${ARCH_FIRST}" CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}" ASFLAGS="${ASFLAGS}"
mv run/john "run/john-${ARCH_FIRST}-non-omp"

# Compile whole chain of binaries, if configured
set $ARCH_CHAIN
while true ; do
    if [ -z $2 ] ; then
        break
    fi
    PREV="$1"
    TARGET="$2"
    # Fallback binary definition is used in #define as a string, pre-procesor seamlessly joins the strings together without using string functions like:
    # gcc -DCPU_FALLBACK_BINARY='"john-linux-x86-64-xop"' ...
    # #define OMP_FALLBACK_PATHNAME JOHN_SYSTEMWIDE_EXEC "/" OMP_FALLBACK_BINARY
    # needs to be double quoted here as one layer is stripped by shell and one by make
    CPU_FALLBACK="${Q}john-${PREV}-non-omp${Q}"
    make -C src clean
    make -C src "${TARGET}" CFLAGS="${CFLAGS} -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='${CPU_FALLBACK}'" LDFLAGS="${LDFLAGS}" ASFLAGS="${ASFLAGS}"
    mv run/john "run/john-${TARGET}-non-omp"
    shift
done

# Compile the OMP binary with fallback to CPU binary
make -C src clean
ARCH_FIRST=$( echo "${ARCH_CHAIN}" | cut -d ' ' -f 1 )
OMP_FALLBACK="${Q}john-${ARCH_FIRST}${Q}"
make -C src "${ARCH_FIRST}" CFLAGS="${CFLAGS} -fopenmp -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='${OMP_FALLBACK}'" OMPFLAGS=-fopenmp LDFLAGS="${LDFLAGS} -fopenmp" ASFLAGS="${ASFLAGS} -fopenmp"
mv run/john "run/john-${ARCH_FIRST}-omp"

# Compile whole chain of OMP binaries
set $ARCH_CHAIN
while true ; do
    if [ -z $2 ] ; then
        break
    fi
    PREV="$1"
    TARGET="$2"
    # fallback to previous CPU optimization, if OMP is present
    CPU_FALLBACK="${Q}john-${PREV}-omp${Q}"
    # fallback to same CPU optimization, if OMP is broken
    OMP_FALLBACK="${Q}john-${TARGET}-non-omp${Q}"
    make -C src clean
    make -C src "${TARGET}" CFLAGS="${CFLAGS} -fopenmp -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='${CPU_FALLBACK}' -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='${OMP_FALLBACK}'" OMPFLAGS=-fopenmp LDFLAGS="${LDFLAGS} -fopenmp" ASFLAGS="${ASFLAGS} -fopenmp"
    mv run/john "run/john-${TARGET}-omp"
    shift
done



%install
install -d -m 755 %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/john
install -p -m 755 run/mailer %{buildroot}%{_bindir}
install -p -m 644 run/{*.chr,password.lst} %{buildroot}%{_datadir}/john
install -p -m 644 run/john.conf %{buildroot}%{_sysconfdir}

LASTJOHN=$(ls -t run/john-* | head -n 1)
LASTJOHN=$(basename "$LASTJOHN")
install -d -m 755 %{buildroot}%{_libexecdir}/john
install -p -m 755 run/john-* %{buildroot}%{_libexecdir}/john/

pushd %{buildroot}%{_bindir}
ln -s %{_libexecdir}/john/${LASTJOHN} john
ln -s john unafs
ln -s john unique
ln -s john unshadow

popd
rm doc/INSTALL

%files
%doc doc/*
%config(noreplace) %{_sysconfdir}/john.conf
%{_bindir}/john
%{_bindir}/mailer
%{_bindir}/unafs
%{_bindir}/unique
%{_bindir}/unshadow
%{_datadir}/john/
%{_libexecdir}/john/

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1.9.0-11
- Add explicit BR: libxcrypt-devel

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.0-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Michal Ambroz <rebus _AT seznam.cz> - 1.9.0-4
- align the fallback binary naming with upstream/kali

* Tue Feb 14 2023 Michal Ambroz <rebus _AT seznam.cz> - 1.9.0-3
- add signature verification

* Tue Feb 14 2023 Michal Ambroz <rebus _AT seznam.cz> - 1.9.0-2
- use cpu/omp fallback chaining for binaries

* Tue Feb 14 2023 Michal Ambroz <rebus _AT seznam.cz> - 1.9.0-1
- bump to version 1.9.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.8.0-13
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.8.0-10
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Till Maas <opensource@till.name> - 1.8.0-1
- Adjust release
- remove INSTALL in install to keep it available after prep
- Add john extra charsets
- Use xz

* Fri May 31 2013 Dhiru Kholia <dhiru@openwall.com> - 1.8.0-0
- Update to latest release john-1.8.0 (RH #969157)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Till Maas <opensource@till.name> - 1.7.9-1
- Update to new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Till Maas <opensource@till.name> - 1.7.8-1
- Update to new release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Till Maas <opensource@till.name> - 1.7.6-1
- Update to latest release (RH #626537)
- use less regexes in %%files

* Mon Jan 18 2010 Till Maas <opensource@till.name> - 1.7.3.4-1
- Update to new release
- fix Source0
- add missing -m parameters to install
- set LDFLAGS to RPM_OPT_FLAGS for non mmx build
- add signature as Source1

* Fri Jan 08 2010 Till Maas <opensource@till.name> - 1.7.0.2-9
- Use %%global instead of %%define

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.7.0.2-6
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Till Maas <opensource till name> - 1.7.0.2-5
- update License Tag
- bump release for rebuild

* Sun May 05 2007 Till Maas <opensouce till name> - 1.7.0.2-4
- use correct target for ppc64

* Tue Feb 27 2007 Till Maas <opensource till name> - 1.7.0.2-3
- fixing wrong characters in specfile
- https://bugzilla.redhat.com/bugzilla/attachment.cgi?id=148873&action=view

* Wed Jan 10 2007 Till Maas <opensource till name> - 1.7.0.2-2
- no mmx version for x86_64 since it is 32bit and does not build

* Tue Jan 09 2007 Till Maas <opensource till name> - 1.7.0.2-1
- prevent stripping in Makefile to get non-empty debuginfo
- version bump
- build mmx and fallback version

* Mon Oct 09 2006 Jeremy Katz <katzj@redhat.com> - 1.6-5
- FC6 Rebuild

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.6-4
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Apr 25 2003 Marius Johndal <mariuslj at ifi.uio.no> 0:1.6-0.fdr.2
- Added epoch.
- Modified makefile patch to honour %%optflags.
- setup -q.
- Added full URL of source.

* Thu Mar  6 2003 Marius Johndal <mariuslj at ifi.uio.no> 1.6-0.fdr.1
- Initial Fedora RPM release.

* Sat Dec  7 2002 Marius Johndal <mariuslj at ifi.uio.no>
- Misc. RH 8.0 changes.

* Mon Dec  2 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.6-2mdk
- config file in /etc
- fix configuration problem

* Mon Sep 16 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.6-1mdk
- first mdk version
