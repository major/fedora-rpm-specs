%global gem_name tomlrb

Name:           rubygem-%{gem_name}
Version:        2.0.1
Release:        %autorelease
Summary:        TOML parser based on racc
License:        MIT

URL:            https://github.com/fbernier/tomlrb
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{url}/archive/v%{version}/%{gem_name}-%{version}.tar.gz

# disable usage of special minitest reporters
Patch0:         00-disable-minitest-reporters.patch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.0

BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(racc)

BuildArch:      noarch

%description
A racc based toml parser.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}

# extract test files not shipped with the gem
mkdir upstream && pushd upstream
tar -xzvf %{SOURCE1}
mv %{gem_name}-%{version}/test ../test
popd && rm -r upstream

%patch0 -p1


%build
# rebuild parser sources from grammar
rm lib/tomlrb/generated_parser.rb
racc lib/tomlrb/parser.y -o lib/tomlrb/generated_parser.rb

gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# remove parser grammar from the installed files
find %{buildroot} -name "*.y" -print -delete


%check
ruby -I"lib:test" -e 'Dir.glob "./test/test*.rb", &method(:require)'


%files
%license %{gem_instdir}/LICENSE.txt

%dir %{gem_instdir}

%{gem_libdir}

%exclude %{gem_cache}

%{gem_spec}


%files doc
%doc %{gem_docdir}


%changelog
%autochangelog
