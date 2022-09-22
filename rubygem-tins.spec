# Generated from tins-1.29.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tins

Name: rubygem-%{gem_name}
Version: 1.31.1
Release: 2%{?dist}
Summary: Useful tools library in Ruby
License: MIT
URL: https://github.com/flori/tins
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
BuildRequires: rubygem(irb)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0
# BuildRequires: rubygem(gem_hadar) >= 1.11.0
# BuildRequires: rubygem(gem_hadar) < 1.12
BuildRequires: rubygem(sync)
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(simplecov)
BuildArch: noarch

%description
All the stuff that isn't good/big enough for a real library.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
ruby -rtest-unit -e 'exit Test::Unit::AutoRunner.run(true)' -Ilib tests/
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/tests
%{gem_instdir}/tins.gemspec

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 07 2022 Otto Urpelainen <oturpe@iki.fi> - 1.31.1-1
- Update to 1.31.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Otto Urpelainen <oturpe@iki.fi> - 1.31.0-1
- Update to 1.31.0

* Mon Dec 27 2021 Otto Urpelainen <oturpe@iki.fi> - 1.30.0-1
- Update to 1.30.0

* Tue Aug 17 2021 Otto Urpelainen <oturpe@iki.fi> - 1.29.1-2
- Do not Require rubygem(irb). Most usage does not need it, and what does,
  should require it separately.

* Sat Jul 24 2021 Otto Urpelainen <oturpe@iki.fi> - 1.29.1-1
- Update to version 1.29.1
- Fixes rhbz#1078788

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.0-5
- Fix test-unit usage for F22+

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Achilleas Pipinellis <axilleas@fedoraproject.org> - 1.0.0-2
- Fix rpmlint errors/warnings

* Sun Feb 23 2014 Achilleas Pipinellis <axilleas@fedoraproject.org> - 1.0.0-1
- Bump to 1.0.0
- Do some cleanup

* Mon Jan 27 2014 Achilleas Pipinellis <axilleas@fedoraproject.org> - 0.13.1-1
- Bump to 0.13.1

* Wed Aug 14 2013 Axilleas Pipinellis <axilleas@fedoraproject.org> - 0.8.4-2
- Add forgotten changelog

* Tue Aug 13 2013 Axilleas Pipinellis <axilleas@fedoraproject.org> - 0.8.4-1
- Version bump

* Tue Aug 13 2013 Axilleas Pipinellis <axilleas@fedoraproject.org> - 0.8.3-1
- Initial package
