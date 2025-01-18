Name:           flowcanvas
Summary:        Interactive widget for "boxes and lines" environments
Version:        0.7.1
Release:        46%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://drobilla.net/software/flowcanvas/
Source0:        http://download.drobilla.net/%{name}-%{version}.tar.bz2
Patch0:         flowcanvas-0.7.1-graphviz23.patch
BuildRequires:  gcc-c++
BuildRequires:  python2
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  graphviz-devel >= 2.3
BuildRequires:  libgnomecanvasmm26-devel


%description
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for graph-based
interfaces (patchers, modular synthesizers, finite state automata,
interactive graphs, etc).


%package devel
Summary:        Development libraries and headers for %{name}
Requires:       boost-devel
Requires:       libgnomecanvasmm26-devel
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}

%description devel
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for graph-based
interfaces (patchers, modular synthesizers, finite state automata,
interactive graphs, etc).

This package contains the headers and development libraries for FlowCanvas.


%prep
%setup -q
%patch -P0 -p1 -b .graphviz23

# Fix Python shebangs
sed -i 's|/usr/bin.*python$|/usr/bin/python2|' autowaf/autowaf.py autowaf/waf wscript

%build
export CXXFLAGS="$RPM_OPT_FLAGS"
export LINKFLAGS="$RPM_LD_FLAGS"
export LIB_AGRAPH="cgraph"
./waf configure \
        --prefix=%{_prefix} \
        --libdir=%{_libdir} \
        --docs \
        --htmldir=%{_docdir}/%{name}-devel

./waf build -v %{?_smp_mflags}


%install
DESTDIR=$RPM_BUILD_ROOT ./waf install

# Correct permission
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.*

%files
%doc AUTHORS ChangeLog README
%{_libdir}/lib%{name}.so.*

%files devel
%{_docdir}/%{name}-devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.1-45
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.1-31
- Replaced BR: python with BR: python2
- Fixed Python shebangs
- Use Fedora link flags

* Sat Jul 21 2018 Adam Huffman <bloch@verdurin.com> - 0.7.1-30
- Add BR for python and gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.7.1-24
- Rebuilt for Boost 1.63

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.7.1-22
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.7.1-20
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.1-18
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.7.1-17
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Adam Huffman <bloch@verdurin.com> - 0.7.1-15
- Use unversioned docdir

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.7.1-13
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.7.1-11
- Rebuild for boost 1.54.0

* Tue Apr 23 2013 Tom Callaway <spot@fedoraproject.org> - 0.7.1-10
- rebuild against new libcgraph

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.7.1-9
- Rebuild for Boost-1.53.0

* Sun Jan 20 2013 Adam Huffman <bloch@verdurin.com> - 0.7.1-8
- Rebuilt for new libgraph

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.1-4
- Rebuild for new libpng

* Sat May 14 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.1-3
- Rebuild against graphviz-2.28.0 on F-16

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.1-1
- Update to 0.7.1

* Wed Sep 29 2010 jkeating - 0.6.4-2
- Rebuilt for gcc bug 634757

* Sat Sep 11 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.6.4-1
- Update to 0.6.4

* Tue Jul 27 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.6.0-2
- Rebuild against new boost on F-14

* Sat Feb 20 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.6.0-1
- New version
- Drop upstreamed patch

* Fri Sep 11 2009 Alexander Chalikiopoulos <dreamer@fedoraproject.org> 0.5.1-1
- Initial RPM release
