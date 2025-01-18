Name:           gifsicle
Version:        1.95
Release:        4%{?dist}
Summary:        Powerful program for manipulating GIF images and animations

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.lcdf.org/gifsicle/
Source0:        http://www.lcdf.org/gifsicle/gifsicle-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires: make


%description
Gifsicle is a command-line tool for creating, editing, and getting
information about GIF images and animations.

Some more gifsicle features:

    * Batch mode for changing GIFs in place.
    * Prints detailed information about GIFs, including comments.
    * Control over interlacing, comments, looping, transparency...
    * Creates well-behaved GIFs: removes redundant colors, only uses local
      color tables if it absolutely has to (local color tables waste space
      and can cause viewing artifacts), etc.
    * It can shrink colormaps and change images to use the Web-safe palette
      (or any colormap you choose).
    * It can optimize your animations! This stores only the changed portion
      of each frame, and can radically shrink your GIFs. You can also use
      transparency to make them even smaller. Gifsicle?s optimizer is pretty
      powerful, and usually reduces animations to within a couple bytes of
      the best commercial optimizers.
    * Unoptimizing animations, which makes them easier to edit.
    * A dumb-ass name.

One other program is included with gifsicle
and gifdiff compares two GIFs for identical visual appearance.


%package -n gifview
Summary:        Lightweight animated-GIF viewer

%description -n gifview
gifview is a lightweight animated-GIF viewer which can show animations as
slideshows or in real time,


%prep
%setup -q


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc NEWS.md README.md
%{_bindir}/gifdiff
%{_bindir}/gifsicle
%{_mandir}/man1/gifdiff.1*
%{_mandir}/man1/gifsicle.1*

%files -n gifview
%license COPYING
%doc NEWS.md README.md
%{_bindir}/gifview
%{_mandir}/man1/gifview.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.95-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 21 2024 Orion Poplawski <orion@nwra.com> - 1.95-1
- Update to 1.95 CVE-2023-46009 (bz#2244935) CVE-2023-44821 (bz#2250064)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Orion Poplawski <orion@nwra.com> - 1.94-1
- Update to 1.94

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Orion Poplawski <orion@nwra.com> - 1.93-1
- Update to 1.93

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.92-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Orion Poplawski <orion@cora.nwra.com> - 1.92-1
- Update to 1.92

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Orion Poplawski <orion@cora.nwra.com> - 1.91-1
- Update to 1.91

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Orion Poplawski <orion@cora.nwra.com> - 1.90-1
- Update to 1.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.89-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Orion Poplawski <orion@cora.nwra.com> - 1.89-1
- Update to 1.89

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.88-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Orion Poplawski <orion@cora.nwra.com> - 1.88-1
- Update to 1.88

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.87-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 10 2014 Orion Poplawski <orion@cora.nwra.com> - 1.87-1
- Update to 1.87

* Fri Oct 17 2014 Orion Poplawski <orion@cora.nwra.com> - 1.86-1
- Update to 1.86

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 7  2014 Orion Poplawski <orion@cora.nwra.com> - 1.84-1
- Update to 1.84

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Orion Poplawski <orion@cora.nwra.com> - 1.83-1
- Update to 1.83

* Wed Mar 26 2014 Orion Poplawski <orion@cora.nwra.com> - 1.81-1
- Update to 1.81

* Tue Mar 18 2014 Orion Poplawski <orion@cora.nwra.com> - 1.79-1
- Update to 1.79

* Tue Dec 17 2013 Orion Poplawski <orion@cora.nwra.com> - 1.78-1
- Update to 1.78

* Mon Dec 2 2013 Orion Poplawski <orion@cora.nwra.com> - 1.77-1
- Update to 1.77

* Sat Nov 16 2013 Orion Poplawski <orion@cora.nwra.com> - 1.74-1
- Update to 1.74

* Fri Nov 15 2013 Orion Poplawski <orion@cora.nwra.com> - 1.72-1
- Update to 1.72

* Fri Aug 16 2013 Orion Poplawski <orion@cora.nwra.com> - 1.71-1
- Update to 1.71
- Some spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 4 2013 - Orion Poplawski <orion@cora.nwra.com> - 1.70-1
- Update to 1.70
- Some spec cleanup

* Mon Nov 26 2012 - Orion Poplawski <orion@cora.nwra.com> - 1.68-1
- Update to 1.68

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 - Orion Poplawski <orion@cora.nwra.com> - 1.67-1
- Update to 1.67

* Tue Apr 3 2012 - Orion Poplawski <orion@cora.nwra.com> - 1.66-1
- Update to 1.66

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 - Orion Poplawski <orion@cora.nwra.com> - 1.64-1
- Update to 1.64

* Thu Jul 21 2011 - Orion Poplawski <orion@cora.nwra.com> - 1.63-1
- Update to 1.63

* Tue Apr 5 2011 - Orion Poplawski <orion@cora.nwra.com> - 1.62-1
- Update to 1.62

* Mon Feb 28 2011 - Orion Poplawski <orion@cora.nwra.com> - 1.61-1
- Update to 1.61

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 - Orion Poplawski <orion@cora.nwra.com> - 1.60-2
- Add license to gifview package

* Tue Apr 13 2010 - Orion Poplawski <orion@cora.nwra.com> - 1.60-1
- Update to 1.60

* Wed Mar 17 2010 - Orion Poplawski <orion@cora.nwra.com> - 1.59-1
- Update to 1.59

* Tue Jan 19 2010 - Orion Poplawski <orion@cora.nwra.com> - 1.58-1
- Update to 1.58

* Thu Nov 12 2009 - Orion Poplawski <orion@cora.nwra.com> - 1.57-1
- Update to 1.57

* Mon Oct 19 2009 - Orion Poplawski <orion@cora.nwra.com> - 1.56-1
- Update to 1.56

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 - Orion Poplawski <orion@cora.nwra.com> - 1.55-1
- Update to 1.55

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 3 2008 - Orion Poplawski <orion@cora.nwra.com> - 1.52-1
- Update to 1.52

* Sat Feb  9 2008 - Orion Poplawski <orion@cora.nwra.com> - 1.48-4
- Rebuild for gcc 3.4

* Tue Aug 21 2007 - Orion Poplawski <orion@cora.nwra.com> - 1.48-3
- Update license tag to GPLv2+
- Rebuild for ppc32

* Tue Jul 10 2007 - Orion Poplawski <orion@cora.nwra.com> - 1.48-2
- Put gifview into separate gifview package

* Tue Jul 10 2007 - Orion Poplawski <orion@cora.nwra.com> - 1.48-1
- Initial Fedora package
