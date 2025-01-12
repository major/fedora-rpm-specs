%if 0%{?fedora} && ! 0%{?flatpak}
%bcond_without mingw
%else
%bcond_with mingw
%endif

#global pre rc1

Name:           podofo
Version:        0.10.4
Release:        3%{?dist}
Summary:        Tools and libraries to work with the PDF file format

License:        LGPL-2.0-or-later
URL:            https://github.com/podofo/podofo
Source0:        https://github.com/podofo/podofo/archive/%{version}%{?pre:-%pre}/%{name}-%{version}%{?pre:-%pre}.tar.gz

# Fix header case
Patch0:         podofo-case.patch
# Downstream patch for CVE-2019-20093
# https://sourceforge.net/p/podofo/tickets/75/
Patch1:         podofo_CVE-2019-20093.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  ghostscript
BuildRequires:  libidn-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  texlive-epstopdf-bin
BuildRequires:  zlib-devel

%if %{with mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-fontconfig
BuildRequires: mingw32-freetype
BuildRequires: mingw32-libidn
BuildRequires: mingw32-libjpeg
BuildRequires: mingw32-libpng
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-openssl
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-fontconfig
BuildRequires: mingw64-freetype
BuildRequires: mingw64-libidn
BuildRequires: mingw64-libjpeg
BuildRequires: mingw64-libpng
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-openssl
BuildRequires: mingw64-zlib
%endif

Obsoletes:      %{name}-libs < 0.10.0-1
Provides:       %{name} < 0.10.0-1
Provides:       %{name}-libs = %{version}-%{release}


%description
PoDoFo is a library to work with the PDF file format. The name comes from
the first letter of PDF (Portable Document Format). A few tools to work
with PDF files are already included in the PoDoFo package.

The PoDoFo library is a free, portable C++ library which includes classes
to parse PDF files and modify their contents into memory. The changes can be
written back to disk easily. The parser can also be used to extract
information from a PDF file (for example the parser could be used in a PDF
viewer). Besides parsing PoDoFo includes also very simple classes to create
your own PDF files. All classes are documented so it is easy to start writing
your own application using PoDoFo.


%package devel
Summary:        Development files for %{name} library
Requires:       openssl-devel%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and documentation for the %{name} library.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw32-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw32-%{name}-tools < 0.10.0-1
Provides:      mingw32-%{name}-tools = %{version}-%{release}

%description -n mingw32-%{name}-tools
Tools for the MinGW Windows %{name} library.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
Obsoletes:     mingw64-%{name}-tools < 0.10.0-1
Provides:      mingw64-%{name}-tools = %{version}-%{release}

%description -n mingw64-%{name}
MinGW Windows %{name} library.


%package -n mingw64-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}-tools
Tools for the MinGW Windows %{name} library.


%{?mingw_debug_package}

%endif


%prep
%autosetup -p1 -n %{name}-%{version}%{?pre:-%pre}

# disable timestamps in docs
echo "HTML_TIMESTAMP = NO" >> Doxyfile


%build
# Natve build
%cmake -DPODOFO_ENABLE_TOOLS=1
%cmake_build

%if %{with mingw}
# MinGW build
%mingw_cmake -DPODOFO_ENABLE_TOOLS=1
%mingw_make_build
%endif

# Doc build
doxygen
# set timestamps on generated files to some constant
find doc/html -exec touch -r %{SOURCE0} {} \;


%install
%cmake_install

%if %{with mingw}
%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}

%mingw_debug_install_post
%endif

# Move incorrectly installed files
mkdir -p %{buildroot}%{_libdir}/cmake/podofo/
mv %{buildroot}%{_datadir}/podofo/*.cmake %{buildroot}%{_libdir}/cmake/podofo/
rmdir %{buildroot}%{_datadir}/podofo/


%check
%ctest


%files
%doc AUTHORS.md CHANGELOG.md README.md TODO.md
%license COPYING
%{_libdir}/*.so.0.10.4
%{_libdir}/*.so.2

%files devel
%doc doc/html examples
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/lib%{name}.pc

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/libpodofo.dll
%{mingw32_libdir}/libpodofo.dll.a
%{mingw32_libdir}/pkgconfig/libpodofo.pc
%{mingw32_includedir}/podofo/

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/libpodofo.dll
%{mingw64_libdir}/libpodofo.dll.a
%{mingw64_libdir}/pkgconfig/libpodofo.pc
%{mingw64_includedir}/podofo/
%endif


%changelog
* Fri Jan 10 2025 Sandro Mani <manisandro@gmail.com> - 0.10.4-3
- Rebuild (icu)

* Sun Sep 15 2024 Sandro Mani <manisandro@gmail.com> - 0.10.4-2
- Refresh tarball

* Tue Sep 10 2024 Sandro Mani <manisandro@gmail.com> - 0.10.4-1
- Update to 0.10.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 07 2023 Sandro Mani <manisandro@gmail.com> - 0.10.3-1
- Update to 0.10.3

* Wed Nov 01 2023 Sandro Mani <manisandro@gmail.com> - 0.10.2-1
- Update to 0.10.2

* Wed Aug 16 2023 Sandro Mani <manisandro@gmail.com> - 0.10.1-1
- Update to 0.10.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Sandro Mani <manisandro@gmail.com> - 0.9.8-1
- Update to 0.9.8

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.9.7-8
- Rebuild with mingw-gcc-12

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 0.9.7-7
- Make mingw subpackages noarch

* Sat Feb 19 2022 Sandro Mani <manisandro@gmail.com> - 0.9.7-6
- Add mingw subpackage

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.9.7-4
- Rebuilt with OpenSSL 3.0.0

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Sandro Mani <manisandro@gmail.com> - 0.9.7-1
- Update to 0.9.7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Sandro Mani <manisandro@gmail.com> - 0.9.6-12
- Add podofo_maxbytes.patch

* Thu Jul 02 2020 Sandro Mani <manisandro@gmail.com> - 0.9.6-11
- Backport proposed patch for CVE-2018-12983

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Sandro Mani <manisandro@gmail.com> - 0.9.6-9
- Add patch for CVE-2019-20093

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-7
- Fix pkg-config file

* Wed Mar 13 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-6
- Backport security fixes: CVE-2019-9199, CVE-2019-9687

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-5
- Backport security fix for CVE-2018-20751

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Sandro Mani <manisandro@gmail.com> - 0.9.6-3
- Backport security fixes:
   CVE-2018-5783, CVE-2018-11254, CVE-2018-11255, CVE-2018-11256,
   CVE-2018-12982, CVE-2018-14320, CVE-2018-19532
- Run unit tests

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Sandro Mani <manisandro@gmail.com> - 0.9.6-1
- Update to 0.9.6
- Fixes: CVE-2018-5309, CVE-2018-8001

* Fri Jun 15 2018 Sandro Mani <manisandro@gmail.com> - 0.9.5-9
- Backport security fixes (taken from debian package):
   CVE-2017-7380, CVE-2017-7381, CVE-2017-7382, CVE-2017-7383, CVE-2017-5852,
   CVE-2017-5853, CVE-2017-6844, CVE-2017-5854, CVE-2017-5855, CVE-2017-5886,
   CVE-2018-8000, CVE-2017-6840, CVE-2017-6842, CVE-2017-6843, CVE-2017-6845,
   CVE-2017-6847, CVE-2017-6848, CVE-2017-7378, CVE-2017-7379, CVE-2017-7994,
   CVE-2017-8054, CVE-2017-8378, CVE-2017-8787, CVE-2018-5295, CVE-2018-5308

* Wed May 16 2018 Kevin Fenzi <kevin@scrye.com> - 0.9.5-8
- Rebuild for new libidn

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Sandro Mani <manisandro@gmail.com> - 0.9.5-3
- Drop -std=c++98 from CXXFLAGS

* Fri Feb 03 2017 Sandro Mani <manisandro@gmail.com> - 0.9.5-2
- Add Requires: openssl-devel to -devel

* Thu Feb 02 2017 Sandro Mani <manisandro@gmail.com> - 0.9.5-1
- Update to 0.9.5

* Fri Sep 23 2016 Sandro Mani <manisandro@gmail.com> - 0.9.4-1
- Update to 0.9.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.1-15
- Fix FTBFS on aarch64 (#1111745)

* Tue Jun 10 2014 Dan Horák <dan[at]danny.cz> - 0.9.1-14
- fix FTBFS (#1106651)
- spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Dan Horák <dan[at]danny.cz> - 0.9.1-12
- fix build with Lua 5.2 (#992811)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.9.1-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.9.1-8
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Dan Horák <dan[at]danny.cz> - 0.9.1-6
- disable timestamps in docs (#565683)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Dan Horák <dan[at]danny.cz> - 0.9.1-4
- build fix for unistd.h

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.1-2
- Rebuild for new libpng

* Thu Apr 28 2011 Dan Horák <dan[at]danny.cz> 0.9.1-1
- updated to 0.9.1

* Thu Apr 14 2011 Dan Horák <dan[at]danny.cz> 0.9.0-1
- updated to 0.9.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  2 2010 Dan Horák <dan[at]danny.cz> 0.8.4-1
- updated to 0.8.4

* Fri Oct 22 2010 Dan Horák <dan[at]danny.cz> 0.8.3-1
- updated to 0.8.3

* Tue Jun  8 2010 Dan Horák <dan[at]danny.cz> 0.8.1-2
- fix building tests

* Mon Jun  7 2010 Dan Horák <dan[at]danny.cz> 0.8.1-1
- updated to 0.8.1

* Thu Apr 29 2010 Dan Horák <dan[at]danny.cz> 0.8.0-1
- updated to 0.8.0

* Tue Feb 16 2010 Dan Horák <dan[at]danny.cz> 0.7.0-4
- set timestamp on generated docs (#565683)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 30 2009 Dan Horák <dan[at]danny.cz> 0.7.0-2
- remove BR: openssl-devel, it could be required in the future (but then
    an exception clause will be added to the licenses)
- add missing doc files

* Sun Mar 29 2009 Dan Horák <dan[at]danny.cz> 0.7.0-1
- initial Fedora package
