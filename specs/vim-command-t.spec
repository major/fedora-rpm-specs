%global commandt_so_dir %{ruby_vendorarchdir}/command-t

Name: vim-command-t
Version: 5.0.5
Release: 2%{?dist}
Summary: An extremely fast, intuitive mechanism for opening files in VIM
License: BSD-2-Clause
URL: https://github.com/wincent/command-t
Source0: https://github.com/wincent/command-t/archive/%{version}/command-t-%{version}.tar.gz
# Relax the Command-T version checking.
# https://github.com/wincent/command-t/issues/192
Patch0: vim-3.0.2-Check-RUBY_LIB_VERSION-instead-of-RUBY_VERSION.patch
# Use SPDX identifier in the AppStream data.
# https://github.com/wincent/command-t/pull/427
Patch1: vim-command-t-5.0.5-Use-SPDX-identifier-in-AppStream-metadata.patch
# https://github.com/wincent/command-t/commit/5147a93a4b6cdb60cfa0ed1b792de711f44cd7b4
# Ruby3.2 finally removes Fixnum
Patch3: vim-command-t-5.0.3-ruby32-Fixnum-removal.patch
Requires: ruby(release)
# Although command-t does not depend on rubygems directly, the RubyGems are
# required by Ruby, but not always (rhbz#845011). So it is necessary to enforce
# the RubyGems dependency, to fix possile SEGFAULT (rhbz#858135). There is
# unfortunately nothing better to do about it, as long as RPM/YUM does not
# support some conditional requires.
Requires: ruby(rubygems)
Requires: vim-common
BuildRequires: make
BuildRequires: ruby(release)
BuildRequires: ruby-devel
BuildRequires: rubygems
BuildRequires: rubygem(rspec) >= 3
BuildRequires: gcc
# Defines %%vimfiles_root
BuildRequires: vim-filesystem
BuildRequires: %{_bindir}/appstream-util

%description
The Command-T plug-in for VIM provides an extremely fast, intuitive mechanism
for opening files with a minimal number of keystrokes. It's named "Command-T"
because it is inspired by the "Go to File" window bound to Command-T
in TextMate.

Files are selected by typing characters that appear in their paths, and are
ordered by an algorithm which knows that characters that appear in certain
locations (for example, immediately after a path separator) should be given
more weight.

%prep
%setup -q -n command-t-%{version}

%patch 0 -p1
%patch 1 -p1
%patch 3 -p1

%build
pushd ./ruby/command-t/ext/command-t

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
ruby extconf.rb --vendor
make %{?_smp_mflags}

popd


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -par {autoload,doc,plugin,ruby} %{buildroot}%{vimfiles_root}

mkdir -p %{buildroot}%{commandt_so_dir}
chmod 0755 %{buildroot}%{vimfiles_root}/ruby/command-t/ext/command-t/ext.so
mv %{buildroot}%{vimfiles_root}/ruby/command-t/ext/command-t/ext.so %{buildroot}%{commandt_so_dir}

# Remove all dot files.
find %{buildroot}%{vimfiles_root} -name '.*' -delete

# Install AppData.
mkdir -p %{buildroot}%{_metainfodir}
install -m 644 appstream/vim-command-t.metainfo.xml %{buildroot}%{_metainfodir}

# GVim ID in Fedora was changed by:
# https://src.fedoraproject.org/rpms/vim/pull-request/25
# therefore extend also the new ID.
# TODO: Submit this upstream if it proves to work.
sed -i '/<\/extends>/a <extends>org.vim.Vim</extends>' %{buildroot}%{_metainfodir}/vim-command-t.metainfo.xml

%check
# Get rid of Bundler
sed -i '/Bundler/,/^end$/ s/^/#/' spec/spec_helper.rb

rspec -Iruby spec

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE
%doc README.md
%{commandt_so_dir}
%{vimfiles_root}/autoload/*
%{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/ext*
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/*.o
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/*.h
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/*.c
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/Makefile
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/mkmf.log
%exclude %{vimfiles_root}/ruby/command-t/ext/command-t/depend
%{vimfiles_root}/ruby
%{_metainfodir}/vim-command-t.metainfo.xml


%changelog
* Tue Jan 07 2025 Vít Ondruch <vondruch@redhat.com> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Tue Oct 01 2024 Vít Ondruch <vondruch@redhat.com> - 5.0.5-1
- Update to Command-T 5.0.5.
  Resolves: rhbz#2091276

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0.3-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.3-10
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Vít Ondruch <vondruch@redhat.com> - 5.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Wed Nov 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.3-6
- Patch from upstream for ruby3.2 Fixnum removal

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.3-4
- F-36: rebuild against ruby31

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 04 2021 Vít Ondruch <vondruch@redhat.com> - 5.0.3-1
- Update to Command-T 5.0.3.
  Resolves: rhbz#1631111

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.2-12
- F-34: rebuild against ruby 3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Vít Ondruch <vondruch@redhat.com> - 5.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.2-6
- F-30: rebuild against ruby26

* Fri Jul 27 2018 Vít Ondruch <vondruch@redhat.com> - 5.0.2-5
- Add "BR: gcc" to fix FTBFS (rhbz#1606647).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 5.0.2-3
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.2-2
- F-28: rebuild for ruby25

* Tue Sep 26 2017 Vít Ondruch <vondruch@redhat.com> - 5.0.2-1
- Update to Command-T 5.0.2.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0-2
- F-26: rebuild for ruby24

* Tue Jun 07 2016 Vít Ondruch <vondruch@redhat.com> - 4.0-1
- Update to Command-T 4.0.

* Tue May 03 2016 Vít Ondruch <vondruch@redhat.com> - 3.0.2-1
- Update to Command-T 3.0.2.
- Relax version check.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Vít Ondruch <vondruch@redhat.com> - 2.0-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3
- Update to Command-T 2.0.

* Wed Sep 30 2015 Vít Ondruch <vondruch@redhat.com> - 1.13-1
- Update to Command-T 1.13.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10-6
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Fix for rspec 3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Vít Ondruch <vondruch@redhat.com> - 1.10-3
- Fix BE arch issues.

* Mon Aug 11 2014 Vít Ondruch <vondruch@redhat.com> - 1.10-2
- Add missing autoload directory.

* Mon Aug 11 2014 Vít Ondruch <vondruch@redhat.com> - 1.10-1
- Update to Command-T 1.10.
- Add Gnome Software plug-in AppData (rhbz#1110300).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Vít Ondruch <vondruch@redhat.com> - 1.8-1
- Update to Command-T 1.8.

* Thu Dec 19 2013 Vít Ondruch <vondruch@redhat.com> - 1.6-1
- Update to command-t 1.6.

* Mon Sep 23 2013 Vít Ondruch <vondruch@redhat.com> - 1.5-1
- Update to command-t 1.5.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Vít Ondruch <vondruch@redhat.com> - 1.4-4
- Add dependency on RubyGems to fix possible SEGFAULT (rhbz#858135).

* Wed Feb 27 2013 Vít Ondruch <vondruch@redhat.com> - 1.4-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 Vít Ondruch <vondruch@redhat.com> - 1.4-1
- Initial package.
