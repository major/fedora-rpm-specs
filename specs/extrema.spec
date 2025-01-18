%ifarch i686
%global _lto_cflags %nil
%endif

Summary:       A powerful visualization and data analysis tool
Name:          extrema
Version:       4.4.5
Release:       41%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://exsitewebware.com/extrema/
Source0:       http://downloads.sourceforge.net/extrema/extrema-%{version}.tar.gz
Patch0:        extrema-4.2.10.desktop.patch
Patch1:        extrema-4.4.5-gcc46.patch
Patch2:        extrema-4.4.5-wx3.0.patch
Patch3:        extrema-4.4.5-wx3.0-2.patch
Patch4:        extrema-4.4.5-wx3.2.patch
BuildRequires: gcc-c++
BuildRequires: wxGTK-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
BuildRequires: make
Requires:      extrema-help

%description
Extrema is a powerful visualization and data analysis tool that
enables researchers to quickly distill their large, complex data sets
into meaningful information. Its flexibility, sophistication, and
power allow you to easily develop your own commands and create highly
customized graphs.

%package       help
Summary:       Help files for Extrema
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description   help
This package contains help files for Extrema.

%package       doc
Summary:       Extrema documentation in PDF format
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description   doc
This package contains Getting Started, User Guide and other
documentation in PDF format for Extrema.

%prep
%autosetup -p1

%build
%configure --disable-static CXXFLAGS="%{optflags} -DNDEBUG"
make %{?_smp_mflags}
convert Images/%{name}.gif %{name}.png

%install
make install DESTDIR=%{buildroot}
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
install -m 0644 -D %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
rm -f %{buildroot}%{_libdir}/lib%{name}.{la,a}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/extrema
%dir %{_datadir}/extrema
%{_datadir}/extrema/Images
%{_datadir}/applications/extrema.desktop
%{_datadir}/pixmaps/extrema.png

%files help
%{_datadir}/extrema/Help

%files doc
%doc doc/*.pdf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.4.5-40
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 4.4.5-34
- Rebuild with wxWidgets 3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 08 2022 Terje Rosten <terje.rosten@ntnu.no> - 4.4.5-32
- Disable LTO on i686

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Scott Talbert <swt@techie.net> - 4.4.5-24
- Rebuild with wxWidgets 3.0

* Sat Jul 14 2018 Terje Rosten <terje.rosten@ntnu.no> - 4.4.5-23
- Add C++ compiler

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.4.5-14
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 15 2013 Terje Rosten <terje.rosten@ntnu.no> - 4.4.5-11
- Remove outdated obsoletes, spec file cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Jon Ciesla <limburgher@gmail.com> - 4.4.5-9
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.4.5-4
- Rebuilt for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.4.5-2
- Add patch to build with gcc 4.6

* Sun Jan 30 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.4.5-1
- 4.4.5

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 4.4.4-2
- rebuilt against wxGTK-2.8.11-2

* Thu Jun 17 2010 Terje Rosten <terje.rosten@ntnu.no> - 4.4.4-1
- 4.4.4

* Sun Dec 06 2009 Terje Rosten <terje.rosten@ntnu.no> - 4.4.2-1
- 4.4.2

* Tue Aug 18 2009 Terje Rosten <terje.rosten@ntnu.no> - 4.3.6-5
- Split out documentation

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 4.3.6-2
- Fix Patch0:/%%patch mismatch.

* Fri Aug 15 2008 Terje Rosten <terje.rosten@ntnu.no> - 4.3.6-1
- 4.3.6

* Wed Feb 27 2008 Terje Rosten <terje.rosten@ntnu.no> - 4.3.5-1
- 4.3.5

* Fri Feb  8 2008 Terje Rosten <terje.rosten@ntnu.no> - 4.3.4-2
- Rebuild

* Sun Jan  6 2008 Terje Rosten <terje.rosten@ntnu.no> - 4.3.4-1
- 4.3.4
- Drop gcc43 patch, upstream now

* Sun Jan  6 2008 Terje Rosten <terje.rosten@ntnu.no> - 4.3.1-1
- 4.3.1
- Add patch to build with gcc 4.3

* Sun Nov 18 2007 Terje Rosten <terje.rosten@ntnu.no> - 4.2.10-3
- Add req. on help subpackage

* Sun Nov  4 2007 Terje Rosten <terje.rosten@ntnu.no> - 4.2.10-2
- Fix license
- Change convert buildreq to ImageMagick
- Move to Graphics menu

* Sat Nov  3 2007 Terje Rosten <terje.rosten@ntnu.no> - 4.2.10-1
- Initial package
