# There have been no official releases yet, so we pull from git
%global gitdate  20241107
%global gittag   8ce9b7bc36a3d1c96b5e98f875e08c724238ec2c
%global shorttag %(cut -b -7 <<< %{gittag})
%global user     gap-packages
%global pkgname  nautytracesinterface
%global giturl   https://github.com/gap-packages/NautyTracesInterface

# When bootstrapping a new architecture, there is no gap-pkg-digraphs package
# yet.  It is only needed for testing this package, but it requires this package
# to function at all.  Therefore, do the following:
# 1. Build this package in boostrap mode.
# 2. Build gap-pkg-digraphs.
# 3. Build this package in non-boostrap mode.
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        0.2
Release:        36.%{gitdate}git%{shorttag}%{?dist}
Summary:        GAP interface to nauty and Traces

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/NautyTracesInterface/
VCS:            git:%{giturl}.git
Source:         %{giturl}/tarball/%{gittag}/%{user}-%{pkgname}-%{shorttag}.tar.gz
# Fedora-only patch: use the system nauty library
Patch:          %{name}-nauty.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
%if %{without bootstrap}
BuildRequires:  gap-pkg-digraphs
BuildRequires:  gap-pkg-grape
%endif
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libnauty)

Requires:       gap-core%{?_isa}

%description
This GAP package provides an interface to nauty and Traces.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        NautyTracesInterface documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{user}-NautyTracesInterface-%{shorttag}

%conf
# Make sure the bundled nauty is not used
rm -fr nauty*

# Generate the configure script
autoreconf -fi

%build
%configure --with-gaproot=%{gap_archdir} --with-nauty=%{_includedir}/nauty \
  --disable-silent-rules
%make_build
%make_build doc

%install
# make install doesn't put ANYTHING where it is supposed to go, so...
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a bin examples gap tst *.g %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g
%endif

%files
%doc README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/gap/
%{gap_archdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/examples/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/examples/

%changelog
* Mon Nov 25 2024 Jerry James <loganjerry@gmail.com> - 0.2-36.20241107git8ce9b7b
- Update to use the kext interface in gap 4.12+

* Mon Sep 23 2024 Jerry James <loganjerry@gmail.com> - 0.2-35.20240323git062bd47
- Rebuild for nauty 2.8.9

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-34.20240323git062bd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 13 2024 Jerry James <loganjerry@gmail.com> - 0.2-33.20240323git062bd47
- Update for gap 4.13.1

* Sat Mar 16 2024 Jerry James <loganjerry@gmail.com> - 0.2-32.20221102gitd54d393
- Rebuild for gap 4.13.0

* Tue Jan 23 2024 Jerry James <loganjerry@gmail.com> - 0.2-31.20221102gitd54d393
- Rebuild for nauty 2.8.8

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-30.20221102gitd54d393
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-29.20221102gitd54d393
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-28.20221102gitd54d393
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 0.2-27.20221102gitd54d393
- Update for split GAP directories

* Wed Dec  7 2022 Jerry James <loganjerry@gmail.com> - 0.2-26.20221102gitd54d393
- Rebuild for nauty 2.8.6

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 0.2-25.20221102gitd54d393
- Update to latest git snapshot for minor build system enhancements
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 0.2-24.20220727git34316a2
- Update to latest git snapshot for gap 4.12.0 support
- Convert License tag to SPDX

* Sun Jul 24 2022 Jerry James <loganjerry@gmail.com> - 0.2-23.20210519git9d2172c
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-22.20210519git9d2172c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-21.20210519git9d2172c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-20.20210519git9d2172c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Jerry James <loganjerry@gmail.com> - 0.2-19.20210519git9d2172c
- Update to latest git snapshot for infrastructure bug fixes

* Wed Feb 24 2021 Jerry James <loganjerry@gmail.com> - 0.2-18.20201207git3fdbfb4
- Update to latest git snapshot for bug fixes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-17.20200603gitf0941ec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-16.20200603gitf0941ec
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Jerry James <loganjerry@gmail.com> - 0.2-15.20200603gitf0941ec
- Update to latest git snapshot due to digraphs changes

* Tue Jun  2 2020 Jerry James <loganjerry@gmail.com> - 0.2-14.20200501git052eba5
- Update to latest git snapshot for further improvements

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 0.2-13.20191001git524c784
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12.20190920git24482e5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Jerry James <loganjerry@gmail.com> - 0.2-11.20190920git24482e5
- Update to latest git snapshot for further improvements
- Drop upstreamed -test patch
- New URLs

* Fri Sep 13 2019 Jerry James <loganjerry@gmail.com> - 0.2-10.20190912git7a658d8
- Update to latest git snapshot for improved tests
- Only run the tests for a non-bootstrap build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9.20181127git6497df8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 0.2-8.20181127git6497df8
- Rebuild for changed bin dir name in gap 4.10.1

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 0.2-7.20181127git6497df8
- Update to latest git snapshot for gap 4.10.0
- Add -test patch
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6.20180710gitc037e1a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov  7 2018 Jerry James <loganjerry@gmail.com> - 0.2-5.20180710gitc037e1a
- Update to latest git snapshot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4.20180309git8b63a9c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jerry James <loganjerry@gmail.com> - 0.2-3.20180309git8b63a9c
- Update to recent git snapshot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2.20171120git5f16120
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Jerry James <loganjerry@gmail.com> - 0.2-1.20171120git5f16120
- Use autosetup
- Fix version number

* Tue Nov 28 2017 Jerry James <loganjerry@gmail.com> - 0.1-1.20171120git5f16120
- Initial RPM
