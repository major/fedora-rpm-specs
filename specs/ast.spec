Name:           ast
Version:        9.2.12
Release:        1%{?dist}
Summary:        A Library for Handling World Coordinate Systems in Astronomy

# proj.c proj.h wcsmath.h wcstrig.c wcstrig.h are LGPLv2+
# Automatically converted from old format: LGPLv3+ and LGPLv2+ - review is highly recommended.
License:        LGPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://starlink.eao.hawaii.edu/starlink/AST
Source0:        https://github.com/Starlink/ast/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  cminpack-devel
BuildRequires:  erfa-devel
BuildRequires:  libpal-devel

%description
The AST library provides a comprehensive range of facilities for attaching
world coordinate systems to astronomical data, for retrieving and interpreting
that information and for generating graphical output based on it. It's main
selling points are:

* Ease of use.
* Facilities for generating plots of generalized non-linear, potentially
  discontinuous 2-D or 3-D coordinate systems, with detailed control of the
  appearance of the plot.
* Facilities for converting transparently between different coordinate
  systems, including a wide range of celestial, spectral and time coordinate
  systems.
* Facilities for searching a general collection of connected coordinate
  systems for a coordinate system with any given set of characteristics.
* Allows code for handling WCS information to be written in a general way
  without regard to the specific nature of the coordinate systems being
  handled (i.e. whether they represent sky positions, spectral positions,
  focal plane positions, pixel positions, etc).
* Flexible system for saving and retrieving WCS information, including (but
  not limited to) a range of different popular FITS descriptions.
* Written in C but has interfaces for C, Fortran, Java (via JNI), Perl, and
  UNIX shell.
* Extensive documentation. 


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

Applications should make use of the ast_link command for setting the
libraries to link to, e.g.:

  cc prog.c `ast_link` -o prog


%package        doc
Summary:        Documentation for %{name}

%description    doc
C and Fortran programming documentation for %{name}.


%prep
%setup -q
rm -r cminpack erfa erfa.h erfam.h pal pal.h
sed -i -e 's,cminpack/,cminpack-1/,' src/polymap.c
sed -i -e '1i#!/bin/bash' ast_link*
# Fix FSF address
sed -i -e 's/675 Mass Ave, Cambridge, MA 02139/51 Franklin Street, Fifth Floor, Boston, MA  02110-1301/' COPYING.LIB


%build
# Do not conflict with libast (bug #978262)
# -std=gnu17 needed for gcc 15 compatibility https://github.com/Starlink/ast/issues/27
%configure CPPFLAGS="-I%{_includedir}/star" CFLAGS="%{optflags} -std=gnu17" --disable-static --libdir=%{_libdir}/%{name} --with-external_cminpack --with-external_pal
%make_build


%install
%make_install
find %buildroot -name '*.la' -delete
# Setup ld.so.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/%{name} > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}_%{_arch}.conf
# Docs are installed to the wrong location, don't need source
mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_prefix}/docs/*.pdf %{buildroot}%{_pkgdocdir}/
rm -r %{buildroot}%{_prefix}/docs
rm -r %{buildroot}%{_datadir}/ast
rm -r %{buildroot}%{_prefix}/{help,manifests,news}
# This references an uninstalled library
rm %{buildroot}%{_bindir}/ast_link_adam
# These reference other libraries
rm %{buildroot}%{_libdir}/%{name}/libast_{drama,ems,pgplot{,3d}}.so*


%check
make check


%files
%license COPYING*
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}_%{_arch}.conf
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so.9*

%files devel
%{_bindir}/ast_link
%{_includedir}/*
%{_libdir}/%{name}/*.so

%files doc
%{_pkgdocdir}/


%changelog
* Sat Feb 01 2025 Orion Poplawski <orion@nwra.com> - 9.2.12-1
- Update to 9.2.12
- Set -std=gnu17 for gcc 15 compatibility (FTBFS rhbz#2339906)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 9.2.10-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 02 2023 Orion Poplawski <orion@nwra.com> - 9.2.10-1
- Update to 9.2.10

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 07 2022 Orion Poplawski <orion@nwra.com> - 9.2.8-1
- Update to 9.2.8

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Orion Poplawski <orion@nwra.com> - 9.2.7-1
- Update to 9.2.7

* Fri Jan 07 2022 Orion Poplawski <orion@nwra.com> - 9.2.6-1
- Update to 9.2.6

* Sun Nov 14 2021 Orion Poplawski <orion@nwra.com> - 9.2.5-1
- Update to 9.2.5
- Build with external pal library

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Orion Poplawski <orion@nwra.com> - 9.2.4-1
- Update to 9.2.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Orion Poplawski <orion@nwra.com> - 9.2.3-1
- Update to 9.2.3

* Mon Sep 21 2020 Orion Poplawski <orion@nwra.com> - 9.2.1-1
- Update to 9.2.1

* Thu Sep 10 2020 Orion Poplawski <orion@nwra.com> - 9.1.3-1
- Update to 9.1.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Orion Poplawski <orion@nwra.com> - 9.1.2-1
- Update to 9.1.2

* Wed Jan 29 2020 Orion Poplawski <orion@nwra.com> - 9.1.0-1
- Update to 9.1.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  8 2019 Orion Poplawski <orion@nwra.com> 9.0.1-1
- Update to 9.0.1 (soname bump)

* Thu Oct  3 2019 Orion Poplawski <orion@nwra.com> 9.0.0-1
- Update to 9.0.0

* Mon Aug 19 2019 Orion Poplawski <orion@cora.nwra.com> 8.7.2-1
- Update to 8.7.2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Orion Poplawski <orion@cora.nwra.com> 8.7.1-1
- Update to 8.7.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Orion Poplawski <orion@cora.nwra.com> 8.6.3-1
- Update to 8.6.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Orion Poplawski <orion@cora.nwra.com> 8.4.0-1
- Update to 8.4.0

* Fri Oct 28 2016 Orion Poplawski <orion@cora.nwra.com> 8.3.0-1
- Update to 8.3.0
- Add BR perl

* Tue Jul 5 2016 Orion Poplawski <orion@cora.nwra.com> 8.2.0-1
- Update to 8.2.0

* Thu Mar 24 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-1
- Update to 8.1.0
- Rebase patches
- Use %%license

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Orion Poplawski <orion@cora.nwra.com> - 8.0.7-2
- Rebuild for cminpack 1.3.4

* Sat Oct 17 2015 Orion Poplawski <orion@cora.nwra.com> 8.0.7-1
- Update to 8.0.7

* Tue Oct 13 2015 Orion Poplawski <orion@cora.nwra.com> 8.0.6-1
- Update to 8.0.6

* Tue Aug 11 2015 Orion Poplawski <orion@cora.nwra.com> 8.0.5-1
- Update to 8.0.5
- Update URL

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Orion Poplawski <orion@cora.nwra.com> 8.0.4-1
- Update to 8.0.4

* Mon Oct 20 2014 Orion Poplawski <orion@cora.nwra.com> 8.0.2-1
- Update to 8.0.2

* Sat Oct 18 2014 Orion Poplawski <orion@cora.nwra.com> 8.0.1-1
- Update to 8.0.1
- Add patch to compile with -Werror=format-security

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Orion Poplawski <orion@cora.nwra.com> 8.0.0-1
- Update to 8.0.0

* Fri Mar 7 2014 Orion Poplawski <orion@cora.nwra.com> 7.3.4-1
- Update to 7.3.4

* Tue Jan 7 2014 Orion Poplawski <orion@cora.nwra.com> 7.3.3-1
- Update to 7.3.3

* Thu Sep 26 2013 Orion Poplawski <orion@cora.nwra.com> 7.3.2-1
- Update to 7.3.2
- Drop path patch applied upstream

* Tue Aug 13 2013 Orion Poplawski <orion@cora.nwra.com> 7.3.1-1
- Update to 7.3.1-1
- Add patch to fix conftest paths

* Sun Aug 11 2013 Orion Poplawski <orion@cora.nwra.com> 6.0.1-6
- Do not conflict with libast (bug #978262)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Orion Poplawski <orion@cora.nwra.com> 6.0.1-2
- Update source to new tarball and URL
- Drop FSF address fixes applied upstream

* Mon Nov 28 2011 Orion Poplawski <orion@cora.nwra.com> 6.0.1-1
- Update to 6.0-1
- Fixup some lib linkages
- Fix license tag
- Fix FSF license
- Fixup doc install
- Drop BuildRoot, clean, defattr

* Fri Oct 14 2011 Orion Poplawski <orion@cora.nwra.com> 5.7.2-1
- Update to 5.7-2
- Truncate description
- Move documentation to subpackage

* Wed Apr 27 2011 Orion Poplawski <orion@cora.nwra.com> 5.6-1
- Initial package
