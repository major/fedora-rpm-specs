# Generated from activestorage-0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activestorage

# Circular dependency with rubygem-railties.
%bcond_with bootstrap

# FFmpeg can be used in tests, but is not available in Fedora
%bcond_with ffmpeg

Name: rubygem-%{gem_name}
Version: 7.0.8
Release: 6%{?dist}
Summary: Local and cloud file storage framework
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# The gem doesn't ship with the test suite.
# You may check it out like so
# git clone https://github.com/rails/rails.git
# cd rails/activestorage && git archive -v -o activestorage-7.0.8-tests.txz v7.0.8 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may check it out like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-7.0.8-tools.txz v7.0.8 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz
# Fixes for Minitest 5.16+.
# https://github.com/rails/rails/pull/45370
Patch0: rubygem-activestorage-7.0.2.3-Fix-tests-for-minitest-5.16.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(activejob) = %{version}
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(rails) = %{version}
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(connection_pool)
BuildRequires: rubygem(image_processing)
BuildRequires: rubygem(mutex_m)
BuildRequires: rubygem(sqlite3)
# FFmpeg is not available in Fedora
%{?with_ffmpeg:BuildRequires: %{_bindir}/ffmpeg}
%{?with_ffmpeg:BuildRequires: %{_bindir}/ffprobe}
BuildRequires: %{_bindir}/mutool
BuildRequires: %{_bindir}/pdftoppm
%endif
# Used for creating file previews
Suggests: %{_bindir}/mutool
Suggests: %{_bindir}/pdftoppm
Suggests: %{_bindir}/ffmpeg
Suggests: %{_bindir}/ffprobe

BuildArch: noarch

%description
Attach cloud and local files in Rails applications.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

pushd %{_builddir}
%patch 0 -p2
popd

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if %{without bootstrap}
# fake RAILS_FRAMEWORK_ROOT
ln -s %{gem_dir}/specifications/rails-%{version}%{?prerelease}.gemspec .%{gem_dir}/gems/rails.gemspec
ln -s %{gem_dir}/gems/railties-%{version}%{?prerelease}/ .%{gem_dir}/gems/railties
ln -s %{gem_dir}/gems/activerecord-%{version}%{?prerelease}/ .%{gem_dir}/gems/activerecord
ln -s %{gem_dir}/gems/activejob-%{version}%{?prerelease}/ .%{gem_dir}/gems/activejob
ln -s %{gem_dir}/gems/actionpack-%{version}%{?prerelease}/ .%{gem_dir}/gems/actionpack
ln -s %{gem_dir}/gems/activesupport-%{version}%{?prerelease}/ .%{gem_dir}/gems/activesupport
ln -s ${PWD}%{gem_instdir} .%{gem_dir}/gems/%{gem_name}

pushd .%{gem_dir}/gems/%{gem_name}
ln -s %{_builddir}/tools ..
# Copy the tests into place.
cp -a %{_builddir}/test .

touch Gemfile
echo 'gem "actionpack"' >> ../Gemfile
echo 'gem "activerecord"' >> ../Gemfile
echo 'gem "activejob"' >> ../Gemfile
echo 'gem "sprockets-rails"' >> ../Gemfile
echo 'gem "image_processing"' >> ../Gemfile
echo 'gem "mutex_m"' >> ../Gemfile
echo 'gem "rails"' >> ../Gemfile
echo 'gem "sqlite3"' >> ../Gemfile

# Disable tests that require FFmpeg
%if %{without ffmpeg}
mv test/analyzer/video_analyzer_test.rb{,.disable}
mv test/analyzer/audio_analyzer_test.rb{,.disable}
mv test/previewer/video_previewer_test.rb{,.disable}
for f in \
  models/preview \
  models/representation \
  %{nil}
do
sed -i '/^  test ".* MP4 video.*" do$/,/^  end$/ s/^/#/g' \
  test/${f}_test.rb
done
%endif

# Blobs seem to be broken
# https://github.com/rails/rails/pull/40226
# https://github.com/rails/rails/issues/44395
sed -i -e '/test "optimized variation of GIF"/ a skip' \
     -e '/thumbnail variation of extensionless GIF/ a skip' \
     -e '/test "resized variation of PSD blob" do/ a skip' \
     -e '/test "resized variation of BMP blob" do/ a skip' \
     -e '/test "resized variation of ICO blob" do/ a skip' \
     -e '/test "resized variation of GIF blob" do/ a skip' \
     -e '/test "optimized variation of GIF blob" do/ a skip' \
  test/models/variant_test.rb

# MiniMagic test incompatibility (depends on other gems versions)
# Similar to: https://github.com/rails/rails/issues/44395
# TODO: investigate or file later if the issue persists
sed -i -e '/test "previewing a cropped PDF document"/ a skip' \
  test/previewer/mupdf_previewer_test.rb

export RUBYOPT="-I${PWD}/../%{gem_name}/lib"
export PATH="${PWD}/../%{gem_name}/exe:$PATH"
export BUNDLE_GEMFILE=${PWD}/../Gemfile

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.0.8-5
- Add BR: rubygem(mutex_m) explicitly for ruby34

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 10 2023 Pavel Valena <pvalena@redhat.com> - 7.0.8-1
- Update to activestorage 7.0.8.

* Mon Aug 28 2023 Pavel Valena <pvalena@redhat.com> - 7.0.7.2-1
- Update to activestorage 7.0.7.2.

* Thu Aug 10 2023 Pavel Valena <pvalena@redhat.com> - 7.0.7-1
- Update to activestorage 7.0.7.

* Sun Jul 23 2023 Pavel Valena <pvalena@redhat.com> - 7.0.6-1
- Update to activestorage 7.0.6.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Pavel Valena <pvalena@redhat.com> - 7.0.5-1
- Update to activestorage 7.0.5.

* Tue Mar 14 2023 Pavel Valena <pvalena@redhat.com> - 7.0.4.3-1
- Update to activestorage 7.0.4.3.

* Wed Jan 25 2023 Pavel Valena <pvalena@redhat.com> - 7.0.4.2-1
- Update to activestorage 7.0.4.2.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Pavel Valena <pvalena@redhat.com> - 7.0.4-1
- Update to activestorage 7.0.4.

* Tue Aug 02 2022 Vít Ondruch <vondruch@redhat.com> - 7.0.2.3-3
- Fix Minitest 5.16+ compatibility.
  Resolves: rhbz#2113686

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 14 2022 Pavel Valena <pvalena@redhat.com> - 7.0.2.3-1
- Update to activestorage 7.0.2.3.

* Wed Feb 09 2022 Pavel Valena <pvalena@redhat.com> - 7.0.2-1
- Update to activestorage 7.0.2.

* Thu Feb 03 2022 Pavel Valena <pvalena@redhat.com> - 7.0.1-1
- Update to activestorage 7.0.1.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 Pavel Valena <pvalena@redhat.com> - 6.1.4.1-1
- Update to activestorage 6.1.4.1.

* Tue Aug 31 2021 Vít Ondruch <vondruch@redhat.com> - 6.1.4-3
- Re-enable TIFF test after ImageMagick issues were resolved.
  Related: rhbz#1993193

* Fri Aug 06 2021 Vít Ondruch <vondruch@redhat.com> - 6.1.4-2
- Disable flaky TIFF test.
  Resolves: rhbz#1987926

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Pavel Valena <pvalena@redhat.com> - 6.1.4-1
- Update to activestorage 6.1.4.

* Tue May 18 2021 Pavel Valena <pvalena@redhat.com> - 6.1.3.2-1
- Update to activestorage 6.1.3.2.

* Fri Apr 16 2021 Pavel Valena <pvalena@redhat.com> - 6.1.3.1-2
- Relax mini_mime dependency.

* Fri Apr 09 2021 Pavel Valena <pvalena@redhat.com> - 6.1.3.1-1
- Update to activestorage 6.1.3.1.

* Thu Feb 18 2021 Pavel Valena <pvalena@redhat.com> - 6.1.3-1
- Update to activestorage 6.1.3.

* Mon Feb 15 2021 Pavel Valena <pvalena@redhat.com> - 6.1.2.1-1
- Update to activestorage 6.1.2.1.

* Wed Jan 27 2021 Pavel Valena <pvalena@redhat.com> - 6.1.1-1
- Update to activestorage 6.1.1.
  Resolves: rhbz#1906180

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 11:56:48 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.4-1
- Update to activestorage 6.0.3.4.
  Resolves: rhbz#1877544

* Tue Sep 22 01:10:44 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.3-1
- Update to activestorage 6.0.3.3.
  Resolves: rhbz#1877544

* Mon Aug 17 05:23:03 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.2-1
- Update to activestorage 6.0.3.2.
  Resolves: rhbz#1742796

* Mon Aug 03 07:01:37 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-1
- Update to ActiveStorage 6.0.3.1.
  Resolves: rhbz#1742796

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Tom Callaway <spot@fedoraproject.org> - 5.2.3-4
- rebuild for new rubygem-connection_pool

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-2
- Enable tests.

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-1
- Update to Active Storage 5.2.3.

* Mon Mar 18 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-2
- Enable tests.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-1
- Update to Active Storage 5.2.2.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 5.2.2-2
- Update to Active Storage 5.2.2.

* Thu Aug 09 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-2
- Enable tests.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-1
- Update to Active Storage 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-2
- Enable tests.

* Wed May 02 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-1
- Update to Active Storage 5.2.0.
- Moved to Rails repository.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Vít Ondruch <vondruch@redhat.com> - 0.1-1
- Initial package
