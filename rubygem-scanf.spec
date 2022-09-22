%global gem_name scanf

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: %autorelease
Summary: A Ruby implementation of the C function scanf(3)
License: BSD
URL: https://github.com/ruby/scanf
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# License is not included in the gem, copied from git
Source1: LICENSE.txt
# Tests are not included in the gem, copied from git
Source2: data.txt
Source3: test_scanf.rb
Source4: test_scanfblocks.rb
Source5: test_scanfio.rb
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3.0
# Required for %check
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
A Ruby implementation of the C function scanf(3).


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
cp %{SOURCE1} LICENSE.txt

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
ruby -I.%{gem_instdir}/lib %{SOURCE3} %{SOURCE4} %{SOURCE5}

%files
%license LICENSE.txt
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
%autochangelog
