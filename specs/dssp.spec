# Copyright (c) 2015 Dave Love, Liverpool University
# The licence for this file is as for the package itself.

Name:		dssp
Version:	3.0.0
Release:	25%{?dist}
Summary:	Protein secondary structure assignment
%{?el5:Group:		Applications/Engineering}
License:	BSL-1.0
URL:		http://swift.cmbi.ru.nl/gv/dssp/
Source0:	ftp://ftp.cmbi.ru.nl/pub/software/dssp/dssp-%version.tgz
# don't suppress make output
Patch1:		dssp-make.patch
# Fix build with boost 1.66 (#1537546)
Patch2:		dssp-tuple.patch
BuildRequires:	zlib-devel bzip2-devel boost-devel gcc-c++
BuildRequires: make

%if 0%{?epel} < 7
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%endif

%description
The DSSP program standardizes protein secondary structure assignment.
DSSP is a database of secondary structure assignments (and much more)
for all protein entries in the Protein Data Bank (PDB).  DSSP is also
the program that calculates DSSP entries from PDB entries.  DSSP does
not predict secondary structure.

References:
"A series of PDB related databases for everyday needs.", Robbie
P. Joosten, Tim A.H. te Beek, Elmar Krieger, Maarten L. Hekkelman, Rob
W.W. Hooft, Reinhard Schneider, Chris Sander, and Gert Vriend.
Nucleic Acids Research 2011 January; 39(Database issue): D411-D419.
doi: 10.1093/nar/gkq1105

"Dictionary of protein secondary structure: pattern recognition of
hydrogen-bonded and geometrical features.", Kabsch W, Sander C,
Biopolymers. 1983 22 2577-2637.

%prep
%setup -q
%patch -P1 -p1 -b .make
%patch -P2 -p1 -b .tuple
chmod -x src/buffer.h


%build
# This changed somewhere between EPEL6 and Fedora 21.
## Set Boost's library directories
if [ -f %{_libdir}/%{?el5:boost141/}libboost_thread-mt.so ]; then
  echo "BOOST_LIB_SUFFIX = -mt" > make.config
else
  echo "BOOST_LIB_SUFFIX = " > make.config
fi
echo "CFLAGS=$RPM_OPT_FLAGS -I/usr/include
LDOPTS=%__global_ldflags -L%_libdir" >>make.config
# The original makefile uses -O3, presumably for good reason, but
# avoid compiler ICE on ppc64le (#1280387).
%ifarch ppc64le
COPT=-O2 \
%endif
make %{?_smp_mflags}


%install
make install DEST_DIR=%_prefix DESTDIR=$RPM_BUILD_ROOT
chmod -x $RPM_BUILD_ROOT%_mandir/man1/*


%{!?_licensedir:%global license %%doc}
%files
%license LICENSE_1_0.txt
%doc changelog README.txt
%_bindir/mkdssp
%_mandir/man1/mkdssp.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 3.0.0-21
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 3.0.0-19
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  8 2022 Dave Love <loveshack@fedoraproject.org> - 3.0.0-17
- Use SPDX licence TAG

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 3.0.0-15
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0.0-13
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0.0-10
- Rebuilt for Boost 1.75

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 3.0.0-8
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 3.0.0-4
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Dave Love <loveshack@fedoraproject.org> - 3.0.0-1
- New version
- Clean up el5-isms
- Patch to fix #1537546

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 2.2.1-14
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 2.2.1-13
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 2.2.1-11
- Rebuilt for Boost 1.63

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 2.2.1-10
- Rebuilt for linker errors in boost (#1331983)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Dave Love <loveshack@fedoraproject.org> - 2.2.1-8
- Rebuild for new boost

* Sun Dec 13 2015 Dave Love <loveshack@fedoraproject.org> - 2.2.1-7
- Avoid compiler ICE on ppc64le (#1280387)

* Thu Jul 30 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.1-6
- Use __global_ldflags and Boost paths unconditionally per review

* Fri May 29 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.1-5
- Support epel5
- Other review nitpicks

* Fri Apr 10 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.1-4
- Maybe use %%licence

* Mon Mar 30 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.1-3
- Review: Patch makefile to use DESTDIR and set BOOST_LIB_SUFFIX in
  make.conf, not environment

* Tue Feb 10 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.1-2
- Adjust BOOST_LIB_SUFFIX correctly

* Mon Feb  9 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.1-1
- Initial packaging
