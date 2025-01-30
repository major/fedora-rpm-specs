# debuginfo not supported for static libraries, RB #209316
%global debug_package %{nil}

# Avoid -Werror=incompatible-pointer-type on 32-bit arches
%ifarch %{ix86}
%global build_type_safety_c 2
%endif

Name:           qm-dsp
Version:        1.7.1
Release:        25%{?dist}
Summary:        Library for DSP and Music Informatics purposes

# some source files with different original licenses, see README.txt
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
# original homepage: http://isophonics.net/QMVampPlugins
URL:            http://vamp-plugins.org/plugin-doc/qm-vamp-plugins.html
Source0:        https://code.soundsoftware.ac.uk/attachments/download/1582/%{name}-%{version}.tar.gz
# build flags
# (not intended for upstream)
Patch0:         qm-dsp-flags.patch
# install header files
# http://vamp-plugins.org/forum/index.php/topic,270.0.html
Patch1:         qm-dsp-install.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  imake
BuildRequires:  kiss-fft-static
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  boost148-devel
%else
BuildRequires:  boost-devel
%endif

%description
%{name} is a C++ library of functions for DSP and Music Informatics purposes
developed at Queen Mary, University of London. It is used by the QM Vamp
Plugins (q.v.) among other things.


%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{name} is a C++ library of functions for DSP and Music Informatics purposes
developed at Queen Mary, University of London. It is used by the QM Vamp
Plugins (q.v.) among other things.

This package contains header files and static library for development with
qm-dsp.


%prep
%setup -q
cp -p build/linux/Makefile.linux32 Makefile
%patch -P0 -p1
%patch -P1 -p1
# use specified CFLAGS for tests
cat >> tests/Makefile <<EOF

%.o: %.cpp
	\$(CXX) \$(CPPFLAGS) \$(CFLAGS) -c \$<
EOF
# unbundle kiss-fft
rm -rf ext/
# helper Makefile without valgrind
sed -e 's/$(VG) //' tests/Makefile > tests/Makefile.novg


%build
# unbundle kiss-fft
make depend

# extra cflags used in upstream
%ifarch %{ix86}
EXTRA_CFLAGS="-msse -mfpmath=sse"
%endif
%ifarch x86_64
EXTRA_CFLAGS="-msse -msse2 -mfpmath=sse"
%endif

# build
CFLAGS="$EXTRA_CFLAGS %{?optflags} -I%{_includedir}/kissfft" \
LDFLAGS="%{?__global_ldflags}" \
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

# Tests are broken

%files devel
%license COPYING
%doc README.txt
%{_libdir}/libqm-dsp.a
%{_includedir}/%{name}/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.1-24
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 06 2024 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-22
- Bump and rebuild package (for riscv64)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.7.1-13
- Drop unneeded dependency

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Guido Aulisi <guido.aulisi@gmail.com> - 1.7.1-10
- Unretire qm-dsp

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 František Dvořák <valtri@civ.zcu.cz> - 1.7.1-3
- Disable valgrind on AArch64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 František Dvořák <valtri@civ.zcu.cz> - 1.7.1-1
- Update to 1.7.1 (#1279112)
- New homepage
- Unbundled new kiss-fft library
- Removed C++ patch released in upstream
- Rebased build flags and install patches
- New packaging guidelines (license tag)
- Enabled tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 František Dvořák <valtri@civ.zcu.cz> - 1.7-2
- Updated patches and added comments

* Sun Aug 3 2014 František Dvořák <valtri@civ.zcu.cz> - 1.7-1
- Initial package
