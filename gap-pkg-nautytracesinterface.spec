# There have been no official releases yet, so we pull from git
%global gitdate  20220727
%global gittag   34316a24d4f5904a513a6d55ad86085e337865cf
%global shorttag %(cut -b -7 <<< %{gittag})
%global user     gap-packages
%global pkgname  nautytracesinterface

# When bootstrapping a new architecture, there is no gap-pkg-digraphs package
# yet.  It is only needed for testing this package, but it requires this package
# to function at all.  Therefore, do the following:
# 1. Build this package in boostrap mode.
# 2. Build gap-pkg-digraphs.
# 3. Build this package in non-boostrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        0.2
Release:        24.%{gitdate}git%{shorttag}%{?dist}
Summary:        GAP interface to nauty and Traces

License:        GPL-2.0-or-later
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://github.com/%{user}/NautyTracesInterface
Source0:        https://github.com/%{user}/NautyTracesInterface/tarball/%{gittag}/%{user}-%{pkgname}-%{shorttag}.tar.gz
# Fedora-only patch: use the system nauty library
Patch0:         %{name}-nauty.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
%if %{without bootstrap}
BuildRequires:  gap-pkg-digraphs
BuildRequires:  gap-pkg-grape
%endif
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(nauty)

Requires:       gap-core%{?_isa}

%description
This GAP package provides an interface to nauty and Traces.

%package doc
Summary:        NautyTracesInterface documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{user}-NautyTracesInterface-%{shorttag}

# Make sure the bundled nauty is not used
rm -fr nauty*

# Generate the configure script
autoreconf -fi

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{gap_dir} --with-nauty=%{_includedir}/nauty \
  --disable-silent-rules
%make_build
%make_build doc

%install
# make install doesn't put ANYTHING where it is supposed to go, so...
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a bin examples gap tst *.g %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g
%endif

%files
%doc README.md
%license LICENSE
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/
%exclude %{gap_dir}/pkg/%{pkgname}/examples/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%docdir %{gap_dir}/pkg/%{pkgname}/examples/
%{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/examples/

%changelog
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
