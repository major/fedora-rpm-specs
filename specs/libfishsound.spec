# Allow building with GCC 14+
# This should be fixed properly but upstream is dead
%global optflags %optflags -Wno-incompatible-pointer-types

%global so_major_version 1
%global so_version %{so_major_version}.3.0

Name:           libfishsound
Version:        1.0.0
Release:        32%{?dist}
Summary:        Simple programming interface for Xiph.Org codecs

License:        BSD-3-Clause
URL:            http://www.xiph.org/fishsound/
Source0:        http://downloads.xiph.org/releases/libfishsound/libfishsound-%{version}.tar.gz

# also pulled in by speex-devel
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  flac-devel
BuildRequires:  speex-devel libvorbis-devel liboggz-devel libsndfile-devel
BuildRequires:  doxygen
BuildRequires:  make

%description
libfishsound provides a simple programming interface for decoding and
encoding audio data using Xiph.Org codecs (FLAC, Speex and Vorbis).

libfishsound by itself is designed to handle raw codec streams from a
lower level layer such as UDP datagrams. When these codecs are used in
files, they are commonly encapsulated in Ogg to produce Ogg FLAC, Speex
and Ogg Vorbis files.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
# note: intentionally not noarch; contains a target-specific Makefile
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains the documentation for %{name}.

%package        tools
Summary:        Sample programs bundled with %{name}
Requires:       %{name} = %{version}-%{release}

%description    tools
The %{name}-tools package contains sample programs that use %{name}.
The source code for these are included in %{name}-doc.


%prep
%setup -q
# These dependencies should not be exported
# http://github.com/kfish/libfishsound/issues/#issue/1
sed -i '/^Requires:.*/d' fishsound.pc.in


%build
%configure --disable-static
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# overriding docdir does not work
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} \
   other-docs
# remove Latex docs, they do not provide hyperlinks and
# thus are less usable than the HTML docs
rm -rf other-docs/latex

# move the examples we want
mkdir -p $RPM_BUILD_ROOT%{_bindir}
(cd src/examples/ && \
  mv .libs/* $RPM_BUILD_ROOT%{_bindir} &&
  make clean && rm -rf .deps .libs Makefile.*)
mv src/examples .


%files
%license COPYING
%doc AUTHORS README
%{_libdir}/*.so.%{so_major_version}
%{_libdir}/*.so.%{so_version}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fishsound.pc

%files doc
%doc examples other-docs/*

%files tools
%{_bindir}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Michel Lind <salimma@fedoraproject.org> - 1.0.0-31
- Fix FTBFS due to incompatible pointer types (rhbz#2261314)
- Modernize spec file
- Convert license to SPDX expression

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.0.0-25
- Rebuilt for flac 1.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul  3 2010 Michel Salim <salimma@fedoraproject.org> - 1.0.0-2
- No longer export dependencies on vorbis, speex, flac

* Sat Jun 12 2010 Michel Salim <salimma@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Wed Jun 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.9.1-5
- Bump for new liboggz

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Michel Salim <salimma@fedoraproject.org> - 0.9.1-2
- Remove (unbuilt) Latex documentation from -doc

* Wed Apr  9 2008 Michel Salim <salimma@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1 (CVE-2008-1686, bz #441246)

* Thu Feb 14 2008 Michel Salim <michel.sylvan@gmail.com> - 0.9.0-5
- Previous revision misspelled speex

* Wed Feb 13 2008 Michel Salim <michel.sylvan@gmail.com> - 0.9.0-4
- Add missing dependencies on libvorbis-devel and speex-devel
  for -devel subpackage

* Sat Jan 19 2008 Michel Salim <michel.sylvan@gmail.com> - 0.9.0-3
- Port FLAC support to new (>= 1.1.3) API

* Fri Jan 18 2008 Michel Salim <michel.sylvan@gmail.com> - 0.9.0-2
- Add dependency on liboggz
- Rename -docs subpackage to -doc
- Note in description that FLAC support is currently disabled

* Wed Jan 16 2008 Michel Salim <michel.sylvan@gmail.com> - 0.9.0-1
- Initial Fedora package
