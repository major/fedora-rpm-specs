%global gstreamer1_version 1.8.0

Name:           python-gstreamer1
Version:        1.24.11
Release:        1%{?dist}
Summary:        Python bindings for GStreamer

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-python/gst-python-%{version}.tar.xz

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  python3-devel
BuildRequires:  pkgconfig
BuildRequires:  gstreamer1-devel >= %{gstreamer1_version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{gstreamer1_version}
BuildRequires:  pkgconfig(pygobject-3.0)

# For the benefit of people migrating from the GStreamer-0.10 package,
# which was called gstreamer-python

%global _description\
This module contains PyGObject overrides to make it easier to write\
applications that use GStreamer 1.x in Python.

%description %_description

%package -n python3-gstreamer1
Summary:        Python bindings for GStreamer

Requires:       python3-gobject%{?_isa}
Requires:       gstreamer1%{?_isa} >= %{gstreamer1_version}

%description -n python3-gstreamer1
This module contains PyGObject overrides to make it easier to write
applications that use GStreamer 1.x in Python 3.

%prep
%autosetup -n gst-python-%{version} -p0

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%meson

%meson_build

%install
%meson_install

%files -n python3-gstreamer1
%license COPYING
%doc ChangeLog NEWS README.md RELEASE
%{python3_sitearch}/gi/overrides/*
%{_libdir}/gstreamer-1.0/libgstpython.*so

%changelog
* Tue Jan 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.24.11-1
- 1.24.11

* Wed Dec 04 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.10-1
- 1.24.10

* Thu Oct 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.9-1
- 1.24.9

* Thu Sep 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.8-1
- 1.24.8

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.24.7-2
- convert license to SPDX

* Wed Aug 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.7-1
- 1.24.7

* Mon Jul 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.6-1
- 1.24.6

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.5-1
- 1.24.5

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.24.4-2
- Rebuilt for Python 3.13

* Wed May 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.4-1
- 1.24.4

* Tue Apr 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.3-1
- 1.24.3

* Tue Mar 05 2024 Wim Taymans <wtaymans@redhat.com> - 1.24.0-1
- Update to 1.24.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 25 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.22.9-1
- 1.22.9

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.8-1
- 1.22.8

* Mon Nov 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.7-1
- 1.22.7

* Tue Oct 31 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.6-2
- Patch for Python 3.13

* Wed Sep 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.6-1
- 1.22.6

* Fri Jul 21 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.5-1
- Update to 1.22.5

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 1.22.4-2
- Rebuilt for Python 3.12

* Tue Jun 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.4-1
- 1.22.4

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.22.3-2
- Rebuilt for Python 3.12

* Thu May 25 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.3-1
- Update to 1.22.3

* Thu Apr 13 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.2-1
- Update to 1.22.2

* Mon Mar 13 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.1-1
- Update to 1.22.1

* Tue Jan 24 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.0-1
- Update to 1.22.0

* Mon Jan 23 2023 Wim Taymans <wtaymans@redhat.com> - 1.21.90-1
- Update to 1.21.90

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Wim Taymans <wtaymans@redhat.com> - 1.20.5-1
- Update to 1.20.5

* Thu Oct 13 2022 Wim Taymans <wtaymans@redhat.com> - 1.20.4-1
- Update to 1.20.4

* Fri Sep 09 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1.20.3-3
- Move gi overrides installation to platform-specific site-packages

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.20.3-1
- 1.20.3

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.20.2-2
- Rebuilt for Python 3.11

* Tue May 24 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.20.2-1
- 1.20.2

* Fri Feb 4 2022 Wim Taymans <wtaymans@redhat.com> - 1.20.0-1
- Update to 1.20.0

* Fri Jan 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.19.90-1
- 1.19.90

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 02 2022 W. Michael Petullo <mike@flyn.org> - 1.19.3-2
- Backport patch (upstream commit f95f63c5) that fixes BZ #2036542 and #2014915

* Thu Nov 11 2021 Wim Taymans <wtaymans@redhat.com> - 1.19.3-1
- Update to 1.19.3

* Thu Sep 23 2021 Wim Taymans <wtaymans@redhat.com> - 1.19.2-1
- Update to 1.19.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.19.1-2
- Rebuilt for Python 3.10

* Thu Jun 03 2021 Wim Taymans <wtaymans@redhat.com> - 1.19.1-1
- Update to 1.19.1

* Tue Mar 16 2021 Wim Taymans <wtaymans@redhat.com> - 1.18.4-1
- Update to 1.18.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.2-1
- Update to 1.18.2

* Fri Oct 30 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.1-1
- Update to 1.18.1

* Tue Sep 8 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.0-1
- Update to 1.18.0

* Fri Aug 21 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.90-1
- Update to 1.17.90

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 6 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.2-1
- Update to 1.17.2

* Mon Jun 22 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.1-1
- Update to 1.17.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.16.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 2 2020 Wim Taymans <wtaymans@redhat.com> - 1.16.2-1
- Update to 1.16.2

* Sun Nov 24 2019 Simon Farnsworth <simon@farnz.org.uk> - 1.16.1-2
- Remove python2 support from Rawhide specfile

* Tue Sep 24 2019 Wim Taymans <wtaymans@redhat.com> - 1.16.1-1
- Update to 1.16.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.16.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Charalampos Stratakis <cstratak@redhat.com> - 1.16.0-2
- Add Python 3.8 compatibility

* Fri Mar 01 2019 Wim Taymans <wtaymans@redhat.com> - 1.16.0-1
- Update to 1.16.0

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 1.15.1-3
- Update requires for pygobject3 -> python2-gobject rename

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Wim Taymans <wtaymans@redhat.com> - 1.15.1-1
- Update to 1.15.1

* Wed Oct 03 2018 Wim Taymans <wtaymans@redhat.com> - 1.14.4-1
- Update to 1.14.4

* Tue Sep 18 2018 Wim Taymans <wtaymans@redhat.com> - 1.14.3-1
- Update to 1.14.3

* Mon Jul 23 2018 Wim Taymans <wtaymans@redhat.com> - 1.14.2-1
- Update to 1.14.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.14.1-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Wim Taymans <wtaymans@redhat.com> - 1.14.1-1
- Update to 1.14.1

* Tue Mar 20 2018 Wim Taymans <wtaymans@redhat.com> - 1.14.0-1
- Update to 1.14.0

* Wed Mar 14 2018 Wim Taymans <wtaymans@redhat.com> - 1.13.91-1
- Update to 1.13.91

* Mon Mar 05 2018 Wim Taymans <wtaymans@redhat.com> - 1.13.90-1
- Update to 1.13.90

* Thu Feb 22 2018 Wim Taymans <wtaymans@redhat.com> - 1.13.1-1
- Update to 1.13.1
- The plugin has been renamed

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Wim Taymans <wtaymans@redhat.com> - 1.12.4-1
- Update to 1.12.4

* Tue Sep 19 2017 Wim Taymans <wtaymans@redhat.com> - 1.12.3-1
- Update to 1.12.3

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.12.2-4
- Python 2 binary package renamed to python2-gstreamer1
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Wim Taymans <wtaymans@redhat.com> - 1.12.2-1
- Update to 1.12.2

* Tue Jun 20 2017 Wim Taymans <wtaymans@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Wed May 10 2017 Wim Taymans <wtaymans@redhat.com> - 1.12.0-1
- Update to 1.12.0

* Fri Apr 28 2017 Wim Taymans <wtaymans@redhat.com> - 1.11.91-1
- Update to 1.11.91

* Tue Apr 11 2017 Wim Taymans <wtaymans@redhat.com> - 1.11.90-1
- Update to 1.11.90

* Fri Feb 24 2017 Wim Taymans <wtaymans@redhat.com> - 1.11.2-1
- Update to 1.11.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Wim Taymans <wtaymans@redhat.com> - 1.11.1-1
- Update to 1.11.1

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.10.2-2
- Rebuild for Python 3.6

* Mon Dec 05 2016 Wim Taymans <wtaymans@redhat.com> - 1.10.2-1
- Update to 1.10.2

* Mon Nov 28 2016 Wim Taymans <wtaymans@redhat.com> - 1.10.1-1
- Update to 1.10.1

* Thu Nov 03 2016 Wim Taymans <wtaymans@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Sat Oct 01 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.90-1
- Update to 1.9.90

* Thu Sep 01 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.2-1
- Update to 1.9.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 07 2016 Wim Taymans <wtaymans@redhat.com> - 1.9.1-1
- Update to 1.9.1

* Thu Jun 09 2016 Wim Taymans <wtaymans@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Thu Apr 21 2016 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Kalev Lember <klember@redhat.com> - 1.6.2-1
- Update to 1.6.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov 09 2015 Kalev Lember <klember@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Sat Aug 15 2015 Kalev Lember <klember@redhat.com> - 1.5.2-1
- Update to 1.5.2
- Use libdir macro instead of hardcoding lib64
- Use license macro for COPYING files

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar  8 2015 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 1.4.0-2
- Add support for writing GStreamer plugins in Python, using upstream patch from bug report.
- BuildRequire automake for now, as patch is against autotools files

* Tue Nov 04 2014 Jon Ciesla <limburgher@gmail.com> - 1.4.0-1
- 1.4.0, BZ 1155141.

* Wed Oct  8 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 1.3.90-4
- And fix 32-bit build without plugin support

* Wed Oct  8 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 1.3.90-3
- Typo fix

* Wed Oct  8 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 1.3.90-2
- Remove patch - it was a cherry-pick from upstream
- Disable support for writing GStreamer plugins in Python - upstream has a plugin name conflict between Python 2 and Python 3

* Wed Oct  8 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 1.3.90-1
- Update to 1.3.90 upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug  2 2014 Simon Farnsworth <simon@farnz.org.uk> - 1.2.1-5
- Patch initialisers for post-release change in pygobject

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4
* Sun Apr 27 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 1.2.1-1
- Upstream release gstreamer-python-1.2.1, fixing Python 3 support

* Mon Mar 17 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 1.2.0-2
- Disable Python 3 support - it's too buggy to ship
- Correct faulty macro setting in Python 3 block - it broke Python 2 build

* Sun Mar 16 2014 Simon Farnsworth <simon.farnsworth@onelan.co.uk> - 1.2.0-1
- Upstream release gstreamer-python-1.2.0
- Python 3 support

* Tue Nov 12 2013 Simon Farnsworth <simon@farnz.org.uk> - 1.1.90-1
- Using the gstreamer-python specfile as an example, package gst-python for GStreamer 1.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Kalev Lember <kalevlember@gmail.com> - 0.10.22-2
- Backport gst.preset_{set,get}_app_dir(), needed for transmageddon 0.21

* Sat Jul 14 2012 Kalev Lember <kalevlember@gmail.com> - 0.10.22-1
- Update to 0.10.22 (#750016)
- Include new headers in -devel subpackage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 Xavier Lamien <laxathom@fedoraproject.org> - 0.10.19-1
- Update release.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.10.16-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Aug 14 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.10-16-1
- Update release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Denis Leroy <denis@poolshark.org> - 0.10.15-1
- Update to upstream 0.10.15 (#502812)
- Added git patch to fix compile fix

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Denis Leroy <denis@poolshark.org> - 0.10.14-1
- Update to upstream 0.10.14, with various bug fixes
- Removed problematic devel Provide

* Sat Jan 10 2009 Denis Leroy <denis@poolshark.org> - 0.10.13-1
- Update to upstraem 0.10.13
- Forked devel package with pkgconfig file (#477310)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10.12-2
- Rebuild for Python 2.6

* Mon Aug 25 2008 Denis Leroy <denis@poolshark.org> - 0.10.12-1
- Update to upstream 0.10.12

* Fri Mar 28 2008 Denis Leroy <denis@poolshark.org> - 0.10.11-2
- Fixed datadir directory ownership (#439291)

* Sun Mar 23 2008 Denis Leroy <denis@poolshark.org> - 0.10.11-1
- Update to upstream 0.10.11, bugfix release updates

* Wed Feb 13 2008 Denis Leroy <denis@poolshark.org> - 0.10.10-1
- Update to upstream 0.10.10, BR updates

* Sun Dec  9 2007 Denis Leroy <denis@poolshark.org> - 0.10.9-1
- Update to upstream 0.10.9
- Removed exit patch, is upstream

* Fri Sep 14 2007 Denis Leroy <denis@poolshark.org> - 0.10.8-2
- Added patch to avoid crash on exit

* Mon Aug 20 2007 Denis Leroy <denis@poolshark.org> - 0.10.8-1
- Update to upstream 0.10.8
- License tag update

* Tue Feb 20 2007 Denis Leroy <denis@poolshark.org> - 0.10.7-2
- Ship examples in doc directory only, fixes multilib conflict (#228363)
- rpmlint cleanup

* Wed Feb 14 2007 Denis Leroy <denis@poolshark.org> - 0.10.7-1
- Update to 0.10.7
- Some spec cleanups

* Mon Dec 11 2006 Denis Leroy <denis@poolshark.org> - 0.10.6-1
- Update to 0.10.6, build with python 2.5

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.10.5-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Denis Leroy <denis@poolshark.org> - 0.10.5-1
- Update to 0.10.5

* Tue Sep 19 2006 Denis Leroy <denis@poolshark.org> - 0.10.4-2
- FE Rebuild

* Thu Jun 15 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.4-1
- new upstream release

* Tue Jan 24 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- update to GStreamer Python Bindings 0.10.2
- remove -devel requirements

* Thu May 19 2005 Thomas Vander Stichele <thomas at apestaart dot org> - 0.8.1-6
- disable docs build - they're already in the tarball

* Tue May 10 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.8.1-5
- Move __init__.py* files from lib to _libdir on multilibarchs
  Found in thias spec file, fixes x86_64

* Fri Apr  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.8.1-3
- include missing directories

* Thu Mar 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.8.1-2
- add deps pygtk2-devel and gstreamer-devel for pkgconfig file

* Fri Dec 24 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1-1: moved to Fedora Extras CVS

* Fri Dec 24 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1-0.fdr.2: various cleanups

* Tue Dec 07 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1-0.fdr.1: new upstream release

* Mon Nov 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.fdr.1: new upstream release

* Fri Nov 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.94-0.fdr.1: new upstream release

* Tue Oct 12 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.93-0.fdr.1: new upstream release

* Mon Jun 21 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.92-0.fdr.1: new upstream release

* Wed Mar 31 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.91-0.fdr.1: new upstream release

* Tue Sep 02 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.1.0-0.fdr.1: first fedora release
