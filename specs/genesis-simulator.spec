# Upstream has been informed of incorrect FSF addresses
# https://github.com/genesis-sim/genesis-2.4/issues/4

# Fails with LTO enabled
%global _lto_cflags %{nil}

%global _package_note_file "%{_builddir}/%{realname}-%{version}-%{commit}/genesis/.package_note-%{name}-%{version}-%{release}.%{_arch}.ld"

%global commit 7b0a66b71ba98d5b7802c32ed856b75b8334fb05
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global realname genesis
%global instdir %{_datadir}/%{name}

Name:       %{realname}-simulator
Summary:    A general purpose simulation platform
Version:    2.4
Release:    24.20210608git%{shortcommit}%{?dist}
Url:        http://www.genesis-sim.org/GENESIS/
Source0:    https://github.com/genesis-sim/%{realname}-%{version}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# fix left over COPT
Patch0:     0001-use-CFLAGS_IN-instead-of-COPT.patch
# pass RNG_CFLAGS variable to ensure they're also built with fpic etc.
Patch1:     0002-feat-pass-RNG_CFLAGS.patch

# GPL and LGPL: Genesis
# MIT: param library
# Public Domain: Scripts
# Automatically converted from old format: GPLv2+ and LGPLv2+ and MIT and Public Domain - review is highly recommended.
License:    GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain

BuildRequires: git-core
BuildRequires: gcc
BuildRequires: bison
BuildRequires: flex
%if %{fedora} > 33
BuildRequires: libfl-devel
%else
BuildRequires: flex-static
%endif
BuildRequires: ncurses-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: netcdf-devel
BuildRequires: make

%description
GENESIS (short for GEneral NEural SImulation System) is a general
purpose simulation platform that was developed to support the
simulation of neural systems ranging from subcellular components and
biochemical reactions to complex models of single neurons, simulations
of large networks, and systems-level models. As such, GENESIS, and its
version for parallel and networked computers (PGENESIS) was the first
broad scale modeling system in computational biology to encourage
modelers to develop and share model features and components. Most
current GENESIS applications involve realistic simulations of
biological neural systems. Although the software can also model more
abstract networks, other simulators are more suitable for
backpropagation and similar connectionist modeling.

Please install the %{name}-%{doc} sub package for documentation.

%package devel
Summary: Static library and tools for building genesis extensions
%description devel
%{summary}.

%package doc
BuildArch: noarch
Summary: Documentation for %{name}
%description doc
%{summary}.

%ifarch x86_64
%global extraflags -DLONGWORDS
%endif

%prep
%autosetup -n %{realname}-%{version}-%{commit}/genesis -S git -p2

# Correct spurious perms
find Doc -type f -exec chmod -x '{}' \;
# Correct shebang for perl scripts
find Scripts/purkinje/perl -exec sed -i 's|#!/usr/local/bin/perl -w|#!/usr/bin/perl -w|' '{}' \;

# Correct executable perms
find Scripts -type f -exec chmod -x '{}' \;
find Tutorials -type f -exec chmod -x '{}' \;

# file-not-utf8
pushd Scripts/burster
# Convert to utf-8
for file in README README.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done
popd

# Remove the binaries they ship
rm -rf ../%{realname}-binaries

# Remove unrelated programs
rm -rf ./src/contrib

# Remove bundled netcdf
rm -rf ./src/diskio/interface/netcdf/netcdf-3.4
# Do not use bundled netcdflib
sed -i 's/netcdflib.o: netcdflib/netcdflib.o:/' ./src/diskio/interface/netcdf/Makefile

# Set up Makefile for Linux installation
# Using configure doesn't quite work for us because the build scripts use ld
# instead of gcc, and the Fedora LD flags are set to be used with gcc. Setting
# them for ld breaks the configure script.
%global build_type_safety_c 0
cp src/Makefile.dist src/Makefile
cat >>src/Makefile <<EOF
MACHINE=Linux
OS=BSD
XLIB=%{_libdir}
CC=gcc -std=gnu89
CPP=cpp -P
RNG_CFLAGS=%{optflags} %{?extraflags}
CFLAGS=%{optflags} %{?extraflags}
CXXFLAGS=%{optflags} %{?extraflags}
LD=gcc
RANLIB=ranlib
AR=ar
YACC=bison -y
LEX=flex -l
LEXLIB=-lfl
LIBS=\$(LEXLIB) -lm -lnetcdf
TERMCAP=-lncurses
TERMOPT=-DTERMIO -DDONT_USE_SIGIO
NETCDFOBJ = \
        \$(DISKIODIR)/interface/\$(NETCDFSUBDIR)/netcdflib.o
EOF

%build
# Kill parallel make, parallel make break build in ramdom ways
make -C src genesis

%install
make -C src install INSTALLDIR=%{buildroot}%{_libdir}/genesis
rm -r %{buildroot}%{_libdir}/genesis/{src,man}
rm -v %{buildroot}%{_libdir}/genesis/.*simrc
chmod -x %{buildroot}%{_libdir}/genesis/startup/*

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/genesis/genesis %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_includedir}
mv %{buildroot}%{_libdir}/genesis/include %{buildroot}%{_includedir}/genesis

mv %{buildroot}%{_libdir}/genesis/bin/convert %{buildroot}%{_bindir}/genesis-convert
install -D man/man1/convert.1 %{buildroot}%{_mandir}/man1/genesis-convert.1
cp src/libsh %{buildroot}%{_libdir}/genesis/lib

find %{buildroot}%{_libdir}/genesis/startup/ -name '*simrc' -exec \
    sed -i -e 's|%{buildroot}||g' -e 's|GENESIS_HELP .*|GENESIS_HELP  %{_docdir}/%{name}-doc/Doc/|' {} \;

# Fix permission for man
chmod -x %{buildroot}%{_mandir}/man1/%{realname}-convert.1*

# Remove docs from libdir
rm -rf %{buildroot}%{_libdir}/%{realname}/Doc
rm -rf %{buildroot}%{_libdir}/%{realname}/Hyperdoc
rm -rf %{buildroot}%{_libdir}/%{realname}/Tutorials

# add emacs mode

%files
%{_bindir}/%{realname}
%{_bindir}/%{realname}-convert
%license GPLicense LGPLicense
%doc AUTHORS COPYRIGHT CONTACTING.GENESIS ChangeLog
%exclude %{_libdir}/%{realname}/lib
%exclude %{_libdir}/%{realname}/*make
%{_libdir}/%{realname}
%{_mandir}/man1/*

%files devel
%license GPLicense LGPLicense
%{_includedir}/%{realname}/
%{_libdir}/%{realname}/lib
%{_libdir}/%{realname}/*make

%files doc
%license GPLicense LGPLicense
%doc Doc Hyperdoc Tutorials

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-24.20210608git7b0a66b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4-23.20210608git7b0a66b
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-22.20210608git7b0a66b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-21.20210608git7b0a66b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-20.20210608git7b0a66b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 2.4-19.20210608git7b0a66b
- Set build_type_safety_c to 0 (#2150772)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-18.20210608git7b0a66b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4-17.20210608git7b0a66b
- Kill parallel make for now as it breaks build in random ways

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-16.20210608git7b0a66b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec  5 2022 Florian Weimer <fweimer@redhat.com> - 2.4-15.20210608git7b0a66b
- Build in C89 mode (#2150772)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-14.20210608git7b0a66b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-13.20210608git7b0a66b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 2.4-12.20210608git7b0a66b
- Rebuild for netcdf 4.8.0

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 2.4-11.20210608git7b0a66b
- Rebuild for netcdf 4.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-10.20210608git7b0a66b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4-9.20210608git7b0a66b
- Add conditional for flex BR

* Tue Jun 08 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4-8.20210608git7b0a66b
- Update flex-devel dep (#1871096)
- Update to latest upstream release (and drop merged patches)
- Disable lto to make it build
- Move Scripts to correct location (#1969343)
- correct env variable for documentation

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7.20181209git374cdbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6.20181209git374cdbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5.20181209git374cdbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4.20181209git374cdbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 2.4-3.20181209git374cdbc
- Rebuild for netcdf 4.6.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2.20181209git374cdbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4-1.20181209git374cdbc
- Add all licenses
- Add gcc to BR
- Add checkout date in timestamp
- Initial build for Fedora repos
- Use latest git commit
