%if 0%{?rhel} == 7
%global docutils python34-docutils
%global rst2man rst2man-3.4
%else
%global docutils python3-docutils
%global rst2man rst2man
%endif

Name: vmod-uuid
Summary: UUID module for Varnish Cache
Version: 1.10
Release: 22%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://github.com/otto-de/libvmod-uuid
Source0: https://github.com/otto-de/lib%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: varnish%{?_isa} = %(pkg-config --silence-errors --modversion varnishapi || echo 0)
Requires: uuid

BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: uuid-devel
BuildRequires: varnish-devel >= 6.3.0
BuildRequires: varnish
BuildRequires: check-devel

# To build from a git checkout, add these
BuildRequires: automake
BuildRequires: libtool
BuildRequires: %docutils
BuildRequires: autoconf-archive


%description
UUID Varnish vmod used to generate a uuid, including versions 1, 3, 4 and 5
as specified in RFC 4122. See the RFC for details about the various versions.


%prep
%setup -q -n lib%{name}-%{version}


%build
./autogen.sh
export RST2MAN=%rst2man
%configure \
  --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# We have to remove rpath - not allowed in Fedora
# (This problem only visible on 64 bit arches)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
        s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%check
%make_build check


%install
%make_install

# None of these for fedora/epel
find %{buildroot}/%{_libdir}/ -name '*.la' -delete
find %{buildroot}/%{_libdir}/ -name  '*.a' -delete


%files
%{_libdir}/varnish*/vmods/
%license LICENSE
%doc README.rst COPYING
%{_mandir}/man3/*.3*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 06 2024 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-21
- Rebuild for varnish-7.6.1

* Wed Sep 18 2024 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-20
- Rebuild for varnish-7.6.0

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10-19
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 23 2024 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-17
- Rebuilt for varnish-7.5.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-15
- Rebuilt for varnish-7.4.2

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-13
- Rebuilt for varnish-7.3.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-11
- Rebuilt for varnish-7.2.1

* Mon Sep 26 2022 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-10
- Rebuilt for varnish-7.2.0

* Mon Aug 15 2022 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-9
- Rebuilt for varnish-7.1.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 04 2022 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-7
- Rebuilt for varnish-7.1.0

* Tue Feb 08 2022 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-6
- Rebuilt for varnish-7.0.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.10-4
- Rebuilt for varnish-7.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.10-2
- Rebuilt for varnish-6.6.1

* Tue May 18 2021 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.10-1
- New upstream release
- Dropped patches included in this release
- Built for varnish-6.6.0

* Fri Mar 26 2021 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.9-1
- New upstream release
- Added patch for autoconf-2.71 from upstream, closes rhbz #1943109

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.8-2
- Built for varnish-6.5.1

* Mon Sep 21 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.8-1
- New upstream release 1.8
- Built for varnish-6.5.0
- Added hacks for newer varnish on older rhel derivates

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 26 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-8
- Rebuilt against varnish-6.4.0

* Thu Mar 26 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-7
- Rebuilt against varnish-6.3.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-5
- Rebuilt against varnish-6.3.1

* Wed Sep 25 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-4
- Rebuilt against varnish-6.3.0-2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-2
- Source tarball has no prebuilt manpages, so buildrequires python3-docutils
  for rst2man
- Now run make check in parallel

* Fri Feb 15 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-1
- New upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5-3
- Rebuilt against varnish-6.1.1

* Thu Oct 11 2018 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5-2
- Rebuilt against varnish-6.0.1

* Tue Aug 07 2018 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5-1
- New upstream release
- Removed patch merged upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.3-4
- Patched away obsolete m4 macro

* Fri Dec 08 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.3-3
- Added pkg-config call to compute correct varnish version dependency
- Removed el6 hacks from fedora candidate package
- Simplified and cleaned up macro usage and other cosmetics according to
  package review
- Added COPYING to doc

* Mon Nov 06 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.3-2
- Set a readable homepage URL
- Removed Group and BuildRoot tags
- Set _isa macro on varnish requirement
- Use license macro on all builds
- Build fixes for el6 added, though commented out (requires a dist tarball)

* Fri Nov 03 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.3-1
- New upstream release 1.3 aka ec75ddd

