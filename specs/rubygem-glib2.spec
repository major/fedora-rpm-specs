%global	header_dir	%{ruby_vendorarchdir}

%global	gem_name	glib2

%global	obsoleteevr	0.90.7-1.999

%undefine        _changelog_trimtime

Summary:	Ruby binding of GLib-2.x
Name:		rubygem-%{gem_name}
Version:	4.2.5
Release:	2%{?dist}
# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# F-19 %%_bindir/ruby wrapper pollutes environ, which makes
# g_spawn_async() test failure
Patch100:	rubygem-glib2-3.5.1-rubywrapper-pollutes-env.patch

Requires:	ruby(release)
# Explicitly require mri for g_spawn_async() test
BuildRequires:	gcc

BuildRequires:	%{_bindir}/ruby-mri
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(pkg-config)
BuildRequires:	rubygem(native-package-installer)
BuildRequires:	ruby-devel
BuildRequires:	glib2-devel
# For patch
#BuildRequires:	rubygem(rake-compiler)
## %%check
BuildRequires:	rubygem(test-unit)
Requires:	rubygems
# Ruby-GetText-Package support in glib2.rb
# Seems no longer needed
#Requires:	rubygem(gettext)
# If someone uses gnome2-win32-binary-downloader.rb, please explicitly
# require the following by yourself
#Requires:	rubygem(mechanize)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description
Ruby/GLib2 is a Ruby binding of GLib-2.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/GLib development environment
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel
Requires:	ruby-devel
# mkmf-gnome2.rb
Requires:	rubygem(pkg-config)
Requires:	rubygem(native-package-installer)
# gnome2-raketask.rb
Requires:	rubygem(rake-compiler)
# Not needed
#Requires:	rubygem(cairo)
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

# Patches and etc
%patch -P100 -p1

# Make pkg-config devel dependency (not runtime)
sed -i \
	-e '\@pkg-config@s|add_\(runtime_\)*dependency|add_development_dependency|' \
	-e '\@native-package-installer@s|add_\(runtime_\)*dependency|add_development_dependency|' \
	%{gem_name}.gemspec \
	Rakefile

sed -i \
	-e '2a require "rubygems"\ngem "test-unit"\n' \
	test/run-test.rb

# shebang issue
find sample/ test/ -name \*.rb | xargs chmod 0644
grep -rl '#![ ]*/usr' sample/ test/ | \
	xargs chmod 0755

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install

# Move C extension library to some private directory
pushd .%{gem_instdir}

# create glib-test-init.rb
cat > lib/glib-test-init.rb <<EOF
\$VERBOSE = true
begin
	require 'rubygems'
	gem 'test-unit'
rescue LoadError
end
require 'test/unit'
EOF

%install
# Once copy all
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
mkdir -p .%{header_dir}
mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# move pkgconfig file
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/


# Cleanups
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
pushd .%{gem_instdir}/

rm -f \
	Rakefile \
	extconf.rb \
	*gemspec \
	version.rb \
	test/test-*.rb \
	%{nil}
# Move the directory
chmod 0644 test/*rb
mv test/ lib/glib2/

popd
popd

%check
pushd .%{gem_instdir}

# Kill unneeded make process
mkdir -p TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd

ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb

popd

%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/

%doc	%{gem_instdir}/[A-Z]*

%{gem_instdir}/lib/glib2.rb
%{gem_instdir}/lib/glib-mkenums.rb
%dir %{gem_instdir}/lib/glib2
%{gem_instdir}/lib/glib2/date-time.rb
%{gem_instdir}/lib/glib2/deprecatable.rb
%{gem_instdir}/lib/glib2/deprecated.rb
%{gem_instdir}/lib/glib2/regex.rb
%{gem_instdir}/lib/glib2/time-zone.rb
%{gem_instdir}/lib/glib2/variant.rb
%{gem_instdir}/lib/glib2/version.rb

%{gem_extdir_mri}/
%{gem_spec}

%files	devel
# Using pkg-config and mkmf, let's move mkmf-gnome2.rb into -devel
# gnome2-raketask.rb uses rake-compiler, so also put this into -devel
# Also install gliglib-test-init.rb
%{gem_instdir}/lib/glib-test-init.rb
%{gem_instdir}/lib/gnome2-raketask.rb
%{gem_instdir}/lib/mkmf-gnome*.rb
%dir	%{gem_instdir}/lib/gnome*/
%dir	%{gem_instdir}/lib/gnome*/rake/
%{gem_instdir}/lib/gnome*/rake/*.rb

# Needs these for test suite for other package
%{gem_instdir}/lib/glib2/test/

%{header_dir}/rbgcompat.h
%{header_dir}/rbglib.h
%{header_dir}/rbglibdeprecated.h
%{header_dir}/rbglib2conversions.h
%{header_dir}/rbgobject.h
%{header_dir}/rbgutil.h
%{header_dir}/rbgutil_list.h
%{header_dir}/rbgutildeprecated.h
%{header_dir}/glib-enum-types.h
%{_libdir}/pkgconfig/ruby-%{gem_name}.pc

%files	doc
%{gem_docdir}/
%{gem_instdir}/sample/


%changelog
* Tue Jan 07 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.5-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Sun Dec 15 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.5-1
- 4.2.5

* Wed Sep 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.4-1
- 4.2.4

* Thu Sep 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.3-1
- 4.2.3

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 02 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.2-1
- 4.2.2

* Fri Feb 23 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.1-1
- 4.2.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.0-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sat Aug 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.0-1
- 4.2.0

* Sat Aug 12 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.9-1
- 4.1.9

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.8-1
- 4.1.8

* Thu Jun  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.7-1
- 4.1.7

* Mon May 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.6-1
- 4.1.6

* Thu May 11 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.5-1
- 4.1.5

* Thu May 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.4-1
- 4.1.4

* Mon May 01 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.3-1
- 4.1.3

* Fri Feb 24 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.2-1
- 4.1.2

* Sun Feb 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.1-1
- 4.1.1
- Backport upstream fix for support for GLib 2.75 wrt G_TYPE_BOOKMARK_FILE
  header exposure

* Fri Feb  3 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.0-1
- 4.1.0

* Sun Jan 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.8-1
- 4.0.8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan  6 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.5-1
- 4.0.5

* Tue Jan 03 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.3-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sun Dec 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.3-2
- Use %%gem_extdir_mri instead of ext for %%check due to ruby3.2 change
  for ext cleanup during build

* Fri Sep 16 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.3-1
- 4.0.3

* Mon Sep  5 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.2-2
- 4.0.2

* Mon Sep  5 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.1-2
- Pull in some upstream patch

* Sun Sep  4 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.1-1
- 4.0.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-2
- Upstream patch to fix pointer <-> VALUE conversion on 32bit

* Sun Jan 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-1
- 3.5.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.9-1
- 3.4.9

* Sun Aug  8 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.7-1
- 3.4.7

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May  2 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.4-2
- Package some test utility files for other package on test suite

* Sun May  2 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.4-1
- 3.4.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-2
- F-34: rebuild against ruby 3.0

* Wed Aug 12 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-1
- 3.4.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-2
- F-32: rebuild against ruby27

* Wed Dec  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1

* Sat Oct 12 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Thu Oct  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.8-1
- 3.3.8

* Fri Sep  6 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-2
- Fix compilation for GLib 2.62.0

* Wed Sep  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-1
- 3.3.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.6-1
- 3.3.6

* Sun Feb 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.2-1
- 3.3.2

* Fri Feb  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.1-1
- 3.3.1

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-2
- F-30: rebuild against ruby26

* Wed Nov 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-1
- 3.3.0

* Mon Aug 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.9-1
- 3.2.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.7-1
- 3.2.7

* Thu May  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.5-1
- 3.2.5

* Wed Apr 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.4-1
- 3.2.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.2.1-3
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-2
- F-28: rebuild for ruby25

* Tue Nov 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Tue Nov 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Sat Oct 21 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.9-1
- 3.1.9

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.8-1
- 3.1.8

* Tue Jul 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-1
- 3.1.7

* Tue Jun  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-1
- 3.1.6

* Thu May  4 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-1
- 3.1.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-2
- F-26: rebuild for ruby24

* Tue Nov 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Sun Aug 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-1
- 3.0.9

* Tue Apr 19 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.8-1
- 3.0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-3
- F-24: rebuild against ruby23

* Mon Oct 12 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-2
- Pull upstream change for GLib::Variant for Gio side fix

* Sun Oct 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-1
- 3.0.7

* Wed Sep 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.5-1
- 3.0.5

* Tue Sep 22 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.4-1
- 3.0.4

* Sun Sep 20 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.3-1
- 3.0.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.5-1
- 2.2.5

* Sun Apr  5 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-3
- Fix compilation with GLib 2.44 (upstream bug 361)

* Thu Jan 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-2
- F-22: Rebuild for ruby 2.2

* Sun Dec 28 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-1
- 2.2.4

* Sun Nov 23 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-2
- Fix converter on bigendian 64bit (bug 1165638, github #270)

* Wed Nov  5 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-1
- 2.2.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-2
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Fri Apr 11 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

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

* Thu Feb 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-4
- F-19: Explicitly require mri for g_spawn_async() test

* Thu Feb 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-3
- Workaround patch for test failure with ruby 2.0.0

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-2
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

* Mon Apr 16 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.3-1
- 1.1.3

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.2-6
- Fix conditionals for F17 to work for RHEL 7 as well.

* Tue Mar 27 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.2-5
- Fix UTF-{16,32} related test failure on ppc{,64}
  (bug 804319, upstream bug 107)

* Fri Mar 23 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.2-4
- Fix build error with GLib >= 2.31.20 (bug 804319, upstream bug 106)

* Wed Feb  1 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.2-3
- Add proper Obsoletes/Provides

* Sun Jan 29 2012 Mamoru Tasaka <mtasaka@fedoraproject.org>
- And rebuild for ruby 1.9

* Sun Jan 29 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.2-1
- 1.1.2

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec  1 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.3-2
- Workaround on build issue and test suite with GLib 2.31.2

* Mon Sep 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Fri Jul 15 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.0-1
- 1.0.0

* Sun Jun 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.9-1
- 0.90.9

* Fri Mar 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.8-2
- Fix files list
- Patch for newer rake (>= 0.9.0 beta.2) to make GNOME2Package.task succeed

* Fri Mar  5 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.8-1
- 0.90.8

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  9 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.7-3
- 0.90.7
- Create "glib-test-init.rb" for testsuite on other ruby-gnome2 related
  gems

* Sun Oct 31 2010 Mamoru Taska  <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.5-3
- 0.90.5
- Move C extension so that "require %%gem_name" works correctly

* Sun Oct 24 2010 Mamoru Taska  <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.4-2
- 0.90.4

* Sun Oct 24 2010 Mamoru Taska  <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.3-2
- 0.90.3

* Fri Oct  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-6
- Fix up summary

* Fri Oct  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-5
- Use formally released gem file

* Tue Sep 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-4
- Modify Obsoletes
- Fix %%description

* Mon Sep 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-2
- 0.90.2 released, release bump

* Sun Sep 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-0.1
- Initial package
