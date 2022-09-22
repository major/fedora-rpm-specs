# -*- rpm-spec -*-

%define with_mingw 0
%if 0%{?fedora}
    %define with_mingw 0%{!?_without_mingw:1}
%endif

Summary: Tools for managing the osinfo database
Name: osinfo-db-tools
Version: 1.10.0
Release: 5%{?dist}
License: GPLv2+
Source: https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
URL: https://libosinfo.org
BuildRequires: meson
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.0.0
%if 0%{?fedora} > 36 || 0%{?rhel} > 9
BuildRequires: libsoup3-devel
%else
BuildRequires: libsoup-devel
%endif
BuildRequires: libarchive-devel
BuildRequires: json-glib-devel
BuildRequires: /usr/bin/pod2man

#Required for testing purposes
BuildRequires: python3
BuildRequires: python3-pytest
BuildRequires: python3-requests

%if %{with_mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-glib2
BuildRequires: mingw32-json-glib
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-libxslt
BuildRequires: mingw32-libarchive
BuildRequires: mingw32-libsoup

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils
BuildRequires: mingw64-glib2
BuildRequires: mingw64-json-glib
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-libxslt
BuildRequires: mingw64-libarchive
BuildRequires: mingw64-libsoup
%endif

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%if %{with_mingw}
%package -n mingw32-osinfo-db-tools
Summary: %{summary}
BuildArch: noarch
Requires: pkgconfig

%description -n mingw32-osinfo-db-tools
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%package -n mingw64-osinfo-db-tools
Summary: %{summary}
BuildArch: noarch
Requires: pkgconfig

%description -n mingw64-osinfo-db-tools
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%{?mingw_debug_package}
%endif

%prep
%autosetup -S git

%build
%meson
%meson_build

%if %{with_mingw}
%mingw_meson
%mingw_ninja
%endif

%check
%meson_test

%install
%meson_install

%find_lang %{name}

%if %{with_mingw}
%mingw_ninja_install

# Manpages don't need to be bundled
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

%mingw_debug_install_post

%mingw_find_lang osinfo-db-tools
%endif

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/osinfo-db-export
%{_bindir}/osinfo-db-import
%{_bindir}/osinfo-db-path
%{_bindir}/osinfo-db-validate
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*

%if %{with_mingw}
%files -n mingw32-osinfo-db-tools -f mingw32-osinfo-db-tools.lang
%doc NEWS README
%license COPYING
%{mingw32_bindir}/osinfo-db-export.exe
%{mingw32_bindir}/osinfo-db-import.exe
%{mingw32_bindir}/osinfo-db-path.exe
%{mingw32_bindir}/osinfo-db-validate.exe

%files -n mingw64-osinfo-db-tools -f mingw64-osinfo-db-tools.lang
%doc NEWS README
%license COPYING
%{mingw64_bindir}/osinfo-db-export.exe
%{mingw64_bindir}/osinfo-db-import.exe
%{mingw64_bindir}/osinfo-db-path.exe
%{mingw64_bindir}/osinfo-db-validate.exe
%endif

%changelog
* Wed Aug 24 2022 Daniel P. Berrangé <berrange@redhat.com> - 1.10.0-5
- Switch to soup3

* Mon Aug  8 2022 Daniel P. Berrangé <berrange@redhat.com> - 1.10.0-4
- Pull in mingw sub-packages

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 14 2022 Victor Toso <victortoso@redhat.com> - 1.10.0-1
- Update to 1.10.0 release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 Fabiano Fidêncio <fidencio@redhat.com> - 1.9.0-1
- Update to 1.9.0 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Fabiano Fidêncio <fidencio@redhat.com> - 1.8.0-1
- Update to 1.8.0 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.7.0-1
- Update to 1.7.0 release

* Fri Jul 26 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.6.0-1
- Update to 1.6.0 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Fabiano Fidêncio <fidencio@redhat.com> -1.5.0-2
- Fix coverity issues

* Thu May 09 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.5.0-1
- Update to 1.5.0 release

* Thu Apr 11 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.4.0-2
- rhbz#1698845: Require GVFS

* Fri Mar 01 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.4.0-1
- Update to 1.4.0 release

* Fri Feb 01 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.3.0-1
- Update to 1.3.0 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Daniel P. Berrangé <berrange@redhat.com> - 1.2.0-1
- Update to 1.2.0 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Daniel P. Berrange <berrange@redhat.com> - 1.1.0-1
- Update to 1.1.0 release

* Fri Jul 29 2016 Daniel P. Berrange <berrange@redhat.com> - 1.0.0-1
- Initial package after split from libosinfo (rhbz #1361594)
