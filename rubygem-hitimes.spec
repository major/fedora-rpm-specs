# Generated from hitimes-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hitimes

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 7%{?dist}
Summary: A fast, high resolution timer library for recording performance metrics
License: ISC
URL: http://github.com/copiousfreetime/hitimes
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Hitimes is a fast, high resolution timer library for recording performance
metrics.  It uses the appropriate low method calls for each system to get the
highest granularity time increments possible. It currently supports any of the
following systems: * any system with the POSIX call `clock_gettime()` * Mac OS
X * Windows * JRuby Using Hitimes can be faster than using a series of
`Time.new` calls, and it will have a much higher granularity. It is definitely
faster than using `Process.times`.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd ./%{gem_instdir}
# Remove simplecov uneeded dependency
sed -i '/^if RUBY_VERSION/,/^end$/ s/^/# /g' spec/spec_helper.rb
ruby -Ilib:spec -e 'Dir.glob "./spec/*spec.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%license %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec/
%{gem_instdir}/tasks/
%{gem_instdir}/examples/
%{gem_instdir}/Rakefile

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 12:50:37 GMT 2020 Pavel Valena <pvalena@redhat.com> - 2.0.0-1
- Update to hitimes 2.0.0.
  Resolves: rhbz#1754539

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-3
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Pavel Valena <pvalena@redhat.com> - 1.3.1-1
- Update to hitimes 1.3.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 21 2018 Pavel Valena <pvalena@redhat.com> - 1.3.0-1
- Update to hitimes 1.3.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.2.6-3
- Rebuilt for switch to libxcrypt

* Fri Jan 12 2018 Vít Ondruch <vondruch@redhat.com> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.5

* Tue Aug 15 2017 Pavel Valena <pvalena@redhat.com> - 1.2.6-1
- Update to 1.2.6.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Vít Ondruch <vondruch@redhat.com> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Pavel Valena <pvalena@redhat.com> - 1.2.3-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3
- Update to 1.2.3
- Removed .travis.yml

* Wed Feb 18 2015 Josef Stribny <jstribny@redhat.com> - 1.2.2-1
- Update to 1.2.2
- Fix the packaging for Ruby 2.2

* Mon Jan 20 2014 Achilleas Pipinellis <axilleaspi@ymail.com> - 1.2.1-1
- Initial package
