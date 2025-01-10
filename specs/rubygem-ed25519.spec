# Generated from ed25519-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ed25519

Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 9%{?dist}
Summary: An efficient digital signature library providing the Ed25519 algorithm
License: MIT
URL: https://github.com/crypto-rb/ed25519
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests are not packaged with the gem. You may get them like so:
# git clone --no-checkout https://github.com/crypto-rb/ed25519
# git -C ed25519 archive -v -o ed25519-1.3.0-spec.txz v1.3.0 spec
Source1: %{gem_name}-%{version}-spec.txz
BuildRequires: ruby(release)
BuildRequires: rubygem(rspec)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 2.0.0
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

%description
A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1

find -type f -iname '*.jar'

%gemspec_remove_file ["lib/ed25519_jruby.jar"]

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .

sed -i -e '/^require .bundler\/setup./ s/^/#/g' \
  -e '/^require .coveralls./ s/^/#/g' \
  -e '/^Coveralls\./ s/^/#/g' \
  ./spec/spec_helper.rb
rspec -rspec_helper -I$(dirs +1)%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGES.md
%{gem_instdir}/ed25519.png

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-9
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Thu Aug 25 2022 Pavel Valena <pvalena@redhat.com> - 1.3.0-1
- Initial package
