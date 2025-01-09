%global	header_dir	%{ruby_vendorarchdir}

%global		gem_name		gstreamer
%global		gemsoname		gst

%global		glibminver		3.0.8
%global		obsoleteevr	0.90.7-1.999


%undefine        _changelog_trimtime

Summary:	Ruby binding of GStreamer
Name:		rubygem-%{gem_name}
Version:	4.2.5
Release:	2%{?dist}
# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	gcc
BuildRequires:	rubygems-devel
BuildRequires:	rubygem-glib2-devel >= %{glibminver}
BuildRequires:	rubygem-gobject-introspection-devel >= %{glibminver}
BuildRequires:	ruby-devel
BuildRequires:	pkgconfig(gstreamer-1.0)
# %%check
BuildRequires:	rubygem(test-unit)
# decodebin / playbin
BuildRequires:	gstreamer1-plugins-base

Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# Kill non-gem support on F-17+
# Obsoletes but not provides
Obsoletes:	ruby-%{gem_name} < %{version}-%{release}

%description
Ruby/GStreamer is a Ruby binding of GStreamer.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/GStreamer development environment
Requires:	%{name}%{?_isa} = %{version}-%{release}
# Obsoletes / Provides
# ruby(%%{gem_name}-devel) Provides is for compatibility
# on F-15 and below
Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}

%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 4\.2\.5|>= 4.2.5|' %{gem_name}-%{version}.gemspec

# Fix wrong shebang
#grep -rl /usr/local/bin sample | \
#	xargs sed -i -e 's|/usr/local/bin|/usr/bin|'

# Kill shebang
grep -rl '#!.*/usr/bin' sample | \
	xargs sed -i -e '\@#![ ]*/usr/bin@d'
find sample/ -name \*.rb | xargs chmod 0644

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
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/


# Cleanups
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -f .%{gem_instdir}/extconf.rb
popd

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
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb
popd


%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile

%{gem_instdir}/lib/%{gemsoname}.rb
%{gem_instdir}/lib/%{gem_name}.rb
%{gem_instdir}/lib/%{gemsoname}/
%{gem_extdir_mri}/

%exclude	%{gem_cache}
%exclude	%{gem_instdir}/*gemspec
%{gem_spec}

%files	devel
%{_libdir}/pkgconfig/ruby-%{gem_name}.pc

%files	doc
%{gem_dir}/doc/%{gem_name}-%{version}
%exclude	%{gem_instdir}/Rakefile
%{gem_instdir}/sample/
%exclude	%{gem_instdir}/test/

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

* Fri Feb  3 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.0-1
- 4.1.0

* Sun Jan 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.8-1
- 4.0.8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan  6 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.5-1
- 4.0.5

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.3-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sun Dec 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.3-2
- Use %%gem_extdir_mri instead of ext for %%check due to ruby3.2 change
  for ext cleanup during build

* Fri Sep 16 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.3-1
- 4.0.3

* Mon Sep  5 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.2-1
- 4.0.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-1
- 3.5.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.9-1
- 3.4.9

* Sun Aug  8 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.7-1
- 3.4.7

* Sun Jul 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.4-2
- Rebuild for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May  2 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.4-1
- 3.4.4

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

* Wed Dec  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1

* Mon Oct 14 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Thu Oct  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.8-1
- 3.3.8

* Sun Sep  8 2019 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-1
- 3.3.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.6-1
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

* Thu Jun 21 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.7-1
- 3.2.7

* Thu May  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.5-1
- 3.2.5

* Thu Apr 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.4-1
- 3.2.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.2.1-3
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-2
- F-28: rebuild for ruby25

* Tue Nov 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Tue Nov 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Sun Oct 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.9-1
- 3.1.9

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.8-1
- 3.1.8

* Wed Jul 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-1
- 3.1.7

* Wed Jun  7 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-1
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

* Sun Aug 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-1
- 3.0.9

* Tue Apr 19 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.8-1
- 3.0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-2
- F-24: rebuild against ruby23

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

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.3-2
- 1.1.3

* Tue Jan 31 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.2-2
- 1.1.2

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Sat Dec 31 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.3-3
- Rescue test failure

* Thu Dec 29 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.3-2
- Add BR: gstreamer-plugins-good for smpte_caps in test/test_caps.rb
- Add BR: rubygem(test-unit)

* Wed Dec 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.3-1
- Initial package

