%{?mingw_package_header}

%global majorver 9
%global minorver 0
%global fullver %{majorver}.%{minorver}

Name:          mingw-tk
Version:       9.0.2
Release:       1%{?dist}
Summary:       MinGW Windows graphical toolkit for the Tcl scripting language

License:       TCL
URL:           http://tcl.sourceforge.net/
Source0:       http://downloads.sourceforge.net/sourceforge/tcl/tk%{version}-src.tar.gz
BuildArch:     noarch

BuildRequires: make

BuildRequires: mingw32-tcl = %{version}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc

BuildRequires: mingw64-tcl = %{version}
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc


%description
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.


%package -n mingw32-tk
Summary:   MinGW Windows graphical toolkit for the Tcl scripting language

%description -n mingw32-tk
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.


%package -n mingw64-tk
Summary:   MinGW Windows graphical toolkit for the Tcl scripting language

%description -n mingw64-tk
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n tk%{version}


%build
pushd win

MINGW32_CONFIGURE_ARGS="--with-tcl=%{mingw32_libdir}"
MINGW64_CONFIGURE_ARGS="--with-tcl=%{mingw64_libdir}"
%{mingw_configure}
%{mingw32_make} -C build_win32 TCL_LIBRARY=%{mingw32_datadir}/tk%{fullver}
%{mingw64_make} -C build_win64 TCL_LIBRARY=%{mingw64_datadir}/tk%{fullver}
popd


%install
make install -C win/build_win32 INSTALL_ROOT=%{buildroot} TK_LIBRARY=%{mingw32_datadir}/tk%{fullver}
make install -C win/build_win64 INSTALL_ROOT=%{buildroot} TK_LIBRARY=%{mingw64_datadir}/tk%{fullver}

ln -s wish%{majorver}%{minorver}.exe %{buildroot}%{mingw32_bindir}/wish.exe
ln -s wish%{majorver}%{minorver}.exe %{buildroot}%{mingw64_bindir}/wish.exe

# for linking with -libtk
ln -s libtcl9tk%{majorver}%{minorver}.dll.a %{buildroot}%{mingw32_libdir}/libtk.dll.a
ln -s libtcl9tk%{majorver}%{minorver}.dll.a %{buildroot}%{mingw64_libdir}/libtk.dll.a

mkdir -p %{buildroot}/%{mingw32_libdir}/tk%{fullver}
mkdir -p %{buildroot}/%{mingw64_libdir}/tk%{fullver}

# postgresql and maybe other packages too need tclConfig.sh
# paths don't look at /usr/lib for efficiency, so we symlink into tcl8.5 for now
ln -s ../tkConfig.sh \
      %{buildroot}/%{mingw32_libdir}/tk%{fullver}/tkConfig.sh
ln -s ../tkConfig.sh \
      %{buildroot}/%{mingw64_libdir}/tk%{fullver}/tkConfig.sh

mkdir -p %{buildroot}/%{mingw32_includedir}/tk-private/{generic/ttk,win}
mkdir -p %{buildroot}/%{mingw64_includedir}/tk-private/{generic/ttk,win}
find generic win -name "*.h" -exec cp -p '{}' %{buildroot}/%{mingw32_includedir}/tk-private/'{}' ';'
find generic win -name "*.h" -exec cp -p '{}' %{buildroot}/%{mingw64_includedir}/tk-private/'{}' ';'
(
cd %{buildroot}/%{mingw32_includedir}
for i in *.h ; do
      [ -f %{buildroot}/%{mingw32_includedir}/tk-private/generic/$i ] && \
      ln -sf ../../$i %{buildroot}/%{mingw32_includedir}/tk-private/generic || : ;
done
)
(
cd %{buildroot}/%{mingw64_includedir}
for i in *.h ; do
      [ -f %{buildroot}/%{mingw64_includedir}/tk-private/generic/$i ] && \
      ln -sf ../../$i %{buildroot}/%{mingw64_includedir}/tk-private/generic || : ;
done
)


%files -n mingw32-tk
%{mingw32_bindir}/wish.exe
%{mingw32_bindir}/wish%{majorver}%{minorver}.exe
%{mingw32_bindir}/tcl9tk%{majorver}%{minorver}.dll
%{mingw32_libdir}/libtcl9tk%{majorver}%{minorver}.dll.a
%{mingw32_libdir}/libtkstub.a
%{mingw32_libdir}/libtk.dll.a
%{mingw32_libdir}/tkConfig.sh
%{mingw32_includedir}/*
%{mingw32_libdir}/tk%{fullver}/
%{mingw32_datadir}/tk%{majorver}.%{minorver}
%license license.terms

%files -n mingw64-tk
%{mingw64_bindir}/wish.exe
%{mingw64_bindir}/wish%{majorver}%{minorver}.exe
%{mingw64_bindir}/tcl9tk%{majorver}%{minorver}.dll
%{mingw64_libdir}/libtcl9tk%{majorver}%{minorver}.dll.a
%{mingw64_libdir}/libtkstub.a
%{mingw64_libdir}/libtk.dll.a
%{mingw64_libdir}/tkConfig.sh
%{mingw64_includedir}/*
%{mingw64_libdir}/tk%{fullver}/
%{mingw64_datadir}/tk%{majorver}.%{minorver}
%license license.terms


%changelog
* Sun Oct 12 2025 Sandro Mani <manisandro@gmail.com> - 9.0.2-1
- Update to 9.0.2

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Sandro Mani <manisandro@gmail.com> - 8.6.15-1
- Update to 8.6.15

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 04 2024 Sandro Mani <manisandro@gmail.com> - 8.6.14-1
- Update to 8.6.14

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Sandro Mani <manisandro@gmail.com> - 8.6.13-1
- Update to 8.6.13

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 8.6.12-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Sandro Mani <manisandro@gmail.com> - 8.6.12-1
- Update to 8.6.12

* Sat Jul 31 2021 Sandro Mani <manisandro@gmail.com> - 8.6.10-1
- Update to 8.6.10

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.8-1
- Update to 8.6.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 8.6.7-2
- Fix debug file in main package

* Thu Aug 10 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.7-1
- Update to 8.6.7

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.6-1
- Update to 8.6.6

* Wed Jun 29 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.4-2
- Build mingw64-tk (#1269746)

* Wed Jun 29 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.4-1
- Update to 8.6.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 22 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.6.1-1
- Update to 8.6.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 12 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.5.13-4
- Fix FTBFS against latest mingw-w64

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 12 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.5.13-1
- Update to 8.5.13 (fixes FTBFS caused by latest mingw-tcl)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 8.5.9-6
- Fix the sed magic after mingw32-tcl -> mingw-tcl rename

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 8.5.9-5
- Renamed the source package to mingw-tk (#801037)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.5.9-4
- Rebuild against the mingw-w64 toolchain
- Fix the compilation with the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 19 2010 Paulo Roma <roma@lcg.ufrj.br> - 8.5.9-1
- Update to 8.5.9 to match rawhide.
- Converted changes to utf8.
- Fixed wish symbolic link.

* Tue Oct 20 2009 Paulo Roma <roma@lcg.ufrj.br> - 8.5.7-5.1
- Copy from native
