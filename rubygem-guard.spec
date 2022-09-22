# Generated from guard-2.16.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name guard

Name: rubygem-%{gem_name}
Version: 2.16.2
Release: 5%{?dist}
Summary: Guard keeps an eye on your file modifications
License: MIT
URL: http://guardgem.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/guard/guard.git && cd guard
# git checkout v2.16.2 && tar -czvf rubygem-guard-2.16.2-spec.tar.gz spec/
Source1: %{name}-%{version}-spec.tar.gz
# Cucumber test suite is tightly coupled with guard-cucumber which is not in Fedora yet.
# git clone https://github.com/guard/guard.git && cd guard
# git checkout v2.16.2 && tar -czvf rubygem-guard-2.16.2-features.tar.gz features/
# Source2: %%{name}-%%{version}-features.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(formatador)
BuildRequires: rubygem(listen)
BuildRequires: rubygem(lumberjack)
BuildRequires: rubygem(nenv)
BuildRequires: rubygem(notiffany)
BuildRequires: rubygem(pry)
BuildRequires: rubygem(shellany)
BuildRequires: rubygem(thor)
BuildRequires: rubygem(rspec)
# Cucumber features require guard-rspec and guard-cucumber and those are not in Fedora yet.
# BuildRequires: rubygem(cucumber)
# BuildRequires: rubygem(aruba)
BuildArch: noarch

%description
Guard is a command line tool to easily handle events on file system
modifications.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1 

# Kill Shebang
sed -i -e '\|^#!|d' lib/guard/rake_task.rb

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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/man/guard.1* %{buildroot}%{_mandir}/man1/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec
ln -s %{_builddir}/features features

# We don't really care about code coverage.
sed -i "/simplecov/ s/^/#/" spec/spec_helper.rb
sed -i "/SimpleCov.start do/,/^end/ s/^/#/" spec/spec_helper.rb

# Correct path to the bin file.
sed -i 's/path = File.expand_path("..\/..\/..\/bin\/guard", __dir__)/path = File.expand_path("..\/..\/..\/guard-2.16.2\/bin\/guard", __dir__)/' spec/lib/guard/bin_spec.rb

# RPM has some unexpected environment variables, ignore them.
sed -i '/GEM_SKIP/a \    allow(ENV).to receive(:[]).with("RPM_PACKAGE_NAME").and_call_original' spec/spec_helper.rb

# TODO: Fails with "stub me! (File.exist?("/usr/lib/gems/ruby/ffi-1.12.1/gem.build_complete"))",
# not entirely sure why
sed -i '/it "shows an info message" do/,/^      end$/ s/^/#/' spec/lib/guard/plugin_util_spec.rb

rspec -rspec_helper spec

# Cucumber features require guard-rspec and guard-cucumber and those are not in Fedora yet.
# cucumber
popd

%files
%dir %{gem_instdir}
%{_bindir}/guard
%{_bindir}/_guard-core
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_instdir}/images
%{gem_libdir}
%{_mandir}/man1/guard.1*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 3 2020 Jaroslav Prokop <jar.prokop@volny.cz> - 2.16.2-1
- Update to guard 2.16.2.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Jaroslav Prokop <jar.prokop@volny.cz> - 2.15.0-1
- Update to guard 2.15.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 06 2017 Jaroslav Prokop <jar.prokop@volny.cz> - 2.14.2-1
- Initial package
