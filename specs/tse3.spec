Name:           tse3
Version:        0.3.1
Release:        37%{?dist}
Summary:        MIDI Sequencer Engine
License:        GPL-1.0-or-later
URL:            http://tse3.sourceforge.net/
Source:         http://downloads.sourceforge.net/tse3/%{name}-%{version}.tar.gz
# patch for archs where size_t != unsigned int
# Fixes tse3 on amd64 systems, possibly others.
# Adapted from ALT Linux
#Patch0:         tse3-0.2.7-size_t-64bit.patch
Patch0:         tse3-size_t-64bit.patch
# This one is to fix compilation issues with gcc 4.3
Patch1:         tse3-gcc43.patch
# Fix FTBFS
Patch2:         tse3-autoconf.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
TSE3 is a powerful open source sequencer engine written in C++. It is a 
'sequencer engine' because it provides the actual driving force elements of a
sequencer but provides no form of user interface. Sequencer applications or 
multimedia presentation packages will incorporate the TSE3 libraries to 
provide a user with MIDI sequencing facilities.

%package devel
Summary:        Development packages for the TSE3 MIDI Sequencer Library
Requires:       %{name} == %{version}-%{release}

%description devel
TSE3 is a powerful open source sequencer engine written in C++. It is a 
'sequencer engine' because it provides the actual driving force elements of a
sequencer but provides no form of user interface. Sequencer applications or 
multimedia presentation packages will incorporate the TSE3 libraries to 
provide a user with MIDI sequencing facilities.

This package holds the development documentation, examples and header files 
for TSE3.

%prep
%setup -q
%patch -P0 -p2 -b .64bit
%patch -P1 -p2 -b .gcc43
%patch -P2 -p1 -b .autoconf

# Fix strange permissions issues
find . -name "*.cpp" -perm /111 -exec chmod 644 {} \;
find . -name "*.h" -perm /111 -exec chmod 644 {} \;

# Fix encoding issues
for i in demos/Demo.tse3 doc/History; do
    iconv -o $i.iso88591 -f iso88591 -t utf8 $i
    touch -r $i $i.iso88591
    mv -f $i.iso88591 $i
done


%build
# Need a newer configure script
autoreconf -fi

# OSS is being deprecated
%configure --with-alsa --with-mutex --with-doc-install --without-oss
# Parallel make not supported
make

%install
make install DESTDIR=%{buildroot} INSTALL="install -p" \
     docsdir=%{_docdir}/%{name}-devel-%{version}/HTML

# Sort out the development documentation. We don't want everything cluttered.

# These files belong to the devel documentation contentwise:
install -pm 0644 ChangeLog NEWS README THANKS TODO \
        %{buildroot}%{_docdir}/%{name}-devel-%{version}/

# Create a demos subdir and install all available demos in there:
install -d -m 0755 %{buildroot}%{_docdir}/%{name}-devel-%{version}/demos/
mv %{buildroot}%{_docdir}/%{name}-devel-%{version}/HTML/*.tse* \
    %{buildroot}%{_docdir}/%{name}-devel-%{version}/demos/
install -pm 0644 demos/*.ins demos/*.mid demos/*.tse* \
    %{buildroot}%{_docdir}/%{name}-devel-%{version}/demos/

# Provide the example source files in devel documentation:
make -C src/examples/ clean
cp -a src/examples/ %{buildroot}%{_docdir}/%{name}-devel-%{version}/

# Remove unneeded files:
rm -rf %{buildroot}%{_docdir}/%{name}-devel-%{version}/*/.deps \
       %{buildroot}%{_docdir}/%{name}-devel-%{version}/*/*/.deps

# Remove the library with the non-standard filename (this is a carbon copy
# of lib%{name}.so.x so we are not losing anything) and the .la file.
rm -rf %{buildroot}/%{_libdir}/lib%{name}-%{version}.so \
       %{buildroot}/%{_libdir}/*.la


%files
%doc AUTHORS
%license COPYING 
%{_bindir}/*
%{_libdir}/libtse3.so.*
%{_mandir}/man1/*


%files devel
%doc %{_docdir}/%{name}-devel-%{version}
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/libtse3.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.1-35
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.1-23
- Fix FTBFS due to changed autoconf behavior
- Some spec cleanup

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.1-15
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-9
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.1-7
- Fix FTBFS by going through an autohell cycle.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.1-3
- Clean the %%buildroot at the beginning of %%install

* Mon Jan 26 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.1-2.1
- Use -perm /111 instead of -executable for find, because it fails to work in F-9

* Sun Jan 25 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.1-2
- Move the HTML documentation into an HTML subdirectory
- Use INSTALL="install -p"
- Drop the oss support, and the related patch

* Tue Jan 20 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.1-1
- Initial Fedora build
