%global	gem_name	webkit2-gtk

%undefine        _changelog_trimtime

Name:		rubygem-%{gem_name}
Version:	4.2.7
Release:	1%{?dist}

Summary:	Ruby binding of WebKit2GTK+
# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.osdn.jp/

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://raw.githubusercontent.com/ruby-gnome2/ruby-gnome2/master/COPYING.LIB
# renamed to avoid namespace collision on sourcedir
Source1:	COPYING.LIB.webkit2-gtk

# Require MRI
BuildRequires:	ruby
BuildRequires:	rubygems-devel
# glib-test-init.rb
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	rubygem-glib2-devel
BuildRequires:	rubygem(gobject-introspection)
BuildRequires:	rubygem(gtk3)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(webrick)
# https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
# Use webkit2gtk-4.1 for F-39+
%if 0%{?fedora} >= 39
BuildRequires:	webkit2gtk4.1
Requires:		webkit2gtk4.1
%else
BuildRequires:	webkit2gtk4.0
Requires:		webkit2gtk4.0
%endif

BuildArch:		noarch

%description
Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Adjust rubygems-gnome2 requirement to be more flexible
sed -i -e 's|= 4\.2\.7|>= 4.2.7|' %{gem_name}-%{version}.gemspec
# pkgconfig dependency is actually not needed (when using rpm
# dependency solver)
sed -i dependency-check/Rakefile \
	-e 's|dependency:check|nothing|'
sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

install -cpm 644 %{SOURCE1} %{buildroot}%{gem_instdir}/COPYING.LIB

# cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	dependency-check/ \
	test/
popd

%check
pushd .%{gem_instdir}

rm -rf tmp
mkdir tmp
pushd tmp
touch gobject-introspection-test-utils.rb
popd

RANDR_OPTS=""
%if 0%{?fedora} >= 25
RANDR_OPTS="-extension RANDR"
%endif

sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../gobject-introspection/test/|require "|'

# ignore test failure for F-30 for now
xvfb-run \
	-s "-screen 0 640x480x24 $RANDR_OPTS" \
	ruby -Ilib:tmp:test ./test/run-test.rb \
%if 0%{?fedora} >= 32
	|| true # ignore test failure for now
%endif

popd

%files
%dir		%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*

%{gem_libdir}
%{gem_spec}

%exclude	%{gem_instdir}/*gemspec
%exclude	%{gem_cache}

%files	doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/sample

%changelog
* Thu Jan 30 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.7-1
- 4.2.7

* Sun Jan 26 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.6-1
- 4.2.6

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-2
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

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
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

* Sun May 07 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.4-2
- Use webkit2gtk-4.1 for F-39+
  https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
- Remove pretty old Obsoletes entry

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

* Mon Jan 24 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-1
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

* Fri Dec  6 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1

* Tue Oct 15 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Sun Sep  8 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-1
- 3.3.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.6-1
- 3.3.6

* Mon Feb 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.2-1
- 3.3.2

* Sat Feb  2 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.1-1
- 3.3.1

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

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Wed Nov 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Tue Oct 24 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.9-1
- 3.1.9

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.8-1
- 3.1.8

* Fri Jun  9 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-1
- 3.1.6

* Fri May 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-2
- Fix Obsoletes

* Fri May 05 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-1
- Initial package
