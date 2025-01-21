Name:           stoken
Version:        0.92
Release:        13%{?dist}
Summary:        Token code generator compatible with RSA SecurID 128-bit (AES) token
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://%{name}.sf.net

Source0:        https://github.com/cernekee/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(hogweed) >= 2.4
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nettle) >= 2.4

%description
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}

%description devel
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package provides the development files for %{name}.

%package libs
Summary:        Libraries for %{name}

%description libs
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains %{name} libraries.

%package cli
Summary:        Command line tool for %{name}

%description cli
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains the command line tool for %{name}.

%package gui
Summary:        Graphical interface program for %{name}

%description gui
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains the graphical interface program for %{name}.

%prep
%autosetup

%build
autoreconf -v -f --install
%configure --with-gtk --disable-static
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui-small.desktop

# Remove stuff we don't need
find %{buildroot} -type f -name "*.la" -delete
rm -fr %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets libs

%files libs
%license COPYING.LIB
%doc CHANGES
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.1.3.0

%files cli
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%files gui
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/applications/%{name}-gui-small.desktop
%{_datadir}/pixmaps/%{name}-gui.png
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}-gui.1.gz

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.92-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Simone Caronni <negativo17@gmail.com> - 0.92-1
- Update to 0.92.
- Update SPEC file.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Simone Caronni <negativo17@gmail.com> - 0.91-1
- Update to 0.91. Remove upstreamed patch.

* Sun Sep 11 2016 Simone Caronni <negativo17@gmail.com> - 0.90-5
- Skip extra newline when run from scripts.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 0.90-3
- Remove no longer required AppData file

* Mon Aug 10 2015 Simone Caronni <negativo17@gmail.com> - 0.90-2
- Upstream has re-released 0.9 as 0.90 fixing versioning issues.

* Thu Aug 06 2015 Simone Caronni <negativo17@gmail.com> - 0.90-1
- Rename 0.9 to 0.90.

* Thu Jul 30 2015 Simone Caronni <negativo17@gmail.com> - 0.9-1
- Update to 0.9.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.81-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 0.81-4
- Rebuilt for nettle soname bump

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.81-3
- Add an AppData file for the software center

* Tue Jan 13 2015 Simone Caronni <negativo17@gmail.com> - 0.81-2
- Use nettle instead of libtomcrypt (#1177180).

* Wed Dec 10 2014 Simone Caronni <negativo17@gmail.com> - 0.81-1
- Update to 0.81.

* Mon Sep 08 2014 Simone Caronni <negativo17@gmail.com> - 0.8-3.git.fd74297
- Update to git master.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2.git.ba44603
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Simone Caronni <negativo17@gmail.com> - 0.8-1.git.ba44603
- Update to 0.8 snapshot, requires gtk 3.
- Validate also small gui desktop file.

* Mon Jun 23 2014 Simone Caronni <negativo17@gmail.com> - 0.6-1
- Update to 0.6.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Simone Caronni <negativo17@gmail.com> - 0.5-1
- Update to 0.5.
- Removed upstreamed patch.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Simone Caronni <negativo17@gmail.com> - 0.2-4
- Change gtk and libtomcrypt build requirements.
- Remove useless "--with-libtomcrypt" parameter from %%configure.

* Tue Jun 04 2013 Simone Caronni <negativo17@gmail.com> - 0.2-3
- Add patch to avoid static CFLAGS.
- Require proper libtomcrypt version.

* Mon Jun 03 2013 Simone Caronni <negativo17@gmail.com> - 0.2-2
- Remove CFLAGS override and rpath commands.

* Mon Jun 03 2013 Simone Caronni <negativo17@gmail.com> - 0.2-1
- First build.
