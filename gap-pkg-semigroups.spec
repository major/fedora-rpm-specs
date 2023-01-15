%global pkgname semigroups

# The standard test suite now regularly consumes on the order of 30GB of
# memory.  This is more than the 32-bit builders can access, and more than even
# some of the 64-bit builders have available (depending on what else is running
# on the same machine).  We skip that test suite.  Brave package maintainers
# with sufficient RAM should build --with-bigtest.
%bcond_with bigtest

Name:           gap-pkg-%{pkgname}
Version:        5.2.0
Release:        2%{?dist}
Summary:        GAP methods for semigroups

License:        GPL-3.0-or-later
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://semigroups.github.io/Semigroups/
Source0:        https://github.com/semigroups/Semigroups/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-datastructures
BuildRequires:  gap-pkg-digraphs-doc
BuildRequires:  gap-pkg-ferret
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-images-doc
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-orb
BuildRequires:  gap-pkg-smallsemi-doc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libsemigroups)
BuildRequires:  tex(a4wide.sty)

Requires:       gap-pkg-datastructures%{?_isa}
Requires:       gap-pkg-digraphs%{?_isa}
Requires:       gap-pkg-genss
Requires:       gap-pkg-images
Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}

Suggests:       gap-pkg-grape%{?_isa}

%description
This is a GAP package containing methods for semigroups, monoids, and
inverse semigroups, principally of transformations, partial
permutations, bipartitions, subsemigroups of regular Rees 0-matrix
semigroups, free inverse semigroups, free bands, and semigroups of
matrices over finite fields.

Semigroups contains more efficient methods than those available in the
GAP library (and in many cases more efficient than any other software)
for creating semigroups, monoids, and inverse semigroup, calculating
their Green's structure, ideals, size, elements, group of units, small
generating sets, testing membership, finding the inverses of a regular
element, factorizing elements over the generators, and many more.  It is
also possible to test if a semigroup satisfies a particular property,
such as if it is regular, simple, inverse, completely regular, and a
variety of further properties.

There are methods for finding congruences of certain types of
semigroups, the normalizer of a semigroup in a permutation group, the
maximal subsemigroups of a finite semigroup, and smaller degree partial
permutation representations of inverse semigroups.  There are functions
for producing pictures of the Green's structure of a semigroup, and for
drawing bipartitions.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Semigraphs documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-digraphs-doc
Requires:       gap-pkg-images-doc
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-smallsemi-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

# Do not use the bundled libsemigroups
rm -fr libsemigroups

# Do not override our build flags
sed -i 's/ -O3//' Makefile.in

%build
export LC_ALL=C.UTF-8
export CPPFLAGS="-I%{_includedir}/eigen3"
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules \
  --with-external-libsemigroups --without-march-native

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin data gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
cd tst
gap -l "%{buildroot}%{gap_archdir};" << EOF
LoadPackage("semigroups");
GAP_EXIT_CODE(Test("testinstall.tst", rec( compareFunction := "uptowhitespace" )));
EOF

%if %{with bigtest}
gap -l "%{buildroot}%{gap_archdir};" teststandard.g
%endif

cd -

%files
%doc CHANGELOG.md README.md VERSIONS
%license GPL LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 5.2.0-2
- Update for split GAP directories

* Mon Dec  5 2022 Jerry James <loganjerry@gmail.com> - 5.2.0-1
- Version 5.2.0

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 5.1.0-1
- Version 5.1.0
- Clarify license of the doc subpackage

* Tue Oct 11 2022 Jerry James <loganjerry@gmail.com> - 5.0.2-2
- Rebuild for libsemigroups 2.3.1

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 5.0.2-1
- Version 5.0.2
- Update for gap 4.12.0
- Convert License tag to SPDX

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 4.0.3-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul  4 2022 Jerry James <loganjerry@gmail.com> - 4.0.3-1
- Version 4.0.3

* Mon Jun  6 2022 Jerry James <loganjerry@gmail.com> - 4.0.2-1
- Version 4.0.2

* Fri Apr 22 2022 Jerry James <loganjerry@gmail.com> - 4.0.1-1
- Version 4.0.1

* Mon Mar  7 2022 Jerry James <loganjerry@gmail.com> - 4.0.0-1
- Version 4.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb  8 2021 Jerry James <loganjerry@gmail.com> - 3.4.2-1
- Version 3.4.2

* Fri Jan 29 2021 Jerry James <loganjerry@gmail.com> - 3.4.1-1
- Version 3.4.1
- Drop upstreamed -libsemigroups patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 3.4.0-1
- Version 3.4.0
- Add -libsemigroups patch

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Jerry James <loganjerry@gmail.com> - 3.3.2-1
- Version 3.3.2

* Fri Jun 12 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-2
- Rebuild for libsemigroups 1.1.0

* Thu May 28 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-1
- Version 3.3.1
- Drop upstreamed -test patch

* Mon May 11 2020 Jerry James <loganjerry@gmail.com> - 3.3.0-1
- Version 3.3.0
- Add BR and R on gap-pkg-images
- Skip the memory-hungry standard tests on all architectures by default

* Fri Apr  3 2020 Jerry James <loganjerry@gmail.com> - 3.2.5-1
- Version 3.2.5
- Drop upstreamed -bool-trim patch

* Wed Mar 25 2020 Jerry James <loganjerry@gmail.com> - 3.2.4-3
- Disable tests on aarch64 again due to random test hangs

* Tue Mar 24 2020 Jerry James <loganjerry@gmail.com> - 3.2.4-2
- Reenable test suite on aarch64

* Sat Feb 29 2020 Jerry James <loganjerry@gmail.com> - 3.2.4-1
- Version 3.2.4
- Add -test patch to fix intermittent FTBFS
- Add -bool-trim patch from upstream to fix bug

* Sat Feb  8 2020 Jerry James <loganjerry@gmail.com> - 3.2.3-1
- Version 3.2.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Jerry James <loganjerry@gmail.com> - 3.2.2-1
- Version 3.2.2

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 3.2.1-1
- Version 3.2.1

* Sat Oct  5 2019 Jerry James <loganjerry@gmail.com> - 3.2.0-1
- New upstream version

* Wed Sep 25 2019 Jerry James <loganjerry@gmail.com> - 3.1.5-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 3.1.3-1
- New upstream version

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 3.1.2-1
- New upstream version
- Drop -libsemigroups patch now that configure supports external lib
- Remove -march=native from build flags

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 3.0.20-1
- New upstream version
- Add -libsemigroups patch to unbundle libsemigroups
- Add -doc subdirectory

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Jerry James <loganjerry@gmail.com> - 2.8.1-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug  5 2016 Jerry James <loganjerry@gmail.com> - 2.8.0-1
- New upstream version
- New URLs

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 2.7.4-1
- New upstream version (bz 1287388)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Jerry James <loganjerry@gmail.com> - 2.6-1
- Initial RPM
