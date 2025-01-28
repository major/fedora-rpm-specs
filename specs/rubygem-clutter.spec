%global	gem_name	clutter

Name:		rubygem-%{gem_name}
Version:	4.2.6
Release:	1%{?dist}
Summary:	Ruby binding of Clutter

%undefine        _changelog_trimtime

# SPDX confirmed
# LGPL-2.1-or-later: gemspec
# LGPL-2.1-only:	sample/box-layout.rb sample/grid-layout.rb
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://raw.github.com/ruby-gnome2/ruby-gnome2/master/COPYING.LIB
Source1:	COPYING.LIB.clutter

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	clutter
BuildRequires:	rubygem(cairo-gobject)
BuildRequires:	rubygem-glib2-devel
BuildRequires:	rubygem(gobject-introspection)
BuildRequires:	rubygem(pango)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-notify)
# Need X
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	mesa-dri-drivers
Requires:	ruby(release)
Requires:	ruby(rubygems)
Requires:	clutter
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
Ruby/Clutter is a Ruby binding of Clutter.


%package	doc
Summary:	Documentation for %{name}
License:	LGPL-2.1-or-later AND LGPL-2.1-only
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

sed -i -e 's|= 4\.2\.6|>= 4.2.6|' %{gem_name}-%{version}.gemspec
# clutter should be okay, pkgconfig(clutter-1.0) not strictly needed.
# hacking
sed -i dependency-check/Rakefile \
	-e '\@PKGConfig\.check_version@s|clutter-1.0|glib-2.0|'
sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

# Add license text
install -cpm 644 %{SOURCE1} ./COPYING.LIB
sed -i -e '/files =/s|\("Rakefile",\)|\1 "COPYING.LIB", |' \
	%{gem_name}-%{version}.gemspec

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Cleanups
pushd %{buildroot}%{gem_instdir}
rm -rf \
	dependency-check/ \
	%{nil}
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
sed -i test/run-test.rb \
	-e 's|require_relative "../../gobject-introspection/test/|require "|'

# Tweak test source directory
sed -i.path \
	-e '\@^clutter_base =@s|^.*$|clutter_base = File.join(File.dirname(__FILE__), "..")|' \
	test/run-test.rb

mkdir tmp
touch tmp/gobject-introspection-test-utils.rb

RANDR_OPTS=""
%if 0%{?fedora} >= 25
RANDR_OPTS="-extension RANDR"
%endif

# Need X
# For screen depth 24, see bug 904851
xvfb-run \
	-s "-screen 0 640x480x24 $RANDR_OPTS" \
%if 0
	-e /dev/stderr \
%endif
	ruby -Ilib:tmp:test ./test/run-test.rb

mv test/run-test.rb{.path,}
rm -rf tmp/

popd

%files
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile
%dir	%{gem_instdir}/
%dir	%{gem_instdir}/lib/
%{gem_instdir}/lib/%{gem_name}.rb
%dir	%{gem_instdir}/lib/%{gem_name}
%{gem_instdir}/lib/%{gem_name}/*.rb

%exclude %{gem_cache}
%exclude	%{gem_instdir}/*gemspec
%{gem_spec}

%files	doc
%doc	%{gem_docdir}
# Contains really executable sample scripts
%{gem_instdir}/sample/
%exclude	%{gem_instdir}/test/

%changelog
* Sun Jan 26 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.6-1
- 4.2.6

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

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

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

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

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May  3 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.4-1
- 3.4.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-1
- 3.4.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1

* Mon Oct 14 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Sun Sep  8 2019 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-1
- 3.3.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.6-1
- 3.3.6

* Mon Feb 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.2-1
- 3.3.2

* Fri Feb  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.1-1
- 3.3.1

* Fri Nov 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-1
- 3.3.0

* Mon Aug 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.9-1
- 3.2.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.7-1
- 3.2.7

* Thu May  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.5-1
- 3.2.5

* Thu Apr 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.4-2
- Bump release

* Thu Apr 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.4-1
- 3.2.4
- Ignore test failure for now

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Tue Nov 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Tue Oct 24 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.9-1
- 3.1.9

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.8-1
- 3.1.8

* Fri Jul 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-1
- 3.1.7

* Wed Jun  7 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-1
- 3.1.6

* Thu May  4 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-1
- 3.1.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Tue Nov 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Mon Aug 15 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-1
- 3.0.9

* Tue Apr 19 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.8-1
- 3.0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

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

* Sun Dec 28 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-1
- 2.2.4

* Sun Nov 23 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-2
- Test failure was fixed on gobject-introspection side,
  removing rescue and rebuild

* Thu Nov 20 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-1
- 2.2.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Sun Jan 19 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-1
- 2.1.0

* Sun Jan 19 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-1
- Initial package
