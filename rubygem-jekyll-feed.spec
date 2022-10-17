%global gem_name jekyll-feed

Name:           rubygem-%{gem_name}
Version:        0.17.0
Release:        %autorelease
Summary:        Jekyll plugin to generate an Atom feed of your Jekyll posts
License:        MIT

URL:            https://github.com/jekyll/jekyll-feed
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{url}/archive/v%{version}/%{gem_name}-%{version}.tar.gz

BuildRequires:  ruby >= 2.4.0
BuildRequires:  rubygems-devel
BuildRequires:  ruby(release)

BuildRequires:  (rubygem(jekyll) >= 3.7 with rubygem(jekyll) < 5.0)
BuildRequires:  (rubygem(nokogiri) >= 1.6 with rubygem(nokogiri) < 2)
BuildRequires:  (rubygem(rspec) >= 3.0 with rubygem(rspec) < 4)
BuildRequires:  rubygem(typhoeus)
BuildRequires:  rubygem(rss)

BuildArch:      noarch

%description
A Jekyll plugin to generate an Atom feed of your Jekyll posts.


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
mv %{gem_name}-%{version}/spec ../spec
popd && rm -r upstream


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
# Tests fail when LANG is not set to a UTF-8 locale
LANG=C.UTF-8 rspec spec


%files
%license %{gem_instdir}/LICENSE.txt

%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}

%exclude %{gem_cache}

%files doc
%doc %{gem_instdir}/History.markdown
%doc %{gem_instdir}/README.md

%doc %{gem_docdir}


%changelog
%autochangelog
