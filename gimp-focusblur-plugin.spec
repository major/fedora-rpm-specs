%global optflags %(echo "%{optflags} -DGIMP_DISABLE_DEPRECATED")
%global plugin_name focusblur
%global gimp_ver 2.4

Name:           gimp-%{plugin_name}-plugin
Version:        3.2.6
Release:        17%{?dist}
Summary:        Simulate an out-of-focus blur

License:        GPLv2+
URL:            http://registry.gimp.org/node/1444
Source0:        http://registry.gimp.org/files/%{plugin_name}-%{version}.tar.bz2

# Replace all #include <glib/*.h> with #include <glib.h>
Patch0:         %{name}-include-main-glib.patch
# Define _() and N() along with #include <libintl.h>
Patch1:         %{name}-fix-gettext.patch
# gcc10, global variables
Patch2:         focusblur-3.2.6-gcc10.patch

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  gimp-devel >= %{gimp_ver}
BuildRequires:  %{_bindir}/gdk-pixbuf-csource
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  fftw3-devel
BuildRequires:  intltool
BuildRequires:  gettext-devel
Requires:       gimp%{?_isa} >= %{gimp_ver}

%description
Focus Blur plug-in is blurring effect, a kind of called DoF. This software
makes a out of focus with luminosity and depth, like a sight or lenses. It
can be used with depth map, depth fakes and shine effect. Also it can work
as simple and applicable blur.

%prep
%autosetup -n %{plugin_name}-%{version} -p1
# Change name of gettext files to our own name
sed -i -e "/GETTEXT_PACKAGE/s/gimp20-%{plugin_name}/%{name}/" configure.ac configure

%build
autoreconf -vfi
# Link with math explicitly
# /usr/bin/ld: diffusion.o: undefined reference to symbol 'expf@@GLIBC_2.2.5'
%configure LIBS=-lm
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc ChangeLog
%{_libdir}/gimp/2.0/plug-ins/%{plugin_name}

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 05 2020 Than Ngo <than@redhat.com> - 3.2.6-11
- Fixed bz#1799405, FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.2.6-7
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 13 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.2.6-1
- Initial package
