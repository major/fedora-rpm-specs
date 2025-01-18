%global         solib tolua++-5.1

Name:           compat-tolua++
Version:        1.0.93
Release:        25%{?dist}
Summary:        Lua-5.1 compatible version of tolua++ (C++ Lua integration)
License:        MIT
# Upstream is defunct, so no URL
Source0:        tolua++-%{version}.tar.bz2
Patch0:         tolua++-1.0.93-lua51.patch
Patch1:         tolua++-1.0.93-lua-include-path.patch
Patch2:         tolua++-1.0.93-scons304.patch
Patch3:         tolua++-1.0.93-scons-env.patch
BuildRequires:  gcc
BuildRequires:  python3-scons
BuildRequires:  compat-lua-devel >= 5.1

%description
This is a lua-5.1 compatible version of tolua++.

tolua++ is an extended version of tolua, a tool to integrate C/C++ code with
Lua. tolua++ includes new features oriented to C++.


%package devel
Summary:        Development files for compat-tolua++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       compat-lua-devel >= 5.1
# tolua++-devel and compat-tolua++ cannot be installed at the same time
Conflicts:      tolua++-devel

%description devel
Development files for compat-tolua++.


%prep
%autosetup -p1 -n tolua++-%{version}
sed -i 's/\r//' doc/tolua++.html


%build
# el8 provides the scons binary as scons-3 from the powertools repo
%if 0%{?el8}
SCONS_BIN=scons-3
%else
SCONS_BIN=scons
%endif

$SCONS_BIN %{?_smp_mflags} -Q CCFLAGS="%{optflags} $(pkg-config --cflags lua-5.1)" \
  LINKFLAGS="%{optflags} %{?build_ldflags} -Wl,-soname,lib%{solib}.so" \
  tolua_lib=%{solib} shared=1
# Relink the tolua++ binary, there are 2 reasons for this:
# -Link it without the soname which we add to LINKFLAGS to build a shared lib
# -On non x86_64 link it against the pre-generated toluabind rather then the
#  bootstapped one as something goes wrong with the bootstrap on ARM, x86_32
#  (rhbz#1094103) and ppc (rhbz#704372) causing a segfault for unknown reasons.
%ifarch x86_64
gcc -o bin/tolua++ src/bin/tolua.o src/bin/toluabind.o $RPM_OPT_FLAGS $RPM_LD_FLAGS \
  -Llib -l%{solib} -llua-5.1 -ldl -lm
%else
gcc -o bin/tolua++ src/bin/tolua.o src/bin/toluabind_default.o $RPM_OPT_FLAGS $RPM_LD_FLAGS \
  -Llib -l%{solib} -llua-5.1 -ldl -lm
%endif


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 bin/tolua++  $RPM_BUILD_ROOT%{_bindir}
install -m 755 lib/lib%{solib}.so $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{solib}.so $RPM_BUILD_ROOT%{_libdir}/libtolua++.so
install -p -m 644 include/tolua++.h $RPM_BUILD_ROOT%{_includedir}


%ldconfig_scriptlets


%files
%doc README
%license COPYRIGHT
%{_libdir}/lib%{solib}.so


%files devel
%doc doc/*
%{_bindir}/tolua++
%{_libdir}/libtolua++.so
%{_includedir}/tolua++.h


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Hans de Goede <hdegoede@redhat.com> - 1.0.93-23
- Fix FTBFS (rhbz#2261040)
- Use distro LD_FLAGS when linking

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Hans de Goede <hdegoede@redhat.com> - 1.0.93-13
- Fix FTBFS (rhbz#1799247)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Hans de Goede <hdegoede@redhat.com> - 1.0.93-11
- Fix FTBFS with scons-3.0.4 (rhbz#1674758)
- Switch to python3-scons

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Hans de Goede <hdegoede@redhat.com> - 1.0.93-2
- Upstream is defunct, remove URLs pointing to it
- Minor specifile cleanups (rhbz#1195255)

* Mon Feb 23 2015 Hans de Goede <hdegoede@redhat.com> - 1.0.93-1
- First version of compat-tolua++, based on the f21 tolua++ package
