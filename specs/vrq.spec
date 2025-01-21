Name:           vrq
Version:        1.0.134
Release:        13%{?dist}
Summary:        Verilog tool framework with plugins for manipulating source code

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://vrq.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         vrq-gcc11.patch

# ---- Exclusive Arch: ----
# plugin/sim uses x86 inline assembly

ExclusiveArch:  %{ix86} x86_64

BuildRequires: make
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  iverilog
BuildRequires:  libtool-ltdl-devel
BuildRequires:  man2html-core
BuildRequires:  perl-Time-HiRes
BuildRequires:  readline-devel
BuildRequires:  zlib-devel


%description
VRQ is modular verilog parser that supports plugin tools to process verilog. 
Multiple tools may be invoked in a pipeline fashion within a single execution 
of vrq. It is a generic front-end parser with support for plugin backend 
customizable tools.

%package devel
Summary:        Header files and libraries for Vrq development
Requires:       %{name} = %{version}-%{release}

%description devel
The vrq-devel package contains the header files and libraries needed
to develop backend plugin customization tools for the vrq tool framework.

%prep
%autosetup -p1
%{__rm} -rf `find . -name CVS`
%{__rm} -f `find . -name *.o`
%{__rm} -f `find . -name *.so`

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure
%make_build

%install
%make_install
%{__rm} -f `find %{buildroot} -name *.la`
%{__rm} -rf `find %{buildroot} -name latex`

# add some doc files into the buildroot manually (#992864)
for f in AUTHORS ChangeLog COPYING README doc/faq.html ; do
    install -p -m0644 -D $f %{buildroot}%{_docdir}/%{name}/${f}
done

install -d -m0755 %{buildroot}%{_docdir}/%{name}/doc
cp -pr doc/html %{buildroot}%{_docdir}/%{name}/doc

install -d -m0755 %{buildroot}%{_docdir}/%{name}/plugin
cp -pr plugin/examples %{buildroot}%{_docdir}/%{name}/plugin

rm -rf %{buildroot}%{_docdir}/%{name}-%{version}


%files
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/doc
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/README
%{_docdir}/%{name}/doc/faq.html
%{_bindir}/%{name}
%{_libdir}/%{name}-%{version}
%{_mandir}/man1/vrq.1.gz

%files devel
%{_docdir}/%{name}/doc/html
%{_docdir}/%{name}/plugin/examples
%{_includedir}/%{name}-%{version}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.134-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Jeff Law <law@redhat.com> - 1.0.134-3
- Make comparison object invocable as const
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.134-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 11 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.134-1
- Update to 1.0.134 fixes rhbz#1747827

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.133-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.133-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.133-1
- New upstream version 1.0.133, fixes rhbz#1708828

* Sun Apr 14 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.132-1
- New upstream version 1.0.132, fixes rhbz#1699446

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.130-6
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.130-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.130-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.130-3
- added gcc as BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.130-1
- Rebuilt for new upstream version 1.0.130, fixes RHBZ#1534804

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.129-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.129-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.129-1
- Rebuilt for new upstream version 1.0.129, fixes RHBZ#1414405

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.128-2
- Rebuild for readline 7.x

* Sun Nov 27 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.128-1
- Rebuilt for new upstream version 1.0.128, fixes rhbz #1397618

* Sat Nov 12 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.127-1
- Rebuilt for new upstream version 1.0.127, fixes rhbz #1394480

* Wed Nov 02 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.126-1
- Rebuilt for new upstream version 1.0.126, fixes rhbz #1387643

* Tue Sep 13 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.125-1
- Rebuilt for new upstream version 1.0.125, fixes rhbz #1299291 #1308232

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.119-1
- Rebuilt for new upstream version 1.0.119, fixes rhbz #1299291

* Sun Dec 06 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.116-2
- Rebuilt for new upstream version 1.0.116
- Attempt to fix mess made by iverilog changes

* Tue Nov 17 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.115-1
- Rebuilt for new upstream version 1.0.115, fixes rhbz #1279918

* Mon Nov 16 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.114-1
- Rebuilt for new upstream version 1.0.114, fixes rhbz #1279918
- Fix BR using iverilog instead deprecated iverilog-devel

* Thu Oct 08 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.113-1
- Rebuilt for new upstream version 1.0.113, fixes rhbz #1269316

* Sat Sep 19 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.111-1
- Rebuilt for new upstream version 1.0.111, fixes rhbz #1250759
- Added libtool-ltdl-devel as BR

* Mon Aug 31 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.110-2
- Rebuilt for new upstream version 1.0.110, fixes rhbz #1250759
- Added perl-Time-HiRes as BR

* Sun Jul 12 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.107-1
- Rebuilt for new upstream version 1.0.107, fixes rhbz #1231592

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.104-1
- Rebuilt for new upstream version 1.0.104

* Mon Mar 23 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.103-1
- Rebuilt for new upstream version 1.0.103, fixes rhbz #1204477

* Sat Nov 08 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.102-1
- Rebuilt for new upstream version 1.0.102, fixes rhbz #1160317

* Mon Aug 25 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.101-1
- Rebuilt for new upstream version 1.0.101, fixes rhbz #1133282

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.100-1
- Updated to upstream version 1.0.100

* Wed Dec 18 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.0.97-1
- Updated to 1.0.97

* Mon Oct 14 2013 Shakthi Kannan <shakthimaan@fedoraproject.org> - 1.0.96-5
- Fix bz #992864

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.0.96-3
- Build with system zlib and bzip2 instead of bundled copies.
- Fix bogus dates in %%changelog.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.0.96-1
- Updated to 1.0.96

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.88-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 31 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.0.88-1
- Updated to upstream package 1.0.88.

* Sun Apr 24 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.0.83-1
- Updated to upstream package 1.0.83.
- Removed make check.

* Wed Dec 08 2010 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.0.82-1
- Updated to upstream package 1.0.82

* Tue Oct 12 2010 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.0.81-1
- Updated to upstream package 1.0.81
- Added BuildRequires gcc-c++

* Sat Sep 11 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.80-1
- Updated to upstream package 1.0.80

* Tue Sep 07 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.79-1
- Updated to upstream package 1.0.79

* Sat Sep 04 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.78-1
- Updated to upstream package 1.0.78

* Thu Jul 22 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.77-1
- Updated to upstream package 1.0.77

* Sat Jun 12 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.76-1
- Updated to upstream package 1.0.76

* Mon May 17 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.75-1
- Updated to upstream package 1.0.75

* Mon Apr 05 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.74-1
- Updated to upstream package 1.0.74

* Sat Mar 27 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.72-1
- Added readline-devel to BuildRequires
- Updated to upstream package 1.0.72

* Fri Dec 04 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.67-1
- Updated to upstream package 1.0.67

* Mon Nov 09 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.65-1
- Updated to upstream package 1.0.65

* Sun Oct 25 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.63-1
- Updated to upstream package 1.0.63

* Thu Oct 15 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.62-1
- Updated to upstream package 1.0.62

* Sat Oct 10 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.61-1
- Updated to upstream package 1.0.61

* Sun Sep 13 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.58-3
- Removed ldconfig for post and postun as shared library not in /usr/lib

* Sat Sep 12 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.58-2
- Removed ldconfig for post and postun in -devel package as it does not
  contain any shared libraries

* Thu Sep 10 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.58-1
- Added comment for using ExclusiveArch
- Removed perl from BR
- Simplified make install command and used -p to preserve timestamps for
  install files
- Updated MYDOCDIR in prep section 
- The main package doc contains AUTHORS ChangeLog COPYING README faq.html
- The devel package doc contains doc/html and example* folders
- Cleanup .so and .o files in example* folders

* Tue Sep 08 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.56-2
- Added Requires for -devel section as it is a MUST requirement.
- Added post, postun for -devel package as well.
- Cleaned up .la files in the shipped package.
- Replaced rm with __rm usage.

* Sun Sep 06 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.0.56-1
- Initial Package
