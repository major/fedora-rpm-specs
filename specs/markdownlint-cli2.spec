%global npm_name markdownlint-cli2

Name:     markdownlint-cli2
Version:  0.23.2
Release:  %autorelease
Summary:  A command-line tool for linting Markdown/CommonMark files

License:  BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND Python-2.0.1
# argparse declare a Python-2.0 license but the LICENSE file is actually a Python-2.0.1 license.
# A pull request was made to fix it upstream https://github.com/nodeca/argparse/pull/188

URL:      https://github.com/DavidAnson/markdownlint-cli2

# Use github source because the one on npm doesn't include tests
Source0:  https://github.com/DavidAnson/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Generated using command `nodejs-packaging-bundler  markdownlint-cli2 0.23.2`
Source1:  %{npm_name}-%{version}-nm-prod.tgz
Source2:  %{npm_name}-%{version}-nm-dev.tgz
# Python-2.0 license was renamed to Python-2.0.1 because of argparse
Source3:  %{npm_name}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-devel
BuildRequires:  npm
BuildRequires:  fdupes

%description
A fast, flexible, configuration-based command-line interface for linting
Markdown/CommonMark files with the markdownlint library.

%prep
%autosetup -n %{name}-%{version}
cp %{SOURCE3} .

%build
# Setup bundled node modules
tar xfz %{SOURCE1}
mv node_modules_prod node_modules

# Remove duplicated files
rm -r node_modules/%{npm_name}
rm node_modules/.bin/%{npm_name}

# Remove fonts and build-time scripts
rm -r node_modules/katex/dist/fonts node_modules/katex/src

# Remove .github dirs
rm -r node_modules/*/.github

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Bundled runtime dependencies
cp -pr node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Application files
cp -p \
    package.json \
    append-to-array.mjs \
    clone-options.mjs \
    constants.mjs \
    export-markdownlint*.mjs \
    markdownlint-cli2.mjs \
    merge-options.mjs \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr parsers schema %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Command
install -pm 0755 markdownlint-cli2-bin.mjs \
      %{buildroot}%{nodejs_sitelib}/%{npm_name}/markdownlint-cli2-bin.mjs
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{npm_name}/markdownlint-cli2-bin.mjs \
      %{buildroot}%{_bindir}/%{name}

# cleanup dupes
%fdupes %{buildroot}

%check
# Smoke test
%{__nodejs} \
      %{buildroot}%{nodejs_sitelib}/%{npm_name}/markdownlint-cli2-bin.mjs \
      --version

# Setup bundled dev node_modules for testing
rm -r node_modules
tar xfz %{SOURCE2}
mv node_modules_dev node_modules
npm test

%files
%doc CHANGELOG.md
%doc README.md
%doc doc/OutputFormatters.md
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%{_bindir}/%{name}
%{nodejs_sitelib}/%{npm_name}

%changelog
%autochangelog
