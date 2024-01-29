%undefine _hardened_build

Name:           templates_parser
Version:        11.8.0
Release:        37%{?dist}
Summary:        AWS templates engine

# GNAT Modified GPL (GMGPL)
License:        GPLv2+ with exceptions
URL:            http://docs.adacore.com/aws-docs/templates_parser/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone https://forge.open-do.org/anonscm/git/template-parser/template-parser.git -b release-11.8 templates_parser-11.8.0
#  tar --exclude-vcs -cJf templates_parser-11.8.0.tar.xz templates_parser-11.8.0
Source0:        %{name}-%{version}.tar.xz
# manpages from Debian package
Source1:        templates2ada.1
Source2:        templatespp.1
# remove static library
Patch1:         %{name}-makefile.patch
# adjust GPRs to Fedora standard
Patch2:         %{name}-gpr.patch

# All Ada packages have to contain these
BuildRequires: make
BuildRequires:  gcc-gnat fedora-gnat-project-common gprbuild
# gprbuild only available on these:
ExclusiveArch: %GPRbuild_arches

BuildRequires:  xmlada-devel
BuildRequires:  chrpath

%description
The templates parser package has been designed to parse files and to
replace some specific tags into these files by some specified values.


%package devel
Summary:        Development files for AWS templates engine
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common >= 2
BuildRequires:  texinfo-tex texlive-harmony


%description devel
The templates parser package has been designed to parse files and to
replace some specific tags into these files by some specified values.

This package contains the development files necessary to build and link
from other project files.


%package tools
Summary:        Tools for AWS templates engine


%description tools
This package contains the tools templates2ada and templatespp from the
AWS templates engine templates_parser.


%prep
%setup -q
%patch1
%patch2


%build
export GNATMAKE_OPTFLAGS="%{Gnatmake_optflags}"
make %{?_smp_mflags} VERSION=%{version}
# doc build wants to link to library
## FIXME debug and enable back
## LD_LIBRARY_PATH="`pwd`/.build/native/release/relocatable/lib/" make doc


%install
make install prefix=/usr \
  I_LIB=%{_libdir} \
  I_GPR=%{_GNAT_project_dir} \
  I_TGP=%{_GNAT_project_dir}/%{name} \
  DESTDIR=$RPM_BUILD_ROOT
ln -sf %{name}/lib%{name}-%{version}.so $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
ln -sf %{name}/lib%{name}-%{version}.so $RPM_BUILD_ROOT%{_libdir}
# delete rpath manually (#674793)
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/%{name}/lib%{name}-%{version}.so
# install manpages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %SOURCE1 $RPM_BUILD_ROOT%{_mandir}/man1/
cp -p %SOURCE2 $RPM_BUILD_ROOT%{_mandir}/man1/


%files
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}-%{version}.so
%{_libdir}/lib%{name}-%{version}.so


%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}.so
%{_libdir}/%{name}/lib%{name}.so
%{_GNAT_project_dir}/%{name}.gpr
%{_GNAT_project_dir}/%{name}
%{_docdir}/%{name}


%files tools
%doc tools/templates.tads tools/all_urls.thtml
%{_bindir}/templates2ada
%{_bindir}/templatespp
%{_mandir}/man1/*


%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-36
- Rebuilt with GCC 14 prerelease.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-34
- Rebuilt with XMLada 23.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-32
- Rebuilt with GCC 13.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.8.0-30
- Rebuild for new gnat

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-27
- rebuilt with gcc-11.0.1-0.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Pavel Zhukov <pzhukov@redhat.com> - 11.8.0-25
- rebuild with new gnat

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org - 11.8.0-18
- rebuilt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Pavel Zhukov <pzhukov@redhat.com> - 11.8.0-15
- Build on GPRbuild_arches only

* Mon Jul 10 2017 Pavel Zhukov <pzhukov@redhat.com> - 11.8.0-14
- Rebuild with new gnat

* Mon Feb 13 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 11.8.0-13
- Disable doc build as a workaround

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-11
- Rebuilt to let it be built on new architectures.

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-10
- Rebuilt with GCC 6 prerelease.

* Thu Jun 25 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 11.8.0-9
- Rebuild with new xmlada
- Build on arm

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 11.8.0-6
- Don't build ADA hardened

* Sun Feb 15 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 11.8.0-5
- Rebuild with gnat-5.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 julian@vgai.de - 11.8.0-3
- add temporary fix for gprbuild using wrong target

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Julian Leyh <julian@vgai.de> - 11.8.0-1
- Update to 11.8.0 and rebuild for gcc

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Tomáš Mráz <tmraz@redhat.com> - 11.6.0-6
- Rebuild (#918586)

* Sat Jan 26 2013 Kevin Fenzi <kevin@scrye.com> - 11.6.0-5
- Rebuild for new gnat

* Mon Aug 06 2012 Julian Leyh <julian@vgai.de> - 11.6.0-3
- add manpages for the tools

* Fri Jun 29 2012 Julian Leyh <julian@vgai.de> - 11.6.0-2
- build documentation
- use other URL
- smaller source tarball with --exclude-vcs
- correct soname
- adjust path to gpr files
- add tools subpackage
- add ldconfig call

* Wed Jun 27 2012 Julian Leyh <julian@vgai.de> - 11.6.0-1
- Initial Package

