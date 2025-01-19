Name:           mypaint
Version:        2.0.1
Release:        13%{?dist}
Summary:        A fast and easy graphics application for digital painters

# MyPaint is GPLv2+, brush library LGPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ and CC-BY - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-CC-BY
URL:            http://mypaint.org
Source0:        https://github.com/mypaint/mypaint/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Backport of https://github.com/mypaint/mypaint/pull/1183
Patch0:         0001-setuptools-fixes.patch
# https://github.com/mypaint/mypaint/pull/1193
Patch1:         0002-python311.patch

BuildRequires:  gcc, gcc-c++

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-scons >= 3.0
BuildRequires:  swig
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  python3-numpy
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(mypaint-brushes-2.0)

Requires:       python3
Requires:       python3-numpy%{?_isa}
Requires:       python3-protobuf
Requires:       python3-gobject%{?_isa}
Requires:       %{name}2-brushes
Requires:       %{name}-data = %{version}-%{release}

%description
MyPaint is a fast and easy graphics application for digital painters. It lets
you focus on the art instead of the program. You work on your canvas with
minimum distractions, bringing up the interface only when you need it.


%package        data
Summary:        Common data files for for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    data
The %{name}-data package contains common data files for %{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

# for 64 bit
sed -i 's|lib/mypaint|%{_lib}/mypaint|g' mypaint.py
sed -i "s|'lib', 'mypaint'|'%{_lib}', 'mypaint'|" mypaint.py

%build
%{__python3} setup.py build_ext
%{__python3} setup.py build_py
%{__python3} setup.py build_translations
%{__python3} setup.py build_config

%install
%{__python3} setup.py managed_install --prefix=%{buildroot}%{_prefix}
[[ %{_lib} != lib ]] && mv %{buildroot}%{_prefix}/lib %{buildroot}%{_prefix}/%{_lib}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'


%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc Changelog.md README*
%{_bindir}/%{name}
%{_bindir}/%{name}-ora-thumbnailer
%{_datadir}/thumbnailers
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/actions/*.svg
%{_datadir}/icons/hicolor/*/actions/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg

%files data
%{_datadir}/%{name}/backgrounds
%{_datadir}/%{name}/palettes
%{_datadir}/%{name}/pixmaps

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.1-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 2.0.1-3
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.7.beta.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.6.beta.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.5.beta.0
- Rebuild to work around koji failure

* Wed Jan 01 2020 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.4.beta.0
- Update to 2.0.0-beta.0

* Thu Oct 10 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.3.alpha.12
- Remove python 2 dependency

* Thu Oct 10 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.2.alpha.12
- Fixed runtime dependency on mypaint2-brushes

* Thu Oct 10 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.1.alpha.12
- Update to 2.0.0-alpha.12

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-18
- Update patch for #1555277 (fix typo in the attribute)

* Tue Mar 27 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-17
- Update patch for #1555277

* Tue Mar 27 2018 Björn Esser <besser82@fedoraproject.org> - 1.2.1-16
- Rebuilt for libjson-c.so.4 (json-c v0.13.1) on fc28

* Mon Mar 26 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-15
- Fix loading cursor from custom theme under Wayland (fixes 1555277)

* Wed Mar 07 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-14
- Added gcc, gcc-c++ as build requirements

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 1.2.1-13
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 14 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-12
- Remove arch-dependent BuildRequires (fixes 1545198)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-10
- Fixes 1541605: do not use deprecated Gdk.Cursor constructor

* Fri Feb 02 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-8
- Fix architecture for python2-protobuf requirement.

* Fri Feb 02 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-7
- Use versioned package name for python gobject dependency.

* Thu Feb 01 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-6
- Use scons for python 2.7. Update requirements.

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-5
- Remove obsolete scriptlets

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.1-4
- Rebuilt for libjson-c.so.3

* Thu Dec 07 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-3
- Add missing runtime dependencies

* Thu Dec 07 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-2
- Add more brushes. Make mypaint-data package platform-independent.

* Tue Dec 05 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-13
- Rebuild for protobuf 3.3.1

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com>
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com>
- Rebuild for protobuf 3.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.1.0-5
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.1.0-3
- json-c renamed json.pc to json-c.pc

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (#891044)
- New devel package to develop brushlibs
- Add patch to make mypaint honor compiler flags
- Move more files over to mypaint-data package to save more space on mirrors
- Make sure scriptlets are called for the right subpackage

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.0-7
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-5
- Rebuild against numpy 1.7 (fixes 4837925)

* Wed Sep 26 2012 Thomas Spura <tomspur@fedoraproject.org> - 1.0.0-4
- patch: assume a prefix of /usr instead of / in a usrmoved system (fixes #797263)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-2
- %%{_bindir}/mypaint is arch specific and belongs into base package (#773079)

* Tue Jan 10 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Add brush sets Ramon2 and Concept Design

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.1-2
- Rebuild for new libpng

* Sat Mar 05 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.8.2-4
- recompiling .py files against Python 2.7 (rhbz#623339)

* Wed Aug 11 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-3
- Rebuild for Python 2.7 (#623339)

* Fri Apr 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8-2-2
- Rebuild (fixes 583156)

* Mon Mar 01 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Sun Feb 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Fri Jan 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Sat Nov 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.1-2
- Require numpy

* Wed Nov 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1
- Move private python modules to a private location
- Add scriptlets for gtk-update-icon-cache and update-desktop-database
- Fix License and Source0 tags

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5.1-3
- Rebuild for Python 2.6

* Mon Nov 3 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.5.1-2
- Add new website and download link
- Fix mydrawwidget location for F-10

* Sun Jul 27 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.5.1-1
- New version

* Wed Feb 13 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.5.0-7
- Rebuild for gcc4.3

* Mon Jan 21 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.5.0-6
- Added python sitearch instead of site lib
- Removed sitelib declaration

* Sat Jan 19 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.5.0-5
- Moved static object around thanks parag

* Mon Jan 14 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.5.0-4
- Fixed spec sheet

* Mon Jan 14 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.5.0-3
- Add devel package
- Remove static libraries

* Mon Jan 14 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.5.0-2
- Changed premissions on generate.py
- Removed static package

* Sun Jan 13 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.5.0-1
- initial spec file with static libraries in static file
