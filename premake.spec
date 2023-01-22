Name:           premake
Version:        4.3
Release:        27%{?dist}
Summary:        Cross-platform build configuration tool

License:        BSD
URL:            http://industriousone.com/premake
Source0:        http://downloads.sourceforge.net/%{name}/premake-%{version}-src.zip
# This patch removes the bundeled Lua sources from the makefile to use the system Lua
Patch0:         premake-4.3-system-lua.patch
# Add the missing manpage
Patch1:         premake-4.3-manpage.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  compat-lua-devel readline-devel

%description
Premake is a build configuration tool that can generate project files for:
 - GNU make
 - Code::Blocks
 - CodeLite
 - MonoDevelop
 - SharpDevelop
 - Apple XCode 
 - Microsoft Visual Studio 

%prep
%setup -q
%patch0 -p0
%patch1 -p0
# Inject optflags into CFLAGS
sed -i "s|^\s*CFLAGS\s*+=.*|CFLAGS += \$(CPPFLAGS) %{optflags}|" build/gmake.unix/Premake4.make
# Disable stripping the executable
sed -i "s|^\s*LDFLAGS\s*+= -s|LDFLAGS +=|" build/gmake.unix/Premake4.make
# Use the release build for running tests
sed -i "s/debug/release/" tests/test

%build
cd build/gmake.unix/
make verbose=true %{?_smp_mflags}

%install
install -m 755 -Dp ./bin/release/premake4 %{buildroot}/%{_bindir}/premake4
install -m 644 -Dp ./premake4.1 %{buildroot}/%{_mandir}/man1/premake4.1

%files
%{_bindir}/premake4
%{_mandir}/man1/premake4.1*
%doc README.txt CHANGES.txt
%license LICENSE.txt



%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.3-12
- Use '|' instead of '/' as pattern delimiter in sed expression to filter
  CFLAGS (Fix FTBFS).
- Modernize spec.
- Add %%license.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 4.3-9
- Fix FTBFS with lua-5.2 (#1106672)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 28 2010 Joachim de Groot <jdegroot@web.de> - 4.3-2
- Let rpm handle the man page compression

* Sat Nov 27 2010 Joachim de Groot <jdegroot@web.de> - 4.3-1
- Update to 4.3, thus changed license to BSD
- Added missing version numbers to changelog
- Added readline-devel to BuildRequires
- Added a man page

* Fri Oct 29 2010 Joachim de Groot <jdegroot@web.de> - 4.2.1-3
- Correct building of the debuginfo package

* Fri Oct 29 2010 Joachim de Groot <jdegroot@web.de> - 4.2.1-2
- Implemented changes proposed by Mohamed El Morabity

* Thu Oct 28 2010 Joachim de Groot <jdegroot@web.de> - 4.2.1-1
- Initial version of the package

