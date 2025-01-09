%global	header_dir	%{ruby_vendorarchdir}

%global	gem_name	gtksourceview2

%global	glibminver	3.0.8
%global	gtkminver	3.0.8
%global	obsoleteevr	0.90.7-1.999

%undefine        _changelog_trimtime

Summary:	Ruby binding of gtksourceview-2.x
Name:		rubygem-%{gem_name}
Version:	3.4.3
Release:	17%{?dist}
# gtksourceview2-3.4.3.gemspec	LGPL-2.1-or-later
# Other source	LGPL-2.1-or-later
# SPDX confirmed
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	gcc
BuildRequires:	rubygem-glib2-devel >= %{glibminver}
BuildRequires:	rubygem-cairo-devel
BuildRequires:	rubygem-gtk2-devel >= %{gtkminver}
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	gtksourceview2-devel
## %%check
BuildRequires:	xorg-x11-server-Xvfb
BuildRequires:	rubygem(test-unit)
Provides:	rubygem(%{gem_name}) = %{version}

Obsoletes:		ruby-%{gem_name} < %{version}-%{release}
Provides:		ruby-%{gem_name} = %{version}-%{release}
Provides:		ruby(%{gem_name}) = %{version}-%{release}

%description
Ruby/GtkSourceView2 is a Ruby binding of gtksourceview-2.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/GtkSourceView2 development environment
Requires:	%{name} = %{version}-%{release}
# Obsoletes / Provides
# ruby(%%{gem_name}-devel) Provides is for compatibility
Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}
Provides:	ruby-%{gem_name}-devel = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 3\.4\.3|>= 3.4.3|' %{gem_name}.gemspec

# Fix wrong shebang
#grep -rl /usr/local/bin sample | \
#	xargs sed -i -e 's|/usr/local/bin|/usr/bin|'

# Kill shebang
grep -rl '#!.*/usr/bin' sample | \
	xargs sed -i -e '\@#![ ]*/usr/bin@d'
find sample/ -name \*.rb | xargs chmod 0644

# Fix test/run-test.rb
sed -i \
	-e 's|test/glib-test-init|glib-test-init|' \
	-e '/gtk-test-utils/d' \
	test/run-test.rb

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
# Once copy all
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# move pkgconfig file
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/


# Cleanups
pushd %{buildroot}%{gem_instdir}
rm -rf \
	ext/ \
	extconf.rb \
	Rakefile \
	test/ \
	*.gemspec \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}

%check
pushd .%{gem_instdir}

# kill unneeded make process
rm -rf ./TMPBINDIR
mkdir ./TMPBINDIR
pushd ./TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd

sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'

export RUBYLIB=$(pwd)/lib:$(pwd)/test:%{buildroot}%{gem_extdir_mri}
xvfb-run \
	ruby ./test/run-test.rb

%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/

%license	%{gem_instdir}/COPYING.LIB
%doc	%{gem_instdir}/README.md

%{gem_instdir}/lib/%{gem_name}.rb
%{gem_extdir_mri}/

%{gem_spec}

%files	devel
%{_libdir}/pkgconfig/ruby-%{gem_name}.pc

%files	doc
%{gem_docdir}/
%{gem_instdir}/sample/

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-17
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan  8 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-13
- SPDX migration

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-12
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-9
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sun Dec 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-8
- Use %%gem_extdir_mri instead of ext for %%check due to ruby3.2 change
  for ext cleanup during build

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-6
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-2
- F-34: rebuild against ruby 3.0

* Thu Aug 13 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-1
- 3.4.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-2
- F-32: rebuild against ruby27

* Fri Dec  6 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1

* Tue Oct 15 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Sun Sep  8 2019 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-1
- 3.3.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.6-1
- 3.3.6

* Mon Feb 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.2-1
- 3.3.2

* Sat Feb  2 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.1-1
- 3.3.1

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-2
- F-30: rebuild against ruby26

* Sun Nov 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-1
- 3.3.0

* Mon Aug 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.9-1
- 3.2.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.7-1
- 3.2.7

* Thu May  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.5-1
- 3.2.5

* Fri Apr 20 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.4-1
- 3.2.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.2.1-3
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-2
- F-28: rebuild for ruby25

* Wed Nov 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Tue Nov 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Tue Oct 24 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.9-1
- 3.1.9

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.8-1
- 3.1.8

* Fri Jul 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-1
- 3.1.7

* Thu Jun  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-1
- 3.1.6

* Thu May  4 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-1
- 3.1.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-2
- F-26: rebuild for ruby24

* Tue Nov 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Mon Aug 15 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-1
- 3.0.9

* Tue Apr 19 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.8-1
- 3.0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-2
- F-24: rebuild against ruby23

* Sun Oct 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-1
- 3.0.7

* Wed Sep 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.5-1
- 3.0.5

* Tue Sep 22 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.4-1
- 3.0.4

* Mon Sep 21 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.3-1
- 3.0.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.5-1
- 2.2.5

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-2
- F-22: Rebuild for ruby 2.2

* Sun Dec 28 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-1
- 2.2.4

* Wed Nov  5 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-1
- 2.2.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-2
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Mon Apr 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Sun Jan 19 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-2
- Fix GtkSource#get_mark_category_background return value

* Thu Jan 16 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-1
- 2.1.0

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-1
- 2.0.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-1
- 1.2.6

* Thu Apr  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-1
- 1.2.5

* Tue Mar 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-1
- 1.2.4

* Wed Mar 20 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-1
- 1.2.3

* Thu Mar  7 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-2
- F-19: Rebuild for ruby 2.0.0

* Mon Feb  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-1
- 1.2.1

* Wed Jan 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-1
- 1.2.0

* Mon Dec 31 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.9-1
- 1.1.9

* Thu Dec  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.6-1
- 1.1.6

* Wed Sep  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.5-1
- 1.1.5

* Mon Aug 13 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.4-1
- 1.1.4

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.3-1
- 1.1.3

* Wed Feb  1 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.2-2
- 1.1.2

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Fri Jul 15 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.0-1
- 1.0.0

* Sun Jun 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.9-1
- 0.90.9

* Tue Mar 22 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.8-2
- Some cleanups

* Thu Mar 10 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.8-1
- 0.90.8

* Sat Feb 19 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.7-2
- Initial package
