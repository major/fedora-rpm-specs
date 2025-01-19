Name:           newsbeuter
Version:        2.9
Release:        27%{?dist}
Summary:        Configurable text-based feed reader

License:        MIT
URL:            http://newsbeuter.org/
Source0:        http://newsbeuter.org/downloads/%{name}-%{version}.tar.gz

# https://github.com/akrennmair/newsbeuter/pull/157
# The included colorscheme is suboptimal.
Patch0:         %{name}-2.8-Improve-solarized-dark-colorscheme.patch
Patch1:         %{name}-2.8-Add-solarized-light-colorscheme.patch

Patch2:         %{name}-2.9-ncurses6.patch
Patch3:         %{name}-2.9_json-c_013.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  json-c-devel
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl(File::Basename)
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  stfl-devel
Requires:       stfl

%description
Newsbeuter is a feed reader for text terminals.  Newsbeuter's great
configurability and vast number of features make it a perfect choice for people
that need a slick and fast feed reader that can be completely controlled via
keyboard.


%prep
%setup -q
%patch -P0 -p1 -b .improve-solarized-dark
%patch -P1 -p1 -b .add-solarized-light
%if 0%{?fedora} > 23
%patch -P2 -p1 -b .ncurses6
%endif
%if 0%{?fedora} >= 28
%patch -P3 -p1 -b .json-c_013
%endif


%build
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
./config.sh
make %{?_smp_mflags} prefix=%{_prefix}


%install
%make_install prefix=%{_prefix}
# %%doc will be used in %%files to pull in the documentation
rm -rf %{buildroot}/%{_datadir}/doc/%{name}
# remove executable permissions on man pages
find %{buildroot}/%{_mandir} -type f -exec chmod -x '{}' ';'
# remove exectuable permissions on contrib/ scripts
find contrib/ -type f -exec chmod -x '{}' ';'
%find_lang %{name}


%files -f %{name}.lang
%doc README doc/xhtml/newsbeuter.html doc/example-config
%doc contrib/
%license LICENSE
%{_mandir}/man1/*
%{_bindir}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 2.9-18
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 2.9-15
- Rebuild (json-c)

* Mon Apr 13 2020 Björn Esser <besser82@fedoraproject.org> - 2.9-14
- Add explicit BuildRequires: perl(File::Basename)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 2.9-9
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.9-7
- Rebuilt for libjson-c.so.3

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.9-6
- Fix build by adding BR: perl-interpreter

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 23 2015 Ben Boeckel <mathstuf@gmail.com> - 2.9-1
- update to 2.9
- use %%license macro
- backup patched files
- use ncurses6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.8-7
- Rebuilt for GCC 5 C++11 ABI change

* Fri Dec 05 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.8-6
- add solarized-light colorscheme

* Thu Dec 04 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.8-5
- remove executable permissions from contrib/ scripts
- improve solarized dark colorscheme

* Thu Dec 04 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.8-4
- include contrib/ folder

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.8-1
- update to upstream release 2.8
- remove redundant patch (merged upstream)

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.7-1
- update to upstream release 2.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.6-1
- update to upstream release 2.6
- remove redundant patch

* Fri Feb 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.5-5
- apply newsbeuter-2.5-json-boolean-include.patch

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Ben Boeckel <mathstuf@gmail.com> - 2.5-1
- Update to 2.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 10 2011 Ben Boeckel <mathstuf@gmail.com> - 2.4-1
- Update to 2.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3-3
- rebuild for new libxml2

* Wed Sep 29 2010 jkeating - 2.3-2
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3-1
- newsbeuter 2.3

* Tue May 18 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.2-1
- bugfix release
- added google reader support

* Mon Jan 25 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.1-1
- New upstream source 2.1

* Wed Nov 11 2009 Thomas Janssen <thomasj@fedoraproject.org> 2.0-8
- Added BR ncurses-devel

* Fri Oct 02 2009 Thomas Janssen <thomasj@fedoraproject.org> 2.0-7
- Minor spec changes

* Sun Jun 28 2009 Byron Clark <byron@theclarkfamily.name> 2.0-6
- Correct changelog version numbers
- Generate config.mk
- Removed executable bits on manpages

* Wed Jun 10 2009 Byron Clark <byron@theclarkfamily.name> 2.0-5
- Better summary

* Sat Jun 6 2009 Byron Clark <byron@theclarkfamily.name> 2.0-4
- Use find_lang macro for translations
- Remove explicit library requires
- Use _prefix macro instead of an explicit prefix
- Install documentation with doc

* Sun May 31 2009 Byron Clark <byron@theclarkfamily.name> 2.0-3
- Add a description

* Thu May 21 2009 Byron Clark <byron@theclarkfamily.name> 2.0-2
- Fix libxml2 dependency

* Thu May 21 2009 Byron Clark <byron@theclarkfamily.name> 2.0-1
- Initial release
