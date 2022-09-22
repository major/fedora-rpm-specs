%global pkgname orb

%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        4.8.5
Release:        1%{?dist}
Summary:        Methods to enumerate orbits in GAP

License:        GPLv3+
URL:            https://gap-packages.github.io/orb/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz
# Indexes needed for the tests
Source2:         https://www.math.rwth-aachen.de/~mfer/mfertoc.json
Source3:         https://www.math.rwth-aachen.de/~Thomas.Breuer/ctblocks/ctblockstoc.json

# The AtlasRep, Browse and CtblLib dependencies are needed for the tests only
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

# Only pull in test dependencies in non-bootstrap mode, because gap-pkg-cvec
# requires this package to run at all.
%if %{without bootstrap}
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-browse
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-cvec
BuildRequires:  gap-pkg-tomlib
%endif

Requires:       gap-pkg-io%{?_isa}

%description
This package enables enumerating orbits in various ways from within GAP.

%package doc
Summary:        ORB documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -b 1
cp -p %{SOURCE2} %{SOURCE3} ../atlasrep

%build
export LC_ALL=C.UTF-8
export CFLAGS='%{build_cflags} -D_FILE_OFFSET_BITS=64'
# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure --with-gaproot=%{_gap_dir}
%make_build V=1

# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
gap < makedoc.g
rm -fr ../../doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
cp -a bin doc examples gap tst *.g %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/{clean,test}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

# Install the shared object without libtool artifacts
pushd %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
rm orb.*
mv .libs/orb.so .
rm -fr .libs
popd

%if %{without bootstrap}
%check
export LC_ALL=C.UTF-8

# Skip the speed test; this is for correctness only
rm -f tst/orbitspeedtest.g

# Find the ATLAS version number
atlasdir=$(ls -1d %{_gap_dir}/pkg/atlasrep-*)

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
SetUserPreference( "AtlasRep", "AtlasRepTOCData", [
  "core|$atlasdir/atlasprm.json",
  "internal|$atlasdir/datapkg/toc.json",
  "mfer|%{_builddir}/atlasrep/mfertoc.json" ,
  "ctblocks|%{_builddir}/atlasrep/ctblockstoc.json" ] );
EOF

gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g
%endif

%files
%doc CHANGES README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%changelog
* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 4.8.5-1
- Version 4.8.5

* Sun Jul 24 2022 Jerry James <loganjerry@gmail.com> - 4.8.4-3
- Add TOC data to fix the tests with recent versions of atlasrep

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep  7 2021 Jerry James <loganjerry@gmail.com> - 4.8.4-1
- Version 4.8.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 4.8.3-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep  4 2019 Jerry James <loganjerry@gmail.com> - 4.8.3-1
- New upstream version
- Add files needed for testing

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 4.8.2-2
- Rebuild for changed bin dir name in gap 4.10.1
- Do not install libtool artifacts

* Sat Feb 23 2019 Jerry James <loganjerry@gmail.com> - 4.8.2-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 4.8.1-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Jerry James <loganjerry@gmail.com> - 4.8.0-1
- New upstream version (bz 1511917)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 4.7.6-1
- New upstream version (bz 1315679)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Jerry James <loganjerry@gmail.com> - 4.7.5-1
- New upstream version (bz 1300480)

* Fri Jan  8 2016 Jerry James <loganjerry@gmail.com> - 4.7.4-1
- New upstream version
- Update URLs

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 4.7.3-2
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Fri Jul 24 2015 Jerry James <loganjerry@gmail.com> - 4.7.3-1
- Initial RPM
