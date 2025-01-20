%global gem_name prawn-svg

Name: rubygem-%{gem_name}
Version: 0.35.1
Release: 3%{?dist}
Summary: SVG renderer for Prawn PDF library
License: MIT
URL: http://github.com/mogest/prawn-svg
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/mogest/prawn-svg/pull/171
Patch0:  %{gem_name}-pr171-support-new-rexml-invalid-xml-handling.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(prawn)
BuildRequires: rubygem(css_parser)
BuildRequires: rubygem(rexml)
BuildArch: noarch

%description
This gem allows you to render SVG directly into a PDF using the 'prawn' gem. 
Since PDF is vector-based, you'll get nice scaled graphics if you use SVG
instead of an image.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}
%patch -P0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Don't use Bundler.
sed -i "/require 'bundler'/ s/^/#/" spec/spec_helper.rb
sed -i "/Bundler/ s/^/#/" spec/spec_helper.rb
rspec -rprawn-svg spec
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.github/
%exclude %{gem_instdir}/Gemfile.lock
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/spec/sample_output
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/prawn-svg.gemspec
%{gem_instdir}/spec

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.35.1-2
- Backport upstream patch to support REXML 3.3.3 invalid XML handling

* Sat Aug 10 2024 Sergi Jimenez <tripledes@fedoraproject.org> - 0.35.1-1
- Update to 0.35.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Sergi Jimenez <tripledes@fedoraproject.org> - 0.34.2-1
- Update to 0.34.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 8 2021 Christopher Brown <chris.brown@redhat.com> - 0.32.0-1
- Update to 0.32.0

* Fri Feb 26 2021 Christopher Brown <chris.brown@redhat.com> - 0.31.0-3
- Add rexml BR

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Christopher Brown <chris.brown@redhat.com> - 0.31.0-1
- Update to 0.31.0
- Enable tests

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Christopher Brown <chris.brown@redhat.com> - 0.30.0-1
- Update to 0.30.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Christopher Brown <chris.brown@redhat.com> - 0.29.1-1
- Update to 0.29.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 8 2018 Christopher Brown <chris.brown@redhat.com> - 0.28.0-1
- Update to 0.28.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 11 2016 Fabio Alessandro Locati <fale@redhat.com> - 0.25.2-1
- Update to 0.25.2

* Fri Jun 17 2016 Fabio Alessandro Locati <fale@redhat.com> - 0.25.1-1
- Initial package
