%global gem_name memoizer

Name: rubygem-%{gem_name}
Version: 1.0.3
Release: 8%{?dist}
Summary: Memoize your methods
License: MIT
URL: https://github.com/wegowise/memoizer
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: ruby(release) >= 1.9.3
BuildRequires: rubygems-devel
BuildRequires: rubygem(timecop) >= 0.8.0
BuildRequires: rubygem(rspec) >= 3.5.0
BuildArch: noarch

%description
Memoizer caches the results of your method calls, works well 
with methods that accept arguments or return nil. It's a 
simpler and more expicit alternative to ActiveSupport::Memoizable

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}
sed -i '/bundler\/setup/d' spec/spec_helper.rb

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
rspec spec

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/memoizer.gemspec
%doc     %{gem_instdir}/README.md
%doc     %{gem_instdir}/CHANGELOG.txt
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}
%exclude %{gem_docdir}/rdoc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 19 2022 Benson Muite <benson_muite@emailplus.org> - 1.0.3-2
- Remove Rakefile from packaged files
- Do not require bundler or rake

* Mon Oct 31 2022 Benson Muite <benson_muite@emailplus.org> - 1.0.3-1
- Initial package

