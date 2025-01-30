%global gem_name jekyll

Name:           rubygem-%{gem_name}
Summary:        Simple, blog aware, static site generator
Version:        4.4.0
Release:        %autorelease
License:        MIT

URL:            https://github.com/jekyll/jekyll
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{url}/archive/v%{version}/%{gem_name}-%{version}.tar.gz
Patch:          0000-jekyll-commands-remove-bundle-install-step-for-new.patch
Patch:          0001-test-helper-disable-simplecov-and-minitest-plugins.patch
Patch:          0002-test-utils-remove-internet-connectivity-test.patch
Patch:          0003-test-disable-tests-requiring-the-test-theme.patch
Patch:          0004-tests-related_posts-disable-tests-requiring-classifi.patch
Patch:          0005-test-coffeescript-disable-tests-requiring-coffeescri.patch
Patch:          0006-test-plugin_manager-disable-tests-requiring-gemspec-.patch
Patch:          0007-Revert-tests-to-expect-jekyll-sass-converter-2.patch


BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.4.0

BuildRequires:  help2man

# gems needed for running the test suite
BuildRequires:  rubygem(addressable) >= 2.4
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(colorator)
BuildRequires:  rubygem(csv)
BuildRequires:  rubygem(em-websocket)
BuildRequires:  rubygem(httpclient)
BuildRequires:  rubygem(i18n)
BuildRequires:  rubygem(jekyll-sass-converter) >= 2.0.0
BuildRequires:  rubygem(jekyll-watch) >= 2.0.0
BuildRequires:  rubygem(kramdown) >= 2.0.0
BuildRequires:  rubygem(kramdown-parser-gfm)
BuildRequires:  rubygem(kramdown-syntax-coderay)
BuildRequires:  rubygem(liquid) >= 4.0
BuildRequires:  rubygem(mercenary)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(pathutil)
BuildRequires:  rubygem(racc)
BuildRequires:  rubygem(rouge)
BuildRequires:  rubygem(rspec-mocks)
BuildRequires:  rubygem(safe_yaml)
BuildRequires:  rubygem(shoulda-context)
BuildRequires:  rubygem(terminal-table)
BuildRequires:  rubygem(tomlrb) >= 2.0.1
BuildRequires:  rubygem(tzinfo)
# https://fedoraproject.org/wiki/Changes/AllowRemovalOfTzdata
BuildRequires:  tzdata
BuildRequires:  rubygem(webrick)

# Additional gems required to run jekyll:
Requires:       rubygem(bigdecimal)
Requires:       rubygem(bundler)
Requires:       rubygem(csv)
Requires:       rubygem(json)

# Additional gems needed to actually deploy jekyll with default settings:
Recommends:     rubygem(jekyll-feed)
Recommends:     rubygem(jekyll-seo-tag)
Recommends:     rubygem(minima)

# Provide "jekyll", since this package ships a binary
Provides:       %{gem_name} = %{version}-%{release}

BuildArch:      noarch

%description
Jekyll is a simple, blog-aware, static site generator.

You create your content as text files (Markdown), and organize them into
folders. Then, you build the shell of your site using Liquid-enhanced
HTML templates. Jekyll automatically stitches the content and templates
together, generating a website made entirely of static assets, suitable
for uploading to any server.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%autosetup -N -n %{gem_name}-%{version}

# extract test files not shipped with the gem
mkdir upstream && pushd upstream
tar -xzvf %{SOURCE1}
mv %{gem_name}-%{version}/test ../test
popd && rm -r upstream

%autopatch -p1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x


# Build man page from "jekyll --help" output
export GEM_PATH="%{buildroot}/%{gem_dir}:%{gem_dir}"

mkdir -p %{buildroot}%{_mandir}/man1

help2man -N -s1 -o %{buildroot}%{_mandir}/man1/%{gem_name}.1 \
    %{buildroot}/usr/share/gems/gems/%{gem_name}-%{version}/exe/%{gem_name}


%check
# Test suite calls 'jekyll' from PATH, which in turn requires 'jekyll' gem.
PATH="$PATH:%{buildroot}%{_bindir}/"
export GEM_PATH="%{buildroot}/%{gem_dir}:%{gem_dir}"
# Tests only pass when timezone offset is zero.
# Related: https://github.com/jekyll/jekyll/pull/9168
TZ=UTC ruby -I"lib:test" -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'


%files
%license %{gem_instdir}/LICENSE

%{_bindir}/jekyll

%{_mandir}/man1/jekyll.1*

%dir %{gem_instdir}
%{gem_instdir}/exe/

%{gem_libdir}
%{gem_spec}

%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/rubocop
%exclude %{gem_cache}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown


%changelog
%autochangelog
