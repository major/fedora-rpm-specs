%?mingw_package_header

%global name1 jimtcl
Name:           mingw-%{name1}
Version:        0.81
Release:        11%{?dist}
Summary:        MinGW small embeddable Tcl interpreter

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://jim.tcl.tk
Source0:        https://github.com/msteveb/%{name1}/archive/%{version}/%{name1}-%{version}.tar.gz
# install documentation into /usr/share/doc/mingw{32,64}-jimtcl instead of
# /usr/{i686,x86_64}-w64-mingw32/sys-root/mingw/lib/mingw{32,64}-jimtcl
# patch from the native jimtcl package
Patch0:         jimtcl-fix_doc_paths.patch
# install libjim.dll into bindir (instead of libdir), and install the implib
# libjim.dll.a into libdir, to comply with mingw packaging guidelines
Patch1:         jimtcl-implib.patch
BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  asciidoc
BuildRequires:  gcc

%description
Jim is an opensource small-footprint implementation of the Tcl programming 
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.

%package -n mingw32-%{name1}
Summary:        MinGW small embeddable Tcl interpreter
Requires:       jimtcl

%description -n mingw32-%{name1}
Jim is an opensource small-footprint implementation of the Tcl programming 
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.

%package -n mingw64-%{name1}
Summary:        MinGW small embeddable Tcl interpreter
Requires:       jimtcl

%description -n mingw64-%{name1}
Jim is an opensource small-footprint implementation of the Tcl programming 
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.

%{?mingw_debug_package}

%prep
%setup -q -n %{name1}-%{version}
%patch -P0 -p0 -b .doc
%patch -P1 -p0 -b .implib

%build
%mingw_configure --full --shared --disable-option-checking

%mingw_make %{?_smp_mflags}


%install
install -d %{buildroot}/%{mingw32_datadir}/doc/%{name1}
install -d %{buildroot}/%{mingw64_datadir}/doc/%{name1}
%mingw_make install DESTDIR=%{buildroot} INSTALL_PROGRAM="cp -p" INSTALL_DATA="cp -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}/%{mingw32_datadir}/doc/%{name1}
rm -rf %{buildroot}/%{mingw64_datadir}/doc/%{name1}
rm -rf %{buildroot}/%{mingw32_datadir}/%{mingw32_prefix}/docs
rm -rf %{buildroot}/%{mingw64_datadir}/%{mingw64_prefix}/docs
rm -rf %{buildroot}/%{mingw32_libdir}/jim/tcltest.tcl
rm -rf %{buildroot}/%{mingw64_libdir}/jim/tcltest.tcl
install -d %{buildroot}/%{_bindir}
rm -f %{buildroot}/%{mingw32_bindir}/build-jim-ext
rm -f %{buildroot}/%{mingw64_bindir}/build-jim-ext
rm -f %{buildroot}/%{mingw32_bindir}/jimdb
rm -f %{buildroot}/%{mingw64_bindir}/jimdb

%files -n mingw32-%{name1}
%license LICENSE
%doc AUTHORS README DEVELOPING STYLE
%doc README.extensions README.metakit README.namespaces README.oo README.utf-8
%{mingw32_bindir}/jimsh.exe
%{mingw32_bindir}/libjim.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libjim.dll.a
%{mingw32_libdir}/pkgconfig/jimtcl.pc

%files -n mingw64-%{name1}
%license LICENSE
%doc AUTHORS README DEVELOPING STYLE
%doc README.extensions README.metakit README.namespaces README.oo README.utf-8
%{mingw64_bindir}/jimsh.exe
%{mingw64_bindir}/libjim.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libjim.dll.a
%{mingw64_libdir}/pkgconfig/jimtcl.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.81-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.81-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Thomas Sailer <fedora@tsailer.ch> - 0.81-1
- update

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.79-1
- update

* Wed May 01 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.78-1
- update

* Fri Mar 23 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.77-1
- update

* Tue Feb 14 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.76-2
- remove BuildRoot and clean sections

* Fri Feb 03 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.76-1
- Initial Specfile
