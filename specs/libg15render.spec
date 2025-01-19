%global svnrev 316

Name:           libg15render
Version:        1.3.0
Release:        0.16.svn%{svnrev}%{?dist}
Summary:        Library for rendering bitmaps for the Logitech G15 keyboard LCD
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://sourceforge.net/projects/g15tools/
# Upstream is dead and never did a proper release of 1.3.0, use a svn snapshot
# as Debian and other distros are doing
Source0:        ftp://ftp.nluug.nl/pub/os/Linux/distr/debian/pool/main/libg/libg15render/libg15render_%{version}~svn%{svnrev}.orig.tar.gz
BuildRequires:  gcc make libtool freetype-devel

%description
libg15render is a library for rendering bitmaps in the format expected
by the LCD screen on the Logitech G15 (and similar) keyboards.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       freetype-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}.svn%{svnrev}
autoreconf -ivf


%build
%configure --disable-static --enable-ttf
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Nuke docs installed in wrong location
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-1.3


%files
%license COPYING
%doc AUTHORS README
%{_libdir}/*.so.1*
%{_datadir}/g15tools

%files devel
%{_bindir}/g15fontconvert
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/libg15render.3*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.16.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.0-0.15.svn316
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.14.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.13.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.12.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.11.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.10.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.9.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.8.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Hans de Goede <hdegoede@redhat.com> - 1.3.0-0.7.svn316
- libg15render.h includes freetype headers, add a Requires: freetype-devel
  to the libg15render-devel package

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.6.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.5.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.4.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.3.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.2.svn316
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Hans de Goede <hdegoede@redhat.com> - 1.3.0-0.1.svn316
- Initial libg15render Fedora package
