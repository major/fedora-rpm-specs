%global pkgname  cvec

Name:           gap-pkg-%{pkgname}
Version:        2.7.6
Release:        1%{?dist}
Summary:        Compact vectors over finite fields

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/cvec/
Source0:        https://github.com/gap-packages/cvec/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-orb-doc
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}

%description
The CVEC package provides an implementation of compact vectors over
finite fields.  Contrary to earlier implementations no table lookups are
used but only word-based processor arithmetic.  This allows for bigger
finite fields and higher speed.

%package doc
Summary:        CVEC documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-orb-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -b 1

%build
export LC_ALL=C.UTF-8

# This is NOT an autotools-generated configure script; do NOT use %%configure
./configure --with-gaproot=%{_gap_dir}
%make_build V=1

# Build the documentation
make doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -p bin/%{_gap_arch}/.libs/cvec.so \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -a doc example gap local test tst *.g \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8

# Find the ATLAS version number
atlasdir=$(ls -1d %{_gap_dir}/pkg/atlasrep-*)

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README.md TIMINGS TODO
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/example/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/example/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/example/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.7.6-1
- Convert License tag to SPDX

* Sat Aug  6 2022 Jerry James <loganjerry@gmail.com> - 2.7.6-1
- Version 2.7.6
- Move TOC data into the testdata tarball

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 2.7.5-3
- Add TOC data to fix the tests with recent versions of atlasrep

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep  7 2021 Jerry James <loganjerry@gmail.com> - 2.7.5-1
- Version 2.7.5

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 2.7.4-5
- Drop aarch64 workaround

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 2.7.4-4
- Rebuild for gap 4.11.0
- Add atlasrep and tomlib BRs so that all tests can be run

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 2.7.4-1
- New upstream version

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 2.7.2-1
- New upstream version

* Mon Mar  4 2019 Jerry James <loganjerry@gmail.com> - 2.7.1-1
- New upstream version

* Wed Feb 20 2019 Jerry James <loganjerry@gmail.com> - 2.7.0-1
- New upstream version

* Tue Dec 18 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.6.1-1
- Initial package.
