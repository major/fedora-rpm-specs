# Generated from psych-comments-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name psych-comments

Name: rubygem-%{gem_name}
Version: 0.1.1
Release: %autorelease
Summary: Comment-aware YAML
License: MIT
URL: https://github.com/wantedly/psych-comments
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/wantedly/psych-comments.git
# git -C psych-comments archive -v -o psych-comments-0.1.1-tests.tar.gz v0.1.1 spec/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Brings comment-aware YAML parsing to Psych.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

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

%check
pushd ./%{gem_instdir}
ln -s %{_builddir}/spec .
rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.rubocop.yml
%license %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/bin/console
%exclude %{gem_instdir}/bin/setup
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%{gem_instdir}/psych-comments.gemspec

%changelog
%autochangelog
