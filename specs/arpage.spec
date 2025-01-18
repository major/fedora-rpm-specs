%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		arpage
Version:	0.3.3
Release:	41%{?dist}
Summary:	A JACK MIDI arpeggiator

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		http://arpage.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-gcc46.patch
Patch1:		%{name}-gcc47.patch

BuildRequires:  gcc-c++
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	gtkmm24-devel
BuildRequires:	intltool libxml++-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires: make

%description

A GTK application that runs up to 4 arpeggiators on incoming MIDI
data, synchronized to JACK.

%prep

%setup -q

#fix compilation with gcc 4.6
%patch -P0 -p1 -b .%{name}-gcc46.patch
#fix compilation with gcc 4.7
%patch -P1 -p1 -b .%{name}.gcc47.patch

# fix bad permissions in debuginfo
chmod 644 %{_builddir}/%{name}-%{version}/src/main.cc

%build

# Fix for aarch64 build
#automake --add-missing
autoreconf -i

%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} arpagedocdir=%{_pkgdocdir}

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps
install -m 644 %{_builddir}/%{name}-%{version}/src/arpage.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/


%files
%doc COPYING ChangeLog AUTHORS README INSTALL NEWS
%{_bindir}/%{name}
%{_bindir}/zonage
%{_datadir}/%{name}/ui/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.3-40
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-24
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.3-18
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Adam Huffman <bloch@verdurin.com> - 0.3.3-16
- More aarch64 build fixes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Adam Huffman <bloch@verdurin.com> - 0.3.3-14
- Fix for aarch64 builds

* Mon Aug 05 2013 Adam Huffman <bloch@verdurin.com> - 0.3.3-13
- Fixes for new %%doc handling

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-9
- Rebuilt for c++ ABI breakage

* Sun Jan  8 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.3.3-8
- add patch for GCC 4.7
- rebuild for GCC 4.7

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3.3-7
- Rebuild for new libpng

* Fri Jun 24 2011 Adam Huffman <bloch@verdurin.com> - 0.3.3-6
- add patch to fix compilation with GCC 4.6

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 23 2010 Adam Huffman <bloch@verdurin.com> - 0.3.3-4
- - minor fix to icon scriptlet path

* Wed Jun 23 2010 Adam Huffman <bloch@verdurin.com> - 0.3.3-3
- fix desktop file and icon handling

* Mon Jun 21 2010 Adam Huffman <bloch@verdurin.com> - 0.3.3-2
- add AUTHORS and README to doc
- add desktop file
- add icon

* Fri May 21 2010 Adam Huffman <bloch@verdurin.com> - 0.3.3-1
- new upstream release
- add libxml++ BR
- add new UI files

* Sun Jan 31 2010 Adam Huffman <bloch@verdurin.com> - 0.2-1
- initial version
- Makefile variable set to move doc files to standard location
- delete empty doc files
