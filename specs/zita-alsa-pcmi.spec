Summary:       ALSA C++ library
Name:          zita-alsa-pcmi
Version:       0.6.1
Release:       7%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later 
URL:           http://kokkinizita.linuxaudio.org
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: gcc-c++

%description
%{name} is the successor of clalsadrv. It provides easy access
to ALSA PCM devices, taking care of the many functions required to
open, initialize and use a hw: device in mmap mode, and providing
floating point audio data.

%package       devel
Summary:       Development libraries and headers for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      alsa-lib-devel

%description   devel
This package contains the headers and development libraries for %{name}.


%package       utils
Summary:       ALSA utilities using the %{name} library
Requires:      %{name}%{?_isa} = %{version}-%{release}
# The following are GPLv2+ licensed:
# /apps/alsa_delay.cc, /apps/alsa_loopback.cc, /apps/mtmd.cc /apps/mtdm.cc
License:       GPL-2.0-or-later AND GPL-3.0-or-later

%description   utils
This package contains the headers and development libraries for %{name}.

%prep
%setup -q

# No -march=native and ldconfig in Makefile and preserve timestamps
sed -i -e '/^CXXFLAGS += -march=native/d' -e '/ldconfig/d' -e 's/install -m/install -p -m/g' source/Makefile
sed -i -e 's/install -m/install -p -m/g' apps/Makefile

# Patch wrong bin destdir (sent upstream by email on 20190803)
sed -i -e 's/install -d $(BINDIR)/install -d $(DESTDIR)$(BINDIR)/' apps/Makefile

%build
%set_build_flags

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} -C source

# Create symlink to build apps
ln -sf lib%{name}.so.%{version} source/lib%{name}.so

%make_build PREFIX=%{_prefix} CXXFLAGS="${CXXFLAGS} -I../source" LDFLAGS="${LDFLAGS} -L../source" -C apps

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} -C source
%make_install PREFIX=%{_prefix} -C apps

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files utils
%{_bindir}/alsa_delay
%{_bindir}/alsa_loopback

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.1-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Guido Aulisi <guido.aulisi@gmail.com> - 0.6.1-1
- Update to 0.6.1
- Fix bug 2156573

* Tue Dec 27 2022 Guido Aulisi <guido.aulisi@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar 13 2022 Guido Aulisi <guido.aulisi@gmail.com> - 0.4.0-1
- Update to 0.4.0
- Correct shared library globbing

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.2-1
- Update to 0.3.2
- Some spec cleanup

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.2.0-19
- Use Fedora link flags
- Add BR: gcc-c++
- Some cleanup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Jørn Lomax <northlomax@gmail.com> 0.2.0-8
- corrected licenses

* Mon Jun 25 2012 Jørn Lomax <northlomax@gmail.com> 0.2.0-7
- fixed licencing information and patch status

* Thu Jun 21 2012 Jørn Lomax <northlomax@gmail.com> 0.2.0-6
- changed from OPTFLAGS as argument to using export in build

* Mon Jun 18 2012 Jørn Lomax <northlomax@gmail.com> 0.2.0-5
- fixed changelog to fit requirements
- added patches to remove sed lines 

* Thu Jun 14 2012 Jørn Lomax <northlomax@gmail.com> 0.2.0-4
- replaced ln with ldconig in the install section

* Thu Jun 14 2012 Jørn Lomax <northlomax@gmail.com> 0.2.0-3
- Edited back to original to prevent rpmlint warnings

* Fri Jun 8  2012 Jørn Lomax <northlomax@gmail.com> 0.2.0-2
- Cleaned up spec for review

* Wed May 23 2012 Jorn Lomax <northlomax@gmail.com> 0.2.0-1
- Initial SPEC creation
