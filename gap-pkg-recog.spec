# The 1.3.2 release fails multiple tests with GAP 4.11.  Until a new version is
# released, we build from git.
%global commit      168ed6258502ed24a14e284d275b3f50b9f07de3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20200127

%global pkgname recog

Name:           gap-pkg-%{pkgname}
Version:        1.3.2
Release:        9.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Group recognition methods

License:        GPLv3+
URL:            https://gap-packages.github.io/%{pkgname}/
#Source0:        https://github.com/gap-packages/%%{pkgname}/releases/download/v%%{version}/%%{pkgname}-%%{version}.tar.bz2
Source0:        https://github.com/gap-packages/%{pkgname}/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz
# Indexes needed for the tests
Source2:         https://www.math.rwth-aachen.de/~mfer/mfertoc.json
Source3:         https://www.math.rwth-aachen.de/~Thomas.Breuer/ctblocks/ctblockstoc.json

BuildArch:      noarch
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-factint
BuildRequires:  gap-pkg-forms
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-orb
BuildRequires:  gap-pkg-tomlib

Requires:       gap-pkg-atlasrep
Requires:       gap-pkg-factint
Requires:       gap-pkg-forms
Requires:       gap-pkg-genss
Requires:       gap-pkg-orb

%description
This is a GAP package for group recognition.

%package doc
Summary:        Recog documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{commit} -b 1
cp -p %{SOURCE2} %{SOURCE3} ../atlasrep

%build
export LC_ALL=C.UTF-8
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{commit} %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/misc
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{.mailmap,CHANGES,LICENSE,Makefile,NOTES,README.md,TODO,WISHLIST}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8

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

%files
%doc CHANGES NOTES README.md TODO WISHLIST
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
* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 1.3.2-9.20200127.168ed62
- Add TOC data to fix the tests with recent versions of atlasrep

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 1.3.2-4.20200127.168ed62
- Rebuild for gap 4.11.0
- Add missing gap-pkg-orb dependency

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Jerry James <loganjerry@gmail.com> - 1.3.2-2
- Drop the ctbllib and tomlib dependencies

* Thu Oct 24 2019 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Initial RPM
