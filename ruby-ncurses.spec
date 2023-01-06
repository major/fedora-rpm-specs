%define realname ncurses-ruby
%define distname ruby-ncurses

Name: %distname
Version: 1.3.1
Release: 42%{?dist}
Summary: A module for ruby applications for using ncurses interfaces
License: LGPLv2+
URL: http://ncurses-ruby.berlios.de/
Source0: http://download.berlios.de/ncurses-ruby/%{realname}-%{version}.tar.bz2
Patch0: 0001-STR2CSTR-deprecated.patch
Patch1: 0002-Werror-format-security.patch
# Fixes "ncurses_wrap.c:827:12: error: variable 'tz' has initializer but incomplete type"
# https://github.com/eclubb/ncurses-ruby/commit/0f7decd5e5a205444c9d31f19b0599a7e42b0fd8
Patch2: ruby-ncurses-fix-missing-tz-prototypes.patch
# rb_thread_select was removed from Ruby 2.2.
# https://bugs.ruby-lang.org/issues/9502#change-45212
# https://github.com/sup-heliotrope/ncursesw-ruby/commit/809e549408bfdf7cab4b98a73f6e78dd3ad81d86
Patch3: ruby-ncurses-1.3.1-use-new-rb_thread_fd_select-avoiding-deprecated-functions.patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: ncurses-devel
Requires: ruby(release)
Requires: ruby
Provides: ruby(ncurses) = %{version}-%{release}

%description
This ruby extension makes most functions, constants, and external variables 
of the C library ncurses accessible from the Ruby programming language.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1 -b .p
%patch1 -p1 -b .format
%patch2 -p1 -b .systime
%patch3 -p1 -b .ruby22
%{__chmod} 0644 ncurses_wrap.c
find examples/ -type f | xargs %{__chmod} 0644

%build
ruby extconf.rb --vendor
%{__make} %{_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT ruby_headers= INSTALL="%{__install} -p"

%check

%files
%doc README COPYING VERSION THANKS Changes
%doc examples
%{ruby_vendorarchdir}/ncurses_bin.so
%{ruby_vendorlibdir}/ncurses.rb
%{ruby_vendorlibdir}/ncurses_sugar.rb

%changelog
* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-42
- Remove undefined rubyabi requirement

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-41
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-39
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-35
- F-34: rebuild against ruby 3.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-31
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-28
- F-30: rebuild against ruby26

* Fri Jan 04 2019 Björn Esser <besser82@fedoraproject.org> - 1.3.1-27
- Add BuildRequires: gcc, fixes FTBFS (#1606149)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.3.1-24
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-23
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-19
- F-26: rebuild for ruby24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Vít Ondruch <vondruch@redhat.com> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Wed Sep 02 2015 Vít Ondruch <vondruch@redhat.com> - 1.3.1-16
- Fix Ruby 2.2 compatibility.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-14
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Vít Ondruch <vondruch@redhat.com> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Mon Feb 03 2014 Šimon Lukašík <slukasik@redhat.com> - 1.3.1-10
- FTBFS if "-Werror=format-security" flag is used (#1037313)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Simon Lukasik <slukasik@redhat.com> - 1.3.1-8
- Workaround ruby 2.0 build bug 921650.

* Thu Mar 14 2013 Simon Lukasik <slukasik@redhat.com> - 1.3.1-7
- Avoid using deprecated macro STR2CSTR (#822814)

* Thu Mar 14 2013 Simon Lukasik <slukasik@redhat.com> - 1.3.1-6
- Fix build requires for Ruby 2.0 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Simon Lukasik <slukasik@redhat.com> - 1.3.1-1
- Update to a new upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun  4 2010 Simon Lukasik <slukasik@redhat.com> - 1.2.4-1
- Update to new upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1-7
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1-6
- Autorebuild for GCC 4.3

*  Sat May 19 2007 Simon Lukasik <lukasim@atlas.cz> - 1.1-5
- Rewrite: rest of commands to macros 

*  Mon May 14 2007 Simon Lukasik <lukasim@atlas.cz> - 1.1-4
- Rewrite: "install -s" to "install"

*  Sun May 13 2007 Simon Lukasik <lukasim@atlas.cz> - 1.1-3
- Rewrite: licence, make parameters, chmod in prep section, 
  added: THANKS and examples/ to doc

*  Sun May 13 2007 Simon Lukasik <lukasim@atlas.cz> - 1.1-2
- Rewrite: General section(provides, (build)requires), 
  install, clean and files (added ruby_site* macros)

*  Sun May 13 2007 Simon Lukasik <lukasim@atlas.cz> - 1.1-1
- Initial package.
    
