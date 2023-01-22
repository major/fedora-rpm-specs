# Generated from uglifier-1.2.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name uglifier

%global uglify_js_version 2.8.22
%global source_map_version 0.5.6

Name: rubygem-%{gem_name}
Version: 3.2.0
Release: 14%{?dist}
Summary: Ruby wrapper for UglifyJS JavaScript compressor
# lib/source-map.js is BSD.
# lib/uglify.js is BSD.
# lib/uglify-harmony.js (UglifyJS2 harmony branch) is BSD.
License: MIT and BSD
URL: http://github.com/lautis/uglifier
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# The uglifier gem doesn't ship with the test suite.
# git clone https://github.com/lautis/uglifier.git && cd uglifier
# git checkout v3.2.0 && tar czvf uglifier-3.2.0-tests.tgz spec/
Source1: %{gem_name}-%{version}-tests.tgz
# Unbundling es5.js and split.js files,
# since they are needed only by JScript engine, which is not supported on Fedora
# https://github.com/lautis/uglifier/issues/99
Patch1: rubygem-uglifier-3.2.0-unbundle-js-files-for-jscript.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(execjs) >= 0.3.0
BuildRequires: rubygem(rspec)
BuildRequires: %{_bindir}/node

# Bundle uglify-js by the request from the Fedora Minimization team.
# https://bugzilla.redhat.com/show_bug.cgi?id=1828876
Provides: bundled(uglify-js) = %{uglify_js_version}
# There is not included dist/source-map.js yet.
# https://bugzilla.redhat.com/show_bug.cgi?id=1358915
Provides: bundled(nodejs-source-map) = %{source_map_version}
BuildArch: noarch

%description
Uglifier minifies JavaScript files by wrapping UglifyJS to be accessible in
Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch1 -p1
sed -i '/files/ s|"lib/es5.js".freeze, ||' %{gem_name}.gemspec
sed -i '/files/ s|"lib/split.js".freeze, ||' %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}
# Disable rubygem-sourcemap because it is not part of fedora yet.
sed -i "/require 'sourcemap'/ s/^/#/"  spec/spec_helper.rb
sed -i '/SourceMap::Map/ i \    pending' spec/source_map_spec.rb

rspec spec
popd


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_instdir}/uglifier.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Jun Aruga <jaruga@redhat.com> - 3.2.0-8
- Bundle uglify-js by the request from the Fedora Minimization team.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Jun Aruga <jaruga@redhat.com> - 3.2.0-1
- Update to Uglifier 3.2.0.

* Wed Mar 29 2017 Jun Aruga <jaruga@redhat.com> - 3.1.11-1
- Update to Uglifier 3.1.11.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Jun Aruga <jaruga@redhat.com> - 3.0.2-2
- Fix FTBFS due to updated RubyGems.

* Thu Oct 13 2016 Vít Ondruch <vondruch@redhat.com> - 3.0.2-1
- Update to Uglifier 3.0.2.

* Wed Jul 27 2016 Jun Aruga <jaruga@redhat.com> - 3.0.0-1
- Fix for FTBFS. (rhbz#1357879)
- Update to uglifier 3.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 07 2014 Josef Stribny <jstribny@redhat.com> - 2.4.0-1
- Update to uglifier 2.4.0

* Wed Oct 30 2013 Josef Stribny <jstribny@redhat.com> - 2.3.0-1
- Update to uglifier 2.3.0

* Mon Oct 21 2013 Josef Stribny <jstribny@redhat.com> - 2.2.1-1
- Update to uglifier 2.2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.0-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 5 2012 Josef Stribny <jstribny@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Mon Jul 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.6-1
- Initial package
