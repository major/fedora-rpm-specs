Name:           PragmARC
Version:        20130728
Release:        36%{?dist}
Summary:        PragmAda Reusable Components, a component library for Ada
Summary(sv):    PragmAda Reusable Components, ett komponentbibliotek för ada

License:        GPL-2.0-or-later WITH GNAT-exception
URL:            https://pragmada.x10hosting.com/pragmarc.htm
Source1:        https://www.Rombobjörn.se/PragmARC/pragmarc-%{version}.zip
Source2:        build_pragmarc.gpr
Source3:        pragmarc.gpr

BuildRequires:  gcc-gnat fedora-gnat-project-common >= 3
BuildRequires:  gprbuild
BuildRequires:  unzip dos2unix
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
The PragmAda Reusable Components (PragmARCs) is a library of containers, \
algorithms and utility components for Ada, ranging from the basic-but-essential \
to the high-level.

%global common_description_sv \
PragmAda Reusable Components (PragmARC) är ett bibliotek med behållare, \
algoritmer och nyttiga komponenter för ada. Det innehåller såväl grundläggande \
byggstenar som högnivåkomponenter.

%description %{common_description_en}

%description -l sv %{common_description_sv}

%package devel
Summary:        Development files for %{name}
Summary(sv):    Filer för programmering med %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common >= 2

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use %{name}.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder %{name}.


%prep
%setup -c -T
unzip %{SOURCE1}
chmod --recursive u=rwX,go=rX .
cp -p %{SOURCE2} .


%build
# Delete files that won't be used.
rm compile_all.adb assertion_handler.adb
# Compile the library.
gprbuild -P build_pragmarc.gpr %{GPRbuild_optflags} -XDESTDIR=build_target
# Convert line breaks.
dos2unix --keepdate license.txt readme.txt arc_list.txt design.txt Test/*


%install
mv build_target/* --target-directory=%{buildroot}
# Add the project file for projects that use this library.
mkdir --parents %{buildroot}%{_GNAT_project_dir}
cp -p %{SOURCE3} %{buildroot}%{_GNAT_project_dir}/


%files
%license license.txt gpl.txt
%{_libdir}/*.so.*

%files devel
%doc readme.txt arc_list.txt design.txt Test
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pragmarc
%{_GNAT_project_dir}/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 20130728-35
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 20130728-31
- Rebuilt with GCC 14 prerelease.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 20130728-28
- Rebuilt with GCC 13.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Björn Persson <Bjorn@Rombobjörn.se> - 20130728-23
- Rebuilt with GCC 11.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Björn Persson <Bjorn@Rombobjörn.se> - 20130728-19
- Built for x86.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Björn Persson <Bjorn@Rombobjörn.se> - 20130728-15
- Switched to building with GPRbuild as project file support was removed from
  Gnatmake in GCC 8.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Björn Persson <Bjorn@Rombobjörn.se> - 20130728-11
- Rebuilt with GCC 7 prerelease.

* Fri Aug 12 2016 Björn Persson <Bjorn@Rombobjörn.se> - 20130728-10
- Rebuilt to let it be built on new architectures.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20130728-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Björn Persson <Bjorn@Rombobjörn.se> - 20130728-8
- Rebuilt with GCC 6 prerelease.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130728-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Björn Persson <bjorn@rombobjörn.se> - 20130728-6
- Tagged the license files as such.

* Sat Feb 07 2015 Björn Persson <bjorn@rombobjörn.se> - 20130728-5
- Rebuilt with GCC 5.0.0.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130728-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130728-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Björn Persson <bjorn@rombobjörn.se> - 20130728-2
- Rebuilt with GCC 4.9.0 prerelease.

* Sat Aug 31 2013 Björn Persson <bjorn@rombobjörn.se> - 20130728-1
- Upgraded to the version released 2013-07-28.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130311-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Björn Persson <bjorn@rombobjörn.se> - 20130311-1
- Upgraded to the version released 2013-03-11.

* Thu Jan 24 2013 Björn Persson <bjorn@rombobjörn.se> - 20060427-17
- Rebuilt with GCC 4.8.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060427-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 24 2012 Björn Persson <bjorn@rombobjörn.se> - 20060427-15
- Rebuilt with fedora-gnat-project-common-3.4.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060427-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jan 05 2012 Björn Persson <bjorn@rombobjörn.se> - 20060427-13
- Marked the library as relocatable in the Gnat project file.

* Thu Aug 04 2011 Björn Persson <bjorn@rombobjörn.se> - 20060427-12
- Added support for linker options.
- Improved the description of PragmARC-devel.

* Sun May 22 2011 Björn Persson <bjorn@rombobjörn.se> - 20060427-11.1
- Removed some obsolete stuff.

* Tue May 03 2011 Björn Persson <bjorn@rombobjörn.se> - 20060427-11
- Updated to make use of fedora-gnat-project-common 3.

* Sat Feb 19 2011 Björn Persson <bjorn@rombobjörn.se> - 20060427-10
- Switched from common.gpr to directories.gpr.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060427-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Björn Persson <bjorn@rombobjörn.se> - 20060427-8
- Rebuilt with GCC 4.6.

* Thu Jul 08 2010 Björn Persson <bjorn@rombobjörn.se> - 20060427-7
- Rebuilt with GCC 4.5.

* Tue Nov 03 2009 Björn Persson <bjorn@rombobjörn.se> - 20060427-6
- Resolved a conflict between debuginfo packages.

* Fri Oct 30 2009 Björn Persson <bjorn@rombobjörn.se> - 20060427-5
- Removed a symlink correction that isn't needed in Fedora 11 and later.

* Wed Aug 05 2009 Björn Persson <bjorn@rombobjörn.se> - 20060427-4
- Updated the URLs because the PragmAda site moved.

* Thu Jul 23 2009 Björn Persson <bjorn@rombobjörn.se> - 20060427-3
- Added a BuildRoot tag even though it's unnecessary.

* Thu Jul 02 2009 Björn Persson <bjorn@rombobjörn.se> - 20060427-2
- updated to require fedora-gnat-project-common

* Sun Jun 28 2009 Björn Persson <bjorn@rombobjörn.se> - 20060427-1
- ready to be submitted for review
