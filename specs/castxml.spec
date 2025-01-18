%undefine __cmake_in_source_build

Name:		castxml
Version:	0.6.10
Release:	2%{?dist}
Summary:	C-family abstract syntax tree XML output tool

License:	Apache-2.0
URL:		https://github.com/CastXML/CastXML
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	llvm-devel >= 3.6.0
BuildRequires:	clang-devel >= 3.6.0
BuildRequires:	libedit-devel
BuildRequires:	zlib-devel
BuildRequires:	/usr/bin/sphinx-build

%description
Parse C-family source files and optionally write a subset of the
Abstract Syntax Tree (AST) to a representation in XML.

Source files are parsed as complete translation units using the clang
compiler. XML output is enabled by the --castxml-gccxml option and
produces a format close to that of gccxml. Future versions of castxml
may support alternative output formats.

%prep
%setup -q -n CastXML-%{version}

%build
%cmake -DCastXML_INSTALL_DOC_DIR:STRING=share/doc/%{name} \
       -DCastXML_INSTALL_MAN_DIR:STRING=share/man \
       -DCLANG_RESOURCE_DIR:PATH=$(clang -print-file-name=include)/.. \
       -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
       -DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
       -DBUILD_TESTING:BOOL=ON \
       -DSPHINX_MAN:BOOL=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_pkgdocdir}/LICENSE
rm %{buildroot}%{_pkgdocdir}/NOTICE

%check
%ctest

%files
%{_bindir}/castxml
%doc %{_mandir}/man1/castxml.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/clang
%{_datadir}/%{name}/detect_vs.c
%{_datadir}/%{name}/detect_vs.cpp
%{_datadir}/%{name}/empty.c
%{_datadir}/%{name}/empty.cpp
%license LICENSE NOTICE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 28 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.10-1
- Update to version 0.6.10

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.7-1
- Update to version 0.6.7

* Fri Jun 28 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.6-2
- Rebuild for llvm/clang 17 (EPEL 8)

* Mon May 06 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.6-1
- Update to version 0.6.6

* Mon Apr 15 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.5-1
- Update to version 0.6.5

* Wed Mar 06 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.4-2
- Backport LLVM 18 support from upstream

* Tue Jan 23 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.4-1
- Update to version 0.6.4

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.3-1
- Update to version 0.6.3

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.2-1
- Update to version 0.6.2

* Fri Sep 01 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.1-4
- Backport support for LLVM 17 from upstream

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 08 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.1-2
- Rebuild for llvm/clang 16 (Fedora 38/39)
- Rebuild for llvm/clang 15 (EPEL 8/9)

* Thu Mar 23 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.1-1
- Update to version 0.6.1

* Wed Mar 22 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.0-1
- Update to version 0.6.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.1-1
- Update to version 0.5.1

* Wed Dec 07 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.0-1
- Update to version 0.5.0

* Wed Nov 23 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.8-1
- Update to version 0.4.8

* Fri Nov 11 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.7-1
- Update to version 0.4.7

* Mon Sep 19 2022 Pete Walter <pwalter@fedoraproject.org> - 0.4.6-2
- Rebuild for llvm 15

* Thu Sep 01 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.6-1
- Update to version 0.4.6

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.5-2
- Rebuild for llvm/clang 13 (EPEL 8)

* Sun Mar 20 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.5-1
- Update to version 0.4.5

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Tom Stellard <tstellar@redhat.com> - 0.4.4-2
- Rebuild for llvm-13.0.0

* Wed Oct 27 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.4-1
- Update to version 0.4.4

* Thu Oct 07 2021 Tom Stellard <tstellar@redhat.com> - 0.4.3-7
- Rebuild for llvm-13.0.0

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.3-6
- Backport fixes for LLVM/Clang 13

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.3-4
- Rebuild for llvm/clang 12 (Fedora 34)

* Fri May 21 2021 Carl George <carl@george.computer> - 0.4.3-3
- Rebuild for llvm/clang 11 (RHEL 8.4)

* Thu May 20 2021 Carl George <carl@george.computer> - 0.4.3-2
- Rebuild for llvm/clang 11 (RHEL 8.4)

* Thu Mar 04 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.3-1
- Update to version 0.4.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Tom Stellard <tstellar@redhat.com> - 0.4.2-2
- Rebuild for clang-11.1.0

* Sat Jan 16 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.2-1
- Update to version 0.4.2

* Thu Jan 14 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.1-1
- Update to version 0.4.1

* Thu Jan 14 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.0-1
- Update to version 0.4.0
- Fix expected test output on 32-bit architectures (i686/armv7hl)

* Tue Nov 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.6-2
- Rebuild for llvm/clang 10 (EPEL 8)

* Sat Aug 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.6-1
- Update to version 0.3.6
- Drop previously backported LLVM/Clang 11 patches

* Tue Aug 18 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.4-4
- Backport compatibility fixes for LLVM/Clang 11 from git master

* Fri Aug 14 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.4-3
- Use backported new cmake macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.4-1
- Update to version 0.3.4
- Adapt to new cmake rpm macro

* Tue Feb 18 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.1-1
- Update to version 0.3.1
- Drop cling-cpp.so linking patch - accepted upstream

* Sat Feb 15 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.0-1
- Update to version 0.3.0

* Wed Jan 29 2020 Tom Stellard <tstellar@redhat.com> - 0.2.0-5
- Link against libclang-cpp.so
- https://fedoraproject.org/wiki/Changes/Stop-Shipping-Individual-Component-Libraries-In-clang-lib-Package

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.0-3
- Backport clang 9 test fix

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.0-1
- First tagged release from upstream

* Tue Mar 12 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.29.20190117git9c91919
- Update sphinx BR

* Mon Feb 25 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.28.20190117git9c91919
- New git snapshot (supports LLVM8)
- Drop castxml-shared.patch in favor of new LLVM_LINK_LLVM_DYLIB cmake option

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.27.20180806gitae93121
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.26.20180806gitae93121
- Add source directory to cmake command

* Thu Aug 30 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.25.20180806gitae93121
- New git snapshot (supports LLVM7)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.20180122git6952441
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.20180122git6952441
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.22.20180122git6952441
- New git snapshot (supports LLVM6)
- Remove BuildRequires on llvm-static - llvm's cmake files have been fixed

* Wed Dec 13 2017 Tom Stellard <tstellar@redhat.com> - 0.1-0.21.20171013git367e90c
- Rebuild for LLVM 5.0

* Wed Oct 25 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.20.20171013git367e90c
- New git snapshot (supports LLVM5)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.19.20170301gitfab9c47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.20170301gitfab9c47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1-0.17.20170301gitfab9c47
- Rebuild for LLVM4

* Wed Mar 15 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.16.20170301gitfab9c47
- New git snapshot
- Remove bundled provides for kwsys components - no longer used
- Rebuild for LLVM 3.9 (Fedora 25)

* Wed Feb 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.15.20170113gite7252f5
- New git snapshot

* Mon Nov 07 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.14.20161006git05db76f
- Rebuild for LLVM 3.9 (Fedora 26)

* Tue Oct 25 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.13.20161006git05db76f
- New git snapshot

* Fri Jul 01 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.12.20160617gitd5934bd
- New git snapshot

* Thu May 26 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.11.20160510git9a83414
- New git snapshot

* Thu Feb 25 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.10.20160125gitfc71eb9
- Adjust to llvm library changes again (the split was revoked)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.20160125gitfc71eb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.8.20160125gitfc71eb9
- New git snapshot
- Properly adjust to the new llvm library split

* Wed Jan 27 2016 Adam Jackson <ajax@redhat.com> 0.1-0.7.20150924git552dd69
- Rebuild for llvm 3.7.1 library split

* Fri Sep 25 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.6.20150924git552dd69
- Adjust gccxml obsolete version

* Thu Sep 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.5.20150924git552dd69
- New git snapshot
- Allow warnings about guessing the float ABI during tests (fixes tests on arm)

* Thu Sep 17 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.4.20150902git7acd634
- New git snapshot

* Fri Aug 21 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.3.20150820git2e55b35
- New git snapshot
- Upstream has deleted the parts of the bundled kwsys sources that are not
  used by castxml from the source repository
- Add bundled provides for the remaining kwsys components according to
  revised FPC decision 2015-08-20
  https://fedorahosted.org/fpc/ticket/555

* Fri Aug 07 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.2.20150807git8a08a44
- New git snapshot
- Unbundle kwsys library according to FPC decision 2015-08-06
  https://fedorahosted.org/fpc/ticket/555

* Tue Apr 14 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.1.20150414git43fa139
- First packaging for Fedora
