Name:           ctemplate
Version:        2.4
Release:        9%{?dist}
Summary:        A simple but powerful template language for C++
License:        BSD-3-Clause
URL:            https://github.com/olafvdspek/ctemplate
Source0:        https://github.com/OlafvdSpek/ctemplate/archive/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  python3
BuildRequires: make

%description
CTemplate is a simple but powerful template language for C++. It
emphasizes separating logic from presentation: it is impossible to
embed application logic in this template language.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n ctemplate-ctemplate-%{version}
./autogen.sh

%build

%configure --disable-static --disable-silent-rules

sed -i 's|^PTHREAD_LIBS = |PTHREAD_LIBS = -lpthread|g' Makefile
# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%make_install

# Remove static libraries and libtool archives.
find %{buildroot} -name '*.*a' -delete -print

# Remove libtool binaries
rm -rf %{buildroot}%{_bindir}/make_tpl_varnames_h
rm -rf %{buildroot}%{_bindir}/diff_tpl_auto_escape

# We ship docs in another way.
rm -rf %{buildroot}%{_datadir}/doc

%check
make check

%files
%license COPYING
%{_bindir}/template-converter
%{_libdir}/libctemplate_nothreads.so.3*
%{_libdir}/libctemplate.so.3*

%files devel
%doc AUTHORS ChangeLog README NEWS
%doc doc/
%{_libdir}/libctemplate_nothreads.so
%{_libdir}/libctemplate.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/libctemplate.pc
%{_libdir}/pkgconfig/libctemplate_nothreads.pc

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 09 2020 Till Hofmann <thofmann@fedoraproject.org> - 2.4-1
- Update to 2.4.0
- Switch to python3
- Remove accidentally installed libtool binaries
- Run autoreconf before build (configure script not included anymore)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.3-12
- Replace unversioned python shebangs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Till Hofmann <till.hofmann@posteo.de> - 2.3-8
- Fix source extraction for new github source

* Mon Mar 27 2017 Till Hofmann <till.hofmann@posteo.de> - 2.3-7
- Switch to github source

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Christopher Meng <rpm@cicku.me> - 2.3-1
- Update to 2.3

* Thu Aug 08 2013 Christopher Meng <rpm@cicku.me> - 2.2-5
- SPEC cleanup.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 2.2-1
- Update to 2.2. Fix FTBFS since F-14

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 05 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.97-1
- Updated to 0.97

* Fri Dec 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.96-1
- Updated to 0.96

* Tue Sep 01 2009 Dennis Gilmore <dennis@ausil.us> - 0.95-2
- make sure that the namespace is ctemplate not google

* Wed Aug 05 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.95-1
- Updated to ctemplate

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.93-2
- Added python as BuildRequires, and bswap patch for ppc

* Sun Apr 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.93-1
- Updated to 0.93, removed patch for consts - fixed upstream

* Tue Mar 03 2009 Caolán McNamara <caolanm@redhat.com> - 0.91-5
- fix up consts to build

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 23 2008 Dennis Gilmore <dennis@ausil.us> - 0.91-3
- clean up headers so that they include each other as intended

* Wed Sep 03 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.91-2
- Added %%check section to run tests

* Sun Aug 24 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.91-1
- Update to 0.91 & removed missing header files patch

* Fri Aug 22 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.90-2
- fix undefined-non-weak-symbol & rpath issue

* Thu Aug 14 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.90-1
-Initial build
