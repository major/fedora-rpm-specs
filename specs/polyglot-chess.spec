%global _vpath_srcdir src
%undefine __cmake_in_source_build

%global srcname     polyglot
%global commitdate  20140902
%global commit0     f46ee068860d363ace27004ec4da588bf4b48147

Name:           %{srcname}-chess
Version:        1.4
Release:        28.%{commitdate}git%(c=%{commit0}; echo ${c:0:7})%{?dist}
Summary:        Polyglot chess opening book program

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/sshivaji/%{srcname}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{srcname}-%{commit0}.tar.gz

# cmake https://github.com/sshivaji/polyglot/issues/2
Source1:        %{srcname}-CMakeLists.txt
# community provides some nice addons
Source2:        https://launchpadlibrarian.net/4993987/%{srcname}_1.4-2.diff.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(leveldb)


%description
PolyGlot is a "UCI adapter". It connects a UCI chess engine to an
xboard interface such as WinBoard. UCI2WB is another such adapter
(for Windows).
PolyGlot tries to solve known problems with other adapters. For
instance, it detects and reports draws by fifty-move rule, repetition,
etc ...

New Features: Builds a polyglot book but supports a leveldb position/game
index as well. The leveldb option can be enabled with -leveldb 
 

%prep
%setup -qn%{srcname}-%{commit0}
zcat %{SOURCE2} |patch -p1
# use proper Fedora flags
rm src/Makefile
cp %{SOURCE1} src/CMakeLists.txt
# W: wrong-file-end-of-line-encoding
sed -i 's,\r$,,' readme.txt debian/example-files/*
# rename binary
sed 's,%{srcname},%{name},' debian/%{srcname}.6 >%{name}.6
sed -i 's,%{srcname},%{name},' src/CMakeLists.txt


%build
%cmake
%cmake_build


%install
# W: unstripped-binary-or-object
install -p -m0755 %{_vpath_builddir}/%{name} -D %{buildroot}%{_bindir}/%{name}
# W: spurious-executable-perm
install -p -m0644 %{name}.6 -D %{buildroot}%{_mandir}/man6/%{name}.6


%files
%license LICENSE
%doc readme.txt README.md
%doc debian/*.Debian debian/example-files/
%{_mandir}/man*/%{name}*
%{_bindir}/%{name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-28.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4-27.20140902gitf46ee06
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-26.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-18.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17.20140902gitf46ee06
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.4-7.20140902gitf46ee06
- Rebuild for LevelDB 1.18

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6.20140902gitf46ee06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Raphael Groner <projects.rg@smart.ms> - 1.4-5.20140902gitf46ee06
- fix rpmlint warnings

* Mon Nov 09 2015 Raphael Groner <projects.rg@smart.ms> - 1.4-4.20140902gitf46ee06
- use install command and avoid extra mkdir
- move example files to documentation

* Sun Oct 25 2015 Raphael Groner <projects.rg@smart.ms> - 1.4-3.20140902gitf46ee06
- use simply pkgconfig to find leveldb
- add debian documentation files
- rename globals

* Sun Mar 01 2015 Raphael Groner <projects.rg@smart.ms> - 1.4-2.20140902gitf46ee06
- implement cmake
- distribute manpage and openbook from ubuntu

* Sat Feb 28 2015 Raphael Groner <projects.rg (AT) smart.ms> - 1.4-1.20140902gitf46ee06
- initial
