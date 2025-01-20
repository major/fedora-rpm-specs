%global gem_name codeclimate-test-reporter

Name:           rubygem-%{gem_name}
Version:        1.0.9
Release:        5%{?dist}
Summary:        Uploads Ruby test coverage data to Code Climate

License:        MIT
URL:            https://github.com/codeclimate/ruby-test-reporter
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/codeclimate/ruby-test-reporter
# git -C ruby-test-reporter archive --format tar.gz v1.0.9 -o $PWD/codeclimate-test-reporter-1.0.9-specs.tar.gz -- spec
Source1: 		%{gem_name}-%{version}-specs.tar.gz

Buildrequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(webmock)
BuildRequires:  rubygem(pry)
BuildRequires:  rubygem(simplecov)
BuildRequires:  git-core

BuildArch:      noarch

%description
Collects test coverage data from your Ruby test suite and sends it to Code
Climate's hosted, automated code review service. Based on SimpleCov.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{gem_name}-%{version} -a 1 -S git
sed -i '/bundler/d' spec/spec_helper.rb
sed -i 's/0.13/0.13.0/g' ../%{gem_name}-%{version}.gemspec

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* %{buildroot}%{_bindir}/

# Run the test suite
%check
rspec -Ilib spec

%files
%license %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%{_bindir}/cc-tddium-post-worker
%{_bindir}/%{gem_name}
%exclude %{gem_instdir}/bin
%exclude %{gem_instdir}/config
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 15 2023 Ilia Gradina <ilgrad@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.8-2
- small fix 

* Mon Jul 10 2017 Ilya Gradina <ilya.gradina@gmail.com> - 1.0.8-1
- update to 1.0.8

* Wed Sep 14 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.6.0-1
- update to 0.6.0

* Wed Sep 30 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.4.8-1
- Initial package
