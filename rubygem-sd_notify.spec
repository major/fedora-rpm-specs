# Generated from sd_notify-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sd_notify

Name: rubygem-%{gem_name}
Version: 0.1.1
Release: 5%{?dist}
Summary: Pure Ruby implementation of systemd's sd_notify(3)
License: MIT
URL: https://github.com/agis/ruby-sdnotify
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# At the time of the packaging there were tests only in master branch.
# The test suite is not shiped with the gem, you may check it out like so
# git clone --no-checkout https://github.com/agis/ruby-sdnotify
# cd ruby-sdnotify && git archive -v -o ruby-sdnotify-0.1.1-tests.txz a7d52eef8dc3e026309c41c2421649863e0cabba test/
Source1: ruby-sdnotify-%{version}-tests.txz

BuildRequires: ruby(release)
BuildRequires: rubygem(minitest)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
sd_notify can be used to notify systemd about various service status changes
of Ruby programs.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Symlink the test suite into plaec
ln -s %{_builddir}/test .

ruby -Ilib -e 'Dir.glob("./test/**/*_test.rb").sort.each{ |f| require f }'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 06 2021 Pavel Valena <pvalena@redhat.com> - 0.1.1-1
- Initial package
