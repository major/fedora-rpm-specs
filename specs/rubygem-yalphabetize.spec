# Generated from yalphabetize-0.13.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name yalphabetize

Name: rubygem-%{gem_name}
Version: 0.13.0
Release: %autorelease
Summary: Alphabetize your YAML files
License: MIT
URL: https://github.com/samrjenkins/yalphabetize
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/samrjenkins/yalphabetize.git
# git -C yalphabetize archive -v -o yalphabetize-0.13.0-tests.tar.gz v0.13.0 spec/
Source1: %{gem_name}-%{version}-tests.tar.gz
# https://github.com/samrjenkins/yalphabetize/pull/296
Source2: https://raw.githubusercontent.com/samrjenkins/yalphabetize/refs/tags/v%{version}/LICENSE
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: git-core
BuildRequires: rubygem(factory_bot)
BuildRequires: rubygem(psych-comments)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(simplecov)
BuildArch: noarch

%description
Yalphabetize is a static code analyzer and code formatter for alphabetizing
key-value pairs in your project's YAML files. Yalphabetize not only alerts you
to alphabetization offenses in your YAML files but can also automatically fix
them for you.

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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

cp -a %{SOURCE2} \
        %{buildroot}%{gem_instdir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
cp -a %{_builddir}/spec .
git init -q .
rspec -rspec_helper spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/yalphabetize
%{gem_instdir}/bin
%exclude %{gem_instdir}/bin/performance_local
%exclude %{gem_instdir}/bin/performance_test
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
