Name:           irstlm
Version:        6.00.05
Release:        22%{?dist}
Summary:        Statistical language model tool

License:        LGPL-2.1-or-later
URL:            http://hlt-mt.fbk.eu/technologies/irstlm
Source0:        https://github.com/irstlm-team/%{name}/archive/v%{version}.tar.gz
# Fix a case of violating the ANSI strict aliasing rules.
# https://sourceforge.net/tracker/?func=detail&aid=3608176&group_id=183064&atid=903742
Patch0:         %{name}-alias.patch
# Update configure.ac.  Sent upstream 24 Oct 2013.
Patch1:         %{name}-configure.patch

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl-generators
BuildRequires:  tex(latex)
BuildRequires:  tex(epsf.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(version.sty)
BuildRequires:  zlib-devel
BuildRequires: make

# date and rm are invoked at runtime
Requires:       coreutils

%description
Irstlm is a tool for the estimation, representation, and computation of
statistical language models.

%package devel
Summary:        Headers and libraries for building with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The headers and libraries needed to build applications that use %{name}.

%package tools
Summary:        Programs and scripts that use the %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Programs and scripts that use the %{name} library.

%prep
%setup -q
%patch -P0
%patch -P1

# Fix executable bits
find src -type f -perm /0111 | xargs chmod a-x
chmod a+x scripts/rm-start-end.sh scripts/wrapper

# Do not compile static binaries, or monkey with the include path or warnings
sed -i 's, -static -isystem/usr/include -W -Wall,,' src/Makefile.am

# Upstream doesn't ship the actual configure script
autoreconf -fi

# The release number file contains the wrong number, and is in the wrong dir
echo %{version} > RELEASE.tex

# Fix a buffer overflow in 6.00.05 (already fixed in upstream git)
sed -i.orig 's/\(i<=LMTMAXLEV\)+1/\1/' src/lmtable.cpp
touch -r src/lmtable.cpp.orig src/lmtable.cpp
rm -f src/lmtable.cpp.orig

%build
%configure --enable-shared --disable-static --enable-interpolatedsearch \
  --enable-doc --enable-cxx0

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
make install DESTDIR=%{buildroot}

# Move the header files into their own directory to avoid name clashes
mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/%{name}

# We don't want libtool archives
rm -f %{buildroot}%{_libdir}/*.la

# We will install the documentation our own way
rm -fr %{buildroot}%{_prefix}/doc

%ldconfig_scriptlets

%files
%doc README.md
%license Copyright LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files tools
%doc doc/irstlm-manual.pdf
%{_bindir}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 6.00.05-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.00.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Jerry James <loganjerry@gmail.com> - 6.00.05-1
- New upstream version
- Update URLs
- Disable caching support; code has bitrotted

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.80.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.80.08-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 13 2015 Jerry James <loganjerry@gmail.com> - 5.80.08-1
- New upstream release

* Tue Jan 27 2015 Jerry James <loganjerry@gmail.com> - 5.80.07-1
- New upstream release
- Build and install the manual

* Tue Sep  9 2014 Jerry James <loganjerry@gmail.com> - 5.80.06-1
- New upstream release
- Drop unused BRs
- Drop upstream patches
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.80.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.80.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Jerry James <loganjerry@gmail.com> - 5.80.03-4
- Update project URL

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 5.80.03-3
- Rebuild for boost 1.55.0

* Wed Oct 23 2013 Jerry James <loganjerry@gmail.com> - 5.80.03-2
- Add -configure patch to update autotools input

* Wed Jul 17 2013 Jerry James <loganjerry@gmail.com> - 5.80.03-1
- Initial RPM
