Name:           qqwing
Version:        1.3.4
Release:        23%{?dist}
Summary:        Command-line Sudoku solver and generator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://qqwing.com/
Source0:        http://qqwing.com/qqwing-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires: make
BuildRequires:  gcc-c++
%description
QQwing is a command-line Sudoku solver and generator.

%package        libs
Summary:        Library for Sudoku solving and generation

%description    libs
libqqwing is a C++ library for solving and generating Sudoku puzzles.

%package        devel
Summary:        Development files for libqqwing
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use libqqwing.

%prep
%setup -q

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets libs


%files
%doc README
%{_bindir}/qqwing
%{_mandir}/man1/qqwing.1*

%files libs
%doc AUTHORS COPYING
%{_libdir}/libqqwing.so.*

%files devel
%{_includedir}/*
%{_libdir}/libqqwing.so
%{_libdir}/pkgconfig/qqwing.pc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.4-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 1.3.4-1
- Update to 1.3.4

* Thu Nov 20 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.3.3-1
- Update to 1.3.3

* Sun Sep 21 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.3.1-1
- Update to 1.3.1 and drop soname patch.

* Sun Sep 21 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.3.0-2
- Revert soname bump.

* Sat Sep 20 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.3.0-1
- Update to 1.3.0.
- Update URLs.

* Sat Aug 23 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.2.0-2
- Really update to 1.2.0. Much learning.

* Sat Aug 23 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.2.0-1
- Update to 1.2.0

* Tue Aug 19 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.1.3-1
- Trivial spec cleanups

* Fri Aug 15 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.1.3-1
- Switch the base package from libqqwing to qqwing
- Update to 1.1.3

* Sat Aug  2 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1.1.2-1
- New package
