%global         majorminor      1.0

Name:           gstreamer1-doc
Version:        1.24.11
Release:        1%{?dist}
BuildArch:      noarch
Summary:        GStreamer documentation

# All tutorial code is licensed under any of the following licenses (your choice):
#  2-clause BSD license ("simplified BSD license") (LICENSE.BSD)
#  MIT license (LICENSE.MIT)
#  LGPL v2.1 (LICENSE.LGPL-2.1)
# Application Developer Manual and Plugin Writer's Guide
#  Open Publication License v1.0 (LICENSE.OPL), for historical reasons.
# Documentation
#  Creative Commons CC-BY-SA-4.0 license, but some parts of the documentation
#  may still be licensed differently (e.g. LGPLv2.1) for historical reasons.
License:        (BSD or MIT or LGPLv2+) and Open Publication and CC-BY-SA
URL:            http://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org/src/gstreamer-docs/gstreamer-docs-%{version}.tar.xz

%description
GStreamer documentation.

%prep
%setup -q -n gstreamer-docs-%{version}

%install

# move devhelp into the right directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/
mv devhelp/books/GStreamer $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}
# Remove the search assets, we use devhelp search
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/assets/js/search
# Rename the devhelp docs to include the version
mv $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/GStreamer.devhelp2 \
   $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/GStreamer-%{majorminor}.devhelp2

%files
%doc README.md html
%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/

%changelog
* Tue Jan 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.24.11-1
- 1.24.11

* Wed Dec 04 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.10-1
- 1.24.10

* Thu Oct 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.9-1
- 1.24.9

* Thu Sep 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.8-1
- 1.24.8

* Wed Aug 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.7-1
- 1.24.7

* Mon Jul 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.6-1
- 1.24.6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.5-1
- 1.24.5

* Wed May 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.4-1
- 1.24.4

* Tue Apr 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.3-1
- 1.24.3

* Tue Mar 05 2024 Wim Taymans <wtaymans@redhat.com> - 1.24.0-1
- Update to 1.24.0

* Thu Jan 25 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.22.9-1
- 1.22.9

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.8-1
- 1.22.8

* Tue Nov 14 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.7-1
- 1.22.7

* Fri Jul 21 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.5-1
- Update to 1.22.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 25 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.3-1
- Update to 1.22.3

* Thu Apr 13 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.2-1
- Update to 1.22.2

* Mon Mar 13 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.1-1
- Update to 1.22.1

* Tue Jan 24 2023 Wim Taymans <wtaymans@redhat.com> - 1.22.0-1
- Update to 1.22.0

* Fri Jan 20 2023 Wim Taymans <wtaymans@redhat.com> - 1.21.90-1
- Update to 1.21.90

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Wim Taymans <wtaymans@redhat.com> - 1.20.5-1
- Update to 1.20.5

* Thu Oct 13 2022 Wim Taymans <wtaymans@redhat.com> - 1.20.4-1
- Update to 1.20.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Wim Taymans <wtaymans@redhat.com> - 1.20.3-1
- Update to 1.20.3

* Fri Feb 4 2022 Wim Taymans <wtaymans@redhat.com> - 1.20.0-1
- Update to version 1.20.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Wim Taymans <wtaymans@redhat.com> - 1.19.3-1
- Update to version 1.19.3

* Thu Sep 23 2021 Wim Taymans <wtaymans@redhat.com> - 1.19.2-1
- Update to version 1.19.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Wim Taymans <wtaymans@redhat.com> - 1.19.1-1
- Update to version 1.19.1

* Tue Mar 16 2021 Wim Taymans <wtaymans@redhat.com> - 1.18.4-1
- Update to version 1.18.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.2-1
- Update to version 1.18.2

* Fri Oct 30 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.1-1
- Update to version 1.18.1

* Tue Sep 8 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.0-1
- Update to version 1.18.0

* Fri Aug 21 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.90-1
- Update to version 1.17.90

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 8 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.2-2
- BuildArch: noarch
- Correct License: field and clarify breakdown
- Small cleanups (see rhbz#1854392)

* Tue Jul 7 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.2-1
- Initial version 1.17.2
