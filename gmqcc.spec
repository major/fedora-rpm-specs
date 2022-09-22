Name:           gmqcc
Version:        0.3.5
Release:        24%{?dist}
Summary:        Improved Quake C Compiler
License:        MIT
URL:            http://graphitemaster.github.io/gmqcc/
Source0:        https://github.com/graphitemaster/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# fix build on big endian arches - stdlib.h required for exit()
Patch0:         %{name}-0.3.5-stdlib.patch

# From old-stable branch in upstream
Patch0001:      0001-clean-include-.d.patch
Patch0002:      0002-Add-GMQCC_FUNCTION.patch
Patch0003:      0003-Add-GMQCC_FALLTHROUGH.patch
Patch0004:      0004-Disable-Werror-for-old-stable.patch
Patch0005:      0005-sanitize-use-1u-unsigned-for-flag-bit-shifts.patch
Patch0006:      0006-sanitize-util_hthash-with-a-hack.patch

# tests fail on big endians
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  valgrind-devel

%description
Modern written-from-scratch compiler for the QuakeC language with
support for many common features found in other QC compilers.

%package -n qcvm
Summary:        Standalone QuakeC VM binary executor

%description -n qcvm
Executor for QuakeC VM binary files created using a QC compiler such
as gmqcc or fteqcc. It provides a small set of built-in functions, and
by default executes the main function if there is one. Some options
useful for debugging are available as well.

%package -n gmqpak
Summary:        Standalone Quake PAK file utility

%description -n gmqpak
Standalone Quake PAK file utility supporting the extraction of files,
directories, or whole PAKs, as well as the opposite (creation of PAK files).

%prep
%autosetup -p1

# and for all for all of those switches they increase the runtime of the compile
# making compiles of code slower

# we don't need compiel time buffer protection, we test with clangs address
# sanatizer and valgrind before releases
%global optflags %(echo %{optflags} | sed 's/-Wp,-D_FORTIFY_SOURCE=2 //')
# there is no exceptions in C
%global optflags %(echo %{optflags} | sed 's/-fexceptions //')
# same with clangs address sanatizer and valgrind testing
%global optflags %(echo %{optflags} | sed 's/-fstack-protector-strong //')

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
make check

%files
%license LICENSE
%doc README AUTHORS CHANGES TODO
%doc gmqcc.ini.example
%{_mandir}/man1/gmqcc.1*
%{_bindir}/gmqcc

%files -n qcvm
%license LICENSE
%doc README AUTHORS CHANGES TODO
%{_mandir}/man1/qcvm.1*
%{_bindir}/qcvm

%files -n gmqpak
%license LICENSE
%doc README AUTHORS CHANGES TODO
%{_mandir}/man1/gmqpak.1*
%{_bindir}/gmqpak

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-15
- Fix build due to wrong CFLAGS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.5-10
- Fix FTBFS (RHBZ #1307543)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.5-8
- Add patch for support gcc5
- Use new RPM macroses

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.5-4
- Build on aarch64 as it's little endian too

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 16 2013 Dan Horák <dan[at]danny.cz> - 0.3.5-2
- fix build on big endian arches
- use the standard wildcarded filename for man pages
- and make it Exclusive for little endians because tests fail on big endians

* Thu Nov 14 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.5-1
- 0.3.5 upstream release

* Thu Sep 26 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-2
- Optimizing compile flags

* Fri Sep 20 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Update to 0.3.0 (improved new package: gmqpak)

* Sat Jul 27 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.9-1
- Initial release
