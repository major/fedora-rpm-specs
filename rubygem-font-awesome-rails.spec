%global gem_name font-awesome-rails

Name: rubygem-%{gem_name}
Version: 4.7.0.8
Release: 2%{?dist}
Summary: An asset gemification of the font-awesome icon font library
# Fonts are licensed with SIL Open Font License 1.1
License: MIT and OFL
URL: https://github.com/bokmann/font-awesome-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: fontawesome-fonts >= 1:4.7.0
Requires: fontawesome-fonts < 1:4.8.0
BuildRequires: rubygems-devel
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(sass-rails)
BuildRequires: fontpackages-devel
BuildRequires: fontawesome-fonts
BuildArch: noarch

%description
A font-awesome icon font library for the Rails asset pipeline.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Symlink *.otf and *.ttf as this is shipped in fontawesome-fonts pkg
rm %{buildroot}%{gem_instdir}/app/assets/fonts/FontAwesome.otf
ln -s %{_fontbasedir}/fontawesome/FontAwesome.otf %{buildroot}%{gem_instdir}/app/assets/fonts/FontAwesome.otf
rm %{buildroot}%{gem_instdir}/app/assets/fonts/fontawesome-webfont.ttf
ln -s %{_fontbasedir}/fontawesome/fontawesome-webfont.ttf %{buildroot}%{gem_instdir}/app/assets/fonts/fontawesome-webfont.ttf

# Fix permissions
find %{buildroot}%{gem_dir}/**/* -type f | xargs chmod 0644

# Remove shebang from non-executable Rakefile
sed -i -e '1d' %{buildroot}%{gem_instdir}/Rakefile

%check
pushd .%{gem_instdir}
# Get rid of bundler
sed -i -e '6d' test/dummy/config/application.rb
ruby -Ilib:test:app:app/helpers/font_awesome/rails -rrails -raction_view -rsass-rails -rfont-awesome-rails -ricon_helper \
     -e 'Dir.glob "./test/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/test/dummy/.gitignore
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Christopher Brown <chris.brown@redhat.com> - 4.7.0.8-1
- Update to 4.7.0.8

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 2 2021 Christopher Brown <chris.brown@redhat.com> - 4.7.0.7-1
- Update to 4.7.0.7

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 1 2021 Christopher Brown <chris.brown@redhat.com> - 4.7.0.6-1
- Update to 4.7.0.6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.7.0.5-5
- Epoch fontawesome dependency

* Fri Apr 17 2020 Vít Ondruch <vondruch@redhat.com> - 4.7.0.5-4
- did_you_mean is now bundled in Ruby.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Christopher Brown <chris.brown@redhat.com> - 4.7.0.5-1
- Update to 4.7.0.5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Christopher Brown <chris.brown@redhat.com> - 4.7.0.4-1
- Update to 4.7.0.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Vít Ondruch <vondruch@redhat.com> - 4.7.0.2-1
- Update to 4.7.0.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.7.0.1-1
- Update to 4.7.0.1

* Thu Oct 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.7.0.0-1
- Update to 4.7.0.0

* Tue Aug 23 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.6.3.1-1
- Update to 4.6.3.1

* Sun May 22 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.6.3.0-1
- Update to 4.6.3.0

* Thu May 05 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.6.2.0-1
- Update to 4.6.2.0

* Wed Apr 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.6.1.0-1
- Update to 4.6.1.0

* Sat Apr 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.5.0.1-1
- Update to 4.5.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Josef Stribny <jstribny@redhat.com> - 4.4.0.0-1
- Update to 4.4.0.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0.0-4
- Fix version dependency on font-awesome-fonts

* Mon Sep 22 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0.0-3
- Remove shebang from Rakefile
- State exact version dependency on fontawesome-fonts

* Tue Sep 16 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0.0-2
- Fix permissions

* Fri Jul 18 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0.0-1
- Initial package
