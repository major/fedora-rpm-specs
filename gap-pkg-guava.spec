%global pkgname guava

Name:           gap-pkg-%{pkgname}
Version:        3.16
Release:        3%{?dist}
Summary:        Computing with error-correcting codes

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/guava/
Source0:        https://github.com/gap-packages/guava/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Enable the optional Sonata code.  Upstream says to uncomment this code if
# Sonata is available, and that is all this patch does.
Patch0:         %{name}-sonata.patch
# Patch to fix C compiler warnings that indicate possible runtime problems.
Patch1:         %{name}-warning.patch
# Use popcount instructions where available.
Patch2:         %{name}-popcount.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-sonata
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  parallel

Requires:       gap-core%{?_isa}
Requires:       gap-pkg-sonata

%description
GUAVA is a package that implements coding theory algorithms in GAP.
Codes can be created and manipulated and information about codes can be
calculated.

GUAVA consists of various files written in the GAP language, and an
external program from J. S. Leon for dealing with automorphism groups of
codes and isomorphism testing functions.  Several algorithms that need
the speed are integrated in the GAP kernel.

The functions within GUAVA can be divided into four categories:
- Construction of codes.  GUAVA can construct non-linear, linear and
  cyclic codes over an arbitrary finite field.  Examples are
  HadamardCode, ReedMullerCode, BestKnownLinearCode, QRCode and
  GoppaCode.
- Manipulation of codes.  These functions allow the user to transform
  one code into another or to construct a new code from two codes.
  Examples are PuncturedCode, DualCode, DirectProductCode and UUVCode.
- Computation of information about codes.  This information is stored in
  the code record.  Examples are MinimumDistance, OuterDistribution,
  IsSelfDualCode and AutomorphismGroup.
- Generation of bounds on linear codes.  The table by Brouwer and
  Verhoeff (as it existed in the mid-1990s) is incorporated into GUAVA.
  For example, BoundsMinimumDistance.

%package doc
Summary:        GUAVA documentation
License:        GFDL-1.2-no-invariants-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

# Avoid name collisions in the documentation
cp -p src/ctjhai/README README.ctjhai

%build
# This is NOT an autoconf-generated script.  Do not use %%configure.
./configure %{_gap_dir}

# Building with %%{?_smp_mflags} fails
make CFLAGS="%{build_cflags} -DLONG_EXTERNAL_NAMES" LDFLAGS="%{build_ldflags}"

# Compress large tables
parallel %{?_smp_mflags} --no-notice gzip --best ::: tbl/*.g

# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg/%{pkgname}
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../../doc ../pkg
pushd src/leon/doc
pdftex manual.tex
popd

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
cp -a *.g bin doc lib tbl tst %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
# The documentation tests cannot be run, as they require breaking out of
# infinite loops.  See comments about a user interrupt.
cd tst
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" << EOF
LoadPackage("guava");
if Test("guava.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("decoding.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("hadamard.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
if Test("external.tst", rec( compareFunction := "uptowhitespace" ) ) = false then GAP_EXIT_CODE(1); fi;
EOF

%files
%doc CHANGES.guava HISTORY.guava README.guava README.md README.ctjhai
%doc src/leon/doc/manual.pdf
%license COPYING.guava
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 3.16-3
- Convert License tags to SPDX

* Mon Jul 25 2022 Jerry James <loganjerry@gmail.com> - 3.16-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 25 2022 Jerry James <loganjerry@gmail.com> - 3.16-1
- Version 3.16

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 3.15-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Jerry James <loganjerry@gmail.com> - 3.15-1
- New upstream version
- License change to GPLv3+

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 3.14-5
- Rebuild for changed bin dir name in gap 4.10.1

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 3.14-4
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Jerry James <loganjerry@gmail.com> - 3.14-1
- New upstream version
- Drop upstreamed -bibtex patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan  6 2017 Jerry James <loganjerry@gmail.com> - 3.13.1-3
- Fix a broken submake command

* Fri Aug 19 2016 Jerry James <loganjerry@gmail.com> - 3.13.1-2
- More compiler warnings fixed

* Tue Aug 16 2016 Jerry James <loganjerry@gmail.com> - 3.13.1-1
- Initial RPM
