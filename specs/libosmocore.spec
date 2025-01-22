%global git_commit 32ee5af8935406578a2b811bd3cec65e980d2918
%global git_date 20170220

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

# git clone git://git.osmocom.org/libosmocore.git
# cd %%{name}
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{git_commit} | \
# bzip2 > ../%%{name}-%%{version}-%%{git_suffix}.tar.bz2

Name:             libosmocore
URL:              https://osmocom.org/projects/libosmocore
Version:          0.9.6
Release:          25.%{git_suffix}%{?dist}
# Automatically converted from old format: GPLv2+ and GPLv3+ and AGPLv3+ - review is highly recommended.
License:          GPL-2.0-or-later AND GPL-3.0-or-later AND AGPL-3.0-or-later
BuildRequires:    autoconf, automake, libtool, pcsc-lite-devel, doxygen
BuildRequires:    libtalloc-devel, findutils, sed, python3
BuildRequires: make
Summary:          Utility functions for OsmocomBB, OpenBSC and related projects
Source0:          %{name}-%{version}-%{git_suffix}.tar.bz2

%description
A collection of common code used in various sub-projects inside the Osmocom
family of projects (OsmocomBB, OpenBSC, ...).

%package devel
Summary:          Development files for libosmocore
Requires:         %{name}%{?_isa} = %{version}-%{release}
# for /usr/include/osmocom directory
Requires:         libosmo-dsp-devel, libtalloc-devel

%description devel
Development files for libosmocore.

%package doc
Summary:        Documentation files for libosmocore
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation files for libosmocore.

%prep
%setup -q

# fix hashbangs for python3
sed -i '1 s|.*|#!%{__python3}|' utils/conv_gen.py utils/conv_codes_gsm.py

# use python3 instead of python2
sed -i '/python2/ s/python2/python3/g' src/gsm/Makefile.am

%build
# Fix pkg-config version, workaround for rhbz#1692517, the fix should be upstreamed
# so it could be dropped upon next rebase
test -x ./git-version-gen && echo %{version}-%{release} > .tarball-version 2>/dev/null

autoreconf -fi
%configure

# Fix unused direct shlib dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}
# Remove libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} \;

%check
make check

%ldconfig_scriptlets

%files
%doc %{_docdir}/%{name}
# fallback for cases where there is no _licensdir
%exclude %{_docdir}/%{name}/codec
%exclude %{_docdir}/%{name}/core
%exclude %{_docdir}/%{name}/gsm
%exclude %{_docdir}/%{name}/vty
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/osmocom/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_docdir}/%{name}/codec
%doc %{_docdir}/%{name}/core
%doc %{_docdir}/%{name}/gsm
%doc %{_docdir}/%{name}/vty

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-25.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.6-24.20170220git32ee5af8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-23.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-22.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-21.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-20.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-19.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-18.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-17.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-16.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-15.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-14.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.6-13.20170220git32ee5af8
- Switched to python3
  Resolves: rhbz#1807943

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-12.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-11.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.6-10.20170220git32ee5af8
- Updated URL
  Related: rhbz#1692517

* Tue Mar 26 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.6-9.20170220git32ee5af8
- Fixed version in pkg-config file
  Resolves: rhbz#1692517

* Tue Feb  5 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.6-8.20170220git32ee5af8
- Fixed FTBFS in f30

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-6.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.6-4.20170220git32ee5af8
- Added libtalloc-devel requirement to devel package
  Resolves: rhbz#1487734

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2.20170220git32ee5af8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.6-1.20170220git32ee5af8
- New version
- Dropped ppc-smscb-fix (upstreamed)
- Fixed compilation with GCC-7
  Resolves: rhbz#1423868

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5.20151109git916423ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4.20151109git916423ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec  9 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.0-3.20151109git916423ef
- Fixed library to pass smscb test on ppc
  Resolves: rhbz#1289940

* Wed Dec  2 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.0-2.20151109git916423ef
- Updated according to review

* Mon Nov  9 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.0-1.20151109git916423ef
- Initial version
