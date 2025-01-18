Name:       diffmark
Version:    0.10
Release:    35%{?dist}
Summary:    XML diff and merge
# COPYING:          diffmark license text
# lib/lcs.hh:       GPL-1.0-or-later OR Artistic-1.0-Perl   (based on Algorithm-Diff)
# lib/xutil.hh:     GPL-1.0-or-later OR Artistic-1.0-Perl   (based on XML-LibXML dom.c)
## Not in any binary package
# aclocal.m4:       FSFUL AND FSFULLR AND FSFULLRWD AND GPL-2.0-or-later WITH Libtool-exception
#                   AND GPL-2.0-or-later WITH Autoconf-exception-generic
# cmd/Makefile.in:  FSFULLRWD
# config.guess:     GPL-2.0-or-later WITH Autoconf-exception-generic
# config.sub:       GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:        FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# depcomp:          GPL-2.0-or-later WITH Autoconf-exception-generic
# diffmark.test/Makefile.in:        FSFULLRWD
# doc/Makefile.in:  FSFULLRWD
# install-sh:       X11
# lib/Makefile.in:  FSFULLRWD
# ltmain.sh:        GPL-2.0-or-later WITH Libtool-exception
# Makefile.in:      FSFULLRWD
# missing:          GPL-2.0-or-later WITH Autoconf-exception-generic
# testdata/diff/Makefile.in:        FSFULLRWD
# testdata/faildiff/Makefile.in:    FSFULLRWD
# testdata/failmerge/Makefile.in:   FSFULLRWD
# testdata/Makefile.in:             FSFULLRWD
# testdata/merge/Makefile.in:       FSFULLRWD
# testdata/roundup/Makefile.in:     FSFULLRWD
License:    diffmark AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
SourceLicense: %{license} AND FSFUL AND FSFULLR AND FSFULLRWD AND X11 AND GPL-2.0-or-later WITH Libtool-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic
URL:        http://www.mangrove.cz/%{name}/
Source0:    %{url}%{name}-%{version}.tar.gz
# Remove a superfluous RPATH from the programs
Patch0:     %{name}-0.09-remove_rpath.patch
# Adjust to GCC 11 that defaults to -std=gnu++17 that forbirds non-const
# comparison objects
Patch1:     %{name}-gcc11.patch
# Because of diffmark-0.08-remove_rpath.patch:
# And to update config.sub to support aarch64, bug #925255
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make

%description
This is an XML diff and merge package. It consists of a shared library and
two utilities: dm and dm-merge. 

%package        devel
Summary:        Development files for %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for developing applications that use %{name}.

%prep
%autosetup -p1
# automake -i -f to support aarch64, bug #925255
libtoolize --force && autoreconf -i -f

%build
%configure --enable-shared --disable-static
%{make_build}

%install
%{make_install}
find "$RPM_BUILD_ROOT" -name '*.la' -delete

%files
%license COPYING
%doc doc/*.html README
%{_bindir}/dm
%{_bindir}/dm-merge
%{_libdir}/libdiffmark.so.1{,.*}

%files devel
%{_includedir}/diffmark
%{_libdir}/libdiffmark.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Petr Pisar <ppisar@redhat.com> - 0.10-34
- Convert a License tag to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Petr Pisar <ppisar@redhat.com> - 0.10-24
- Modernize a spec file
- License corrected to "diffmark and (GPL+ or Artistic)"

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 0.10-23
- Make comparison object invocable as const

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Petr Pisar <ppisar@redhat.com> - 0.10-17
- Modernize spec file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Remi Collet <remi@fedoraproject.org> - 0.10-10
- rebuild with gcc 5 (thanks Koschei)

* Mon Feb 16 2015 Remi Collet <remi@fedoraproject.org> - 0.10-9
- rebuild with gcc 5 (thanks Koschei)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Petr Pisar <ppisar@redhat.com> - 0.10-5
- Update config.sub to support aarch64 (bug #925255)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Tue Nov 15 2011 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump

* Thu Oct 27 2011 Petr Pisar <ppisar@redhat.com> - 0.08-1
- Version 0.08 packaged


